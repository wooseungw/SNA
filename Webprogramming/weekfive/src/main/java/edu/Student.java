package edu;

import lombok.*;
import lombok.extern.slf4j.Slf4j;


@Slf4j
@ToString
@AllArgsConstructor @NoArgsConstructor
@Getter @Setter
public class Student {
    private Long id;
    private String firstName;
    private String lastName;

    public void logInfo() {
        log.info("Student id:{}, Name: {}, Age: {} " , id, firstName, lastName);
    }
}
