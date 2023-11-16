setwd("C:/Workspace/SNA/NLP")
getwd()
install.packages("N2H4", repos = "https://forkonlp.r-universe.dev")

source('https://install-github.me/forkonlp/N2H4')
library(N2H4)
library(httr)
library(rvest)
# 메인 카테고리 id 가져옵니다.
cate<-getMainCategory()
print(cate)
# 예시를 위해 하나만 선택합니다.
# 여기는 100(정치)를 선택했습니다.
tcate<-cate$sid1[5]
print(tcate)
#세부 카테고리를 가져옵니다.
subCate<-cbind(sid1=tcate,getSubCategory(sid1=tcate))
print(subCate)
#세부 카테고리를 정했습니다.
tscate<-subCate$sid2[3:4]
print(tscate)
# 목표 날짜를 지정합니다.
strDate<-"20230101"
endDate<-"20230102"

# 파일 이름을 지정하면 한 파일에 계속 저장합니다.
# "" 로 두면 페이지 별로 이름을 자동으로 생성하여 저장합니다.
save_path <- getwd()

strTime<-Sys.time()
midTime<-Sys.time()


for (date in strDate:endDate){
  for (sid1 in tcate){
    for (sid2 in tscate){
      print(sid1)
      print(sid2)
      print(date)
      print(paste0(date," / ",sid1," / ",sid2 ," / start Time: ", strTime," / spent Time: ", Sys.time()-midTime," / spent Time at first: ", Sys.time()-strTime))
      midTime<-Sys.time()
      
      # 뉴스 리스트 페이지의 url을 sid1, sid2, date로 생성합니다.
      #                https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=732&sid1=105&date=20231110
      #                https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=283
      pageUrl<- paste0("https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2",sid2,"&sid1=",sid1,"&date=",date)
      # 리스트 페이지의 마지막 페이지수를 가져옵니다.
      max<-getMaxPageNum(pageUrl)
      
      for (pageNum in 1:max){
        print(paste0(date," / ",sid1," / ",sid2," / ",pageNum, " / start Time: ", strTime," / spent Time: ", Sys.time()-midTime," / spent Time at first: ", Sys.time()-strTime))
        midTime<-Sys.time()
        # 페이지넘버를 포함한 뉴스 리스트 페이지의 url을 생성합니다.
        pageUrl<-paste0("https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2",sid2,"&sid1=",sid1,"&date=",date,"&page=",pageNum)
        # 뉴스 리스트 페이지 내의 개별 네이버 뉴스 url들을 가져옵니다.
        newsList<-getUrlList(pageUrl)
        newsData<-c()
        
        # 가져온 url들의 정보를 가져옵니다.
        for (newslink in newsList$links){
          ## 불러오기에 성공할 때 까지 반복합니다.
          # 성공할때 까지 반복하면 못나오는 문제가 있어서 5회로 제한합니다.
          tryi<-0
          tem<-try(getContent(newslink), silent = TRUE)
          while(tryi<=5&&any(class(tem)=="try-error")){
            tem<-try(getContent(newslink), silent = TRUE)
            tryi<-tryi+1
            print(paste0("try again: ",newslink))
          }
          print(tem)
          print((tem$datetime)[1])
          if(class(tem$datetime)[1]=="POSIXct"){
            newsData<-rbind(newsData, tem)
          }
        }
        
        dir.create("./data",showWarnings=F)
        if(save_path==getwd()){
          # 가져온 뉴스들(보통 한 페이지에 20개의 뉴스가 있습니다.)을 csv 형태로 저장합니다.
          write.csv(newsData, file=paste0("./data/news",sid1,"_",sid2,"_",date,"_",pageNum,".csv"),row.names = F)
        } else {
          if (!file.exists(save_path)){
            write.csv(newsData, file=save_path, row.names = F)
          }
          write.table(newsData, file=save_path, append=T, row.names = F, col.names = F, sep=",")
        }
      } 
    }
  }
}
print("Process end")

source("getnavernews.R",encoding="UTF-8")
install.packages("rvest")

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

