package com.hot.ticket.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.hot.ticket.model.Ticket;
import com.hot.ticket.repository.TicketRepository;

@Service
public class TicketService {

    @Autowired
    private TicketRepository ticketRepository;

    public Ticket createTicket(com.hot.ticket.model.Service service) {
        Ticket ticket = new Ticket();
        ticket.setTicketNumber(generateTicketNumber());
        ticket.setStatus("Đang chờ");
        ticket.setService(service);
        ticketRepository.save(ticket);
        return ticket;
    }

    public List<Ticket> getTicketsByStatusAndService(String status, com.hot.ticket.model.Service service) {
        return ticketRepository.findByStatusAndService(status, service);
    }

    // Hàm để generate mã số thứ tự
    private String generateTicketNumber() {
        return String.valueOf(1); // ví dụ đơn giản
    }

    public void callNextTicket(Long ticketId) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'callNextTicket'");
    }

    public Ticket findById(String id) {
        return ticketRepository.findById(id).orElse(null);
    }
}
