setwd("C:/Users/shiva/Documents/MS Data Science/631-Foundations of Data Analysis/Class7/Homework4")

ames <- data.frame(load("ames.RData"))

head(ames)
View(ames)

(area <- ames$Gr.Liv.Area)

(price <- ames$SalePrice)

summary(area)

hist(area)  #right skewed


samp0 <- sample(area,50)

samp1 <- sample(area,50)

summary(samp0)

summary(samp1)

# Histogram of sample0
hist(samp0)

hist(samp1)

samp.df <- data.frame(samp0=samp0,samp1=samp1)

library(ggplot2)

ggplot(data=samp.df) +
  geom_density(aes(x=samp0,color="red")) +
  geom_density(aes(x=samp1,color="blue"))


samp2 <- sample(area,100)

samp3 <- sample(area,1000)

summary(samp2)

summary(samp3)

sample_means50 <- rep(NA,5000)

for(i in 1:5000){
  samp <- sample(area,50)
  sample_means50[i] <- mean(samp)
}

x <- hist(sample_means50)

summary(sample_means50)

sample_means10 <- rep(NA,5000)
sample_means100 <- rep(NA,5000)


for(i in 1:5000){
  samp <- sample(area,10)
  sample_means10[i] <- mean(samp)
  samp <- sample(area,100)
  sample_means100[i] <- mean(samp)
}

par(mfrow=c(3,1))
xlimits = range(sample_means10)
hist(sample_means10, breaks = 20, xlim = xlimits)
hist(sample_means50, breaks = 20, xlim = xlimits)
hist(sample_means100, breaks = 20, xlim = xlimits)

samp.df2 <- data.frame(samp.size = rep(c(10,50,100),each=5000),samp.means = c(sample_means10,sample_means50,sample_means100))


ggplot(samp.df2, aes(x = samp.means)) +
  face_grid(rows = vars(samp.size)) +
  geom_histogram(col = "black", alpha = 0.2)



ggplot(samp.df2,aes(x=samp.means, color = as.factor(samp.size))) +
  geom_density()

samp0_price <- sample(price,50)

summary(samp0_price)

hist(samp0_price)

sample_price_means50 <- rep(NA,5000)

for(i in 1:5000){
  samp <- sample(price,50)
  sample_price_means50[i] <- mean(samp)
}

hist(sample_price_means50)

summary(sample_price_means50)

summary(price)

sample_means_150 <- rep(NA,5000)

for(i in 1:5000){
  samp <- sample(price,150)
  sample_means_150[i] <- mean(samp)
}

par(mfrow=c(2,1))
xlimits = range(sample_price_means50)
hist(sample_price_means50, breaks = 20, xlim = xlimits)
hist(sample_means_1_50, breaks = 20, xlim = xlimits)

summary(sample_means_150) # IQR = 8739 , 15428

