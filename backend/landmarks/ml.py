from transformers.models.clip import CLIPProcessor, CLIPModel
from PIL import Image
import json

import torch

processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")

with open("landmarks/labels.json") as f:
    LABELS = json.load(f)
    
def recognize_landmark(img_path):
    image = Image.open(img_path).convert("RGB")
    inputs = processor(text=LABELS, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    idx   = outputs.logits_per_image.argmax().item()
    return LABELS[idx], outputs.image_embeds.detach().cpu()

def find_similar(query_embed, top_k=5, exclude_name=None):
    from .models import Landmark
    import numpy as np
    all_objs = Landmark.objects.exclude(embedding=None)
    if exclude_name:
        all_objs = all_objs.exclude(name=exclude_name)
    sims = []
    q = np.array(query_embed).astype(np.float32).flatten()
    for obj in all_objs:
        emb = np.array(obj.embedding).astype(np.float32).flatten()
        if q.shape != emb.shape:
            min_len = min(q.shape[0], emb.shape[0])
            q_ = q[:min_len]
            emb_ = emb[:min_len]
        else:
            q_ = q
            emb_ = emb
        cos = np.dot(q_, emb_) / (np.linalg.norm(q_) * np.linalg.norm(emb_))
        sims.append((cos, obj))
    top = sorted(sims, key=lambda x: -x[0])[:top_k]
    return [obj for _, obj in top]