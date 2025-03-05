package com.example.week5;

import java.util.List;

import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;

@Repository
public interface MemberService{


    List<Member> getMemberList();

    Member findMemberById(String userId);
    

    Member findMemberByEmail(String email);

    Member findMemberByName(String name);

    List<Member> getMenMemberListOrderByAgeDesc();

    boolean validMember(String userId, String password);

    public List<Member> getGenration(int generation);
}