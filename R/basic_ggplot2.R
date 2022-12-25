library(palmerpenguins)
library(ggplot2)
data(penguins)
View(penguins)
# Penguins Data sets
ggplot(data = penguins) + geom_point(mapping = aes(x = flipper_length_mm, y = body_mass_g))
ggplot(data = penguins, mapping = aes(x = flipper_length_mm, y = body_mass_g)) +  geom_point() # Another Way

ggplot(data=penguins) + geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g))

ggplot(data=penguins) + geom_point(mapping = aes(x=bill_length_mm,y=bill_depth_mm))


ggplot(data=penguins) + geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color= species))

ggplot(data=penguins) + geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,shape= species,color=species))
ggplot(data=penguins) + geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g, alpha=species))

ggplot(data=penguins) + 
  geom_smooth(mapping = aes(x=flipper_length_mm,y=body_mass_g)) +
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g))

ggplot(data=penguins) + 
  geom_smooth(mapping = aes(x=flipper_length_mm,y=body_mass_g,linetype = species))
ggplot(data=penguins) + geom_jitter(mapping = aes(x=flipper_length_mm,y=body_mass_g))



