penguins %>%
  select(species)
  #select(-species)

# Changing colums name
penguins %>%
  rename(island_new = island)

rename_with(penguins,toupper)
rename_with(penguins,tolower)

clean_names(penguins)

