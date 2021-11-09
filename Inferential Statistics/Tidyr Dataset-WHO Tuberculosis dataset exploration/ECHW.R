#Step1.Loading the dataset 'who' from tidyr package.
library(tidyverse)
library(tidyr)
library(ggplot2)
View(who)

# Dataset definition:
#   A subset of data from the World Health Organization Global Tuberculosis 
#   Report, and accompanying global populations with with 7,240 rows.
# Columns:
#   country-Country name
#   iso2-2 letter ISO country code
#   iso3-3 letter ISO country code
#   year- Year for which data is recorded
#   new_sp_m014...new_rel_f65-Counts of TB cases recorded by grouping
#   Note: These column names are named as explained.
#   e.g. new_sp_m014 
#   new - stands for new cases
#   sp - code for method of diagnosis (rel = relapse, sn = negative pulmonary smear, sp = positive pulmonary smear, ep = extrapulmonary)
#   m - code for gender (f = female, m = male)
#   014 - code for age group (014 = 0-14 yrs of age, 1524 = 15-24 years of age, 2534 = 25 to 34 years of age, 3544 = 35 to 44 years of age, 4554 = 45 to 54 years of age, 5564 = 55 to 64 years of age, 65 = 65 years of age or older)

#Step2.Data exploration

# Taking a subset for country India.
who_IN <- filter(who,who$iso2 == "IN")

View(who_IN)

# There are total 34 rows for IN as country. Checking the summary statistics.
summary(who_IN)

# From summary statistics we can see that there are 30 plus NA values for
# other diagnosis methods like 'sn','ep' etc except 'sp'.
# Hence, subsetting the data for diagnosis method 'sp' for this analysis.

who_IN_sp <- select(who_IN,country,iso2,iso3,year,contains("sp"))
View(who_IN_sp)

# Visualizing new TB cases for different age groups from 1980-2015

# Function for ploting new cases for all age groups
plotNewTBCases <- function(ageGrp) {
  plot(who_IN_sp[[paste("new_sp_m",ageGrp,sep="")]]~who_IN_sp$year,
       xlab="Year",
       ylab="Count of Cases",
       main=paste("TB cases for",ageGrp,"age group"),
       type="l",
       col="blue")
  lines(who_IN_sp[[paste("new_sp_f",ageGrp,sep="")]]~who_IN_sp$year,col="red")
  legend("topleft",c("Male","Female"),fill=c("blue","red"))
}

dev.off()


#par(mfrow=c(3,2))
#0-14
plotNewTBCases("014")

#15-24
plotNewTBCases("1524")

#25-34
plotNewTBCases("2534")

#25-34
plotNewTBCases("3544")

#45-54
plotNewTBCases("4554")

#55-64
plotNewTBCases("5564")

#65 and above
plotNewTBCases("65")

#Observations:
#1.All the plots show visible trend from year 1995 to 2015 as from the year 1980 to 1994 the values
#are NA. Verifying this by calculating summary stats for years 1980-1994.

who_IN_SP_1980_1994 <- filter(who_IN_sp,between(year,1980,1994))
View(who_IN_SP_1980_1994)

summary(who_IN_SP_1980_1994)
#From summary we can see that all the columns from new_sp_m014 to new_sp_f65 have NA values.
#Hence we remove these rows before performing the further analysis.

who_mod <- filter(who_IN_sp,between(year,1995,2012))

#2.From above plot we can say that as the years pass on the number of new
#cases the count of new cases increases for both males and females.

#3. 0-14 - From the plot it looks that the number of cases for females are higher than males 
#over the years. Let's calculate the average number of new cases for both males and females.

colnames(who_mod)
summary(select(who_mod,new_sp_m014,new_sp_f014))
#From summary stats we can see that the average number of new cases for females 
#(4625)are nearly twice of the number of cases for males(2560).

#4.Plot the average count of cases(average of cases from 1994-2015) for males
#across different age groups.

#Creating a new data frame with average number of cases for both males and females
#across all age groups
mean_males <- c(mean(who_mod$new_sp_m014,na.rm = TRUE),mean(who_mod$new_sp_m1524,na.rm = TRUE),mean(who_mod$new_sp_m2534,na.rm = TRUE),mean(who_mod$new_sp_m3544,na.rm = TRUE),mean(who_mod$new_sp_m4554,na.rm = TRUE),mean(who_mod$new_sp_m5564,na.rm = TRUE),mean(who_mod$new_sp_m65,na.rm = TRUE))
mean_females <- c(mean(who_mod$new_sp_f014,na.rm = TRUE),mean(who_mod$new_sp_f1524,na.rm = TRUE),mean(who_mod$new_sp_f2534,na.rm = TRUE),mean(who_mod$new_sp_f3544,na.rm = TRUE),mean(who_mod$new_sp_f4554,na.rm = TRUE),mean(who_mod$new_sp_f5564,na.rm = TRUE),mean(who_mod$new_sp_f65,na.rm = TRUE))
sd_males <-c(sd(who_mod$new_sp_m014,na.rm = TRUE),sd(who_mod$new_sp_m1524,na.rm = TRUE),sd(who_mod$new_sp_m2534,na.rm = TRUE),sd(who_mod$new_sp_m3544,na.rm = TRUE),sd(who_mod$new_sp_m4554,na.rm = TRUE),sd(who_mod$new_sp_m5564,na.rm = TRUE),sd(who_mod$new_sp_m65,na.rm = TRUE))
sd_females <- c(sd(who_mod$new_sp_f014,na.rm = TRUE),sd(who_mod$new_sp_f1524,na.rm = TRUE),sd(who_mod$new_sp_f2534,na.rm = TRUE),sd(who_mod$new_sp_f3544,na.rm = TRUE),sd(who_mod$new_sp_f4554,na.rm = TRUE),sd(who_mod$new_sp_f5564,na.rm = TRUE),sd(who_mod$new_sp_f65,na.rm = TRUE))
n_males <- c(18,18,18,18,18,18,18)
n_females <- c(18,18,18,18,18,18,18)

who_avg_mf <- data.frame("Age group" = c("0-14","15-24","25-34","35-44","45-54","55-64","65+"),
              "Mean_cases_males" = mean_males,
              "Mean_cases_females" = mean_females,
              "SD_cases_males" = sd_males,
              "SD_cases_females" = sd_females,
              "N_males" = n_males,
              "N_females" = n_females)

View(who_avg_mf)

#5.Plotting number of cases across all age groups for males
boxplot(who_avg_mf$Mean_cases_males~who_avg_mf$Age.group,ylab="Count of cases",
        xlab="Age groups",main="Males: Average cases v/s Age groups")

# qqnorm(who_avg_mf$Mean_cases_males)
# qqline(who_avg_mf$Mean_cases_males, col = "blue", lwd = 1)

#Conclusion: From the above plots we can see that average number of cases vary
#for males across different age groups.
#We can test this using hypothesis testing.

#6.Plotting average number of cases across all age groups for females
boxplot(who_avg_mf$Mean_cases_females~who_avg_mf$Age.group,ylab="Count of cases",
        xlab="Age groups",main="Females: Average cases v/s Age groups")

# qqnorm(who_avg_mf$Mean_cases_females)
# qqline(who_avg_mf$Mean_cases_females, col = "blue", lwd = 1)

#Conclusion: From the above plots we can see that average number of cases vary
#for females as well across different age groups.
#We can test this hypothesis by using ANOVA.

#3.Hypothesis testing using ANNOVA

#Question1: The average number of new TB cases are different for different age
#groups for males. Test using ANOVA test statistics.

#Question2: The average number of new TB cases are different for different age
#groups for females. Test using ANOVA test statistics.

#4.Hypothesis testing

#a.Question1 - The average number of new TB cases are different for different age
#groups for males. Test using ANOVA test statistics.

#b.Reason: As seen from the boxplot in step2 - Observation point-5, for males we see 
#considerable difference in average number of new cases for different age groups.
#Hence, decided to confirm this claim using hypothesis testing.

#c.Type of test: ANOVA analysis using F statistics.

#d.Checking model assumptions
#1.Independence: In this study all the individuals are independent of each other the 
#hence observations are independent.

#2.Normal approximation: By plotting the normal qqplot and histogram we can verify
#normality of data for all age groups.

#3.Constant Variance: By plotting boxplots we can check for constant variance across
#all age groups.

#0-14
par(mfrow=c(1,3))
qqnorm(who_mod$new_sp_m014)
qqline(who_mod$new_sp_m014, col = "blue")
hist(who_mod$new_sp_m014)
boxplot(who_mod$new_sp_m014)

#15-24
par(mfrow=c(1,3))
qqnorm(who_mod$new_sp_m1524)
qqline(who_mod$new_sp_m1524, col = "blue")
hist(who_mod$new_sp_m1524)
boxplot(who_mod$new_sp_m1524)


#25-34
par(mfrow=c(1,3))
qqnorm(who_mod$new_sp_m2534)
qqline(who_mod$new_sp_m2534, col = "blue")
hist(who_mod$new_sp_m2534)
boxplot(who_mod$new_sp_m1524)


#35-44
par(mfrow=c(1,3))
qqnorm(who_mod$new_sp_m3544)
qqline(who_mod$new_sp_m3544, col = "blue")
hist(who_mod$new_sp_m3544)
boxplot(who_mod$new_sp_m3544)


#45-54
par(mfrow=c(1,3))
qqnorm(who_mod$new_sp_m4554)
qqline(who_mod$new_sp_m4554, col = "blue")
hist(who_mod$new_sp_m4554)
boxplot(who_mod$new_sp_m4554)

#55-64
par(mfrow=c(1,3))
qqnorm(who_mod$new_sp_m5564)
qqline(who_mod$new_sp_m5564, col = "blue")
hist(who_mod$new_sp_m5564)
boxplot(who_mod$new_sp_m5564)

#65+
par(mfrow=c(1,3))
qqnorm(who_mod$new_sp_m65)
qqline(who_mod$new_sp_m65, col = "blue")
hist(who_mod$new_sp_m65)
boxplot(who_mod$new_sp_m65)

#e.Null and alternate hypothesis
# H0: Mu_m_014 = Mu_m_1524 = Mu_m_2534 = Mu_m_3544 = Mu_m_45-54 = Mu_m_5564 = Mu_m_65
# HA: At least average number of cases is different for one age group for males.  .

#f.Calculating f statistics.

who_avg_mf
# Total sample size
n<- 18*7

# Total groups
k <- 7

# Determine df for groups, error and total.
(dfg <- k-1)
(dft <- n-1)
(dfe <- dft-dfg)

#Determine mean of mean number of cases for all groups
t_mean <- mean(who_avg_mf$Mean_cases_males)

#Appending number of cases for all observations
(no_of_sp_m <- (c(who_mod$new_sp_m014,who_mod$new_sp_m1524,who_mod$new_sp_m2534,
                  who_mod$new_sp_m3544,who_mod$new_sp_m4554,who_mod$new_sp_m5564,
                  who_mod$new_sp_m65)))

# Determine Sum of squares total
(SST <- sum((no_of_sp_m-t_mean)^2))

# Determine Sum of squares between groups
(SSG <- sum(who_avg_mf$N_males * (who_avg_mf$Mean_cases_males - t_mean)^2))

# Determine sum of squares error
(SSE <- SST - SSG)

# Determine mean square error
(MSE <- SSE/dfe)

# Determine mean square for groups
(MSG <- SSG/dfg)

# F-statistics
(f <- MSG/MSE)

# Determine p-value
(round(pf(f,dfg,dfe,lower.tail = FALSE)))

#g.Conclusion:
#The p-value is 0 which is less than significance level of 0.05. Hence, we reject
#the null hypothesis.
#We have enough evidence to say that average number of new cases for males are different
#for at least one of the age groups.

#a.Question2 - The average number of new TB cases are different for different age
#groups for females. Test using ANOVA test statistics.

#b.Reason: As seen from the boxplot in step2 - Observation point-6, for females we see 
#considerable difference in average number of new cases for different age groups.
#Hence, decided to confirm this claim using hypothesis testing.

#c.Type of test: ANOVA analysis using F statistics.

#d.Checking model assumptions
#1.Independence: In this study all the individuals are independent of each other the 
#hence observations are independent.

#2.Normal approximation: By plotting the normal qqplot and histogram we can verify
#normality of data for all age groups.

#3.Constant Variance: By plotting boxplots we can check for constant variance across
#all age groups.

#0-14
par(mfrow=c(1,3))
qqnorm(who_mod$new_sp_f014)
qqline(who_mod$new_sp_f014, col = "blue")
hist(who_mod$new_sp_f014)
boxplot(who_mod$new_sp_f014)

#15-24
par(mfrow=c(1,3))
qqnorm(who_mod$new_sp_f1524)
qqline(who_mod$new_sp_f1524, col = "blue")
hist(who_mod$new_sp_f1524)
boxplot(who_mod$new_sp_f1524)


#25-34
par(mfrow=c(1,3))
qqnorm(who_mod$new_sp_f2534)
qqline(who_mod$new_sp_f2534, col = "blue")
hist(who_mod$new_sp_f2534)
boxplot(who_mod$new_sp_f1524)


#35-44
par(mfrow=c(1,3))
qqnorm(who_mod$new_sp_f3544)
qqline(who_mod$new_sp_f3544, col = "blue")
hist(who_mod$new_sp_f3544)
boxplot(who_mod$new_sp_f3544)


#45-54
par(mfrow=c(1,3))
qqnorm(who_mod$new_sp_f4554)
qqline(who_mod$new_sp_f4554, col = "blue")
hist(who_mod$new_sp_f4554)
boxplot(who_mod$new_sp_f4554)

#55-64
par(mfrow=c(1,3))
qqnorm(who_mod$new_sp_f5564)
qqline(who_mod$new_sp_f5564, col = "blue")
hist(who_mod$new_sp_f5564)
boxplot(who_mod$new_sp_f5564)

#65+
par(mfrow=c(1,3))
qqnorm(who_mod$new_sp_f65)
qqline(who_mod$new_sp_f65, col = "blue")
hist(who_mod$new_sp_f65)
boxplot(who_mod$new_sp_f65)

#e.Null and alternate hypothesis
# H0: Mu_f_014 = Mu_f_1524 = Mu_f_2534 = Mu_f_3544 = Mu_f_45-54 = Mu_f_5564 = Mu_f_65
# HA: At least average number of cases is different for one age group for females.  .

#f.Calculating f statistics.

who_avg_mf

# Total sample size
n<- 18*7

# Total groups
k <- 7

# Determine df for groups, error and total.
(dfg <- k-1)
(dft <- n-1)
(dfe <- dft-dfg)

#Determine mean of mean number of cases for all groups
t_mean <- mean(who_avg_mf$Mean_cases_females)

#Appending number of cases for all observations
(no_of_sp_f <- (c(who_mod$new_sp_f014,who_mod$new_sp_f1524,who_mod$new_sp_f2534,
                  who_mod$new_sp_f3544,who_mod$new_sp_f4554,who_mod$new_sp_f5564,
                  who_mod$new_sp_f65)))

# Determine Sum of squares total
(SST <- sum((no_of_sp_f-t_mean)^2))

# Determine Sum of squares between groups
(SSG <- sum(who_avg_mf$N_females * (who_avg_mf$Mean_cases_females - t_mean)^2))

# Determine sum of squares error
(SSE <- SST - SSG)

# Determine mean square error
(MSE <- SSE/dfe)

# Determine mean square for groups
(MSG <- SSG/dfg)

# F-statistics
(f <- MSG/MSE)

# Determine p-value
(round(pf(f,dfg,dfe,lower.tail = FALSE)))

#g.Conclusion:
#The p-value is 0 which is less than significance level of 0.05. Hence, we reject
#the null hypothesis.
#We have enough evidence to say that average number of new cases for females are different
#for at least one of the age groups.


