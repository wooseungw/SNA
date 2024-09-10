package com.example.first.controller;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.time.LocalDate;

@Controller
public class SecondController {
    @GetMapping("/responsebody")
    @ResponseBody
    // ResponseBody는 view를 거치지 않고 바로 데이터를 보내줌
    // json 파일이나 xml 등을 파싱할때 사용
    public String ResponseBody() {
        return "<h1>Response Body</h1>";
    }
    
    @GetMapping("/now")
    @ResponseBody
    public String now() {
        String resultString = "<br><h1 style=\\\"text-align: center;\\\">현재날짜 : " + LocalDate.now() + "</h1>";
        return resultString;
    }
    

    int cnt = 0;
    @GetMapping("/count")
    @ResponseBody
    public String count() {
        cnt ++;
        String resultString = String.format("<br><h1 style=\\\"text-align: center;\\\">카운트 : %d</h1>", cnt);
        return resultString;
    }
}
