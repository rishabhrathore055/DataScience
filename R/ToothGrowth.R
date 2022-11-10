data("ToothGrowth")
View(ToothGrowth)
filtered_tg<- filter(ToothGrowth, dose==0.5)
View(filtered_tg)

arrange(filtered_tg,len)
arrange(filter(ToothGrowth, dose==0.5),len) 

filerted_toothgrowth <- ToothGrowth %>% 
  filter(dose==0.5) %>% 
  group_by(supp) %>% 
  summarize(mean_len = mean(len,na.rm=T),.groups = "drop")

View(filerted_toothgrowth)
