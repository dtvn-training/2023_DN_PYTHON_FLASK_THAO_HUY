import React, { useState, useCallback, useEffect, useRef } from "react";
import ReactCrop from "react-image-crop";
import axios from "axios";
import "react-image-crop/dist/ReactCrop.css";
const setCanvasImage = (image, canvas, crop) => {
  if (!crop || !canvas || !image) {
    return;
  }

  const scaleX = image.naturalWidth / image.width;
  const scaleY = image.naturalHeight / image.height;
  const ctx = canvas.getContext("2d");
  const pixelRatio = window.devicePixelRatio;

  canvas.width = crop.width * pixelRatio * scaleX;
  canvas.height = crop.height * pixelRatio * scaleY;

  ctx.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0);
  ctx.imageSmoothingQuality = "high";

  ctx.drawImage(
    image,
    crop.x * scaleX,
    crop.y * scaleY,
    crop.width * scaleX,
    crop.height * scaleY,
    0,
    0,
    crop.width * scaleX,
    crop.height * scaleY
  );
};
export default function CampaignImage() {
  const [image, setImage] = useState();
  const imgRef = useRef(null);
  const previewCanvasRef = useRef(null);
  const [crop, setCrop] = useState({
    unit: "px",
    width: 30,
    aspect: 1,
  });
  const [completedCrop, setCompletedCrop] = useState(null);
  console.log(crop);
  console.log("file: CampaignImage.jsx:39 ~ completedCrop:", completedCrop);
  // Read the image from browser files
  const handleImageChange = (e) => {
    if (e.target.files && e.target.files.length > 0) {
      const reader = new FileReader();
      reader.addEventListener("load", () => setImage(reader.result));
      reader.readAsDataURL(e.target.files[0]);
    }
  };

  const onLoad = useCallback((img) => {
    imgRef.current = img;
  }, []);

  useEffect(() => {
    setCanvasImage(imgRef.current, previewCanvasRef.current, completedCrop);
  }, [completedCrop]);
  console.log(
    "file: CampaignImage.jsx:60 ~ previewCanvasRef:",
    previewCanvasRef
  );

  return (
    <div>
      <div>
        <input type="file" accept="image/*" onChange={handleImageChange} />
      </div>
      {image && (
        <div>
          <ReactCrop
            src={image}
            onImageLoaded={onLoad}
            crop={crop}
            onChange={(c) => setCrop(c)}
            onComplete={(c) => setCompletedCrop(c)}
          >
            <img src={image} />
          </ReactCrop>
          <div>
            <canvas
              ref={previewCanvasRef}
              style={{
                width: Math.round(completedCrop?.width ?? 0),
                height: Math.round(completedCrop?.height ?? 0),
              }}
            ></canvas>
          </div>
          <button>Get your final URL</button>
          {/* {completedCrop && (
            <canvas
              ref={previewCanvasRef}
              style={{
                display: "none",
              }}
            />
          )} */}
        </div>
      )}
    </div>
  );
}
