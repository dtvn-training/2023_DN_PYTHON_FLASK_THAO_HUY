import React, { useState, useRef } from "react";
import ReactCrop from "react-image-crop";
import axios from "axios";
import "react-image-crop/dist/ReactCrop.css";

const CampaignImage = () => {
  const [imgSrc, setImgSrc] = useState(null);
  const [crop, setCrop] = useState({
    unit: "%",
    width: 30,
    height: 30,
    x: 0,
    y: 0,
    aspect: 16 / 9,
  });
  const [completedCrop, setCompletedCrop] = useState(null);
  const fileInputRef = useRef(null);
  const previewCanvasRef = useRef(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => setImgSrc(e.target.result);
      reader.readAsDataURL(file);
    }
  };

  const handleImageLoaded = (image) => {
    const defaultCrop = { unit: "%", width: 30, aspect: 16 / 9 };
    setCrop(defaultCrop);
    setCompletedCrop(makeClientCrop(defaultCrop, image));
  };

  const handleCropChange = (newCrop, percentCrop) => {
    setCrop(newCrop);
  };

  const makeClientCrop = (crop, image) => {
    if (!image.width || !image.height) {
      return crop;
    }
    const scaleX = image.naturalWidth / image.width;
    const scaleY = image.naturalHeight / image.height;
    const pixelCrop = {
      x: Math.round(crop.x * scaleX),
      y: Math.round(crop.y * scaleY),
      width: Math.round(crop.width * scaleX),
      height: Math.round(crop.height * scaleY),
    };
    return pixelCrop;
  };

  const uploadImage = async () => {
    if (!completedCrop || !imgSrc) return;

    const formData = new FormData();
    const croppedImageBlob = await getCroppedImageBlob(
      imgSrc,
      completedCrop,
      "newFile.jpeg"
    );
    formData.append("file", croppedImageBlob);

    try {
      const response = await axios.post(
        `https://api.cloudinary.com/v1_1/${process.env.REACT_APP_CLOUDINARY_CLOUD_NAME}/image/upload`,
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      console.log("Cloudinary response:", response.data);
    } catch (error) {
      console.error("Error uploading image to Cloudinary:", error);
    }
  };

  const getCroppedImageBlob = (url, crop, fileName) => {
    return new Promise((resolve, reject) => {
      const image = new Image();
      image.onload = () => {
        const canvas = document.createElement("canvas");
        const ctx = canvas.getContext("2d");

        canvas.width = crop.width;
        canvas.height = crop.height;

        ctx.drawImage(
          image,
          crop.x,
          crop.y,
          crop.width,
          crop.height,
          0,
          0,
          crop.width,
          crop.height
        );

        canvas.toBlob(
          (blob) => {
            if (!blob) {
              console.error("Canvas is empty");
              reject(new Error("Canvas is empty"));
              return;
            }
            blob.name = fileName;
            resolve(blob);
          },
          "image/jpeg",
          1
        );
      };

      image.src = url;
    });
  };

  const handleDownloadClick = () => {
    if (completedCrop && previewCanvasRef.current) {
      const canvas = previewCanvasRef.current;
      const blob = getCroppedImageBlob(imgSrc, completedCrop, "preview.jpeg");

      blob.then((result) => {
        const url = URL.createObjectURL(result);
        const link = document.createElement("a");
        link.href = url;
        link.download = "preview.jpeg";
        link.click();
        URL.revokeObjectURL(url);
      });
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} ref={fileInputRef} />
      {imgSrc && (
        <div>
          <ReactCrop
            src={imgSrc}
            crop={crop}
            onImageLoaded={handleImageLoaded}
            onChange={handleCropChange}
          />
          <button onClick={uploadImage}>Upload Image</button>
          <button onClick={handleDownloadClick}>Download Preview</button>
          {completedCrop && (
            <canvas
              ref={previewCanvasRef}
              style={{
                display: "none",
              }}
            />
          )}
        </div>
      )}
    </div>
  );
};

export default CampaignImage;
