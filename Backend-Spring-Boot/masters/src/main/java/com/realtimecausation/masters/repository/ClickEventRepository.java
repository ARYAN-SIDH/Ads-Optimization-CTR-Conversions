package com.realtimecausation.masters.repository;
import org.springframework.data.jpa.repository.JpaRepository;
import com.realtimecausation.masters.model.ClickEvent;

public interface ClickEventRepository extends JpaRepository<ClickEvent, Long> {}
