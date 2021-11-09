# Hypothesis Tests with R

# Read in the movies.csv file

library(tidyverse)

# z-test
# IQ is standardized so that the mean is 100 
# and the standard deviation is 15. We want to know if 
# musicians have higher than average IQs.
# sample 80 musicians and measure their IQs
# here are the data

IQ <- c(117, 106, 122, 123, 117, 121, 96, 92, 94, 115, 100, 96, 119, 97, 101, 103, 98, 100, 127, 115, 104, 105, 91, 133, 123, 121, 94, 110, 93, 100, 132, 139, 103, 90, 106, 118, 111, 114, 119, 110, 92, 100, 89, 98, 90, 76, 131, 123, 109, 101, 129, 102, 107, 129, 109, 105, 100, 106, 91, 110, 123, 97, 123, 134, 114, 116, 95, 82, 94, 111, 106, 95, 115, 105, 110, 64, 111, 126, 114, 98)

# descriptive
summary(IQ)
sd(IQ)
hist(IQ)
boxplot(IQ)

# Do the z-test

SE <- 15/sqrt(length(IQ))  #length of the data set is "n", sample size

z.stat <- (mean(IQ)-100)/SE

p.val <- pnorm(z.stat, lower.tail = FALSE)

# CI
a <- 0.05

z.star <- qnorm(a, lower.tail = FALSE)  #one tail
z.star <- qnorm(a/2, lower.tail = FALSE) #two tail

CI.lower <- mean(IQ)-z.star*SE
CI.upper <- mean(IQ)+z.star*SE

# For a one sided CI, use only one boundary. Which one for this case?


# Only do one of these
movies <- read_csv(file.choose()) #this makes a tibble
movies <- read.csv(file.choose()) #this makes a dataframe 

#------------------
# z test for two proportions
# Tests for one or two proportions are always z-tests
# z.stat = (p.hat - p)/SE,  SE = sqrt(np(1-p))
#------------------

#What proportion of movies won oscars?
sum(movies$Oscar.Nominated)
mean(movies$Oscar.Nominated)

#What proporition of movies were franchise?
sum(movies$Franchise)
mean(movies$Franchise)

movies.table <- table(movies$Franchise, movies$Oscar.Nominated)
prop.table(movies.table)
prop.table(movies.table,1)

# Same thing, but with "janitor" package (tidy)
library(janitor)
tidy.table <- tabyl(movies, Franchise, Oscar.Nominated)

tidy.table %>% 
  adorn_totals(c("row","col")) %>%
  adorn_percentages("all") %>%
  adorn_pct_formatting() %>%
  adorn_ns()
  

#Is the proportion of movies that got Oscar Noms different 
#for franchise and non-franchise movies?

prop.test(movies.table)

#------------------
# t tests 
#------------------

# Is the average budget for movies = $0?  (Obviously not, this is just to show the syntax)

#1 sample t, mu=0 
t.test(movies$Budget)

# Is the average budget for movies = $70 million?
# 1 sample t, mu=7E7, 2 sided
t.test(movies$Budget, mu=7E7)

#1 sample t, mu=7E7 1 sided (greater)
t.test(movies$Budget, alternative="greater", mu=7E7)

#1 sample t, mu=7E7 1 sided (less than)
t.test(movies$Budget, alternative="less", mu=7E7)

#paired t test
t.test(movies$CriticRate.RT, movies$UserRating.RT, paired = TRUE)

#2 sample t test
t.test(movies$Budget~movies$Franchise, alternative="less")

#----------------
#Chi squared test
#----------------

#Let's look at MPAA Rating
table(movies$MPAA.Rating)

#Are those differences significant?
chisq.test(table(movies$MPAA.Rating))

#From 1968 to present, 55% of movies are R, 24% are PG and 21% are PG-13
#Is our sample different from that?

chisq.test(table(movies$MPAA.Rating),p=c(0.24, 0.21, 0.55))

#Is rating independent of genre?
table(movies$MPAA.Rating,movies$Genre)

chisq.test(table(movies$MPAA.Rating,movies$Genre))

#Why did we get a warning?

#----------------
# Regression and ANOVA
#----------------

#Is there a relationship between the budget of a movie 
#and how long it's in the theaters?

cor(movies$In.Theatres.wks,movies$Budget)

plot(movies$In.Theatres.wks~movies$Budget)

#OR using ggplot2

ggplot(data = movies, aes(x=Budget, y=In.Theatres.wks))+
  geom_point() +
  theme_bw()

#linear regression

RunLn.mod1 <- lm(In.Theatres.wks~Budget, data = movies)
RunLn.mod1

summary(RunLn.mod1)

plot(movies$In.Theatres.wks~movies$Budget)
abline(RunLn.mod1$coefficients)

#Residual Plot

RunLn.res <- resid(RunLn.mod1)
hist(RunLn.res)

plot(movies$Budget, RunLn.res, 
     ylab="Residuals", xlab="Budget", 
     main="Residual Plot for Wks vs. Budget") 
abline(0, 0)


#with ggplot

ggplot(data = movies, aes(x=Budget, y=In.Theatres.wks)) +
  geom_point() +
  geom_smooth(method = "lm", se = TRUE)


#ANOVA

movies.groups <- group_by(movies, Genre)

boxplot(movies$Runtime~movies$Genre)

summarize(movies.groups, mean = mean(Runtime), sd = sd(Runtime), n=n())

anova(lm(Runtime~Genre, data=movies))


#Note that you can use the anova() function on regular linear regression models

anova(RunLn.mod1)


#---------------
# Multiple Regession
#---------------

#Predict Total Gross using a combination of variables

mlm1 <- lm(Total.Gross~Budget+Theatres.Opening+In.Theatres.wks, data=movies)

summary(mlm1)
anova(mlm1)

mlm2 <- lm(Total.Gross~Budget+In.Theatres.wks, data=movies)

summary(mlm2)

mlm3 <- lm(Total.Gross~
             Budget+
             Theatres.Opening+
             In.Theatres.wks+
             Genre+
             CriticRate.RT+
             Month+
             Season+
             Franchise+
             Oscar.Nominated,
           data = movies)

summary(mlm3)

# What should we do now?