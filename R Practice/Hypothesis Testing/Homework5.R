setwd("C:/Users/shiva/Documents/MS Data Science/631-Foundations of Data Analysis/Class9/Homework5")

nc <- data.frame(load("nc.RData"))

head(nc)

View(nc)

count(nc)


summary(nc)

library(tidyverse)
nc %>%
  group_by(habit) %>%
summarise(mean_weight = mean(weight), sd_weight = sd(weight,na.rm=TRUE), N = n())

numerator <- 7.14-6.83-0
sd()

denom <- sqrt(((1.52^2)/873) + ((1.39^2)/126))

Z_score = numerator/denom
Z_score
pnorm(Z_score,0,1)

qnorm(0.026)

?sd

t.test(weight~habit, data = nc, alternative = "two.sided", var.equal = TRUE, conf.level = 0.95)
