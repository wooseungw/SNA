package com.example.weekfour.controller;

import com.example.weekfour.Person;

import java.lang.reflect.Array;
import java.util.List;
import java.util.Arrays;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;


@Controller
public class myController {
    @GetMapping("/welcome")
    public String welcome(Model model) {
    model.addAttribute("name","John");
    return "welcome"; // templates/welcome.mustache 파일을 렌더링
    }
    // Get인지 Post인지 구분하지 않을때 RequestMapping 사용
    @RequestMapping("/hi")
    public String hi(Model model) {
    model.addAttribute("name","John");
    return "welcome"; // templates/welcome.mustache 파일을 렌더링
    }

    @RequestMapping("/object")
    public String object(Model model) {
    Person person1 = new Person("John", 30, "Developer");
    Person person2 = new Person("박박박", 30, "Developer");
    
    List<Person> people = List.of(person1, person2);
    List<Person> people2 = Arrays.asList(
        person1, 
        person2,
        new Person("김김김", 30, "Developer")   
        );

    String[] fruits = {"apple", "banana", "cherry"};

    boolean isAdmin = true;
    model.addAttribute("isAdmin", isAdmin);
    model.addAttribute("fruits", fruits);
    model.addAttribute("people", people2);
    return "object"; // templates/object.mustache 파일을 렌더링
    }

    @RequestMapping("/partial")
    public String partial(Model model) {
        
        String[] buttons = {"Cancel", "Button", "Submit"};
        model.addAttribute("buttons", buttons);
        model.addAttribute("nonEscape", "<b>Non Escape</b>");
        model.addAttribute("escape", "<b>Escape</b>");
        return "partial"; // templates/partial.mustache 파일을 렌더링
    }

    @RequestMapping("/greeting")
    public String greeting(Model model) {
        model.addAttribute("username", "김박박");
        return "greeting"; // templates/layout.mustache 파일을 렌더링
    }

    @RequestMapping("/bye2")
    public String requestMethodName(Model model) {
        model.addAttribute("username", "김박박");
        return  "bye2"; // templates/bye2.mustache 파일을 렌더링
    }
    
}
