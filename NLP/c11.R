install.packages("rvest")
library(rvest)
setwd('C:/Workspace/SNA/NLP')
getwd()

url  <- "영화1.html"
html <- read_html(url, encoding = "utf-8")
html

# 영화 목록
#요소로 가져오기
movie <- html_nodes(html, "table tr td") %>%
  html_text()
movie

# install.packages("rvest")
library(rvest)

url  <- "영화2.html"
html <- read_html(url, encoding = "utf-8")
html
# #은 아이디 이름 , 게시판을 긇어올때 좋음
movie1 <- html_nodes(html, "#movie1 tr td") %>%
  html_text()
movie1

movie1 <- html_nodes(html, "#movie1 tr td")[c(-1, -2)] %>%
  html_text()
movie1

# install.packages("rvest")
library(rvest)
#클래스를 이용한 방법
# . 은 클래스 이름
url  <- "영화3.html"
html <- read_html(url, encoding = "utf-8")
html

movie.title1 <- html_nodes(html, ".title1") %>%
  html_text()

movie.title1

movie.rate1 <- html_nodes(html, ".rate1") %>%
  html_text()
movie.rate1

# 응용

# install.packages("rvest")
library(rvest)

url <- "https://www.epeople.go.kr/nep/prpsl/opnPrpl/opnpblPrpslList.npaid"
html <- read_html(url)
html

proposal <- html_nodes(html, ".left") %>%
  html_text()
proposal

proposal <- gsub('\r|\n|\t', "", proposal)
proposal
