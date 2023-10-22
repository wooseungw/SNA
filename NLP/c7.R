install.packages("stringr")
library(stringr)
str_c("I", "love", c("da","do","du"), sep = "-")#문자열,문자열벡터를 이어붙히는 역할 , sep은 패턴
paste("I", "love", c("da", "do", "du"), "R", sep = "-")#paste가 좀 더 효율적
paste(1:9,1:9,sep="",collapse = "?")
paste('X',1:5,collapse = "")#collapse는 하나의 string으로 리턴됨
texts <- c("텍스트마이닝", "Text Mining","자연어처리",
 "Natural Language Processing","\n\n\n\n\n\n\n\n\n\n")
texts
str_length(texts)#띄어쓰기 포함 길이값
substr(texts[2],0,5)
substr(texts,0,100/10)
substr(texts,-1,5)
str_sub(texts[1],start =0,end = 1)#start가 0,-1이어도 1일때랑 똑같음 end가 길이보다 길때 최대길이를 출력함

bad_text = c("T h i s", " example ", "has several ", " whitespaces ")
bad_text
str_trim(bad_text,side = "both")#앞뒤 공백만 삭제해줌# side는 “both”,“left”,“right


change = c(" T T T  T T","Be the change", "you want to be")
word(change,1)#띄어쓰기 기준 n번째 단어가 출력됨 단어의 길이가 충분하지 않으면 NA


texts <- c("텍스트마이닝", "Text Mining","자연어처리", "텍스트 처리",
 "Natural Language Proces3sing", "텍스트 데이터")
texts
 #패턴을 찾는것 입력한 텍스트가 포함된 index반환
grep("텍스트", x = texts)
#value반환
grep("텍스트|Text", x = texts, value=TRUE)#하나의 string으로 묶어 and나 or 연산도 가능
grep("[텍스g]",x=texts,value=TRUE)

numerics = c("123", "17-April", "I-II-III", "R 3.0.1")
grep("[0-9]",x=numerics, value=TRUE)#숫자가 있는 데이터
grep("[^0-9]",x=numerics, value=TRUE)#숫자로만 된 데이터를 제외한 데이터

text = "GPT 3.5를 기반으로 하는 대화형 인공지능 서비스이며,간단한 회원가입 후 무료 혹은 유료로 이용할 수 있다
ChatGPT는 사용자와 주고받는 대화에서 질문에 답하도록 설계된 언어모델이며,
오픈AI는 블로그 게시글을 통해 ChatGPT가 대화 형식으로 추가적인 질문에 답하고,
실수를 인정하며, 정확하지 않은 전제에 대해서는 이의를 제기하고
부적절한 요청을 거부할 수 있다”고 설명했다.
마이크로소프트가 \'ChatGPT\'의 개발사 OpenAI에
10억 달러(약 1조 2,400억 원)를 투자한 데 이어
추가로 총 100억 달러(약 12조 4,000억원)의
투자를 협의 중인 것으로 알려졌다.
마이크로소프트는 챗GPT를 오피스(Office) 제품과 검색엔진 빙(Bing)에 적용할 계획이다.
이러한 기능 중 일부는 빠르면 2023년 3월에 출시될 수도 있다."

result = str_replace_all(text,pattern = "ChatGPT",replacement = "챗GPT")
cat(result)

mysentence <- 'Learning R is so interesting'
my = strsplit(mysentence,split = " ")
my[[1]][5]
strsplit(my[[1]][5],split = "")
