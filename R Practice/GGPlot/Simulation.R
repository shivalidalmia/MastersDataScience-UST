# The sample function

sample(letters, 4)

sample(1:10, 6)

sample(1:5, 7)

#What went wrong?

sample(1:5, 7, replace = TRUE)

s <- sample(1:5, 7, replace = TRUE)

sample(1:10, 6, replace = TRUE)  # put the numbers back in before picking the next

sample(c(2,3,5),30, replace = TRUE)

sample(c(2,3,5),30, replace = TRUE, prob =c(0.8,0.1,0.1))

#coin flip simulation
outcomes <- c(1,0)  # 1 = Heads, 0 = tails

sample(outcomes, 17, replace = TRUE)

flips <- sample(outcomes, 17, replace = TRUE)

# How many heads?
sum(flips)


# Running the simulation many times

# For Loops
#
# for(index variable in a list){
#   do this repeatedly
# }
#
# index variable can be any unused variable name (i is common)
# list can be any list (or vector). 
# The length of the list determines how many times
# the loop iterates

# Example

for(i in c(3,4,10)){
  print(i)
}

# Each time through the loop, i takes on a different value
# from the list c(3,4,10), and the loops prints it.
# This is a pretty useless "for loop" but it illustrates
# how the loop works.

# Setting up the simulation 

N <- 17          # # of flips per trials
trials <- 10000  # # of trials

# Before running the simulation we need a place
# to store the results

results1 <- NULL # Empty vector for storing the results

for(i in 1:trials){      
  flips <- sample(outcomes, size = N, replace = T)
  heads <- sum(flips)
  results1 <-c(results1, heads)
}

mean(results1)
hist(results1, breaks = 0:(N+1)-0.5)
table(results1)

# How many times in our 10000 trials did we get 11 heads?

sum(results1 == 11)

# What is that as a proportion (probability)?

sum(results1 == 11)/trials

# What about at least 11 heads?

sum(results1 >= 11)
x <- sum(results1 >= 11)
p.value <- x/trials
p.value

# A different version that's more memory & time efficient

results2 <- rep(0, trials)  # a vector of '# of trials' zeros. Reserves memory for the results

for(i in 1:trials){
  flips <- sample(outcomes, N, replace = TRUE)
  results2[i] <- sum(flips)
}

sum(results2 >= 11)/trials

# Simulation without for loops

results3 <- replicate(trials, 
                            sum(sample(outcomes, N, replace = TRUE))
                            )

sum(results3 >= 11)/trials

# Comparing the methods for efficiency

system.time({
  results1 <- NULL 
  for(i in 1:trials){      
    flips <- sample(outcomes, size = N, replace = T)
    heads <- sum(flips)
    results1 <-c(results1, heads)
  }
}
)

system.time({
  results2 <- rep(0,trials)
  for(i in 1:trials){
    flips <- sample(outcomes, size = N, replace = T)
    results2[i] <- sum(flips)
  }
})


system.time(replicate(trials, sum(sample(outcomes, N, replace = T))))

