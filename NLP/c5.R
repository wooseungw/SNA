vec <- c(1:6, 'a')
print(vec)
print(vec[2])
print(vec[7])
list1 <- list(1:5, 'a')
print(list1)
print(list1[[1]][[2]])
unlist1 <- unlist(list1)
print(unlist1)
print(str(unlist1))
print(unlist1[1:5])
print(mean(list1[[1]]))
#print(mean(unlist1[1:5]))
#[] list 반환 , [[]] vec 반환
obj1 <- 1:4
obj2 <- 2:10
obj3 <- list(obj1, obj2)
print("obj3")
print(obj3)
name1 <- "Donald"
space1 <- " "
name2 <- "Duck"
names <- c(name1, space1, name2)
print(names)
names <- list(names)
print(names)
names <- unlist(names)
print(names)#하나의 벡터로 저장됨



names <- c('갑', '을', '병', "정")
gender <- c(0,1,1,0)
df <- data.frame(names,gender)
attr(df$names, "attribute") <- "응답자 이름"
print(df$names)
attr(df, "names")

list1 <- list(1:4, 6:11, list(2:4, 7:12))

#print(a)
print("list1")
print(list1)
print(lapply(list1[1], mean))#list로 return
print(lapply(list1[2], mean))
print(sapply(list1[1], sum))#벡터로 return
print(sapply(list1[2], sum))

wordlist <- c("the", "is", "a", "the")
doc1freq <- c(3, 12, 2, 4)
doc2freq <- c(1, 2, 6, 2)
tapply(doc1freq, wordlist, sum) #단어의 빈도수를 계산할때 많이 씀
tapply(doc2freq, wordlist, sum)
#tapply, sapply의 사용 빈도수가 높음

letters[2]
LETTERS[2]
letters[1:26]
LETTERS[1:26]

tolower("Eye EYE eye")
toupper("Eye EYE eye")

nchar("KOREA")
nchar("Republic of Korea")
nchar("Republic \nof \nKorea")
