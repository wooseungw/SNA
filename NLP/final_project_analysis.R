setwd("C:/Workspace/SNA/NLP")
getwd()
df <- read.csv('C:/Workspace/SNA/NLP/prerpeoceed_attetion.csv')
# 필요한 라이브러리 로드
#install.packages('tm')
#install.packages('wordcloud')
#install.packages('topicmodels')
#install.packages('LDAvis')
library(LDAvis)
library(tm)
library(wordcloud)
library(topicmodels)
library(RColorBrewer)
library(ggplot2)
library(dplyr)
library(tidyr)
library(tibble)

# 데이터 프레임에서 제목 컬럼 추출
titles <- df$Title

# 텍스트 전처리
corpus <- Corpus(VectorSource(titles))
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removeWords, c(stopwords("english"), "htmlhtml","attention","learning","transformer","transformers","survey","review","models","model"))
corpus <- tm_map(corpus, stripWhitespace)

# 단어 빈도 분석
dtm <- TermDocumentMatrix(corpus)
m <- as.matrix(dtm)
word_freqs <- sort(rowSums(m), decreasing = TRUE)
word_freqs <- data.frame(word = names(word_freqs), freq = word_freqs)

# 색상 팔레트 생성
palette <- c(brewer.pal(8, "Dark2"), brewer.pal(4, "Set3"))
# 가장 많이 사용된 단어 시각화
wordcloud(words = word_freqs$word, freq = word_freqs$freq, min.freq = 3, max.words = 300, scale = c(3.9, 0.9), random.order = FALSE,colors = palette)

print("Done")
# 주제 모델링 (예: LDA)
# LDA 모델 생성
lda_model <- LDA(dtm, k = 5) # k는 추출할 주제의 수
dtm_matrix <- as.matrix(dtm)
lda_vis_data <- createJSON(phi = posterior(lda_model)$terms,
                           theta = posterior(lda_model)$topics,
                           doc.length = rowSums(dtm_matrix),
                           vocab = colnames(dtm_matrix),
                           term.frequency = colSums(dtm_matrix))

# 시각화를 직접 보기
serVis(lda_vis_data)

# 또는 웹 브라우저에서 보기
serVis(lda_vis_data, out.dir = 'LDAvis', open.browser = TRUE)

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



