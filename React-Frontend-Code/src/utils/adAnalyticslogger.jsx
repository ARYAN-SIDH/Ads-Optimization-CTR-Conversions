import axios from 'axios';

// Log an Impression (ad seen)
export function logImpression(adId) {
  axios.post('http://localhost:8081/api/log', {
    adId: adId,
    impressions: 1,
    clicks: 0
  })
  .then(() => console.log(`Impression logged for adId: ${adId}`))
  .catch(err => console.error('Failed to log impression:', err));
}

// Log a Click (ad clicked)
export function logClick(adId) {
  axios.post('http://localhost:8081/api/log', {
    adId: adId,
    impressions: 0,
    clicks: 1
  })
  .then(() => console.log(`Click logged for adId: ${adId}`))
  .catch(err => console.error('Failed to log click:', err));
}
