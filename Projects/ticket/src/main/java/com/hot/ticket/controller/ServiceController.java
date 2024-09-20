package com.hot.ticket.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.hot.ticket.repository.ServiceRepository;

@Controller
@RequestMapping("/service")
public class ServiceController {
    @Autowired
    private ServiceRepository serviceRepository;

    // Màn hình lấy số
    @GetMapping({ "/", "" })
    public String show(Authentication authentication, Model model) {
        // User user ;
        model.addAttribute("services", serviceRepository.findByOrganization("ACB").get());
        return "org/service/services";
    }

    // Màn hình lấy số
    @GetMapping("/add")
    public String addService(Authentication authentication, Model model) {
        model.addAttribute("services", serviceRepository.findAll());
        return "/org/service/add-new-service";
    }
}
