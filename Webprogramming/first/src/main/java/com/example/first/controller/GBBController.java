package com.example.first.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.ArrayList;

@Controller
public class GBBController {

    // 생성자: GBBController 객체가 만들어질 때 호출됨
    public GBBController() {
        System.out.println("Hello GBB Controller~~ ^^^^^^^^");
    }

    @GetMapping("/gbb/{my}")
    @ResponseBody
    public String gbb(@PathVariable("my") int my){
        // 반환할 HTML 내용을 담을 문자열
        String html = "";
        // GBBGame 객체 생성 (이미지 파일명들을 전달)
        GBBGame game = new GBBGame("gawi.png, bawi.png, bo.png", "draw.png, win.png, lose.png");

        // 게임 실행 (사용자의 선택을 전달)
        game.run(my);

        // 게임 결과에 따른 이미지 파일명들 가져오기
        String myImg = game.showMyImg();    // 내가 낸 이미지
        String comImg = game.showComImg();  // 컴퓨터가 낸 이미지
        String result = game.getDetImg();   // 게임 결과 이미지

        // 중앙 정렬을 위한 CSS 스타일
        String centerDiv = "display: flex; justify-content: center; align-items: center; height: 600px;";

        // HTML 내용 작성
        html += "<h2>게임 결과</h2>";
        html += String.format("<div style='%s'>", centerDiv);
        html += "내가 낸 것: ";
        html += String.format("<img src='/img/gbb/%s' width='225' height='225'>", myImg);
        html += "컴퓨터가 낸 것: ";
        html += String.format("<img src='/img/gbb/%s' width='225' height='225'>", comImg);
        html += "결과: ";
        html += String.format("<img src='/img/gbb/%s' width='161' height='500'><br>", result);
        html += "</div>";
        // 다시 시작할 수 있는 링크 추가
        html += "<a href='/gbb.html'>다시 시작</a>";

        // 완성된 HTML 문자열 반환
        return html;
    }
}

/**
 * 가위바위보 게임을 처리하는 클래스
 */
class GBBGame {
    private int my; // 내가 낸 것 (0, 1, 2)
    private int com; // 컴퓨터가 낸 것 (0, 1, 2)
    private ArrayList<String> gbbImg = new ArrayList<>(); // 가위바위보 이미지 파일명 리스트
    private ArrayList<String> detImg = new ArrayList<>(); // 결과 이미지 파일명 리스트

    /**
     * 생성자: 이미지 파일명들을 받아서 리스트에 저장
     * gbb: 가위바위보 이미지 파일명들 (쉼표로 구분된 문자열)
     * det: 결과 이미지 파일명들 (쉼표로 구분된 문자열)
     */
    public GBBGame(String gbb, String det) {
        // 가위바위보 이미지 파일명들을 리스트에 추가
        for(String img: gbb.split(",")){
            gbbImg.add(img.trim());
        }
        // 결과 이미지 파일명들을 리스트에 추가
        for(String img: det.split(",")){
            detImg.add(img.trim());
        }
    }

    // 게임을 실행하는 메서드
    // my: 내가 낸 것
    public void run(int my) {
        this.my = my; // 내가 낸 것 저장
        getCom();     // 컴퓨터가 낼 것 결정
    }

    // 컴퓨터가 낼 것을 결정하는 메서드
    public void getCom(){
        // 0부터 2까지의 랜덤한 숫자 생성 (가위, 바위, 보)
        this.com = (int) (Math.random() * 3);
    }

    // 게임 결과를 계산하는 메서드(0: 무승부, 1: 승리, 2: 패배)
    public int detResult() {
        // 가위바위보 승패를 결정하는 공식
        return (my - com + 3) % 3;
    }

    // 내가 낸 것의 이미지 파일명을 반환하는 메서드
    public String showMyImg() {
        return gbbImg.get(my);
    }

    
    // 컴퓨터가 낸 것의 이미지 파일명을 반환
    public String showComImg() {
        return gbbImg.get(com);
    }

    
    // 게임 결과에 따른 이미지 파일명을 반환
    public String getDetImg(){
        // detResult()의 결과에 해당하는 이미지 파일명 반환
        return detImg.get(detResult());
    }
}
