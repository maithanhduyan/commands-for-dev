package com.example.snakegame.controller;

import com.example.snakegame.model.User;
import com.example.snakegame.service.UserService;

import jakarta.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/auth")
public class AuthController extends BaseController {

    private final UserService userService;

    @Autowired
    public AuthController(UserService userService) {
        this.userService = userService;
    }

    @PostMapping("/register")
    public ResponseEntity<String> register(@RequestBody UserDto userDto) {
        User user = userService.registerUser(userDto.getUsername(), userDto.getPassword());
        return ResponseEntity.ok("Đăng ký thành công!");
    }

    @PostMapping("/login")
    public ResponseEntity<String> login(@RequestBody UserDto userDto, HttpSession session) {
        return userService.loginUser(userDto.getUsername(), userDto.getPassword())
                .map(user -> {
                    // Lưu thông tin người dùng vào session
                    session.setAttribute("user", user);
                    return ResponseEntity.ok("Đăng nhập thành công!");
                })
                .orElseGet(
                        () -> ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("Sai tên đăng nhập hoặc mật khẩu!"));
    }

    // Lớp DTO để nhận dữ liệu từ client
    public static class UserDto {
        private String username;
        private String password;

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
}
