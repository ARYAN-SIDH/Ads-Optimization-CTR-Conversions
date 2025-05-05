package com.realtimecausation.masters.controller;

import com.realtimecausation.masters.dto.AdResponse;
import com.realtimecausation.masters.model.AdClickEvent;
import com.realtimecausation.masters.repository.AdClickEventRepository;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import com.maxmind.geoip2.DatabaseReader;
import com.maxmind.geoip2.model.CityResponse;

import java.io.File;
import java.io.IOException;
import java.net.InetAddress;
import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Autowired;
import java.time.LocalDateTime;
import java.util.List;

@RestController
@RequestMapping("/api/ads")
@CrossOrigin(origins = "http://localhost:5173/")
public class AdClickController {

    @Autowired
    private AdClickEventRepository adClickEventRepository;
    private DatabaseReader dbReader;

    @PostConstruct
    public void initGeoIP() throws IOException {
        File database = new File("src/main/resources/GeoLite2-City.mmdb");
        dbReader = new DatabaseReader.Builder(database).build();
    }


    @PostMapping("/click")
    public ResponseEntity<?> trackAdClick(@RequestBody AdResponse request, HttpServletRequest httpReq) {
        // Step 1: Get IP from X-Forwarded-For (if available)
        String ip = httpReq.getHeader("X-Forwarded-For");

        // Step 2: If missing, fall back to remote address
        if (ip == null || ip.isEmpty() || "unknown".equalsIgnoreCase(ip)) {
            ip = httpReq.getRemoteAddr();
        }

        // Step 3: Handle localhost testing (IPv6 and IPv4 loopback)
        if ("127.0.0.1".equals(ip) || "::1".equals(ip)) {
            ip = "8.8.8.8"; // Use a public IP for local GeoIP testing
        }

        // Optional: Log final IP used
        System.out.println("Tracking ad click from IP: " + ip);

        String city = "Edison", state = "NJ", region = "Middlesex", country = "USA";
        try {
            InetAddress ipAddress = InetAddress.getByName(ip);
            CityResponse response = dbReader.city(ipAddress);
            city = response.getCity().getName();
            state = response.getMostSpecificSubdivision().getName();
            country = response.getCountry().getName();
        } catch (Exception e) {
            System.out.println("GeoIP lookup failed: " + e.getMessage());
        }
        AdClickEvent event = new AdClickEvent();

        event.setAdId(request.getAdId());
        event.setDeviceType(request.getDeviceType());
        event.setBrowser(request.getBrowser());
        event.setTimestamp(LocalDateTime.now());
        event.setType(request.getType());
        event.setCity(city);
        event.setState(state);
        event.setCountry(country);

        adClickEventRepository.save(event);
        return ResponseEntity.ok("Ad click tracked");
    }

    // ✅ New method: Fetch all clicks
    @GetMapping("/clicks")
    public ResponseEntity<List<AdClickEvent>> getAllClicks() {
        List<AdClickEvent> clicks = adClickEventRepository.findAll();
        return ResponseEntity.ok(clicks);
    }
}
