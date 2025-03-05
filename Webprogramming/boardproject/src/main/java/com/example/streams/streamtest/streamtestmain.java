package com.example.streams.streamtest;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.stream.Collector;
import java.util.stream.Collectors;

public class streamtestmain {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Edward", "Frank", "George", "Hannah", "Ivan", "John");

        for (String name: names){
            if(name.startsWith("A")){
                System.out.println(name);
            }
        }

        names.stream()
                .filter(name -> name.startsWith("A"))
                .forEach(System.out::println);
        
        List<Integer> numbers = Arrays.asList(1, 2,2,4,2,11,2,23, 3, 4, 5, 6, 7, 8, 9, 10);

        List<Integer> uniqueNumber = new ArrayList<>(new HashSet<Integer>(numbers));
        List<Integer> filteredList = new ArrayList<>();
        for (Integer num: uniqueNumber){
            if(num % 3 == 0){
                filteredList.add(num);
            }
        }
        System.out.println(filteredList);

        System.out.println(
            numbers.stream()
                .distinct()
                .filter(num -> num % 3 == 0)
                .collect(Collectors.toList())
        );
    
        List<String> names2 = Arrays.asList("Alice", "Bob", "Charlie", "David", "Edward", "Frank", "George", "Hannah", "Ivan", "John");

        names2.stream().filter(name -> name.length() <= 3)
        .map(name -> name.toUpperCase())
        .sorted().forEach(name -> System.out.println(name+" "));
    
        
    
    }
}
