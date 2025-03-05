package com.example.game.gbb1;

import java.util.Scanner;


//if 문장
public class GBBMain {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("0~2(0:가위, 1:바위, 2:보) 사이의 숫자를 입력하시오 => ");
        int my = sc.nextInt();      //0, 1, 2

        int com = (int) (Math.random() * 3);  //0, 1, 2  (int) 0 * 3 <=  (int) Math.random() *3 < (int) 1 *3 실수를 리턴
        System.out.println(com);

        if(my == 0) System.out.println("my: 가위");
        if(my == 1) System.out.println("my: 바위");
        if(my == 2) System.out.println("my: 보");

        if(com == 0) System.out.println("com: 가위");
        if(com == 1) System.out.println("com: 바위");
        if(com == 2) System.out.println("com: 보");

        /*
        비김: 0, 0 or 1, 1 or 2, 2
        이김: 0, 2 or 1, 0 or 2, 1
        짐: 0, 1 or 1, 2 or 2, 0
         */

        if(my == com) System.out.println("비김");
        if(my == 0 && com == 2 || my == 1 && com == 0 || my == 2 && com == 1) System.out.println("이김");
        if(my == 0 && com == 1 || my == 1 && com == 2 || my == 2 && com == 0) System.out.println("짐");

    }
}
