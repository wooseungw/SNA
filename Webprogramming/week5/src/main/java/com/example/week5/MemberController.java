package com.example.week5;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class MemberController {
    @Autowired
    private MemberService memberService;

    @GetMapping("/list")
    public String getMemberList(Model model) {
        
        model.addAttribute("members", memberService.getMemberList());
        return "memberlist";
    }

    @GetMapping("/list2")
    public String getMemberListOrderByAge(Model model) {
        model.addAttribute("members", memberService.getMenMemberListOrderByAgeDesc());
        return "memberlist";
    }

    @GetMapping("/list3")
    public String getGeneration(Model model) {
        model.addAttribute("members", memberService.getGenration(20));
        return "memberlist";
    }

}
