############  Normal Distribution, Binomial Dist, & Sampling ################

## Examining Normal Distributions

# Let's look at chicken weights in the built in data set ChickWeights

hist(ChickWeight$weight)

# Does it look normal?

# Overlay a normal distribution:
library(tidyverse)

ggplot(ChickWeight, aes(x = weight)) +
  geom_histogram(aes(y = ..density..), 
            fill = "blue",
            colour = "black", 
            alpha = 0.6, 
            binwidth = 25) + 
  stat_function(fun = dnorm,
                args = c(mean(ChickWeight$weight), sd(ChickWeight$weight)))

# Create a Normal-Probability Plot

qqnorm(ChickWeight$weight)
qqline(ChickWeight$weight)

# Another example: The famous "iris" data set

iris %>%
  filter(Species == "versicolor") %>%
  select(Sepal.Length) %>%
  unlist() %>%
  mean() -> SL.mean

iris %>%
  filter(Species == "versicolor") %>%
  select(Sepal.Length) %>%
  unlist() %>%
  sd() -> SL.sd

iris %>%
  filter(Species == "versicolor") %>%
ggplot(aes(x = Sepal.Length)) +
  geom_histogram(aes(y = ..density..), 
                 fill = "blue",
                 colour = "black", 
                 alpha = 0.6,
                 binwidth = 0.2) + 
  stat_function(fun = dnorm,
                args = c(SL.mean, SL.sd))

iris %>%
  filter(Species == "versicolor") %>%
  select(Sepal.Length) %>%
  unlist() %>%
  qqnorm()

iris %>%
  filter(Species == "versicolor") %>%
  select(Sepal.Length) %>%
  unlist() %>%
  qqline() 

## Roll a dice 10000 times
d <- sample(1:6,10000,replace = TRUE)
hist(d, breaks = c(1:7-0.5))

## Roll two dice and add them, 10000 times

d1 <- sample(1:6, 10000, replace = TRUE)
d2 <- sample(1:6, 10000, replace = TRUE)

hist(d1+d2, breaks = c(1:13-0.5))

## Roll 3 dice and add them, 10000 times

d1 <- sample(1:6, 10000, replace = TRUE)
d2 <- sample(1:6, 10000, replace = TRUE)
d3 <- sample(1:6, 10000, replace = TRUE)


hist(d1+d2+d3, breaks = c(1:19-0.5))


## Roll N dice?

N = 100
t = 10000
rolling_sum <- rep(0,t)

for(i in 1:N){
  rolling_sum <- rolling_sum + sample(1:6, t, replace = TRUE)
}

ggplot(as.data.frame(rolling_sum), aes(x = rolling_sum)) + 
  geom_histogram(fill = "blue", 
                 colour = "black", 
                 alpha = 0.6,
                 binwidth = 1)

## Exercise: repeat for 10 dice, 100 dice. Bonus: What about a 20 sided die?


## Simulating Measurement Errors
## Making measurements are complicated. Assume a single measurement has
## many sources of error. Also assume each of these errors is random,
## uniformly distributed over some interval.

N = 5
t = 10000
error_sum <- NULL

for(j in 1:t){
  error_sum <- c(error_sum, sum(runif(N, min=-1,max=1)))
}
hist(error_sum)

###### Working with the Normal distrubtion in R

# Get a random sample from a normal distribution

n <- rnorm(30, mean = 50, sd = 10)
hist(n)

n <- rnorm(100)  # no mean or sd --> Standard Normal, mean = 0, sd = 1

# What's proportion of test takers score below 1200
# on the SAT (mean = 1500, sd = 300)

pnorm(1200, mean = 1500, sd = 300)

# Alternatively

z_score <- (1200-1500)/300

pnorm(z_score)  # z-scores are standard normal

# Above 2000?

pnorm(2000, mean = 1500, sd = 300, lower.tail = FALSE)

# What score is needed to be in the 90% percentile?

qnorm(0.9, mean = 1500, sd = 300)


## Binomial Distributions & The Normal Approximation

# Coin Flip: probability of success, p = 0.5

# Sanity check: What's the probability of getting 1 head out of 1 flips?
dbinom(x = 1, size = 1, prob = 0.5)   # x: # of success, size: # of trials, prob: # prob of success

# What's the probability of getting 5 heads out of 10 flips
dbinom(x = 5, size = 10, prob = 0.5)

# Exercise: What's the probability of getting 10 heads out of 20?
#           50 out of 100?
#           500 out of 1000?

# What's the probabiity of getting between 4 & 6 heads out of 10 (inclusive)?

sum(dbinom(4:6, size=10, prob = 0.5))

# Excercise: What's the probabiity of getting between 40 & 60 heads out of 100 (inclusive)?
#            What's the probabiity of getting between 400 & 600 heads out of 1000 (inclusive)?

# Basketball: Zion Williamson is 68% shooter (p = 0.68). 
# If Zion takes 23 shots in a game, what is the probability 
#    he makes 12 or fewer basekts?

#Using dbinom
sum(dbinom(0:12, size = 23, prob = 0.68))

#Using pbinom
pbinom(12, size = 23, prob = 0.68)

# In 70% of the games, you'd expect him to score at least how many basekts?

qbinom(0.7, 23, lower.tail = FALSE, 0.68)

## Let's generate a sample of games
rbinom(1,23,0.68)

## Let's simulate 1000 games:
zion <- rbinom(1000,23,0.68)
hist(zion)


### Binomial Distribution vs. Normal Distribution

## 70% of the dogs in the TSA program have floppy ears. If we randomly sample
## 75 dogs, what's the probability that our sample has between 45 and 55 (inclusive)
## dogs with floppy ears?

sum(dbinom(45:55,75,0.7))

## OR

pbinom(55,75,0.7)-pbinom(44,75,0.7)  #Note the 44. Why?

## Normal Approx
m = 0.7*75
std = sqrt(75*0.7*0.3)

pnorm(55, m, std) - pnorm(45, m, std)

## Notice it's not so good...
## With the correction:

pnorm(55+0.5, m, std) - pnorm(45-.5, m, std)

N <- rnorm(10000, m, std)
B <- rbinom(10000, 75, 0.7)

NormVBin <- data.frame(distr = rep(c("Norm","Binom"),each = 10000), val = c(N,B))

ggplot(NormVBin, aes(x = val)) + 
  facet_wrap(~distr) +
  geom_histogram(binwidth = 1)

ggplot(NormVBin, aes(x = val, color = distr)) + 
  geom_freqpoly(binwidth = 1)




######  How do samples compare to the population: For a proportion  ######

## We'll let R store the population in the background and sample from it

## let's say the Ture Proportion P = 0.65. Let's sample of size n from that population.

P <- 0.65
n <- 25

samp <- sample(c(1,0),n,c(P,1-P), replace = TRUE)

mean(samp)

# Let's repeat this lots of times and see what we get

samp_props <- NULL

for(i in 1:10000){
  temp_samp <- sample(c(1,0),n,c(P,1-P), replace = TRUE)
  
  samp_props <- c(samp_props,mean(temp_samp))
  
}

mean(samp_props)
sd(samp_props)

ggplot(as.data.frame(samp_props),aes(x=samp_props))+
  geom_histogram(binwidth = 0.05, # binwidth specifies the width of each bin, while bins specifies the # of bins
                 col="blue", 
                 fill="green", 
                 alpha = .2) + 
  labs(title="Sampling Distribution for a Proportion. Red Line Indicates the True Proportion", x="Sample Proportion", y="Count") +
  geom_vline(xintercept = P, color = "red")

# Exercise: repeat this for larger samples. (Note that you may want to change the bin width.) 
# What do you notice?


# Let's do this a function so we can easily repeat.

propSamplingDist <- function(true_p, N, trials){
  samp_props <- NULL
  
  for(i in 1:trials){
    temp_samp <- sample(c(1,0),N,c(true_p,1-true_p), replace = TRUE)
    
    samp_props <- c(samp_props,mean(temp_samp))
    
  }
  
  print(paste("Mean proportion for all sammples:",mean(samp_props)))
  print(paste("Standard Deviation for the proportions for all sammples:",sd(samp_props)))
  
  ggplot(as.data.frame(samp_props),aes(x=samp_props))+
    geom_histogram(bins=20,
                   col = "blue",
                   fill = "green",
                   alpha = 0.2) +
    labs(title = "Sampling Distribution for a Proportion. Red Line Indicates the True Proportion", x="Sample Proportion", y="Count") +
    geom_vline(xintercept = true_p, color = "red")
  }
  
  