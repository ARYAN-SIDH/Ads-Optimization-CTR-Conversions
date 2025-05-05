package com.realtimecausation.masters.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "ad_click_events")
public class AdClickEvent {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String adId;
    private String type;
    private String deviceType;
    private String browser;
    private LocalDateTime timestamp;
    private String city;
    private String state;
    private String country;

    // Getters and setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getAdId() { return adId; }
    public void setAdId(String adId) { this.adId = adId; }

    public String getType() { return type; }
    public void setType(String type) { this.type = type; }

    public String getDeviceType() { return deviceType; }
    public void setDeviceType(String deviceType) { this.deviceType = deviceType; }

    public String getBrowser() { return browser; }
    public void setBrowser(String browser) { this.browser = browser; }

    public LocalDateTime getTimestamp() { return timestamp; }
    public void setTimestamp(LocalDateTime timestamp) { this.timestamp = timestamp; }

    public String getCity() { return city; }
    public void setCity(String city) { this.city = city; }
    public String getState() { return state; }
    public void setState(String state) { this.state = state; }
    public String getCountry() { return country; }
    public void setCountry(String country) { this.country = country; }
}
