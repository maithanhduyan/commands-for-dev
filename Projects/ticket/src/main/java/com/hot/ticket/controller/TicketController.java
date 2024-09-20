package com.hot.ticket.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.hot.ticket.model.Service;
import com.hot.ticket.model.Ticket;
import com.hot.ticket.repository.ServiceRepository;
import com.hot.ticket.service.TicketService;

@Controller
@RequestMapping("/ticket")
public class TicketController {

    private static final Logger logger = LoggerFactory.getLogger(TicketController.class);

    @Autowired
    private TicketService ticketService;

    @Autowired
    private ServiceRepository serviceRepository;

    // Màn hình lấy số
    @GetMapping("/new")
    public String getNewTicket(Authentication authentication, Model model) {
        model.addAttribute("services", serviceRepository.findAll());
        return "org/new-ticket";
    }

    // Xử lý lấy số thứ tự cho dịch vụ
    @PostMapping("/new")
    public String createTicket(@RequestParam Long serviceId, Model model) {
        Service service = serviceRepository.findById(serviceId).orElse(null);
        if (service != null) {
            Ticket ticket = ticketService.createTicket(service);
            // model.addAttribute("ticket", ticket);
            // Redirect sang URL /ticket?id=werwer với giá trị id là ticketId
            return "redirect:/ticket/ticket-details?id=" + ticket.getId();
        }
        return "redirect:/error"; // Trong trường hợp không tìm thấy service hoặc lỗi
    }

    // Public link for everyone http://localhost:8080/ticket/ticket-details?id=0
    @GetMapping("/ticket-details")
    public String viewTicket(@RequestParam(value = "id", required = false) String ticketId, Model model) {
        Ticket ticket;
        Service service = null;
        try {
            Long id = Long.parseLong(ticketId);
            ticket = ticketService.findById(id);
            if (ticket != null) {
                service = ticket.getService();
            }
            model.addAttribute("ticket", ticket);
            model.addAttribute("service", service);
            return "/org/ticket/ticket-details"; // Trang hiển thị chi tiết ticket

        } catch (Exception e) {
            logger.error("ticket không tồn tại");
            model.addAttribute("error", "Ticket không tồn tại");
            return "/org/ticket/ticket-error";
        }

    }

    // Màn hình của nhân viên xử lý danh sách khách hàng chờ
    @GetMapping("/queue")
    public String getTicketQueue(Model model) {
        model.addAttribute("waitingTickets");
        return "employee-dashboard";
    }

    // Gọi số tiếp theo
    @PostMapping("/call")
    public String callNextTicket(@RequestParam Long ticketId) {
        ticketService.callNextTicket(ticketId);
        return "redirect:/ticket/queue";
    }

    @GetMapping({ "/error" })
    public String getTicketError() {
        return "org/ticket/ticket-error";
    }
}