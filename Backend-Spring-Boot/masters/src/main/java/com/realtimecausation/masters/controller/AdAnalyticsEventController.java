package com.realtimecausation.masters.controller;

import com.realtimecausation.masters.dto.AdAnalyticsRequest;
import com.realtimecausation.masters.model.AdAnalyticsEvent;
import com.realtimecausation.masters.repository.AdAnalyticsEventRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDateTime;
import java.util.Optional;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "http://localhost:5173/")
public class AdAnalyticsEventController {

    @Autowired
    private AdAnalyticsEventRepository adAnalyticsEventRepository;

    @PostMapping("/log")
    public ResponseEntity<String> logAdAnalytics(@RequestBody AdAnalyticsRequest request) {
        Optional<AdAnalyticsEvent> existingEventOpt = adAnalyticsEventRepository.findByAdId(request.getAdId());

        AdAnalyticsEvent event;
        if (existingEventOpt.isPresent()) {
            // Update existing record
            event = existingEventOpt.get();
            event.setImpressions(event.getImpressions() + request.getImpressions());
            event.setClicks(event.getClicks() + request.getClicks());
            event.setTimestamp(LocalDateTime.now());
        } else {
            // Create new record
            event = new AdAnalyticsEvent();
            event.setAdId(request.getAdId());
            event.setImpressions(request.getImpressions());
            event.setClicks(request.getClicks());
            event.setTimestamp(LocalDateTime.now());
        }

        adAnalyticsEventRepository.save(event);
        return ResponseEntity.ok("Ad analytics event logged successfully");
    }
}
