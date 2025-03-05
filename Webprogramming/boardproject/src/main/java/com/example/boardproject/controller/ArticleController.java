package com.example.boardproject.controller;

import java.lang.ProcessBuilder.Redirect;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import com.example.boardproject.dto.ArticleForm;
import com.example.boardproject.entity.Article;
import com.example.boardproject.repository.ArticleRepository;

import lombok.extern.slf4j.Slf4j;

import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;





@Controller @Slf4j
public class ArticleController {
    @Autowired
    ArticleRepository articleRepository;

    @GetMapping("/articles/{id}")
    public String show(@PathVariable("id") Long id, Model model) {
        

        Article article = articleRepository.findById(id).orElse(null);
        model.addAttribute("article", article);

        return "articles/show";
    }

    @GetMapping("/articles")
    public String articlesList(Model model) {

        List<Article> articleList = articleRepository.findAll();
        model.addAttribute("articleList", articleList);
        return "articles/index";
    }

    @GetMapping("/articles/new")
    public String newArticleForm() {
        return "articles/new";
    }
    
    @PostMapping("/articles/create")
    public String createArticle(ArticleForm articleFrom) {
        articleFrom.loginfo();

        Article article = articleFrom.toEntity();
        article.loginfo();  

        Article saved = articleRepository.save(article);
        saved.loginfo();

        return "redirect:/articles";
    }
    
    @GetMapping("/articles/{id}/edit")
    public String edit(@PathVariable("id") Long id, Model model) {
        Article article = articleRepository.findById(id).orElse(null);
        model.addAttribute("article", article);
        
        return "articles/edit";
    }
    
    @PostMapping("/articles/update")
    public String update(ArticleForm articleForm){
        log.info(articleForm.toString()); //DTO
        //DTO -> Entity
        Article articleEntity = articleForm.toEntity();
        log.info(articleEntity.toString()); //entity

        Article target = articleRepository.findById(articleEntity.getId()).orElse(null);
        
        if(target != null) {
            articleRepository.save(articleEntity);
        }
        // redirect
        return "redirect:/articles/" + target.getId();

        }

    @GetMapping("/articles/{id}/delete")
    public String delete(@PathVariable("id") Long id,
                        RedirectAttributes rttr) {
        Article target = articleRepository.findById(id).orElse(null);
        if( target != null) {
            articleRepository.deleteById(id);
            //
            rttr.addFlashAttribute("msg" ,"삭제되었습니다.");
        }
        //index redirect
        return "redirect:/articles";
    }
        
}
