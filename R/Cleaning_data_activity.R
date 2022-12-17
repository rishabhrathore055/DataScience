library(tidyverse)
library(skimr)
library(janitor)

df <- read.csv("hotel_bookings.csv")

head(df)

str(df)

glimpse(df)

colnames(df)

skim_without_charts(df)

trimmed_df <- bookings_df %>% 
  select(hotel, is_canceled, lead_time)

trimmed_df %>% 
  select(hotel, is_canceled, lead_time) %>% 
  rename(hotel_type = hotel)

example_df <- bookings_df %>%
  select(arrival_date_year, arrival_date_month) %>% 
  unite(arrival_month_year, c("arrival_date_month", "arrival_date_year"), sep = " ")
