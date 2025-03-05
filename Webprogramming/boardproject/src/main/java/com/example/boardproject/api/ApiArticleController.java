package com.example.boardproject.api;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;

import com.example.boardproject.dto.ArticleForm;
import com.example.boardproject.entity.Article;
import com.example.boardproject.repository.ArticleRepository;
import java.util.List;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;



import lombok.extern.slf4j.Slf4j;


@RestController @Slf4j
public class ApiArticleController {

    @Autowired
    ArticleRepository articleRepository;

    @GetMapping("/api/articles")
    public List<Article> index(){

        List<Article> articles = articleRepository.findAll();
        return articles;
    }

    @PostMapping("/api/articles")
    public String create(@RequestBody ArticleForm articleForm){ 
        
        log.info(articleForm.toString());
        articleForm.setId(-1L);

        Article article = articleForm.toEntity();
        log.info(article.toString());

        Article newArticle = articleRepository.save(article);

        return newArticle.toString();
    }

    @GetMapping("/api/articles/{id}")
    public Article read(@PathVariable("id") Long id){
        Article article = articleRepository.findById(id).orElse(null);
       
        return article;
    }

    @PatchMapping("/api/articles/{id}")
    public ResponseEntity<Article> update(
        @PathVariable("id") Long id, 
        @RequestBody ArticleForm articleForm
        ){ 
        
        Article article = articleForm.toEntity();
        article.loginfo();

        Article target = articleRepository.findById(id).orElse(null);

        if(target == null || id != article.getId()){
            log.info("잘못된 요청입니다.");
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(null);
        }
        target.patch(article);
        Article updated = articleRepository.save(target);
        return ResponseEntity.status(HttpStatus.OK).body(updated);
    }

    @DeleteMapping("/api/articles/{id}")
    public ResponseEntity<String> delete(@PathVariable("id") Long id){

        Article article = articleRepository.findById(id).orElse(null);
        if(article == null)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("잘못된 요청입니다.");
        
        articleRepository.delete(article);
        return ResponseEntity.status(HttpStatus.OK).body("삭제되었습니다.");
    }


}