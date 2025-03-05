package com.example.week5;

import java.util.List;
import java.util.Optional;

import org.hibernate.internal.util.collections.ConcurrentReferenceHashMap.Option;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

@Repository
public interface MemberRepository extends JpaRepository<Member, Long> {
    
    Optional<Member> findByName(String userId);

    @Query("SELECT m FROM Member m WHERE m.age between 20 and 29")
    List<Member> twentyGenerateMembers();

    @Query("SELECT m FROM Member m WHERE m.age between :stratAge and :endAge")
    List<Member> findMemberByAgeBetween(@Param("stratAge")int stratAge , @Param("endAge") int endAge);
}


