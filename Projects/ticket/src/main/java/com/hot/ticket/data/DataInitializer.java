package com.hot.ticket.data;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

import com.hot.ticket.model.Organization;
import com.hot.ticket.model.Role;
import com.hot.ticket.model.Service;
import com.hot.ticket.model.User;
import com.hot.ticket.repository.OrganizationRepository;
import com.hot.ticket.repository.RoleRepository;
import com.hot.ticket.repository.ServiceRepository;
import com.hot.ticket.repository.UserRepository;

@Component
public class DataInitializer implements CommandLineRunner {

    @Autowired
    private UserRepository userRepository;

   @Autowired
    private PasswordEncoder passwordEncoder;

    @Autowired
    private OrganizationRepository organizationRepository;

    @Autowired
    private RoleRepository roleRepository;

    @Autowired
    private ServiceRepository serviceRepository;

    @Override
    public void run(String... args) throws Exception {
        createUSerDemo("admin");
        // Tạo các vai trò nếu chưa tồn tại
        createRoleIfNotFound("ROLE_USER");
        createRoleIfNotFound("ROLE_ADMIN");

        createOrganization("ACB");
        createServiceDemo("ACB", "Dịch Vụ Thẻ");
        createServiceDemo("ACB", "Dịch Vụ Vay");
        createServiceDemo("ACB", "Dịch Vụ Gủi Tiền");
        createServiceDemo("ACB", "Dịch Vụ Rút Tiền");
    }

    private void createUSerDemo(String name) {
        Optional<User> userOptional = userRepository.findByUsername(name);
        if (!userOptional.isPresent()) {
            List<Role> roles = new ArrayList<Role>();
            roles.add(roleRepository.findByName("ROLE_ADMIN").get());
            User user = new User();
            user.setUsername(name);
            user.setEmail("admin@company.com");

            user.setPassword(passwordEncoder.encode("admin"));
            user.setRoles(roles);
            userRepository.save(user);
        }
    }

    private void createOrganization(String name) {
        Optional<Organization> optional = organizationRepository.findByName(name);
        if (!optional.isPresent()) {
            Organization org = new Organization();
            org.setName(name);
            organizationRepository.save(org);
        }
    }

    private void createRoleIfNotFound(String roleName) {
        Optional<Role> roleOpt = roleRepository.findByName(roleName);
        if (!roleOpt.isPresent()) {
            Role role = new Role();
            role.setName(roleName);
            roleRepository.save(role);
        }
    }

    private void createServiceDemo(String orgName, String serviceName) {
        Optional<Organization> orgOptional = organizationRepository.findByName(orgName);
        Optional<Service> serviceOptional = serviceRepository.findByName(serviceName);
        if (!orgOptional.isPresent()) {

        } else {
            if (!serviceOptional.isPresent()) {
                Service service = new Service();
                service.setName(serviceName);
                service.setOrganization(orgOptional.get());
                serviceRepository.save(service);
            }
        }
    }
}
