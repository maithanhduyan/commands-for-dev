package com.example.snakegame.config;

import com.example.snakegame.handler.SnakeWebSocketHandler;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.socket.config.annotation.*;

@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {

    private final SnakeWebSocketHandler snakeWebSocketHandler;

    public WebSocketConfig(SnakeWebSocketHandler snakeWebSocketHandler) {
        this.snakeWebSocketHandler = snakeWebSocketHandler;
    }

    @SuppressWarnings("null")
    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(snakeWebSocketHandler, "/examples/websocket/snake").setAllowedOrigins("*");
    }
}
