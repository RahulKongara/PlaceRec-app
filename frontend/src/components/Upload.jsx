import React, { useRef, useState } from "react";
import { BsUpload } from "react-icons/bs";
import { identifyLandmark } from "../services/api";

export default function Upload({ onResult }) {
    const [preview, setPreview] = useState(null);
    const [file, setFile] = useState(null);
    const inputRef = useRef(null);
    const handleChange = e => {
        const img = e.target.files[0];
        setPreview(URL.createObjectURL(img));
        setFile(img);
    };

    const handleSubmit = async () => {
        const res = await identifyLandmark(file);
        onResult(res.data);
    };

    const handleDrop = e => {
        e.preventDefault();
        const img = e.dataTransfer.files[0];
        if (img) {
            setPreview(URL.createObjectURL(img));
            setFile(img);
        }
    }

    const handleDragOver = e => {
        e.preventDefault();
    }

    const handlePaste = e => {
        const items = e.clipboardData.items;
        for (let i = 0; i < items.length; i++) {
            if (items[i].type.indexOf("image") !== -1) {
                const file = items[i].getAsFile();
                setPreview(URL.createObjectURL(file));
                setFile(file);
                break;
            }
        }
    }

    return (
        <div className="upload-container">
            {/* <input type="file" accept="image/*" onChange={handleChange} /> */}
            {!file && (
                <div className="dropzone"
                    onDrop={handleDrop}
                    onDragOver={handleDragOver}
                    onPaste={handlePaste}
                >
                    <BsUpload size={50} />
                    <h2>Drag & drop or Ctrl + V</h2>
                    <h3>OR</h3>
                    <input type="file" accept="image/*" onChange={handleChange} hidden ref={inputRef} />
                    <button onClick={() => inputRef.current.click()}>Select File</button>
                </div>
            )}
            {preview && <img src={preview} className="preview" alt="Preview" width={200} />}
            <button onClick={handleSubmit}>Identify Landmark</button>
        </div>
    );
}