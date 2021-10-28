library(tidyverse)

students <- read_csv(file.choose())

heights <- select(students, gender, height)

m_sds <- heights %>%
  group_by(gender) %>%
  summarise(mean = mean(height), sd = sd(height))


# Female without normal curve
heights %>%
  filter(gender == "Female") %>%
  ggplot(aes(height)) +
  geom_histogram(binwidth = 4, fill = "red", alpha = 0.6, color = "black", aes(y=..density..)) +
  theme_bw()

# Female with normal curve
heights %>%
  filter(gender == "Female") %>%
  ggplot(aes(height)) +
  geom_histogram(binwidth = 4, fill = "red", alpha = 0.6, color = "black", aes(y=..density..)) +
  stat_function(fun = dnorm, args = m_sds[1,2:3])+
  theme_bw()
  

# Male without normal curve
heights %>%
  filter(gender == "Male") %>%
  ggplot(aes(height)) +
  geom_histogram(binwidth = 4, fill = "blue", alpha = 0.6, color = "black", aes(y=..density..)) +
  theme_bw()

# Male with normal curve
heights %>%
  filter(gender == "Male") %>%
  ggplot(aes(height)) +
  geom_histogram(binwidth = 4, fill = "blue", alpha = 0.6, color = "black", aes(y=..density..)) +
  stat_function(fun = dnorm, args = m_sds[2,2:3])+
  theme_bw()
    

# Stacked no normal curve
ggplot(heights, aes(height)) +
  geom_histogram(binwidth = 4, aes(fill = gender), color = "black",alpha = 0.6) +
  facet_wrap(vars(gender), nrow = 2)


# Stacked with normal curves

heights %>% 
  group_by(gender) %>% 
  nest(data = c(height)) %>% 
  mutate(y = map(data, ~ dnorm(
    .$height, mean = mean(.$height), sd = sd(.$height)
  ))) %>% 
  unnest(c(data,y)) %>% 
  
  ggplot(aes(x = height)) +
  geom_histogram(data = heights, 
                 binwidth = 4, 
                 colour = "black", 
                 aes(y = ..density.., fill = gender), 
                 alpha = 0.6) +
  geom_line(aes(y = y)) + 
  facet_wrap(~ gender, nrow = 2)

# Combined no normal curve

ggplot(heights, aes(height)) +
  geom_histogram(aes(y = ..density..), binwidth = 4, fill = "green", color = "black", alpha = 0.6) +
  theme_bw()

# with normal curve

ggplot(heights, aes(height)) +
  geom_histogram(aes(y = ..density..), binwidth = 4, fill = "green", color = "black", alpha = 0.6) +
  stat_function(fun = dnorm, args = c(mean(heights$height), sd(heights$height))) +
  theme_bw()
