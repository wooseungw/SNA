package com.example.midexam;
// 엔티티 작성

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.Setter;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Entity
@Getter @Setter @NoArgsConstructor @AllArgsConstructor
@Slf4j
public class Member {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String email;
    private int age;

    @Column(name = "userid")  
    private String userId;

    @Column(name = "password")
    private String userPwd;

    

    public Member(String name, String email, int age, String userId, String userPwd) {
        this.name = name;
        this.email = email;
        this.age = age;
        this.userId = userId;
        this.userPwd = userPwd;
     
    }
    

    public void logMemberInfo() {
        log.info("Member Info: ID : {}, Name: {}, Email: {}, Age: {}", id, name, email, age);
    }
}
