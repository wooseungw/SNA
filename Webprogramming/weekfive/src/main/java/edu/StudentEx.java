package edu;

public class StudentEx {
    public static void main(String[] args) {
        Student student1 = new Student();
        System.out.println(student1);
        student1.logInfo();

        Student student2 = new Student(1L, "김", "Doe");
        System.out.println(student2);
        student2.logInfo();

        Student student3 = new Student(2L, "Jane", "Jiji");
        System.out.println(student3.getFirstName());
        student3.setFirstName("KKKK");
        student3.logInfo();
    }   
}
