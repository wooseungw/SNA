package com.example.midexam;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface MemberRepository extends JpaRepository<Member, Long> {


    Optional<Member> findByUserId(String userId);

    //email을 기반으로 Member 가져오기
    Optional<Member> findByEmail(String email);

    //20대인 Member 리스트 가져오기
    @Query("SELECT m from Member m where m.age between 20 and 29")
    List<Member> twentyGenerateMembers();

    //X세대인 Member 리스트 가져오기
    @Query("SELECT m from Member m where m.age between :startAge and :endAge")
    List<Member> getGenerationMembers(@Param("startAge") int startAge, @Param("endAge")int endAge);

}