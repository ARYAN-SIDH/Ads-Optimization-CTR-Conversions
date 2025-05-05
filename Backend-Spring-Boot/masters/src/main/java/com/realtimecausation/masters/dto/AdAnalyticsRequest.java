package com.realtimecausation.masters.dto;

public class AdAnalyticsRequest {
    private String adId;
    private int impressions;
    private int clicks;

    // Getters and Setters

    public String getAdId() {
        return adId;
    }

    public void setAdId(String adId) {
        this.adId = adId;
    }

    public int getImpressions() {
        return impressions;
    }

    public void setImpressions(int impressions) {
        this.impressions = impressions;
    }

    public int getClicks() {
        return clicks;
    }

    public void setClicks(int clicks) {
        this.clicks = clicks;
    }
}
