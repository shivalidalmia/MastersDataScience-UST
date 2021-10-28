# Tidyverse basics

# Tibbles vs. Data Frames

install.packages("tidyverse")
library(tidyverse)

movies <- read.csv(file.choose())

tidy.movies <- read_csv(file.choose())

#  Finding subsets of data with filter() and select()
#  filter([dataframe or tibble], var1 == cond1, var2 == cond2, ...)
#  select([dataframe or tibble], var1)

filter(tidy.movies, MPAA.Rating == "PG13", Year == 2013)

wide14 <- filter(tidy.movies, Theatres.Opening > 3000, Year == 2014)


movies.slim <- select(tidy.movies, Title, MPAA.Rating, Theatres.Opening, Year, Budget)

filter(movies.slim, MPAA.Rating == "PG13", Year == 2013)




# Add new columns with mutate
# mutate([dataframe or tibble], new.col1 == formula, new.col2 == formula2, etc....)

mutate(movies.slim, Theat.Budg = Budget/Theatres.Opening)

# Note that you can refer to columns you just created.




# Summarise with summarise()
# summarise([dataframe or tibble], summary.val1 = function or formula, summary.val2 = function or formula, ...)

summarise(tidy.movies, AvgBudg = mean(Budget), MedBudg = median(Budget))

# Grouping and summarising
# summarise is nice, but it's better if we group

movies_by_rating <- group_by(tidy.movies, MPAA.Rating)

summarise(movies_by_rating, AvgBudg = mean(Budget), MedBudg = median(Budget))


# Piping
# Piping allows for a much more readable way to combine this functions.

tidy.movies %>% 
  select(Title, Budget, Theatres.Opening, MPAA.Rating, Total.Gross) %>% 
  filter(Theatres.Opening > 2000) %>% 
  mutate(Total.Net = Total.Gross-Budget) %>%
  group_by(MPAA.Rating) %>%
  summarise(Avg.Budg = mean(Budget), Avg.Net = mean(Total.Net))



#  Exercise
#  1. Just view the horror movies (Genre H)
#  2. made a new tibble with just title, genre, and budget.
#  3. find the average budget for each genre.
#  4. add a column to the tidy.movies object that shows the 
#     difference between theatres opening weekend vs the theaters in widest release