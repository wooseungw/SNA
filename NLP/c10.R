setwd("C:/Workspace/SNA/NLP")
install.packages("rvest")
library(rvest)
url <- "https://www.data.go.kr/tcs/dss/selectDataSetList.do"
html <- read_html(url)
html
#목록의 아이템 추출 #이 목록의 위치 .title추출
title <- html_nodes(html, "#apiDataList .title") %>%
html_text()
title

desc <- html_nodes(html, "#apiDataList .ellipsis") %>%
html_text()
desc

title <- gsub("[|\r|\n|\t]", "", title)
title
api <- data.frame(title, desc)
api
source("getnavernews.R",encoding="UTF-8")
