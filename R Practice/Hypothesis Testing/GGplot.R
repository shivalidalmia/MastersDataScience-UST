############  GGPlot2  #################
install.packages("ggplot2")

library(ggplot2)

##############################################
# ggplot2 is a very powerful visualization package
# We'll get a brief introduction here
# 
# The first principle is that we build graphics
# with layers. We add layers with the + symbol
##############################################

ggplot(data = movies)  #This works, but doesn't do anything. It just initializes the window

ggplot(data = movies, aes(x = Budget))

#aes() is short for "Aesthetic" This is how we describe how to put the data in the window.

ggplot(data = movies, aes(x = Budget)) + geom_histogram()  # Add our first layer with +

# Another plot

ggplot(data = movies, aes(x = Genre)) + geom_bar() # Add's a bar plot layer instead of hist


## Notice the difference in these next three lines. They all create the same graph
ggplot(data = movies, aes(x = Budget, y = Theatres.Opening)) + geom_point()

ggplot(data = movies) + geom_point(aes(x = Budget, y = Theatres.Opening))

ggplot(data = movies, aes(x = Budget)) + geom_point(aes(y = Theatres.Opening))


## Add returns after "+"  or "," to make the code more readable ##
ggplot(data = movies, aes(x = Budget, y = Theatres.Opening)) + 
  geom_point()

## More!! 
ggplot(data = movies, aes(x = Budget, y = Theatres.Opening)) + 
  geom_point(aes(colour = Genre))

## More!!!
ggplot(data = movies, aes(x = Budget, y = Theatres.Opening)) + 
  geom_point(aes(colour = Genre)) +
  geom_smooth()


## More!!!!
ggplot(data = movies, aes(x = Budget, y = Theatres.Opening)) + 
  geom_point(aes(colour = Genre)) +
  geom_smooth() + 
  theme_classic()

## You can add layers by storing the graph in a variable.

gr <- ggplot(data = movies, aes(x = Budget, y = Theatres.Opening))

gr <- gr + geom_point(aes(colour = Genre))
gr

(gr <- gr + geom_smooth())
gr

movies %>%
  group_by(Franchise) %>%
  ggplot(aes(x = Budget, y = Theatres.Opening, group = Franchise)) +
  geom_point(colour = Franchise) +
  geom_smooth()

?geom_point
