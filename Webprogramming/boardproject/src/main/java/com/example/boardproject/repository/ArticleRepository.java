package com.example.boardproject.repository;

import org.springframework.stereotype.Repository;

import com.example.boardproject.entity.Article;

import org.springframework.data.jpa.repository.JpaRepository;

@Repository
public interface ArticleRepository extends JpaRepository<Article, Long>{

}
