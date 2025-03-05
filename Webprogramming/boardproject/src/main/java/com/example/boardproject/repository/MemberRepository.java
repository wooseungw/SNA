package com.example.boardproject.repository;

import org.springframework.stereotype.Repository;

import com.example.boardproject.entity.Member;

import org.springframework.data.jpa.repository.JpaRepository;

@Repository
public interface MemberRepository  extends JpaRepository<Member, Long>{

}
