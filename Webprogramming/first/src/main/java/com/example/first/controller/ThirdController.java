package com.example.first.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class ThirdController {
    int cnt = 0;
    @GetMapping("/count3")
    @ResponseBody
    public String count3(Model model) {
        cnt ++;
        String countString = Integer.toString(cnt);
        String OutputString = "";
        for (int i = 0; i < countString.length(); i++) {
            String str = String.format("<h1>"+countString.charAt(i)+"</h1>");
            //String str = String.format("<img src = 'img/number/%c.png' alt='%c' width = '100' height='100'>", countString.charAt(i));
            OutputString = OutputString + str;
        }
        
        return OutputString;
    }
}
