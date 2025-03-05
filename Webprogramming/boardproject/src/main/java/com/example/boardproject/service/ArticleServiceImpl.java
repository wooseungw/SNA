package com.example.boardproject.service;

import com.example.boardproject.entity.Article;
import com.example.boardproject.dto.ArticleForm;
import com.example.boardproject.repository.ArticleRepository;

import lombok.extern.slf4j.Slf4j;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collector;
import java.util.stream.Collectors;

@Service
@Transactional @Slf4j
public class ArticleServiceImpl implements ArticleService {
    
    @Autowired
    ArticleRepository articleRepository;

    @Override
    public List<Article> index() {
        return articleRepository.findAll();
    }

    @Override
    public Article show(Long id) {
        return articleRepository.findById(id).orElse(null);
    }

    @Override
    public Article create(ArticleForm articleForm) {
        articleForm.setId(-1L);
        Article article = articleForm.toEntity();
        Article created = articleRepository.save(article);
        return created;
    }

    @Override
    public Article update(Long id, ArticleForm articleForm) {
        
        articleForm.setId(-1L);
        
        Article article = articleForm.toEntity();

        Article target = articleRepository.findById(id).orElse(null);

        if (target == null) {
            return null;
        }

        target.patch(article);
        Article updated = articleRepository.save(target);

        return updated;
    }

    @Override
    public Article delete(Long id) {
        Article target = articleRepository.findById(id).orElse(null);

        if (target == null) {
            return null;
        }

        articleRepository.delete(target);

        return target;
    }

    @Override
    @Transactional
    public List<Article> createArticles(List<ArticleForm> articleForms) {
        for (ArticleForm articleForm : articleForms) {
            articleForm.setId(-1L);
            log.info(articleForm.toString());
        }
        
        List<Article> articles = articleForms.stream()
                .map(articleForm -> articleForm.toEntity())
                .collect(Collectors.toList());

        List<Article> updatedList = (List<Article>) articleRepository.saveAll(articles);

        articleRepository.findById(-1L).orElseThrow(() -> new IllegalArgumentException("결제 실패"));

        return updatedList;
        
    }

    @Override
    @Transactional
    public List<Article> updateArticles(List<ArticleForm> articleForms) {
        List<Article> updatedList = new ArrayList<>();
        
        for (ArticleForm articleForm : articleForms) {
            // ID 값이 있는지 확인
            if (articleForm.getId() == null) {
                throw new IllegalArgumentException("ID가 필요합니다.");
            }
            
            // 기존 엔티티 조회
            Article target = articleRepository.findById(articleForm.getId())
                .orElseThrow(() -> new IllegalArgumentException(
                    "해당 게시글이 없습니다. id=" + articleForm.getId()));
            
            // 변경사항 적용
            target.patch(articleForm.toEntity());
            
            // 수정된 엔티티 추가
            updatedList.add(target);
            
            log.info("Update article: {}", target);
        }
        
        // 벌크 업데이트 수행
        return articleRepository.saveAll(updatedList);
    }
}