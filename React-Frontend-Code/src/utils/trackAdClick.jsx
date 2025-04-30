import axios from "axios";

export function trackAdClick(adId) {
  axios.post("http://localhost:8081/api/ads/click", {
    adId,
    type: "Banner",
    browser: navigator.userAgent,
    deviceType: /Mobi|Android/i.test(navigator.userAgent) ? "Mobile" : "Desktop",
    timestamp: new Date().toISOString()
  })
  .then(() => {
    console.log(`Ad click tracked: ${adId}`);
  })
  .catch((err) => {
    console.error("Error tracking ad click:", err);
  });
}
