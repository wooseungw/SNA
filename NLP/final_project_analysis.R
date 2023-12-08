setwd("C:/Workspace/SNA/NLP")
getwd()
df <- read.csv('C:/Workspace/SNA/NLP/prerpeoceed_attetion.csv')
# 필요한 라이브러리 로드
#install.packages('tm')
#install.packages('wordcloud')
#install.packages('topicmodels')
#install.packages('LDAvis')
#install.packages('treemapify')
#install.packages('cli')
library(treemapify)
library(wordcloud)
library(tm)
library(topicmodels)
library(RColorBrewer)
library(ggplot2)
library(dplyr)
library(tidyr)
library(tibble)
library(LDAvis)

library(tidytext)
library(topicmodels)
library(dplyr)

# 데이터 프레임에서 제목 컬럼 추출
titles <- df$Title

# 텍스트 전처리
corpus <- tm::Corpus(VectorSource(titles))
print(paste("Original corpus size:", length(corpus)))

# 소문자로 변환
corpus <- tm_map(corpus, content_transformer(tolower))
print(paste("Corpus size after tolower:", length(corpus)))
inspect(corpus[1:5])  # 처음 5개 문서의 내용을 확인

# 구두점 제거
corpus <- tm_map(corpus, removePunctuation)
print(paste("Corpus size after removePunctuation:", length(corpus)))
inspect(corpus[1:5])

# 숫자 제거
corpus <- tm_map(corpus, removeNumbers)
print(paste("Corpus size after removeNumbers:", length(corpus)))
inspect(corpus[1:5])

# 불용어 제거
corpus <- tm_map(corpus, removeWords, c(stopwords("english"),"deep","network","networks","via", "htmlhtml","attention","learning","transformer","transformers","survey","review","models","model"))
print(paste("Corpus size after removeWords:", length(corpus)))
inspect(corpus[1:5])

# 공백 제거
corpus <- tm_map(corpus, stripWhitespace)
print(paste("Corpus size after stripWhitespace:", length(corpus)))
inspect(corpus[1:5])

writeLines(as.character(corpus[[1]]))

# 단어 빈도 분석
tdm <- TermDocumentMatrix(corpus)
print(tdm)
print(rownames(tdm))

# 워드 클라우드 생성을 위한 단어 빈도 계산
m <- as.matrix(tdm)  # tdm 사용
word_freqs <- sort(rowSums(m), decreasing = TRUE)
#print(word_freqs)
word_freqs <- data.frame(word = names(word_freqs), freq = word_freqs)

# 색상 팔레트 생성
palette_colors <- c(brewer.pal(8, "Dark2"), brewer.pal(4, "Set3"))

# 워드 클라우드 생성
png("wordcloud.png", width = 800, height = 600)
wordcloud(words = word_freqs$word, freq = word_freqs$freq, min.freq = 2, max.words = 300, scale = c(3.9, 0.9), random.order = FALSE, colors = palette_colors)
dev.off()

# 워드 클라우드 생성
png("wordcloud 10.png", width = 800, height = 600)
wordcloud(words = word_freqs$word, freq = word_freqs$freq, min.freq = 10, max.words = 300, scale = c(3.9, 0.9), random.order = FALSE, colors = palette_colors)
dev.off()

print("Word Cloud Created")


#topic 모델링을 위한 추가 불용어 제거
#corpus2 <- tm_map(corpus, removeWords, c("data","deep","image","vision")) resnet
#corpus2 <- tm_map(corpus, removeWords, c("image","deep")) GAN
# 어텐션
corpus2 <- tm_map(corpus, removeWords, c("image","vision"))
print(paste("Corpus size after removeWords:", length(corpus)))
# 코퍼스를 데이터 프레임으로 변환
text_data <- sapply(corpus2, as.character)
data <- data_frame(line = 1:length(text_data), text = text_data)

# tidytext를 사용한 추가 전처리 및 LDA 모델 생성
tidy_data <- data %>%
  unnest_tokens(word, text) %>%
  anti_join(stop_words) %>%
  count(document = line, term = word) %>%
  cast_dtm(document, term, n)

# LDA 모델 생성
lda_model <- LDA(tidy_data, k = 5)  # k는 추출할 주제의 수

topics <- tidy(lda_model, matrix = "beta")

#트리맵
document_topics <- lda_model %>%
  tidy(matrix = "gamma") %>%
  group_by(document) %>%
  top_n(1, gamma) %>%
  ungroup() %>%
  count(topic, sort = TRUE)

top_terms_per_topic <- lda_model %>%
  tidy(matrix = "beta") %>%
  group_by(topic) %>%
  top_n(1, beta) %>%
  ungroup()

treemap_data <- document_topics %>%
  left_join(top_terms_per_topic, by = "topic")

ggplot(treemap_data, aes(area = n, fill = factor(topic), label = term)) +
  geom_treemap() +
  geom_treemap_text(fontface = "italic", colour = "white", place = "centre", grow = TRUE) +
  theme_minimal() +
  labs(title = "LDA Topic Distribution", subtitle = "Size of each box represents the number of documents per topic")

ggsave("lda_treemap.png", width = 10, height = 8)


# LDA 모델에서 토픽별 상위 단어 추출
top_terms <- lda_model %>%
  tidy(matrix = "beta") %>%
  group_by(topic) %>%
  top_n(15, beta) %>%
  ungroup() %>%
  arrange(topic, -beta)

# 시각화
ggplot(top_terms, aes(x = reorder_within(term, beta, topic), y = beta, fill = factor(topic))) +
  geom_col(show.legend = FALSE) +
  facet_wrap(~ topic, scales = "free") +
  scale_x_reordered() +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 8)) +  # 각도 조정 및 글자 크기 조정
  labs(x = NULL, y = "Beta")

ggsave("lda_topic.png", width = 12, height = 12)


