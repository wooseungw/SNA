package com.example.boardproject.dto;

import com.example.boardproject.entity.Member;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;
import lombok.extern.slf4j.Slf4j;


@Getter @Setter @NoArgsConstructor @AllArgsConstructor @ToString @Slf4j
public class MemberForm {

    private String email;
    private String password;

    public Member toEntity(){
        return new Member(email, password);
    }

    public void loginfo(){
        log.info("email: {}, password: {}", email, password );
    }
}
