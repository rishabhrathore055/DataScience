library(ggplot2)
library(palmerpenguins)
ggplot(data = diamonds) +
  geom_bar(mapping = aes(x=cut, fill= cut))

ggplot(data = diamonds) +
  geom_bar(mapping = aes(x=cut, fill= clarity))

ggplot(data = penguins) +
  geom_point(mapping = aes(x = flipper_length_mm, y = body_mass_g,color = species)) +
  facet_wrap(~species)

ggplot(data = penguins) +
  geom_point(mapping = aes(x = flipper_length_mm, y = body_mass_g,color = species)) +
  facet_grid(~species)

ggplot(data = diamonds) +
  geom_bar(mapping = aes(x = color, fill = cut)) +
  facet_wrap(~cut)

ggplot(data = penguins) +
  geom_point(mapping = aes(x = flipper_length_mm, y = body_mass_g,color = species)) +
  labs(title = "Palmer Penguins : Body Mas vsFlipper Lenght", subtitle = "Sample of the Three penguins species",
  caption ="Data is collected by Dr.Kristen Gorman") +
  annotate("text", x = 220,y = 3500, label = "The Gentoos are the largest", fontface = "bold",size = 4.5,angle = 28)

  ggsave("Three Penguin Species.png")
