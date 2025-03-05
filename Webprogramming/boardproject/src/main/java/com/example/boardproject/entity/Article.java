package com.example.boardproject.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;
import lombok.extern.slf4j.Slf4j;

@Entity @ToString @Slf4j @Getter @Setter
@NoArgsConstructor @AllArgsConstructor
public class Article {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    private String content;

    public Article(String title, String content){
        this.title = title;
        this.content = content;
    }

    public void patch(Article article){
        if(article.getTitle() != null){
            this.title = article.getTitle();
        }
        if(article.getContent() != null){
            this.content = article.getContent();
        }
    }
    

    public void loginfo(){
        log.info("\nid: {}, title: {}, content: {}", id, title, content );
    }

}
