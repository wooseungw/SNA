package com.example.boardproject.dto;


import com.example.boardproject.entity.Article;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;
import lombok.extern.slf4j.Slf4j;

@Getter @Setter @NoArgsConstructor @AllArgsConstructor @ToString @Slf4j
public class ArticleForm {
    private Long id;
    private String title;
    private String content;

    public Article toEntity(){
        return new Article(id, title, content);
    }

    public void loginfo(){
        log.info("\ntitle: {}, content: {}", title, content );
    }
}
