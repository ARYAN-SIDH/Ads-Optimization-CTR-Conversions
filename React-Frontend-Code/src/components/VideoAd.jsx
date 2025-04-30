import { useEffect, useRef, useState } from "react";
import axios from "axios";
import "../css/VideoAd.css";

function VideoAd({ adId, videoSrc, clickUrl }) {
  const videoRef = useRef(null);        // to control the video element
  const [tracked, setTracked] = useState(false);  // to track once

  const handleClick = async () => {
    try {
      await axios.post("http://localhost:8081/api/ads/click", {
        adId,
        type: "video",
        timestamp: new Date().toISOString(),
        deviceType: /Mobi|Android/i.test(navigator.userAgent) ? "Mobile" : "Desktop",
        browser: navigator.userAgent
      });
      console.log(`Click successfully logged for ${adId}`);
  
      await axios.post("http://localhost:8081/api/log", {
        adId: adId,
        impressions: 0,
        clicks: 1
      });
      console.log(`Video click logged for ${adId}`);
  
      window.open(clickUrl, "_blank"); // After logging both
    } catch (err) {
      console.error("Error tracking ad click or video click:", err);
      window.open(clickUrl, "_blank"); // Still open ad even if error
    }
  };

  const handleTimeUpdate = async () => {
    const video = videoRef.current;
    if (video && video.currentTime >= 10 && !tracked) {
      try {
        await axios.post("http://localhost:8081/api/ads/click", {
          adId,
          type: "video",
          timestamp: new Date().toISOString(),
          deviceType: /Mobi|Android/i.test(navigator.userAgent) ? "Mobile" : "Desktop",
          browser: navigator.userAgent
        });
        console.log(`Impression tracked after 10 seconds for ${adId}`);
        setTracked(true);
  
        await axios.post("http://localhost:8081/api/log", {
          adId: adId,
          impressions: 1,
          clicks: 0
        });
        console.log(`Video impression logged for ${adId}`);
      } catch (err) {
        console.error("Failed to log video impression:", err);
      }
    }
  };

  return (
    <div className="video-ad">
      <video
        ref={videoRef}
        width="100%"
        height="auto"
        controls
        autoPlay
        muted
        onClick={handleClick}
        onTimeUpdate={handleTimeUpdate}
      >
        <source src={videoSrc} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
  );
}

export default VideoAd;
