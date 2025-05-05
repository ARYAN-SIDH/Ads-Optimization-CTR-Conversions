package com.realtimecausation.masters.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "ad_analytics_events")
public class AdAnalyticsEvent {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true)  // Ensure adId is UNIQUE
    private String adId;

    private Integer impressions = 0; // default to 0
    private Integer clicks = 0;       // default to 0
    private LocalDateTime timestamp;

    // Getters and Setters

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getAdId() {
        return adId;
    }

    public void setAdId(String adId) {
        this.adId = adId;
    }

    public Integer getImpressions() {
        return impressions;
    }

    public void setImpressions(Integer impressions) {
        this.impressions = impressions;
    }

    public Integer getClicks() {
        return clicks;
    }

    public void setClicks(Integer clicks) {
        this.clicks = clicks;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDateTime timestamp) {
        this.timestamp = timestamp;
    }
}
