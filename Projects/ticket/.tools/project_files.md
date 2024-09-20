# Cấu trúc Dự án

```
├── .dockerignore
├── .gitignore
├── Dockerfile
├── HELP.md
├── README.md
├── compose.yaml
├── logs
│   └── ticket.log
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
    │   │               │   ├── TicketDto.java
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
    │       │   │   ├── thymeleaf.html
    │       │   │   └── ticket.html
    │       │   └── js
    │       └── templates
    │           ├── account
    │           │   └── my-account.html
    │           ├── error
    │           │   └── 404.html
    │           ├── index.html
    │           ├── login.html
    │           ├── org
    │           │   ├── new-ticket.html
    │           │   ├── service
    │           │   │   ├── add-new-service.html
    │           │   │   ├── services.html
    │           │   │   └── table-service.html
    │           │   └── ticket
    │           │       ├── ticket-confirmation.html
    │           │       ├── ticket-details.html
    │           │       └── ticket-error.html
    │           └── register.html
    └── test
        └── java
            └── com
                └── hot
                    └── ticket
                        └── TicketApplicationTests.java
```

# Danh sách Các Tệp Dự án

## ../Dockerfile

```
# Giai đoạn 1: Sử dụng Maven image để build dự án
FROM maven:3.9.9-ibm-semeru-21-jammy AS builder

# Đặt thư mục làm việc trong container
WORKDIR /app

# Copy file pom.xml và các file cấu hình Maven
COPY pom.xml ./
COPY src ./src

# Build ứng dụng
RUN mvn clean package -DskipTests

# Giai đoạn 2: sử dụng OpenJDK để chạy ứng dụng
FROM openjdk:21

# Tạo một thư mục cho ứng dụng
VOLUME /tmp

# Copy file JAR từ giai đoạn build trước vào container
COPY --from=builder /app/target/*.jar app.jar

# Chạy ứng dụng Spring Boot
ENTRYPOINT ["java", "-jar", "/app.jar"]

# Expose port 8080
EXPOSE 8080


```

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
	<description>Ticket project for Spring Boot</description>
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
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
		<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
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
                        .requestMatchers("/register", "/login", "/css/**", "/js/**","/ticket/ticket-details").permitAll()
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
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import com.hot.ticket.dto.UserDto;
import com.hot.ticket.model.User;
import com.hot.ticket.repository.UserRepository;
import com.hot.ticket.service.UserService;

@Controller
public class AuthController {

    @Autowired
    private UserService userService;

    @Autowired
    private UserRepository userRepository;

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

    @GetMapping("/my-account")
    public String myAccount(Authentication authentication, Model model) {
        User _user = null;
        if (authentication != null) {
            // Giả sử bạn có một lớp UserDetails tùy chỉnh
            UserDetails userDetails = (UserDetails) authentication.getPrincipal();

            // Lấy thông tin từ đối tượng tùy chỉnh của bạn
            String username = userDetails.getUsername();

            _user = userRepository.findByUsername(username).get();

        }

        model.addAttribute("user", _user);
        return "account/my-account";
    }
}

```

## ../src\main\java\com\hot\ticket\controller\ServiceController.java

```
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

```

## ../src\main\java\com\hot\ticket\controller\TicketController.java

```
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
```

## ../src\main\java\com\hot\ticket\data\DataInitializer.java

```
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
        String description = "Bạn sẽ nhận được thông báo khi số của bạn sắp được gọi. Chờ gọi tên và đến quầy dịch vụ";
        createServiceDemo("ACB", "Dịch Vụ Thẻ", description);
        createServiceDemo("ACB", "Dịch Vụ Vay", description);
        createServiceDemo("ACB", "Dịch Vụ Gủi Tiền", description);
        createServiceDemo("ACB", "Dịch Vụ Rút Tiền", description);
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
            Organization _org = new Organization();
            User _user = userRepository.findByUsername("admin").get();
            _org.setName(name);
            _org.addUser(_user);
            _org.setCreateBy(_user.getUsername());
            organizationRepository.save(_org);
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

    private void createServiceDemo(String orgName, String serviceName, String description) {
        Optional<Organization> orgOptional = organizationRepository.findByName(orgName);
        Optional<Service> serviceOptional = serviceRepository.findByName(serviceName);
        if (!orgOptional.isPresent()) {

        } else {
            if (!serviceOptional.isPresent()) {
                Service service = new Service();
                service.setName(serviceName);
                service.setDescription(description);
                service.setOrganization(orgOptional.get());
                serviceRepository.save(service);
            }
        }
    }

}

```

## ../src\main\java\com\hot\ticket\dto\TicketDto.java

```
package com.hot.ticket.dto;

import com.hot.ticket.model.Organization;

public class TicketDto {
    String id;
    private String ticketNumber;
    private String status; // "Đang chờ", "Đang gọi", "Hết hạn"
    private String qrCode; // Mã QR
    private Organization organization;

    public String getId() {
        return id;
    }

    public void setId(String id) {
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

    public Organization getOrganization() {
        return organization;
    }

    public void setOrganization(Organization organization) {
        this.organization = organization;
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
    private String createBy;

    @OneToMany(mappedBy = "organization")
    private List<Service> services;

    @OneToMany(mappedBy = "organization")
    private List<User> users;

    /**
     * return 0 : fail
     * return 1 : success
     * return 2 : exist
     */
    public int addUser(User user) {
        try {
            if (!this.users.contains(user)) {
                this.users.add(user);
            } else {
                return 2;
            }
        } catch (Exception e) {
            return 0;
        }
        return 1;
    }

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

    public String getCreateBy() {
        return createBy;
    }

    public void setCreateBy(String createBy) {
        this.createBy = createBy;
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
    private String description;
    
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

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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

import java.util.List;

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
    private List<Role> roles;

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

    public List<Role> getRoles() {
        return roles;
    }

    public void setRoles(List<Role> roles) {
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

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.hot.ticket.model.Organization;

@Repository
public interface OrganizationRepository extends JpaRepository<Organization, Long> {
    Optional<Organization> findByName(String name);
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

    public Ticket findById(Long id) {
        return ticketRepository.findById(id).orElse(null);
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
# ===============================
# WEB SERVER
# ===============================
# server.address=0.0.0.0
# server.compression.enabled=true
# server.http2.enabled=true
# server.port=8080
# server.tomcat.uri-encoding=UTF-8

spring.application.name=ticket
# spring.http.encoding.charset=UTF-8
# spring.http.encoding.force=true
# spring.messages.encoding=UTF-8
spring.output.ansi.enabled=always
# spring.output.encoding=UTF-8
# spring.output.encoding.force=true
# ===============================
# DATABASE
# ===============================
# MySQL Configuration
# spring.datasource.url=jdbc:mysql://mysqldb:3306/ticket?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC&useUnicode=true&characterEncoding=UTF-8
spring.datasource.url=jdbc:mysql://localhost:3306/ticket?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC&useUnicode=true&characterEncoding=UTF-8
spring.datasource.username=admin
spring.datasource.password=admin@2024
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

# ===============================
# JPA / HIBERNATE
# ===============================
# Hibernate Configuration
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
# spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQL5Dialect

# ===============================
# Security Config
# ===============================
spring.security.user.name=admin
spring.security.user.password=admin123

# ===============================
# Logging
# ===============================
# logging.level.org.springframework.web=DEBUG
# logging.level.org.hibernate=DEBUG
logging.file.name=logs/ticket.log
logging.file.encoding=UTF-8
#logging.pattern.console= %d{yyyy-MMM-dd HH:mm:ss.SSS} %-5level [%thread] %logger{15} - %msg%n

# ===============================
# THYMELEAF
# ===============================
#spring.thymeleaf.cache=true
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

## ../src\main\resources\static\demo\thymeleaf.html

```
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">

<head>
    <meta charset="UTF-8">
    <title>Thymeleaf</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>

</body>

</html>
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
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org" xmlns:sec="http://www.thymeleaf.org/extras/spring-security">

<head>
    <meta charset="UTF-8">
    <title>Ticket</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>
    <h1>Ticket</h1>
    <p>Chào mừng, <a th:href="@{/my-account}" th:text="${#authentication.name}"></a>! &nbsp; </p>
    <div th:if="${#authentication?.name != null}">
        <!-- Nội dung cho người dùng đã đăng nhập -->
        <p><a th:href="@{/service/my-services}">Dịch Vụ</a></p>
    </div>
    <div th:unless="${#authentication?.name != null}">
        <h1>Chào mừng, Khách!</h1>
        <p><a th:href="@{/login}">Đăng nhập</a> hoặc <a th:href="@{/register}">Đăng ký</a> để tiếp tục.</p>
    </div>

    <p><a th:href="@{/logout}">Đăng xuất</a></p>
</body>

</html>
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

## ../src\main\resources\templates\account\my-account.html

```
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">

<head>
    <meta charset="UTF-8">
    <title>Tài khoản của tôi</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>
    <p><a th:href="@{/}">Trở lại</a></p>
    Tài khoản của tôi <br>
    <p><span th:text="${user.username}">Username</span></p>

</body>

</html>
```

## ../src\main\resources\templates\error\404.html

```
404 Error! 
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

## ../src\main\resources\templates\org\service\add-new-service.html

```
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">

<head>
    <meta charset="UTF-8">
    <title>Thymeleaf</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>
    <p><a th:href="@{/service/my-services}">Trở lại</a></p>
    <h1>Thêm Dịch vụ mới</h1>
    <form th:action="@{/service/add}" method="post" th:object="${service}">
        <label>Tên dịch vụ:</label>
        <input type="text" th:field="*{name}" /><br/>
        <label>Mô tả:</label>
        <input type="text" th:field="*{description}" /><br/>
        <button type="submit">Lưu</button>
    </form>
</body>

</html>
```

## ../src\main\resources\templates\org\service\services.html

```
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">

<head>
    <title>Dịch Vụ</title>
</head>

<body>
    <p><a th:href="@{/}">Trở lại</a></p>
    <h1>Danh Sách Dịch Vụ</h1>
    <a th:href="@{/service/add}">Thêm mới</a>
    <table border="1">
        <tr>
            <th>ID</th><th>Tên dịch vụ</th>
        </tr>
        <tr th:each="service : ${services}">
            <td th:text="${service.id}">1</td>
            <td>
                <a th:href="@{/service/}" th:text="${service.name}">dịch vụ</a>
            </td>
        </tr>
    </table>
</body>

</html>
```

## ../src\main\resources\templates\org\service\table-service.html

```
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">

<head>
    <meta charset="UTF-8">
    <title>Thymeleaf</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>
    <h1>Bàn Dịch Vụ</h1>
    <h3>Chọn Dịch Vụ</h3>
    <form th:action="@{/ticket/new}" method="post">
        <select name="serviceId">
            <option th:each="service : ${services}" th:value="${service.id}" th:text="${service.name}"></option>
        </select>
        <button type="submit">Lấy Số</button>
    </form>
</body>

</html>
```

## ../src\main\resources\templates\org\ticket\ticket-confirmation.html

```
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">

<head>
    <meta charset="UTF-8">
    <title>Thymeleaf</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>
    <h1>Vé <span th:text="${ticket.ticketNumber}"></span>!</h1>
</body>

</html>
```

## ../src\main\resources\templates\org\ticket\ticket-details.html

```
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">

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
        <h1 th:text="${service.organization.name}">Tên Tổ Chức</h1>
        <h2 th:text="${service.name}">Tiếp Nhận Hồ Sơ</h2>
    </div>
    <!-- Hiển thị lỗi nếu có -->
    <div th:if="${error != null}" class="status">
        <h2 class="text-center" style="color:red;" th:text="${error}"></h2>
    </div>

    <div class="main" th:unless="${error != null}">
        <div class="receipt">
            <div class="receipt-header">Số Thứ Tự</div>
            <div class="receipt-body" th:text="${ticket.ticketNumber}">374</div>
        </div>
        <div class="status">
            <div class="text-left">Bạn đứng thứ</div>
            <div class="text-center">4</div>
            <div class="text-right">trong hàng đợi.</div>
            <p>Cập nhật mới nhất: 2023/12/28 12:41:48.</p>
        </div>
        <div class="call-by-text">
            <h3>Thông tin dịch vụ</h3>
            <p th:utext="${service.description}">Bạn sẽ nhận được thông báo khi số của bạn sắp được gọi.</p>
        </div>
    </div>
    <div class="footer">
        <p>Copyright &copy;2024</p>
    </div>
</body>

</html>
```

## ../src\main\resources\templates\org\ticket\ticket-error.html

```
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">

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
        <h1>Tên Tổ Chức</h1>
        <h2>Tiếp Nhận Hồ Sơ</h2>
    </div>
    <!-- Hiển thị lỗi nếu có -->
    <div th:if="${error != null}" class="status">
        <h2 class="text-center" style="color:red;" th:text="${error}"></h2>
    </div>

    <div class="main" th:unless="${error != null}">
        <div class="receipt">
            <div class="receipt-header">Số Thứ Tự</div>
            <div class="receipt-body" th:text="${ticket.ticketNumber}">374</div>
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

