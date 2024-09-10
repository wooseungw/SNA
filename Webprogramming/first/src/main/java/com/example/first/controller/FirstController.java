package com.example.first.controller;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
// 데이터 핸들링하기 위한 클래스가 Model, 여기에 Attribute함수가 있음
import org.springframework.ui.Model;

@Controller
public class FirstController {
    //Get 방식의 path 처리
    @GetMapping("/greetings")
    public String greetings() {
        // return에는 처리할 view를 넣어야함 Templates 폴더에 있는 mustache 파일명을 넣어줌
        return "greetings";
    }

    @GetMapping("/greetings2")
    public String greetings2(Model model) {
        // model에 데이터를 넣어서 view로 넘겨줌
        // Attribute라는 방식을 사용해서 데이터를 넘겨줌
        // 변수의 name과 value를 넣어줘야함
        model.addAttribute("name","조정석");
        return "greetings2";
    }

    @GetMapping("/bye")
    public String bye(Model model) {
        model.addAttribute("name","조정석");
    
        return "bye";
    }

    
    
}



