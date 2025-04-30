import "../css/prac.css";
import { useEffect } from 'react';
import { trackAdClick } from "../utils/trackAdClick";
import { logClick, logImpression } from "../utils/adAnalyticslogger";

function AdBanner({ position }) {
  useEffect(() => {
    // Log impressions as soon as the banner ads are loaded on page
    logImpression("ad-lv");
    logImpression("ad-furniture");
    logImpression("ad-vizio");
  }, []);

  return (
    <div className="ad-banner">
      <div className="ad-container">
        <a href="https://tinyurl.com/4hmpmmp5" target="_blank" rel="noopener noreferrer" onClick={() => {trackAdClick("ad-lv"); logClick("ad-lv");}}>
            <img src="/img.jpg" alt="Louis Vuitton Ad" />
        </a>
        <a href="https://tinyurl.com/3budvstz" target="_blank" rel="noopener noreferrer" onClick={() => {trackAdClick("ad-furniture"); logClick("ad-furniture");}}>
            <img src="/img2.jpg" alt="Furniture Ad" />
        </a>
        <a href="https://tinyurl.com/2r3jfkcx" target="_blank" rel="noopener noreferrer" onClick={() => {trackAdClick("ad-vizio");logClick("ad-vizio");}}>
            <img src="/img3.jpg" alt="TV Ad" />
        </a>
      </div>
    </div>
  );
}

export default AdBanner;

  