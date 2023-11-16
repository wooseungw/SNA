# Neural Information Processing Systems	309	503
# 2.	International Conference on Learning Representations	303	563
# 3.	International Conference on Machine Learning	254	463
# 4.	AAAI Conference on Artificial Intelligence	212	344
# 5.	Expert Systems with Applications	148	221 
library(httr)
library(rvest)
library(dplyr)
library(XML)


# 라이브러리 로드
library(dplyr)

# 각 페이지의 데이터 프레임을 저장할 리스트 초기화
all_pages_data <- list()

max_page = 980
for (i in 1:99){
  #html <- read_html(paste0("https://scholar.google.co.kr/scholar?start=",(i-1)*10,"&q=source:Neural+source:Information+source:Processing+source:Systems&hl=ko&as_sdt=0,5&as_ylo=",years))
  
  html <- read_html(paste0("https://scholar.google.co.kr/scholar?start=",(i-1)*10,"&hl=ko&as_sdt=2005&sciodt=0,5&cites=2960712678066186980&scipsc="))
  title <- html_nodes(html, "#gs_res_ccl_mid .gs_rt") %>% 
    html_text()
  title
  title <- gsub("\\[PDF]","",title)
  title <- gsub("\\[html]","",title)
  #title
  
  authors <- html_nodes(html, "#gs_res_ccl_mid .gs_a") %>% 
    html_text()
  authors
  authors <- gsub("¡¦","",authors)
  # 학술지 정보 추출
  journal_names <- sub(".*- (.+), [0-9]{4} -.*", "\\1", text)
  # 출판연도 추출
  publication_years <- sub(".*([0-9]{4}).*", "\\1", text)
  #authors
  
  page_data <- data.frame(
    Title = title,
    Authors = authors,
    Journal = journal_names,
    Year = publication_years
  )
  # 리스트에 추가
  all_pages_data[[i]] <- page_data
}
# 모든 페이지의 데이터를 하나의 데이터 프레임으로 합치기
final_data <- bind_rows(all_pages_data)
# 데이터 프레임을 CSV 파일로 저장
write.csv(final_data, "attention.csv", row.names = FALSE)

# https://scholar.google.co.kr/scholar?start={0}&q=source:Neural+source:Information+source:Processing+source:Systems&hl=ko&as_sdt=0,5&as_ylo={2020}
i <- 1
years = 2020
urls = paste0("https://scholar.google.co.kr/scholar?start=",i*10,"&q=source:Neural+source:Information+source:Processing+source:Systems&hl=ko&as_sdt=0,5&as_ylo=",years)
url = "https://scholar.google.co.kr/scholar?start=0&q=source:Neural+source:Information+source:Processing+source:Systems&hl=ko&as_sdt=0,5&as_ylo=2020"
html <- read_html(urls)
html

article_len <- html_nodes(html,"#gs_ab_md .gs_ab_mdw")%>% 
html_text()
for ( i in 10){
    
}
#목록의 아이템 추출 #이 목록의 위치 .title추출
title <- html_nodes(html, "#gs_res_ccl_mid .gs_rt") %>% 
html_text()
title
title <- gsub("\\[PDF]","",title)
title
# title 변수의 자료형 확인
class(title)

authors <- html_nodes(html, "#gs_res_ccl_mid .gs_a") %>% 
html_text()
authors
authors <- gsub("¡¦","",authors)
authors


page <-html_nodes(html, ".gs_ab_mdw") %>% 
  html_text()
page


machine_learning_papers <- grepl("machine learning|deep learning|neural networks", title, ignore.case = TRUE)
natural_language_processing_papers <- grepl("natural language processing|nlp", title, ignore.case = TRUE)

# 출력
cat("Machine Learning 관련 논문:\n")
cat(title[machine_learning_papers], "\n\n")

cat("Natural Language Processing 관련 논문:\n")
cat(title[natural_language_processing_papers], "\n")
