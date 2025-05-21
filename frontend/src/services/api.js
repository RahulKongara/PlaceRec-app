import axios from "axios";

export const identifyLandmark = (file) => {
    const data = new FormData();
    data.append("image", file);
    return axios.post("http://localhost:8000/api/landmarks/identify/", data, {
        headers: { "Content-Type": "multipart/form-data" }
    });
};