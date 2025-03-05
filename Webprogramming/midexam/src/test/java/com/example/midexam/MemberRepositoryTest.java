package com.example.midexam;

import com.example.midexam.Member;
import com.example.midexam.MemberRepository;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import jakarta.transaction.Transactional;
import java.util.List;


@SpringBootTest
public class MemberRepositoryTest {
    @Autowired
    MemberRepository memberRepository;

    @Test
    @Transactional
    void ContextLoads() {
        Member member = new Member("test", "asf@cads.com", 20, "test", "1234");
        Member member2 = new Member("test2", "asd@asd.com", 30, "test2", "1234");
        
        memberRepository.save(member);
        memberRepository.save(member2);

        member.logMemberInfo();
        member2.logMemberInfo();
       
        memberRepository.findAll().forEach(m -> m.logMemberInfo());
        memberRepository.findById(1L).ifPresent(m -> m.logMemberInfo());
        List<Member> members = memberRepository.findAll();
        for (Member m : members) {
            m.logMemberInfo();
        }
    
    }
}
