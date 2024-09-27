package com.hot.ticket.repository;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import com.hot.ticket.model.Service;

@Repository
public interface ServiceRepository extends JpaRepository<Service, Long> {
    Optional<Service> findByName(String name);

    @Query("SELECT s FROM Service s WHERE s.organization.name = :orgName")
    Optional<List<Service>> findByOrganization(String orgName);

}