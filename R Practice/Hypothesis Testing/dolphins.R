###  Swimming With Dolphings Simulation ####

# There are several ways to do this, but here is one. 
# 13 out of 30 people improved. If we assume the
# dophin treatment had no effect, then they would have 
# improved anyway.
#
# 10 of those 13 were in the treatment group. If they
# would have improved anyway, then they ended up in
# the treatment group by random chance alone.
#
# How likely is that?

# Method 1: Simulate randomly assigning Treatment (T)
# or Control (C) to the 13 people who improved.

dolphins <- NULL
trials <- 1000

for(i in 1:trials){
  s <- sample(rep(c("T","C"),each = 15),13,replace = FALSE)
  treatments <- sum(s == "T")
  dolphins <- c(dolphins,treatments)
}

hist(dolphins)
successes <- sum(dolphins >= 10)

p_value <- successes/trials

# Method 2: 13 out of 30 people improved (I) versus 
# no improvement (N). Randomly select 15 for the
# treatment group.

dolphins2 <- NULL

for(i in 1:trials){
  treats <- sample(c(rep("I",13),rep("N",17)),15)
  improvers <- sum(treats == "I")
  dolphins2 <- c(dolphins2,improvers)
}

hist(dolphins2)

successes2 <- sum(dolphins2 >= 10)
p_value2 <- successes2/trials
