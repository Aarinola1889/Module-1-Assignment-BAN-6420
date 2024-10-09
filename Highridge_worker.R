Step 1: Set seed for reproducibility
set.seed(456)
 
# Step 2: Generate a list of 400 workers dynamically with varying salary ranges
Highridge_workers_v2 <- data.frame(
 name = paste0("Worker_", 1:400),
 gender = sample(c("Male", "Female"), 400, replace = TRUE),
 salary = sample(8000:35000, 400, replace = TRUE)
)
 
# Step 5:Exception handling is implemented to manage potential errors
generate_payment_slips_v2 <- function(workers_v2) {
payment_slips <- vector("list", nrow(workers_v2)) 
 
 for (i in 1:nrow(workers_v2)) {
   tryCatch({
     # Step 4: Conditional logic for assigning employee levels
     if (workers_v2$salary[i] >= 15000 & workers_v2$salary[i] < 25000) {
       employee_level[i] <- "A1"
     } else if (workers_v2$salary[i] > 9000 & workers_v2$salary[i] < 20000 & workers_v2$gender[i] == "Female") {
       employee_level[i] <- "A5-F"
     } else {
       employee_level[i] <- "others"
     }