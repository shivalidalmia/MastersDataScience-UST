##### ANOVA in R #####

# Load the movies data set #

movies <- read.csv(file.choose())

# Is there a relationship between Critic Rating and Genre?

boxplot(CriticRate.RT~Genre, data = movies)

# Let's do ANOVA to check

# First fit a linear model (more on this later)

mod1 <- lm(CriticRate.RT~Genre, data = movies)

# View the Anova Table

anova(mod1)


# What do we think?

# Looking at pairwise comparisons

mod2 <- aov(CriticRate.RT~Genre, data = movies)

TukeyHSD(mod2)


##### Linear Regression #####

# Load the Burger King data

burgers <- read.csv(file.choose())

# Let's look at calories vs. Fat

lm0 <- lm(Calories~Fat.g., data = burgers) 

lm0

summary(lm0)

anova(lm0)

ggplot(data = burgers, aes(x = Fat.g., y= Calories)) +
  geom_point() +
  geom_smooth(method = "lm")






