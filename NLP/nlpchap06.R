# 1.기본 package 설정

## 1.1 package 설치
#library()
## 1.1.1 jdk 설치
#install.packages("rJava")
#install.packages("multilinguer")

library(rJava)
library(multilinguer)
#install_jdk()

## 1.1.2 KoNLP 설치(github이용)
#install.packages("remotes")
#remotes::install_github('haven-jeon/KoNLP', upgrade = "never", INSTALL_opts=c("--no-multiarch"))

## 1.1.3 KoNOP 로드
library(KoNLP)

useNIADic() # 단어사전 사용 - 
useSejongDic()

extractNoun("나는 학생이며 오늘도 공부를 합니다.")
MorphAnalyzer("나는 강남대학교 학생이며 오늘도 공부를 합니다.")
library()
#install.packages("wordcloud")
library(wordcloud)

word <- c("인천광역시", "강화군", "옹진군")
frequency <- c(651, 85, 61)

wordcloud(word, frequency, colors ="blue")

wordcloud(word, frequency, random.order=F, random.color=F, colors=rainbow(length(word)))

# 연설문

#install.packages("KoNLP")
#install.packages("RColorBrewer")
#install.packages("wordcloud")

library(KoNLP)
library(RColorBrewer)
library(wordcloud)
#NIC,세종Dictionary 등 말뭉치 사전이 있어야 한글문장분석 가능
useSejongDic()  
#팔레트 생성
pal2 <- brewer.pal(8,"Dark2")   
#인코딩 utf-8로 array형태로 만들어줌
text <- readLines(file.choose())
#head(text)
#str(text)
#행별 명사 추출 extractNoun sapply(data, function,)
noun <- sapply(text, extractNoun, USE.NAMES=F)
#head(noun)
# unlist: list -> vector
noun2 <- unlist(noun) 
#head(noun2)

#빈도수 계산 집계함수 table
word_count <- table(noun2) 
word_count
#str(word_count)
head(sort(word_count, decreasing=TRUE), 10)
set.seed(42)

wordcloud(names(word_count),freq=word_count,scale=c(6,0.9),min.freq=4, random.order=F,rot.per=.1,colors=pal2)


noun <- sapply(text, extractNoun, USE.NAMES=F)
noun2 <- unlist(noun) 
#불용어 제거
noun2 <- gsub("여러분", "", noun2)
noun2 <- gsub("우리", "", noun2)
noun2 <- gsub("오늘", "", noun2)
noun2 <- gsub("하겠읍니다", "", noun2)

noun2 <- Filter(function(x){nchar(x) >= 2}, noun2)


word_count <- table(noun2)
wordcloud(names(word_count),freq=word_count,scale=c(6,0.9),min.freq=3, random.order=F,rot.per=.1,colors=pal2)
