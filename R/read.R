getwd()
bookings_df <- read_csv("hotel_bookings.csv")
head(bookings_df)

str(bookings_df)
colnames(bookings_df)
new_df <- select(bookings_df, `adr`, adults)
mutate(new_df, total = `adr` / adults)
