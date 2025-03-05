package com.example.midexam;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class MemberServiceImpl implements MemberService{

    private MemberRepository memberRepository;      //memberRepository 객체 생성 ( Dependency Injection )

    @Autowired
    public MemberServiceImpl(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;

        //memory database
        List<Member> members = new ArrayList<>() {{
            add(new Member("Alice", "alice@aaa.net", 30, "alice", "1111"));
            add(new Member("Bob", "bob@aaa.net", 25, "bob", "1111"));
            add(new Member("Charlie", "charlie@aaa.net", 45, "charlie", "1111"));
            add(new Member("David", "david@aaa.net", 29, "david", "1111"));
            add(new Member("Engela", "engela@aaa.net", 35,  "angela", "1111"));
            add(new Member("Steeve", "steeve@aaa.net", 21, "steeve", "1111"));
        }};

        //멤버 저장 (배치 처리)
        memberRepository.saveAll(members);
    }

    @Override
    public List<Member> getMemberList() {
        List<Member> members = memberRepository.findAll();
        return members;
    }

}