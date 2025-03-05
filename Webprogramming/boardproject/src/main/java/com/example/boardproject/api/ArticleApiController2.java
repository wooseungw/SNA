package com.example.boardproject.api;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.example.boardproject.dto.ArticleForm;
import com.example.boardproject.entity.Article;
import com.example.boardproject.service.ArticleService;

import lombok.extern.slf4j.Slf4j;

@RestController @Slf4j
public class ArticleApiController2 {

    @Autowired
    ArticleService articleService;

    @GetMapping("/api2/articles")
    public List<Article> index() {
        return articleService.index();
    }

    @GetMapping("/api2/articles/{id}")
    public Article show(@PathVariable("id") Long id) {
        return articleService.show(id);
    }

    @PostMapping("/api2/articles")
    public Article create(@RequestBody ArticleForm articleForm) {
        return articleService.create(articleForm);
    }

    @PatchMapping("/api2/articles/{id}")
        public ResponseEntity<Article> update(@PathVariable("id") Long id,
                                            @RequestBody ArticleForm articleForm) {
        Article updated = articleService.update(id, articleForm);
        return (updated != null) ?
        ResponseEntity.status(HttpStatus.OK).body(updated) :
        ResponseEntity.status(HttpStatus.BAD_REQUEST).build();
    }

    @DeleteMapping("/api2/articles/{id}")
    public ResponseEntity<Article> delete(@PathVariable("id") Long id) {
        Article deleted = articleService.delete(id);
        return (deleted != null) ?
            ResponseEntity.status(HttpStatus.NO_CONTENT).build() :
            ResponseEntity.status(HttpStatus.BAD_REQUEST).build();
    }
    
    @PostMapping("/api2/articles/bulk")
    public ResponseEntity<List<Article>> createArticles(@RequestBody List<ArticleForm> articleForms) {
        try {
            List<Article> createdArticles = articleService.createArticles(articleForms);
            return ResponseEntity.status(HttpStatus.CREATED).body(createdArticles);
        } catch (IllegalArgumentException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).build();
        }
    }
}
