package com.hot.ticket.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.hot.ticket.model.Service;
import com.hot.ticket.repository.ServiceRepository;

@Controller
@RequestMapping("/service")
public class ServiceController {
    @Autowired
    private ServiceRepository serviceRepository;

    // Màn hình lấy số
    @GetMapping({ "/", "" })
    public String show(Authentication authentication, Model model) {
        UserDetails userDetails = (UserDetails) authentication.getPrincipal();
        
        model.addAttribute("services", serviceRepository.findByOrganization("ACB").get());
        return "org/service/table-service";
    }

    // http://localhost:8080/services/my-services
    @GetMapping("/my-services")
    public String showMyServices(Model model) {
        model.addAttribute("services", serviceRepository.findByOrganization("ACB").get());
        return "org/service/services";
    }

    @GetMapping("/add")
    public String addService(Authentication authentication, Model model) {
        model.addAttribute("service", new Service());
        return "org/service/add-new-service";
    }

    @PostMapping("/add")
    public String addNewService(@ModelAttribute Service service) {
        serviceRepository.save(service);
        return "redirect:/service/my-services";
    }
}
