setwd("C:/Workspace/SNA/NLP")
getwd()
df <- read.csv('C:/Workspace/SNA/NLP/prerpeoceed_attetion.csv')
# 필요한 라이브러리 로드
#install.packages('tm')
#install.packages('wordcloud')
#install.packages('topicmodels')
#install.packages('LDAvis')

library(wordcloud)
library(tm)
library(topicmodels)
library(RColorBrewer)
library(ggplot2)
library(dplyr)
library(tidyr)
library(tibble)
library(LDAvis)

# 데이터 프레임에서 제목 컬럼 추출
titles <- df$Title

# 텍스트 전처리
corpus <- tm::VCorpus(VectorSource(titles))
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removeWords, c(stopwords("english"), "htmlhtml","attention","learning","transformer","transformers","survey","review","models","model"))
corpus <- tm_map(corpus, stripWhitespace)

# 단어 빈도 분석
tdm <- TermDocumentMatrix(corpus, control = list(wordLengths=c(2,Inf)))
print(tdm)
print(rownames(tdm))

# 워드 클라우드 생성을 위한 단어 빈도 계산
m <- as.matrix(tdm)  # tdm 사용
word_freqs <- sort(rowSums(m), decreasing = TRUE)
word_freqs <- data.frame(word = names(word_freqs), freq = word_freqs)

# 워드 클라우드 생성
png("wordcloud.png", width = 800, height = 600)
wordcloud(words = word_freqs$word, freq = word_freqs$freq, min.freq = 3, max.words = 300, scale = c(3.9, 0.9), random.order = FALSE, colors = palette)
dev.off()
print("Word Cloud Created")



# TDM을 DTM으로 변환
dtm <- t(tdm)
print(colnames(dtm))
library(Matrix)
density(dtm)

dtm <- removeSparseTerms(dtm, sparse = 0.9999)  # sparse 파라미터를 조정하여 필요한 수준으로 설정


# LDA 모델 생성
lda_model <- LDA(dtm, k = 3)  # 이제 dtm 사용
# LDA 시각화 데이터 생성
lda_vis_data <- createJSON(phi = posterior(lda_model)$terms,
                           theta = posterior(lda_model)$topics,
                           doc.length = rowSums(dtm),
                           vocab = colnames(dtm),
                           term.frequency = colSums(dtm))
# LDA 시각화
serVis(lda_vis_data)

# # 각 주제별 상위 단어 추출
# top_terms <- terms(lda_model, 10) # 각 주제별 상위 10개 단어
# top_terms
# # 데이터 프레임으로 변환
# topics_df <- as.data.frame(top_terms)

# # 데이터 프레임 재구성 (pivot_longer 사용)
# topics_df <- topics_df %>%
#   t() %>%
#   as.data.frame() %>%
#   rownames_to_column("Term") %>%
#   pivot_longer(cols = -Term, names_to = "Topic", values_to = "Word")

# # 시각화
# ggplot(topics_df, aes(x = Term, y = Word, fill = Topic)) +
#   geom_tile() +
#   theme_minimal() +
#   coord_flip() +
#   labs(x = "Terms", y = "Words", title = "Top Words in Each LDA Topic")
# print("Done")





