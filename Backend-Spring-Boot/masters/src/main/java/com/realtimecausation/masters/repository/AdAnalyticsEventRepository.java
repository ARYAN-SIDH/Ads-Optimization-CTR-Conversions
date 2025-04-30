package com.realtimecausation.masters.repository;

import com.realtimecausation.masters.model.AdAnalyticsEvent;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

public interface AdAnalyticsEventRepository extends JpaRepository<AdAnalyticsEvent, Long> {
    Optional<AdAnalyticsEvent> findByAdId(String adId);
}
