package com.realtimecausation.masters.controller;
import com.maxmind.geoip2.DatabaseReader;
import com.maxmind.geoip2.model.CityResponse;

import jakarta.servlet.http.HttpServletRequest;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.File;
import java.io.IOException;
import java.net.InetAddress;
import java.time.LocalDateTime;
import com.realtimecausation.masters.model.ClickEvent;
import com.realtimecausation.masters.dto.ClickRequest;
import com.realtimecausation.masters.repository.ClickEventRepository;


@RestController
@RequestMapping("/api/clicks")
@CrossOrigin(origins = "http://localhost:5173/")
public class ClickEventController {

    private final ClickEventRepository repository;
    private final DatabaseReader geoDbReader;

    public ClickEventController(ClickEventRepository repository) throws IOException {
        this.repository = repository;
        File database = new File("src/main/resources/GeoLite2-City.mmdb");
        this.geoDbReader = new DatabaseReader.Builder(database).build();
    }

    @PostMapping("/track")
    public ResponseEntity<?> trackClick(@RequestBody ClickRequest request, HttpServletRequest httpReq) {
        String ipAddress = httpReq.getRemoteAddr();
        ClickEvent event = new ClickEvent();

        event.setMovieId(request.getMovieId());
        event.setUserId(request.getUserId());
        event.setIpAddress(ipAddress);
        event.setTimestamp(LocalDateTime.now());
        event.setBrowser(request.getBrowser());
        event.setDeviceType(request.getDeviceType());

        try {
            InetAddress ip = InetAddress.getByName(ipAddress);
            CityResponse location = geoDbReader.city(ip);
            event.setCountry(location.getCountry().getName());
            event.setRegion(location.getMostSpecificSubdivision().getName());
            event.setCity(location.getCity().getName());
        } catch (Exception e) {
            System.err.println("GeoIP lookup failed for IP: " + ipAddress + " - " + e.getMessage());
        }

        repository.save(event);
        return ResponseEntity.ok("Click Tracked");
    }
}
