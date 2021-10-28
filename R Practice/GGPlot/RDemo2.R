### Exploring Data with R  ###

# Lecture 2 (and probably 3) R Demonstration

# Load Data
movies <- read.csv(file.choose())

# OR

movies <- read.csv("~/Dropbox/SEIS 631/R/Movies.csv") #Must specify an exact file path

# OR

install.packages("tidyverse")
library(tidyverse)
tidy.movies <- read_csv(file.choose())  # This loads it as a "tibble." More on this later.

# calling the name of a dataframe (or tibble) prints
# a portion of the object to the screen.
# Note difference between the base R dataframe and the tibble

movies

tidy.movies

# Check data structure and attributes
str(movies) # base

glimpse(movies) # tidyverse

class(movies$Title)  #Note the "$" operator allows you to access specific variables

names(movies)

# View first and last 6 obs
head(movies)
tail(movies)

# Check the help page. How can you view a different number of observations than 6?

# View entire data set in RStudio viewer

View(movies) # Note the capital V

### Accessing Specific Values or Sets of Values from a dataframe (or tibble)
# This works for most data objects (matrices, vectors, lists, etc)
# View first movie title

movies[1,1]  # row 1, column 1. df[row, col]

movies$Title[1] # access column by name, row by number

# View first movie's total gross (column 2)
movies[1,2]

movies$Total.Gross[1]

# View all movie titles
movies[,1] # displays as a "vector"

movies[1]   # displays as a "data.frame"

movies$Title # displays as a "vector"

select(movies, Title) # data.frame

# Try these four with the tibble.
# What's different?

# Which movies were released in 2014? 
# View only 2014 movie titles

movies[1:30,1]  # Note that 1:30 creates a list of the numbers from 1 to 30 inclusive. This works any time a list is called for

movies[movies$Year == 2014, 1]

# Using the filter() function

filter(movies, Year == 2014)

filter(movies, Year == 2014)$Title

#Combining select() & filter()
select(filter(movies, Year == 2014), Title) 

# Other subsets
movies[c(1,5,9),1]

# Note the use of a list here:  
# the "c( )" function creates lists or vectors. 
# c stands for "combine" 
# Enter items separated by commas.
# Can combine individual items or existing vectors.

c(2,4,6)
c(1:3,7,20:25)

# Multiple arguments for filter() & select()

select(filter(movies, Year == 2014, Budget.mil > 100), Title, Budget.mil)

# The following is the exact same code, just using line breaks
# to make it more readable.

select(
  filter(movies, 
         Year == 2014, 
         Budget.mil > 100
         ), 
  Title, 
  Budget.mil
  )

# Exercise
# 1) Display only the Genre's of the movies
# 2) Display only Title and Genre of the movies
# 3) Display only Title and Genre of Franchise movies (1 in the Franchise column)
# 4) Display only Title and Genre of Franchise movies that were Oscar Nominated


#sums, averages (means) and medians

sum(movies$Budget)
mean(movies$Budget)
median(movies$Budget)

#Say I don't care about "Total.Gross" and want to remove it from my dataset
movies_new <- movies[ ,c(1,3:20)]

#Alternatively
movies_new <- movies[ ,-c(2)]

movies_new <- select(movies, -Total.Gross)

#Get rid of 2014 movies
movies_new <- movies_new[31:180, ]

#OR

movies_new <- movies_new[movies_new$Year != 2014,]

movies_new <- filter(movies_new, Year != 2014)

# Create a new column by combining other columns

movies_new$Domestic.Deficit <- movies_new$Domestic.Gross - movies_new$Foreign.Gross


#Replace the 4th observation of the 5th variable with a missing value
movies_new[4,5] <- NA
#Replace it with a "1"
movies_new[4, "Theatres.Opening"] <- 1
#Replace it with missing value again
movies_new[4, "Theatres.Opening"] <- NA

# How would you change the Budget value for the 4 row to NA?
# Change it. Also change the Budget value for the 2nd row to NA.

#Test to see what has the missing value

is.na(movies_new$Theatres.Opening)

head(is.na(movies_new))

sum(is.na(movies_new))  # "counts" the TRUEs

complete.cases(movies_new)

sum(complete.cases(movies_new))

dim(movies_new)

#remove the observations with missing values
movies_new <- movies_new[complete.cases(movies_new),]

#Change a variable into a factor
movies_new$Franchise <- as.factor(movies_new$Franchise)

#histogram of movie budgets
hist(movies$Budget)

hist(movies$Budget, breaks = 15)


#Q: Will mean > median?
mean(movies$Budget)
median(movies$Budget)

sd(movies$Budget)  #Standard Deviation
IQR(movies$Budget)  #Interquartile Range

boxplot(movies$Budget, main="Boxplot of Budget")

plot(x=movies$Budget,y=movies$Total.Gross)


#Making the charts of Movie Data

#Pie chart
table(movies$Genre)
count <- table(movies$Genre)
names(count)
pie(count,labels=names(count))

#Bar plot
barplot(count)

prop.table(count)

barplot(prop.table(count))


#Contingency table

table(movies$Franchise, movies$Genre)

movie.table <- table(movies$Franchise, movies$Genre)  #Store the table

movie.table  #Print a stored table

#Sums across rows
margin.table(movie.table,1)
#Sums across columns
margin.table(movie.table,2)

#Proportion of the total sample
prop.table(movie.table)
#Proportion of row total
prop.table(movie.table,1)
#Proportion of column total
prop.table(movie.table,2)

#segmented bar plot
barplot(movie.table)
legend("topright", legend=c("Franchise","non-Fran"),fill=c("grey","black"))

#Mosaic plot
mosaicplot(movie.table)

#Side-by-side boxplot
boxplot(movies$Budget~movies$Franchise)

boxplot(movies$Budget~movies$MPAA.Rating)
#Note "~" means "versus" or "as a function of"
# A~B is often read as "A modeled by B"

