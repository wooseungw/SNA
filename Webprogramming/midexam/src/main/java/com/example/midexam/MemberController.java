package com.example.midexam;

import org.springframework.stereotype.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;




@Controller
public class MemberController {

    @Autowired
    MemberService memberService;

    @GetMapping("/list")
    public String getMemberList(Model model) {

        model.addAttribute("members", memberService.getMemberList());
        return "memberList";
    }

}
