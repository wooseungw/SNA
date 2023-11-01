
getwd()
setwd("C:/Workspace/SNA/NLP")
dir.create("data")#생성 이력이 있으면 경고 메시지나옴(별다른 의미는 없음)
file_url <- 'https://www.dropbox.com/s/ug3pi74dnxb66wj/jikji.epub?dl=1'
# 윈도에서 mode = "wb"추가 필요
download.file(url = file_url, 
              destfile = "data/jikji.epub",
              mode="wb")

list.files(path = "data", pattern = "epub")

install.packages("epubr")

install.packages("tidyverse")
library(tidyverse)

library(epubr)
jikji_df <- epub("data/jikji.epub")
jikji_df %>% str()

jikji_df %>% glimpse()

df <- jikji_df$data[[1]]
df %>% glimpse()

tibble(text = df$text[1])

install.packages("tidytext")
library(tidytext)
library(ggplot2)
tibble(text = df$text[1]) %>% 
  unnest_tokens(output = word, input = text) %>% 
  count(word, sort = T) %>% 
  filter(n >=10) %>% 
  mutate(word = reorder(word, n)) %>% 
  ggplot() + geom_col(aes(word, n)) +
  coord_flip()


moby_url <- 'https://www.gutenberg.org/files/2701/2701-0.txt'
moby_v <- read_lines(moby_url)

moby_v %>% glimpse()
moby_v %>% head(6)
moby_v %>% tail(6)

moby_scan <- scan(moby_url, what = "character")

library(rvest)
moby_url_h <- 'https://www.gutenberg.org/files/2701/2701-h/2701-h.htm'
moby_html <- read_html(moby_url_h)
moby_html

moby_html %>% html_node("body")

moby_html %>% html_node("body") %>% html_text()