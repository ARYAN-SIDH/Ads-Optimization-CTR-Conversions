package com.realtimecausation.masters.dto;

public class AdResponse {
    private String adId;
    private String userId;
    private String type;
    private String deviceType;
    private String browser;

    // Getters and setters
    public String getAdId() { return adId; }
    public void setAdId(String adId) { this.adId = adId; }

    public String getType() { return type; }
    public void setType(String type) { this.type = type; }

    public String getDeviceType() { return deviceType; }
    public void setDeviceType(String deviceType) { this.deviceType = deviceType; }

    public String getBrowser() { return browser; }
    public void setBrowser(String browser) { this.browser = browser; }
}