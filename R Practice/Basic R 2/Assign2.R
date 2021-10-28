setwd("C:/Users/shiva/Documents/MS Data Science/631-Foundations of Data Analysis/Class2/Homework2")

load("cdc.RData")

View(cdc)

names(cdc)

summary(cdc)

head(cdc)

tail(cdc)

summary(cdc$weight)

summary(cdc$weight)[5]-summary(cdc$weight)[2]

mean(cdc$weight)

var(cdc$weight)

median(cdc$weight)

table(cdc$smoke100)

table(cdc$smoke100)/20000

barplot(table(cdc$smoke100))

or

smoke_tbl = table(cdc$smoke100)

smoke_tbl

barplot(smoke_tbl)

table(cdc$gender)

barplot(table(cdc$gender))

table(cdc$genhlth)/20000

gender_smoke_tbl = table(cdc$gender,cdc$smoke100)

gender_smoke_tbl

mosaicplot(gender_smoke_tbl)

dim(cdc)

cdc[567,6]

names(cdc)

cdc[1:10,6]

cdc[1:10,]

cdc[,6]

cdc$weight

cdc$weight[1:10]

cdc$gender == "m"

men_data = subset(cdc,cdc$gender=="m")
men_data

m_and_over30 = subset(cdc,cdc$gender == "m" & cdc$age>30)

m_and_over30

under23_and_smoke = subset(cdc,cdc$age < 23 & cdc$smoke100==1)
View(under23_and_smoke)

boxplot(cdc$weight)

boxplot(cdc$height)

summary(cdc$height)

boxplot(cdc$height ~ cdc$gender)

bmi = (cdc$weight/cdc$height^2) * 703

boxplot(bmi ~ cdc$genhlth)

boxplot(bmi ~ cdc$gender)

hist(cdc$age)

hist(bmi)

hist(bmi,breaks = 50)

plot(cdc$weight,cdc$wtdesire)

savehistory(file = "Assign2.Rhistory")
