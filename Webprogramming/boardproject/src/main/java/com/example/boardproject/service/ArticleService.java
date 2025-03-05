package com.example.boardproject.service;

import java.util.List;
import com.example.boardproject.entity.Article;
import com.example.boardproject.dto.ArticleForm;

public interface ArticleService {
    //read all articles
    List<Article> index();
    //read one article
    Article show(Long id);
    //insert
    Article create(ArticleForm articleForm);
    //update article
    Article update(Long id, ArticleForm articleForm);
    //delete article
    Article delete(Long id);

    List<Article> createArticles(List<ArticleForm> articleForms);

    List<Article> updateArticles(List<ArticleForm> articleForms);
}