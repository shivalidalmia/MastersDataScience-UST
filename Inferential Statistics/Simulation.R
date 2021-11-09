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

N <- 17
trials <- 10000

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

# Before running the simulation we need a place
# to store the results

numb_of_heads <- NULL # Empty vector for storing the results

for(i in 1:trials){      
  flips <- sample(outcomes, size=N, replace=T)
  H <- sum(flips)
  numb_of_heads <-c(numb_of_heads,H)
}

mean(numb_of_heads)
hist(numb_of_heads, breaks = 0:(N+1)-0.5)
table(numb_of_heads)

# How many times in our 10000 trials did we get 11 heads?

sum(numb_of_heads == 11)

# What is that as a probability?

sum(numb_of_heads == 11)/trials

# What about at least 11 heads?

sum(numb_of_heads >= 11)
x <- sum(numb_of_heads >= 11)
p.value <- x/trials
p.value
