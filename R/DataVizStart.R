install.packages("Tmisc")

library(Tmisc)
data(quartet)
View(quartet)
library(dplyr)
quartet %>%
  group_by(set) %>%
  summarize(mean(x),sd(x),mean(y),sd(y),cor(x,y))

