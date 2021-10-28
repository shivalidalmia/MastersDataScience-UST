pnorm(2,0,1,lower.tail = FALSE)*100

pnorm(-2,0,1)*100 + pnorm(2,0,1,lower.tail = FALSE)*100

pnorm(-1.13,0,1,lower.tail = FALSE) * 100

pnorm(0.18,0,1) * 100

pnorm(8,0,1,lower.tail = FALSE) * 100

pnorm(0.5,0,1) - pnorm(-0.5,0,1)

(zverbal <- (160-151)/7) #1.28

(zquant <- (157-153)/7.67) # 0.5215124

pnorm(1.28,0,1)*100

pnorm(0.52,0,1) * 100

(4948-4313)/583 

(5513-5261)/807

pnorm(0.3122677,0,1)

qnorm(0.70,151,7,lower.tail = FALSE)

qnorm(0.05,4313,583,)

qnorm(0.10,5261,807,lower.tail = FALSE)

pnorm(0,14.7,33)

qnorm(0.15,14.7,33,lower.tail = FALSE)

pnorm(28,25,2.8,lower.tail = FALSE)

qnorm(0.75,25,2.8) - qnorm(0.25,25,2.8)

pnorm(-1.17)

pnorm(48,55,6)

pnorm(65,55,6) - pnorm(60,55,6)

qnorm(0.10,55,6,lower.tail = FALSE)

pnorm(54,55,6)

qnorm(0.75,1650,223.88)

pnorm(80,72.6,4.78)

pnorm(80,72.6,4.78) - pnorm(60,72.6,4.78)

qnorm(0.05,72.6,4.78, lower.tail = FALSE)

pnorm(70,72.6,4.78,lower.tail = FALSE)

pnorm(50,45,3.2,lower.tail = FALSE)

pnorm(75,89,15) - 0.1753239 17% is below 75$
  
qnorm(0.75,89,15)  #The 75th percentile price is 99.11.

sum(dbinom(1:6,size=6,p=0.125))

pnorm(2100,1500,300)
1- pnorm(2100,1500,300) + pnorm(1900,1500,300)

qnorm(0.68,77.7,8.44)   81.64



N <- 15        # # of flips per trials
trials <- 1000  # # of trials

# Before running the simulation we need a place
# to store the results
outcomes <- c(1,0)
results1 <- NULL # Empty vector for storing the results

for(i in 1:trials){      
  flips <- sample(outcomes, size = N, replace = T)
  heads <- mean(flips)
  results1 <-c(results1, heads)
}

hist(results1)


