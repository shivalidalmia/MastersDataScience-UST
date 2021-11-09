library(tidyverse)

library(fivethirtyeight)

View(flying)

(x <- count(filter(flying, gender == "Male", children_under_18 == "TRUE")))

nycflights <- read.csv(file.choose())

View(nycflights)

View(nyc_more_2 <- filter(nycflights, arr_delay >= 2))

View(nyc_houston <- filter(nycflights, dest == "IAH" | dest == "HOU"))

nyc_oprt <- filter(nycflights, carrier == "UA" | carrier == "AA" | carrier == "DL")

View(nyc_oprt)

nyc_dept_summer <- filter(nycflights, month %in% list(7,8,9))

View(nyc_dept_summer)

#Arrived more than two hours late, but didn't leave late

View(nyc_arrival <- filter(nycflights, arr_delay > 2 & dep_delay <= 0))

#Were delayed by at least an hour, but made up over 30 minutes in flight
nyc_delayed <- filter(nycflights, arr_delay>= 1 & abs(arr_delay-dep_delay >=30))
     
View(nyc_delayed)            

#Departed between midnight and 6am (inclusive)
nyc_dept <- filter(nycflights, dep_time >= 2400 & dep_time <= 6)
View(nyc_dept)

sum(is.na(nycflights$dep_time))

sum(is.na(nycflights))

NA ^ 0

NA * 0

FALSE * NA

NA | TRUE

View(arrange(nycflights,dep_time,arr_time))

arrange(is.na(nycflights))

View(arrange(nycflights,desc(dep_delay+arr_delay)))

View(arrange(nycflights,air_time))
     
nycflights[32735,] <- NA

#select(filter(movies, Year == 2013, Oscar.Nominated == 1), Title) 

head(select(nycflights, starts_with("dep")))

rename(nycflights, tail_num = tailnum)

head(select(nycflights,flight,origin,dest,everything()))

head(select(nycflights,dep_time,dep_time,dep_delay,arr_time,arr_delay))

vars <- c("year", "month", "day", "dep_delay", "arr_delay")

head(select(nycflights,any_of(vars)))

head(select(nycflights, contains("TIME")))

nyc_flight_d <- select( 
  filter(nycflights,dest == "ORF" | dest == "SJU" | dest == "LAX")
,origin, dest,arr_time,dep_time)

View(nyc_flight_d)

nyc_flight_d <- mutate(nyc_flight_d, short_fl = arr_time - dep_time)

