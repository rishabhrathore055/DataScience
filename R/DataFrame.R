id <- c(1:10)


name <- c("John Mendes", "Rob Stewart", "Rachel Abrahamson", "Christy Hickman", "Johnson Harper", "Candace Miller", "Carlson Landy", "Pansy Jordan", "Darius Berry", "Claudia Garcia")


job_title <- c("Professional", "Programmer", "Management", "Clerical", "Developer", "Programmer", "Management", "Clerical", "Developer", "Programmer")


employee <- data.frame(id, name, job_title)

head(employee)

enroll <-c(1:5)

name <- c("Akash Rajput","Aditya Soni","Ajay Rathore","Ajeet raghuwanshi","Ashish singh")

feild <- c("Webd","Cloud","Java","Webd","Andriod")

student <- data.frame(enroll,name,feild)

head(student)
separate(student,name,into=c('first_name','last_name'),sep=' ')

