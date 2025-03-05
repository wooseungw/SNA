package com.example.week5;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;
import lombok.extern.slf4j.Slf4j;

@Entity
@Getter @Setter @NoArgsConstructor @ToString
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
    private String password;

    public Member(String name, String email, int age, String userId, String password){
        this.name = name;
        this.age = age;
        this.email = email;
        this.userId = userId;
        this.password = password;
    }
    

    public void logMemberInfo(){
        log.info("Member Info: - Id: {}, Email: {}, Age: {}", id, email, age);
    }

}
