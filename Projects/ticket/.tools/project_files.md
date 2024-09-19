# Cấu trúc Dự án

```
├── .gitignore
├── HELP.md
├── compose.yaml
├── mvnw
├── mvnw.cmd
├── pom.xml
└── src
    ├── main
    │   ├── java
    │   │   └── com
    │   │       └── hot
    │   │           └── ticket
    │   │               ├── TicketApplication.java
    │   │               ├── config
    │   │               │   └── SecurityConfig.java
    │   │               ├── controller
    │   │               │   ├── AdminController.java
    │   │               │   ├── AuthController.java
    │   │               │   ├── ServiceController.java
    │   │               │   └── TicketController.java
    │   │               ├── data
    │   │               │   └── DataInitializer.java
    │   │               ├── dto
    │   │               │   └── UserDto.java
    │   │               ├── model
    │   │               │   ├── Organization.java
    │   │               │   ├── Role.java
    │   │               │   ├── Service.java
    │   │               │   ├── Ticket.java
    │   │               │   └── User.java
    │   │               ├── repository
    │   │               │   ├── OrganizationRepository.java
    │   │               │   ├── RoleRepository.java
    │   │               │   ├── ServiceRepository.java
    │   │               │   ├── TicketRepository.java
    │   │               │   └── UserRepository.java
    │   │               └── service
    │   │                   ├── TicketService.java
    │   │                   ├── UserDetailsServiceImpl.java
    │   │                   └── UserService.java
    │   └── resources
    │       ├── application.properties
    │       ├── static
    │       │   ├── css
    │       │   │   └── styles.css
    │       │   ├── demo
    │       │   │   └── ticket.html
    │       │   └── js
    │       └── templates
    │           ├── index.html
    │           ├── login.html
    │           ├── org
    │           │   ├── new-ticket.html
    │           │   └── services.html
    │           └── register.html
    └── test
        └── java
            └── com
                └── hot
                    └── ticket
                        └── TicketApplicationTests.java
```

# Danh sách Các Tệp Dự án

## ../pom.xml

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>3.3.3</version>
		<relativePath/> <!-- lookup parent from repository -->
	</parent>
	<groupId>com.hot</groupId>
	<artifactId>ticket</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>ticket</name>
	<description>Demo project for Spring Boot</description>
	<url/>
	<licenses>
		<license/>
	</licenses>
	<developers>
		<developer/>
	</developers>
	<scm>
		<connection/>
		<developerConnection/>
		<tag/>
		<url/>
	</scm>
	<properties>
		<java.version>21</java.version>
	</properties>
	<dependencies>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-data-jpa</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-security</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-thymeleaf</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>
		<dependency>
			<groupId>org.thymeleaf.extras</groupId>
			<artifactId>thymeleaf-extras-springsecurity6</artifactId>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-devtools</artifactId>
			<scope>runtime</scope>
			<optional>true</optional>
		</dependency>
		<dependency>
			<groupId>com.mysql</groupId>
			<artifactId>mysql-connector-j</artifactId>
			<scope>runtime</scope>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.springframework.security</groupId>
			<artifactId>spring-security-test</artifactId>
			<scope>test</scope>
		</dependency>
	</dependencies>

	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
			</plugin>
		</plugins>
	</build>

</project>

```

## ../src\main\java\com\hot\ticket\TicketApplication.java

```
package com.hot.ticket;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class TicketApplication {

	public static void main(String[] args) {
		SpringApplication.run(TicketApplication.class, args);
	}

}

```

## ../src\main\java\com\hot\ticket\config\SecurityConfig.java

```
package com.hot.ticket.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
                .authorizeHttpRequests(authorizeRequests -> authorizeRequests
                        .requestMatchers("/register", "/login", "/css/**", "/js/**").permitAll()
                        .anyRequest().authenticated())
                .formLogin(formLogin -> formLogin
                        .loginPage("/login")
                        .permitAll())
                .logout(logout -> logout.permitAll());

        return http.build();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration authenticationConfiguration)
            throws Exception {
        return authenticationConfiguration.getAuthenticationManager();
    }
}

```

## ../src\main\java\com\hot\ticket\controller\AdminController.java

```
package com.hot.ticket.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/admin")
public class AdminController {
    // For webmaster
}

```

## ../src\main\java\com\hot\ticket\controller\AuthController.java

```
package com.hot.ticket.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import com.hot.ticket.dto.UserDto;
import com.hot.ticket.model.User;
import com.hot.ticket.service.UserService;

@Controller
public class AuthController {

    @Autowired
    private UserService userService;

    @Autowired
    private AuthenticationManager authenticationManager;

    @GetMapping("/")
    public String home(Authentication authentication, Model model) {
        model.addAttribute("username", authentication.getName());
        return "index"; // Tạo file home.html
    }

    @GetMapping("/login")
    public String login() {
        return "login"; // Tạo file login.html
    }

    @PostMapping("/login")
    public ResponseEntity<String> login(@RequestBody UserDto userDto) {
        try {
            UsernamePasswordAuthenticationToken authToken = new UsernamePasswordAuthenticationToken(
                    userDto.getUsername(), userDto.getPassword());

            Authentication authentication = authenticationManager.authenticate(authToken);

            SecurityContextHolder.getContext().setAuthentication(authentication);

            return ResponseEntity.ok("Đăng nhập thành công!");
        } catch (AuthenticationException e) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("Sai tên đăng nhập hoặc mật khẩu!");
        } catch (Exception e) {
            // Ghi log lỗi nếu cần
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Đã xảy ra lỗi. Vui lòng thử lại.");
        }
    }

    @GetMapping("/register")
    public String registerForm(Model model) {
        model.addAttribute("user", new User());
        return "register"; // Tạo file register.html
    }

    @PostMapping("/register")
    public String register(@ModelAttribute("user") User user) {
        userService.save(user);
        return "redirect:/login";
    }

    @GetMapping("/logout")
    public String logout() {
        return "redirect:/login?logout";
    }
}

```

## ../src\main\java\com\hot\ticket\controller\ServiceController.java

```
package com.hot.ticket.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/service")
public class ServiceController {
    
}

```

## ../src\main\java\com\hot\ticket\controller\TicketController.java

```
package com.hot.ticket.controller;

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

    @Autowired
    private TicketService ticketService;

    @Autowired
    private ServiceRepository serviceRepository;

    // Màn hình lấy số
    @GetMapping("/new")
    public String getNewTicket(Authentication authentication, Model model) {
        model.addAttribute("services", serviceRepository.findAll());
        return "/org/new-ticket";
    }

    // Xử lý lấy số thứ tự cho dịch vụ
    @PostMapping("/new")
    public String createTicket(@RequestParam Long serviceId, Model model) {
        Service service = serviceRepository.findById(serviceId).orElse(null);
        if (service != null) {
            Ticket ticket = ticketService.createTicket(service);
            model.addAttribute("ticket", ticket);
        }
        return "ticket-confirmation";
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
}
```

## ../src\main\java\com\hot\ticket\data\DataInitializer.java

```
package com.hot.ticket.data;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import com.hot.ticket.model.Role;
import com.hot.ticket.repository.RoleRepository;

@Component
public class DataInitializer implements CommandLineRunner {

    @Autowired
    private RoleRepository roleRepository;

    @Override
    public void run(String... args) throws Exception {
        // Tạo các vai trò nếu chưa tồn tại
        createRoleIfNotFound("ROLE_USER");
        createRoleIfNotFound("ROLE_ADMIN");
    }

    private void createRoleIfNotFound(String roleName) {
        Optional<Role> roleOpt = roleRepository.findByName(roleName);
        if (!roleOpt.isPresent()) {
            Role role = new Role();
            role.setName(roleName);
            roleRepository.save(role);
        }
    }
}

```

## ../src\main\java\com\hot\ticket\dto\UserDto.java

```
package com.hot.ticket.dto;

// Lớp DTO để nhận dữ liệu từ client
public class UserDto {
    private String username;
    private String password;

    // Getters và Setters
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
```

## ../src\main\java\com\hot\ticket\model\Organization.java

```
package com.hot.ticket.model;

import java.util.List;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;

@Entity
public class Organization {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String address;
    private String email;

    @OneToMany(mappedBy = "organization")
    private List<Service> services;

    @OneToMany(mappedBy = "organization")
    private List<User> users;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public List<Service> getServices() {
        return services;
    }

    public void setServices(List<Service> services) {
        this.services = services;
    }

    public List<User> getUsers() {
        return users;
    }

    public void setUsers(List<User> users) {
        this.users = users;
    }

}

```

## ../src\main\java\com\hot\ticket\model\Role.java

```
package com.hot.ticket.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Role {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true)
    private String name;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

}

```

## ../src\main\java\com\hot\ticket\model\Service.java

```
package com.hot.ticket.model;

import java.util.List;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToMany;

@Entity
public class Service {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;

    @ManyToOne
    @JoinColumn(name = "organization_id")
    private Organization organization;

    @OneToMany(mappedBy = "service")
    private List<Ticket> tickets;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Organization getOrganization() {
        return organization;
    }

    public void setOrganization(Organization organization) {
        this.organization = organization;
    }

    public List<Ticket> getTickets() {
        return tickets;
    }

    public void setTickets(List<Ticket> tickets) {
        this.tickets = tickets;
    }

}

```

## ../src\main\java\com\hot\ticket\model\Ticket.java

```
package com.hot.ticket.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;

@Entity
public class Ticket {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String ticketNumber;
    private String status; // "Đang chờ", "Đang gọi", "Hết hạn"
    private String qrCode; // Mã QR

    @ManyToOne
    @JoinColumn(name = "service_id")
    private Service service;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTicketNumber() {
        return ticketNumber;
    }

    public void setTicketNumber(String ticketNumber) {
        this.ticketNumber = ticketNumber;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getQrCode() {
        return qrCode;
    }

    public void setQrCode(String qrCode) {
        this.qrCode = qrCode;
    }

    public Service getService() {
        return service;
    }

    public void setService(Service service) {
        this.service = service;
    }

}

```

## ../src\main\java\com\hot\ticket\model\User.java

```
package com.hot.ticket.model;

import java.util.Set;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToMany;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String username;

    @Column(nullable = false)
    private String password;

    @Column(nullable = false)
    private String email;

    private boolean enabled;

    @ManyToOne
    @JoinColumn(name = "organization_id")
    private Organization organization;

    @ManyToMany(fetch = FetchType.EAGER)
    private Set<Role> roles;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public boolean isEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }

    public Set<Role> getRoles() {
        return roles;
    }

    public void setRoles(Set<Role> roles) {
        this.roles = roles;
    }

    public Organization getOrganization() {
        return organization;
    }

    public void setOrganization(Organization organization) {
        this.organization = organization;
    }

}

```

## ../src\main\java\com\hot\ticket\repository\OrganizationRepository.java

```
package com.hot.ticket.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.hot.ticket.model.Organization;

@Repository
public interface OrganizationRepository extends JpaRepository<Organization, Long> {
}

```

## ../src\main\java\com\hot\ticket\repository\RoleRepository.java

```
package com.hot.ticket.repository;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.hot.ticket.model.Role;

@Repository
public interface RoleRepository extends JpaRepository<Role, Long> {
    Optional<Role> findByName(String name);
}
```

## ../src\main\java\com\hot\ticket\repository\ServiceRepository.java

```
package com.hot.ticket.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.hot.ticket.model.Service;

@Repository
public interface ServiceRepository extends JpaRepository<Service, Long> {
}
```

## ../src\main\java\com\hot\ticket\repository\TicketRepository.java

```
package com.hot.ticket.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.hot.ticket.model.Service;
import com.hot.ticket.model.Ticket;

@Repository
public interface TicketRepository extends JpaRepository<Ticket, Long> {
    public List<Ticket> findByStatusAndService(String status, Service service);
}

```

## ../src\main\java\com\hot\ticket\repository\UserRepository.java

```
package com.hot.ticket.repository;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.hot.ticket.model.User;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByUsername(String username);
}

```

## ../src\main\java\com\hot\ticket\service\TicketService.java

```
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
        return String.valueOf(System.currentTimeMillis()); // ví dụ đơn giản
    }

    public void callNextTicket(Long ticketId) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'callNextTicket'");
    }
}

```

## ../src\main\java\com\hot\ticket\service\UserDetailsServiceImpl.java

```
package com.hot.ticket.service;

import java.util.Collection;
import java.util.stream.Collectors;

import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import com.hot.ticket.model.User;
import com.hot.ticket.repository.UserRepository;

@Service
public class UserDetailsServiceImpl implements UserDetailsService {

    private final UserRepository userRepository;

    public UserDetailsServiceImpl(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User user = userRepository.findByUsername(username)
                .orElseThrow(() -> new UsernameNotFoundException("User not found"));

        return new org.springframework.security.core.userdetails.User(user.getUsername(), user.getPassword(),
                getAuthorities(user));
    }

    private Collection<? extends GrantedAuthority> getAuthorities(User user) {
        return user.getRoles().stream()
                .map(role -> new SimpleGrantedAuthority(role.getName()))
                .collect(Collectors.toList());
    }

}

```

## ../src\main\java\com\hot\ticket\service\UserService.java

```
package com.hot.ticket.service;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import com.hot.ticket.model.User;
import com.hot.ticket.repository.UserRepository;

@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;

    public User save(User user) {
        user.setPassword(passwordEncoder.encode(user.getPassword()));
        user.setEnabled(true);
        return userRepository.save(user);
    }

    public Optional<User> findByUsername(String username) {
        return userRepository.findByUsername(username);
    }
}

```

## ../src\main\resources\application.properties

```
spring.application.name=ticket
# MySQL Configuration
spring.datasource.url=jdbc:mysql://localhost:3306/ticket?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC
spring.datasource.username=admin
spring.datasource.password=admin@2024
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

# Hibernate Configuration
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
# spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQL5Dialect

# Security Config
spring.security.user.name=admin
spring.security.user.password=admin123
```

## ../src\main\resources\static\css\styles.css

```
body,
html {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  height: 100%;
}

.header {
  background-color: #065482;
  color: white;
  text-align: center;
  padding: 20px;
  margin-bottom: 10px;
}

.footer {
  background-color: #065482;
  color: white;
  text-align: center;
  margin: 10px 0px 0px 0px;
  padding: 10px;
}

.footer p {
  text-align: center;
}

.main {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.receipt {
  margin: 10px;
  padding: 10px;
  border: 2px solid #065482;
  text-align: center;
  width: 90%;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

div .receipt-header {
  font-size: 30px;
}
div .receipt-body {
  color: #065482;
  font-size: 70px;
  padding: 10px;
  margin: 10px;
}

.receipt span {
  color: #333;
}

.receipt h1 {
  color: #007bff;
  font-size: 70px;
}

.status {
  color: #c9213a;
  border: solid 2px #c9213a;
  width: 90%;
  padding: 10px;
  margin: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.status h1 {
  margin: 10px 0;
}
div .text-right {
  text-align: right;
}
div .text-left {
  text-align: left;
}
div .text-center {
  text-align: center;
  font-size: 70px;
}

.status p {
  margin: 5px 0;
  color: #000;
  text-align: center;
  margin: 10px 10px 10px 10px;
}

.call-by-text {
  background-color: #f0f0f0;
  border: solid 2px #147e08bc;
  width: 90%;
  padding: 10px;
  margin: 10px;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.call-by-text h3 {
  color: #e3e6ea;
  background-color: #147e08bc;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 15px;
  /* flex-grow: 1; */
  /* width: 100%; */
  margin: 0px 0px 0px 0px;
}

.call-by-text p {
  color: #333;
}

```

## ../src\main\resources\static\demo\ticket.html

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ticket System</title>
    <!-- <link rel="stylesheet" href="css/styles.css"> -->
    <style>
        body,
        html {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            height: 100%;
        }

        .header {
            background-color: #065482;
            color: white;
            text-align: center;
            padding: 20px;
            margin-bottom: 10px;
        }

        .footer {
            background-color: #065482;
            color: white;
            text-align: center;
            margin: 10px 0px 0px 0px;
            padding: 10px;
        }

        .footer p {
            text-align: center;
        }

        .main {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .receipt {
            margin: 10px;
            padding: 10px;
            border: 2px solid #065482;
            text-align: center;
            width: 90%;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        div .receipt-header {
            font-size: 30px;
        }

        div .receipt-body {
            color: #065482;
            font-size: 70px;
            padding: 10px;
            margin: 10px;
        }

        .receipt span {
            color: #333;
        }

        .receipt h1 {
            color: #007bff;
            font-size: 70px;
        }

        .status {
            color: #c9213a;
            border: solid 2px #c9213a;
            width: 90%;
            padding: 10px;
            margin: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .status h1 {
            margin: 10px 0;
        }

        div .text-right {
            text-align: right;
        }

        div .text-left {
            text-align: left;
        }

        div .text-center {
            text-align: center;
            font-size: 70px;
        }

        .status p {
            margin: 5px 0;
            color: #000;
            text-align: center;
            margin: 10px 10px 10px 10px;
        }

        .call-by-text {
            background-color: #f0f0f0;
            border: solid 2px #147e08bc;
            width: 90%;
            padding: 10px;
            margin: 10px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .call-by-text h3 {
            color: #e3e6ea;
            background-color: #147e08bc;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 15px;
            /* flex-grow: 1; */
            /* width: 100%; */
            margin: 0px 0px 0px 0px;
        }

        .call-by-text p {
            color: #333;
        }
    </style>
</head>

<body>
    <div class="header">
        <h1>Cục Xuất Nhập Cảnh</h1>
        <h2>Tiếp Nhận Hồ Sơ</h2>
    </div>
    <div class="main">
        <div class="receipt">
            <div class="receipt-header">Số Thứ Tự</div>
            <div class="receipt-body">374</div>
        </div>
        <div class="status">
            <div class="text-left">Bạn đứng thứ</div>
            <div class="text-center">4</div>
            <div class="text-right">trong hàng đợi.</div>
            <p>Cập nhật mới nhất: 2023/12/28 12:41:48.</p>
        </div>
        <div class="call-by-text">
            <h3>Thông tin dịch vụ</h3>
            <p>Bạn sẽ nhận được thông báo khi số của bạn sắp được gọi.</p>
            <p>Chờ gọi tên và đến quầy dịch vụ</p>
        </div>
    </div>
    <div class="footer">
        <p>Copyright 2024</p>
    </div>
</body>

</html>
```

## ../src\main\resources\templates\index.html

```
Helloworld
```

## ../src\main\resources\templates\login.html

```
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Login</title>
</head>
<body>
    <form th:action="@{/login}" method="post">
        <div>
            <label>Username:</label>
            <input type="text" name="username"/>
        </div>
        <div>
            <label>Password:</label>
            <input type="password" name="password"/>
        </div>
        <div>
            <button type="submit">Login</button>
        </div>
    </form>
</body>
</html>

```

## ../src\main\resources\templates\register.html

```
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Register</title>
</head>
<body>
    <form th:action="@{/register}" th:object="${user}" method="post">
        <div>
            <label>Username:</label>
            <input type="text" th:field="*{username}"/>
        </div>
        <div>
            <label>Password:</label>
            <input type="password" th:field="*{password}"/>
        </div>
        <div>
            <label>Email:</label>
            <input type="email" th:field="*{email}"/>
        </div>
        <div>
            <button type="submit">Register</button>
        </div>
    </form>
</body>
</html>

```

## ../src\main\resources\templates\org\new-ticket.html

```
<!-- new-ticket.html -->
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Chọn Dịch Vụ</title>
</head>
<body>
    <h1>Chọn Dịch Vụ</h1>
    <form action="/ticket/new" method="post">
        <select name="serviceId">
            <option th:each="service : ${services}" th:value="${service.id}" th:text="${service.name}"></option>
        </select>
        <button type="submit">Lấy Số</button>
    </form>
</body>
</html>
```

## ../src\main\resources\templates\org\services.html

```
<!-- new-ticket.html -->
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Chọn Dịch Vụ</title>
</head>
<body>
    <h1>Chọn Dịch Vụ</h1>
    <form action="/ticket/new" method="post">
        <select name="serviceId">
            <option th:each="service : ${services}" th:value="${service.id}" th:text="${service.name}"></option>
        </select>
        <button type="submit">Lấy Số</button>
    </form>
</body>
</html>
```

## ../src\test\java\com\hot\ticket\TicketApplicationTests.java

```
package com.hot.ticket;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class TicketApplicationTests {

	@Test
	void contextLoads() {
	}

}

```

