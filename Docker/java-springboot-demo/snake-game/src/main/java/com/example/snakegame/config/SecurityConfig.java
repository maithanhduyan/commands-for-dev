package com.example.snakegame.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            // Cho phép truy cập ẩn danh vào các tài nguyên tĩnh và các URL cụ thể
            .authorizeHttpRequests(authorize -> authorize
                .requestMatchers(
                    "/login.html",
                    "/api/auth/login",
                    "/register.html",
                    "/api/auth/register",
                    "/css/**",
                    "/js/**",
                    "/images/**",
                    "/sounds/**",
                    "/webjars/**",
                    "/game-oop.js",
                    "/"
                ).permitAll()
                .anyRequest().authenticated()
            )
            // Cấu hình trang đăng nhập tùy chỉnh (nếu có)
            .formLogin(form -> form
                .loginPage("/login.html") // Trang đăng nhập tùy chỉnh
                .permitAll()
            )
            // Cho phép đăng xuất
            .logout(logout -> logout.permitAll())
            // Vô hiệu hóa CSRF (nếu cần, nhưng cần cân nhắc bảo mật)
            .csrf(csrf -> csrf.disable());

        return http.build();
    }
}
