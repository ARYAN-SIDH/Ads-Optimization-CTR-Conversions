package com.realtimecausation.masters.controller;

import com.realtimecausation.masters.model.AdAnalyticsEvent;
import com.realtimecausation.masters.dto.AdAnalyticsResponse;
import com.realtimecausation.masters.repository.AdAnalyticsEventRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/analytics")
@CrossOrigin(origins = "http://localhost:5173/")
public class AdAnalyticsController {

    @Autowired
    private AdAnalyticsEventRepository adAnalyticsEventRepository;

    @GetMapping
    public List<AdAnalyticsResponse> getAnalyticsData() {
        List<AdAnalyticsEvent> events = adAnalyticsEventRepository.findAll();

        return events.stream()
                .map(event -> {
                    double ctr = 0.0;
                    if (event.getImpressions() > 0) {
                        ctr = (event.getClicks() * 100.0) / event.getImpressions();
                    }
                    return new AdAnalyticsResponse(
                            event.getAdId(),
                            event.getClicks(),
                            event.getImpressions(),
                            ctr,
                            event.getTimestamp()
                    );
                })
                .collect(Collectors.toList());
    }
}