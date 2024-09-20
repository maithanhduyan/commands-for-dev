package com.hot.ticket.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.hot.ticket.model.Service;
import com.hot.ticket.model.Ticket;

@Repository
public interface TicketRepository extends JpaRepository<Ticket, String> {
    public List<Ticket> findByStatusAndService(String status, Service service);
}
