package com.example.boardproject.api;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;



@RestController
public class ApiContoller {

    @GetMapping("/api/hello")
    public String hello() {
        return "Hello World!";
    }
    
}
