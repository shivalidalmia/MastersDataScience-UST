#### Linear Regression & Model Conditions ####

# Load Burger_King_Items.csv 

burger <- read.csv(file.choose())

# Again, we'll start by regressing Calories on Fat.g.

# Check Model Assumptions: Linearity

plot(Calories~Fat.g., data = burger)

# To check the other assumptions we have to build the linear model

lm1.fat <- lm(Calories~Fat.g., data = burger)

# Are the residuals distributed roughly normally?
# First we have to generate the residuals. Fortunately, 
# lm() does that for us automatically.

head(lm1.fat$residuals)

hist(lm1.fat$residuals)
qqnorm(lm1.fat$residuals)
qqline(lm1.fat$residuals)  # add the identity line for reference

# What do we think?

# Constant Variability?
# To check this we create a scatter plot with the regression line
# and a residual plot.

plot(Calories~Fat.g., data = burger)
abline(lm1.fat)  # abline() adds the line to the most recent plot

# Note the shortcut in the last command.

coefficients(lm1.fat) # returns the intercept (a) and slope (b) 

# The intercept is...

(a <- coefficients(lm1.fat)[1])

# And the slope is...

(b <- coefficients(lm1.fat)[2])

# The abline() functions take a = ..., b = ... OR coef = c(a,b)
# OR it will take a suitable lm object (like ours) and figure
# out the slope and intercept on its own.

# All three of these give the same output

plot(Calories~Fat.g., data = burger)
abline(a = a, b = b)

plot(Calories~Fat.g., data = burger)
abline(coef = coefficients(lm1.fat))

plot(Calories~Fat.g., data = burger)
abline(reg = lm1.fat)

# Now let's do a residual plot.
# We can plot the residuals against x, y, or y-hat (predicted)
# Here it is against y:

plot(lm1.fat$residuals~burger$Calories)
abline(h = 0)  # h = 0 tells abline() to create a horizontal line at 0

# How would you plot residuals against x or y-hat?

### Advanced Level ###

# the plot() function will take a lm object. What does it do?

plot(lm1.fat)

# let's see them all at once

par(mfrow= c(2,2))
plot(lm1.fat) # Note that it does not show a scatter plot

# reset the plot window

par(mfrow = c(1,1))   # or
dev.off()  # turns of the plot window. When you call a plot it will turn back on and reset.

### Advanced and Fancy ###
install.packages("gridExtra")

library(gridExtra)
library(ggplot2)

p1 <- ggplot(burger, aes(x = Fat.g., y = Calories)) +
  geom_point(color = "blue", shape = 21, size = 2) +
  geom_smooth(method = "lm", color = "red") +
  xlab("Fat (g)") +
  theme_bw()

p2 <- ggplot(burger, aes(x = Fat.g.)) + 
  geom_point(aes(y=lm1.fat$residuals), 
             color = "blue", 
             shape = 21, 
             size = 2) +
  geom_abline(slope = 0, intercept = 0, color = "red") +
  xlab("Fat (g)") + ylab("Residuals") +
  theme_bw()


grid.arrange(p1,p2,nrow =2)

### Regression Analysis ###

summary(lm1.fat)

anova(lm1.fat)

# What does our model predict for a food with 70 g of fat?

# Hard way
lm1.fat$coefficients[1] + 70*lm1.fat$coefficients[2]

# Easier way
sum(c(1,70)*lm1.fat$coefficients)

# Easiest (??) way
predict(lm1.fat, newdata = data.frame(Fat.g. = 70))

# Note that you must type "newdata" and 
# newdata MUST be a data.frame and
# the name of the variable in the newdata data.frame
# must match exactly the name in your model.

### Multiple Regression ###

# Continuing on with our burger data:
# Carbs & Protein also contribute calories to foods.
# Let's include them in our model.
# The model will look like this
#
#   Cal.hat = b0 + b1*Fat + b2*Protein + b3*Carbs
#
# The corresponding R formula will look like this
#
#   Calories~Fat.g.+ Protein.g. + Carb.g.
#
# R knows to fill in the slopes and automatically includes
# an intercept.

# New Model
lm2.full <- lm(Calories~Fat.g.+Protein.g.+Carb.g., data = burger)

# Model Assumptions

hist(lm2.full$residuals)

qqnorm(lm2.full$residuals)
qqline(lm2.full$residuals)

plot(lm2.full$residuals~lm2.full$fitted.values) #resid vs. y-hat
plot(lm2.full$residuals~burger$Calories) #resid vs. y

plot(lm2.full) #just for fun

## Colinnearity of predictors? ##

library(psych)

pairs.panels(burger[,c(5,10,13)], # just the predictors
             method = "pearson") 

pairs.panels(burger[,c(3,5,10,13)], # with the response as well
             method = "pearson")


## Analsyis 

lm2.full

summary(lm2.full)
anova(lm2.full)

# Conclusions?

# What do we predict for a food with 10 g of fat, 8 g of Protein, and 6 g Carbs?

predict(lm2.full, 
        newdata = data.frame(Fat.g. = 10, 
                             Protein.g. = 8, 
                             Carb.g. = 6)
        )


avg.food <- predict(lm2.full, 
        newdata = data.frame(Fat.g. = 0, 
                             Protein.g. = mean(burger$Protein.g.), 
                             Carb.g. = mean(burger$Carb.g.))
)

pct20.food <- predict(lm2.full, 
                    newdata = data.frame(Fat.g. = 0, 
                                         Protein.g. = quantile(burger$Protein.g., 0.2), 
                                         Carb.g. = quantile(burger$Carb.g.,0.2))
)

pct80.food <- predict(lm2.full, 
                    newdata = data.frame(Fat.g. = 0, 
                                         Protein.g. = quantile(burger$Protein.g.,0.8), 
                                         Carb.g. = quantile(burger$Carb.g.,0.8))
)

plot(Calories~Fat.g., burger)
abline(a = avg.food, b= lm2.full$coefficients[2])
abline(a = pct20.food, b= lm2.full$coefficients[2], col = "green")
abline(a = pct80.food, b= lm2.full$coefficients[2], col = "red")

# The same in ggplot
ggplot(burger, aes(x = Fat.g., y = Calories)) + 
  geom_point(shape = 21) + 
  geom_abline(slope = lm2.full$coefficients[2], 
              intercept = avg.food) +
  geom_abline(slope = lm2.full$coefficients[2], 
              intercept = pct20.food, color = "green", linetype = "dashed") +
  geom_abline(slope = lm2.full$coefficients[2], 
              intercept = pct80.food, color = "red", linetype = "dashed") +
  theme_bw()

# Highlighting Foods High in carbs.

carb.avg = mean(burger$Carb.g.)

ggplot(burger, aes(x = Fat.g., y = Calories)) + 
  geom_point(shape = 21, 
             aes(colour = cut(Carb.g.,c(-Inf,carb.avg,Inf))))
