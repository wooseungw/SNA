library(prettyR)
#c는 벡터 생성
a <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("인덱스 슬라이싱")
print(a[0:2])
print(a[1:2])
#R은 1부터 시작함
print(mode(a))
#속성, 인덱스와 요소 return
str_a <- str(a)
print(str_a)
print(length(a))
hi <- "hello World"#문자열은 "" char는 ''
hi
str(hi)
#문자열도 벡터에 넣기가능
his <- c("안녕", "hi", "안녕", "hi", "안녕", "hi", "안녕", "hi", "안녕", "hi")
print(his)
a_mat <- matrix(a, nrow=2, ncol=5)
a_arr <- array(a, dim = c(5, 2, 1))#row,col,dim
a_arr
a_arr[1,1,1]
a_arr[1][1][0]
a_list <- list(a, "heelo")#리스트 형태로 데이터를 많이 합친다
print(a_mat)
print(a_arr)
print(a_list)#데이터의 순서대로 저장됨
print(str(a_list))
#길이가 맞지 않으면 안된다.
#df <- data.frame(a,his,c(1,2,2,3,3,3))
#print((df))

df_co <- data.frame(a, a, his)
print(df_co)
sum_test <- sum(1:6)
print(sum_test)
print(Sys.Date())
#함수만들기 중요
#변수는 앞서 선언된 변수를 사용하면 안된다
get_multi <- function(i, j, k){
    r <- i * j * k
    return(r)
}
print(get_multi(199, 22212112, 3))
i <- 0
j <- 12
if(i<j){
    print("j가 더 큼")
}else{
    print("i가 더 큼")
}
#내장 데이터셋은 그냥 가져올수있음
data()
str(quakes)
names(quakes)
dim(quakes)
summary(quakes)
url <- "url.csv"#웹이든 로컬이든 가능할듯
x <- read.csv(url)

install.packages("XML")
library(XML)
xml_data <- xmlToDataFrame(url)
View(xml_data)

install.packages("jsonlite")
library(jsonlite)
height <- c(9,15,10,6)
name <- c("영업1팀", "영업2팀", "영업3팀", "영업4팀") 
barplot(height, names.arg = name, main="부서별 영업실적", col= rainbow(length(height)), xlab ="부서", ylab="영업실적")


ncol(iris)
nrow(iris)
dim(iris)
names(iris)
iris$Sepal.Length
summa <- summary(iris)

boxplot(iris, main = "iris box plot", col = rainbow(length(iris)))

for(i in 2:10){
    for(j in 1:9){
        print(paste(i, " * ", j, " = ", i*j))
    }
}

