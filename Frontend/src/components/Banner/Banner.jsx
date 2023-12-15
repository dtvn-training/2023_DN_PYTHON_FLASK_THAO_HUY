import React from "react";
import "./Banner.scss";
import { Slide } from "react-slideshow-image";
import "react-slideshow-image/dist/styles.css";
const Banner = () => {
  const images = [
    "https://res.cloudinary.com/dooge27kv/image/upload/v1701586838/project/6SB-7138-87000072_fpnway.jpg",
    "https://images.unsplash.com/photo-1506710507565-203b9f24669b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1536&q=80",
    "https://images.unsplash.com/photo-1536987333706-fc9adfb10d91?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80",
  ];
  return (
    <>
      <div
        style={{ height: "30vh", width: "15%", "justify-content": "center" }}
      >
        <Slide className="slide-show">
          <div className="each-slide-effect">
            <div style={{ backgroundImage: `url(${images[0]})` }}></div>
          </div>
          <div className="each-slide-effect">
            <div style={{ backgroundImage: `url(${images[1]})` }}></div>
          </div>
          <div className="each-slide-effect">
            <div style={{ backgroundImage: `url(${images[2]})` }}></div>
          </div>
        </Slide>
      </div>
    </>
  );
};

export default Banner;
