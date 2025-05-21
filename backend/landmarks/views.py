from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Landmark
from .serializers import LandmarkSerializer
from .ml import recognize_landmark, find_similar
import os
import tempfile

class LandmarkViewSet(viewsets.ModelViewSet):
    queryset = Landmark.objects.all()
    serializer_class = LandmarkSerializer
    
    @action(detail=False, methods=["post"])
    def identify(self, request):
        img = request.FILES["image"]
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            for chunk in img.chunks():
                tmp.write(chunk)
            tmp_path = tmp.name  # Save the path before closing

        try:
            name, embed = recognize_landmark(tmp_path)
            import numpy as np
            if hasattr(embed, "numpy"):
                embed = embed.numpy()
            embed = np.squeeze(embed)
        finally:
            os.remove(tmp_path) 
        landmark, _ = Landmark.objects.get_or_create(name=name, defaults={"embedding": embed.tolist()})
        recs = find_similar(embed, top_k=5)  # get one extra in case the identified is in recs
        # Exclude the identified landmark from recommendations
        recs = [rec for rec in recs if rec.name != landmark.name][:5]
        data = {
            "identified": LandmarkSerializer(landmark).data,
            "recommendations": LandmarkSerializer(recs, many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)
