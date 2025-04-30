package com.realtimecausation.masters.dto;

import java.time.LocalDateTime;

public class AdAnalyticsResponse {
    private String adId;
    private int clicks;
    private int impressions;
    private double ctr;
    private LocalDateTime timestamp;

    public AdAnalyticsResponse(String adId, int clicks, int impressions, double ctr, LocalDateTime timestamp) {
        this.adId = adId;
        this.clicks = clicks;
        this.impressions = impressions;
        this.ctr = ctr;
        this.timestamp = timestamp;
    }

    // Getters and Setters
    public String getAdId() { return adId; }
    public void setAdId(String adId) { this.adId = adId; }

    public int getClicks() { return clicks; }
    public void setClicks(int clicks) { this.clicks = clicks; }

    public int getImpressions() { return impressions; }
    public void setImpressions(int impressions) { this.impressions = impressions; }

    public double getCtr() { return ctr; }
    public void setCtr(double ctr) { this.ctr = ctr; }

    public LocalDateTime getTimestamp() { return timestamp; }
    public void setTimestamp(LocalDateTime timestamp) { this.timestamp = timestamp; }
}
