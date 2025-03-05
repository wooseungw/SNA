package com.example.boardproject.controller;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;

import com.example.boardproject.dto.MemberForm;
import com.example.boardproject.entity.Article;
import com.example.boardproject.entity.Member;
import com.example.boardproject.repository.MemberRepository;
import org.springframework.web.bind.annotation.RequestParam;


@Controller
public class MemberController {

    @Autowired
    MemberRepository memberRepository;

    @GetMapping("/members")
    public String memberList(Model model) {
        List<Member> memberList = memberRepository.findAll();
        model.addAttribute("memberList", memberList);
        return "members/index";
    }
    

    @GetMapping("/members/new")
    public String newMember() {
        return "members/register";
    }

    @PostMapping("/members/create")
    public String createMember(MemberForm memberform) {
        memberform.loginfo();

        Member member = memberform.toEntity();
        member.loginfo();

        Member newMember = memberRepository.save(member);
        newMember.loginfo();
        
        return "members/register";
    }

}
