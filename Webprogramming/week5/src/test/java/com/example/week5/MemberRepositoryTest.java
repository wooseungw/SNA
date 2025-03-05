package com.example.week5;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;
import java.util.List;
import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;



@SpringBootTest
class Week5ApplicationTests {

	@Test
	void contextLoads() {
	}


}
@SpringBootTest
public class MemberRepositoryTest {

	private final MemberRepository memberRepository;
	
	// 호출될때만 생성되는 생성자니 이게 더 안전한 방식이다.
	// 의존성 주입, 생성자 위에쓴는 방법
	@Autowired
	public MemberRepositoryTest(MemberRepository memberRepository){
		this.memberRepository = memberRepository;
		List<Member> members = new ArrayList<>() {{
			add(new Member("Alice", "qwd@wve.net", 30, "alice", "1234"));
			add(new Member("Bob", "qd", 25, "bob", "1234"));
			add(new Member("Tom", "qdqw", 35, "tom", "1234"));
			add(new Member("Tom", "qdqw@cwc.vom", 21, "tom", "1234"));
		}};
		memberRepository.saveAll(members);
	}
	
	@Test
    void findByName() {
        Optional<Member> member = memberRepository.findByName("Alice");
        if (member.isPresent()) {
            System.out.println(member.get());
        } else {
            System.out.println("Member를 찾을 수 없습니다.");
        }
    }

    @Test
    void twentyGenerateMembers() {
        List<Member> members = memberRepository.twentyGenerateMembers();
        if (!members.isEmpty()) {
            members.forEach(System.out::println);
        } else {
            System.out.println("Member를 찾을 수 없습니다.");
        }
    }
	@Test
	void findMemberByAgeBetween() {
		List<Member> members = memberRepository.findMemberByAgeBetween(20, 29);
		if(!members.isEmpty()) members.forEach(System.out::println);
		else System.out.println("Member를 찾을 수 없습니다.");
	}

	@Test
	@Transactional
	void contextLoads() {
		Member member1 = new Member("Alice","alice@aaa.net", 30, "alice", "1234");
		Member member2 = new Member("Bob","bob@aaa.net", 25, "bob", "1234");	
		Member member3 = new Member("Bob","bob@aaa.net", 95, "bob", "1234");	
		memberRepository.save(member1);
		memberRepository.save(member2);
		memberRepository.save(member3);

		member1.logMemberInfo();
		member2.logMemberInfo();
		member3.logMemberInfo();

		Optional<Member> serachmember = memberRepository.findById(4L);
		if(serachmember.isPresent()) System.out.println(serachmember.get());
		else System.out.println("Member를 찾을 수 없습니다.");

		//4-1. Member List 가져오기
		List<Member> memberLlist = memberRepository.findAll();
		for(Member member: memberLlist) System.out.println(member);
		//4-2. Member List 가져오기 2 (나이순으로 정렬 )
		List<Member> memberListByAge =
		memberRepository.findAll(Sort.by(Sort.Direction.DESC,
		"age"));
		for(Member member: memberListByAge) System.out.println(member);
		//5. Member 객수 출력
		long count = memberRepository.count();
		System.out.println("Number of Members: " + count);
	}

}
