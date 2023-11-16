
# 각 페이지의 데이터 프레임을 저장할 리스트 초기화
all_pages_data <- list()

# 페이지 1부터 10까지 반복
for (page in 1:10) {
  url <- paste0("https://academic.naver.com/search.naver?field=0&docType=1&query=","ai","&page=",page)
  html <- read_html(url)
  title <- html_nodes(html,'.ui_listing_list .ui_listing_subtit') %>%
    html_text()
  data <- html_nodes(html,'.ui_listing_desc .ui_listing_source') %>%
    html_text() 
  journal_names <- data[seq(1, length(data), by = 4)]
  publication_years <- data[seq(2, length(data), by = 4)]
  authors_list <- data[seq(4, length(data), by = 4)]
  cited <- html_nodes(html,'.ui_listing_desc .ui_listing_cited_num') %>%
    html_text()
  
  page_data <- data.frame(
    Title = title,
    Journal = journal_names,
    Year = publication_years,
    Authors = authors_list,
    Cited = cited
  )
  
  # 리스트에 추가
  all_pages_data[[page]] <- page_data
}

# 모든 페이지의 데이터를 하나의 데이터 프레임으로 합치기
final_data <- bind_rows(all_pages_data)

# 데이터 프레임을 CSV 파일로 저장
write.csv(final_data, "collected_data.csv", row.names = FALSE)

#https://finance.naver.com/news/mainnews.naver?date=2023-11-13&page=2
date = 2023-11-13
page = 1
url <- paste0("https://academic.naver.com/search.naver?field=0&docType=1&query=","ai","&page=",2)
print(url)

page_max_num <- 10

html <- read_html(url)
html

title <- html_nodes(html,'.ui_listing_list .ui_listing_subtit') %>%
  html_text()
title


data <- html_nodes(html,'.ui_listing_desc .ui_listing_source') %>%
  html_text()
data


journal_names <- data[seq(1, length(data), by = 4)]
publication_years <- data[seq(2, length(data), by = 4)]
authors_list <- data[seq(4, length(data), by = 4)]

journal_names
publication_years
authors_list

cited <- html_nodes(html,'.ui_listing_desc .ui_listing_cited_num') %>%
  html_text()
cited







