import React, { useState } from "react";
import "./Banner.scss";
import { Slide } from "react-slideshow-image";
import "react-slideshow-image/dist/styles.css";
import { useSelector } from "react-redux";
const Banner = () => {
  const listCampaigns = useSelector((state) => state.campaign.listCampaigns);
  const [count, setCount] = useState(0);
  const images = [];

  listCampaigns.forEach((item, index) => {
    images.push(`${item.creatives[0].final_url}`);
  });

  const properties = {
    autoplay: true,
    duration: 1000,
    transitionDuration: 1000,
    infinite: true,
    indicators: true,
    arrows: false,
    canSwipe: false,
  };

  const handleChange = (e) => {
    // Tăng giá trị của count mỗi khi handleChange được gọi
    setCount((prevCount) => prevCount + 1);
  };

  console.log(count);
  return (
    <>
      <div className="slide">
        <Slide {...properties} onChange={(e) => handleChange(e)}>
          <div className="each-slide-effect">
            <div style={{ backgroundImage: `url(${images[0]})` }}>
              {images[0]}
            </div>
          </div>
          <div className="each-slide-effect">
            <div style={{ backgroundImage: `url(${images[1]})` }}>
              {images[1]}
            </div>
          </div>
          {/* <div className="each-slide-effect">
            <div style={{ backgroundImage: `url(${images[2]})` }}>
              {images[2]}
            </div>
          </div>
          <div className="each-slide-effect">
            <div style={{ backgroundImage: `url(${images[3]})` }}>
              {images[3]}
            </div>
          </div>
          <div className="each-slide-effect">
            <div style={{ backgroundImage: `url(${images[4]})` }}>
              {images[4]}
            </div>
          </div> */}
        </Slide>
      </div>
    </>
  );
};

export default Banner;
