import random
 
#Step 2: Generate a list of 400 highridge workers with varrying salary ranges
Highridge_workers = []
for i in range(400):
    worker = {
        "name": f"worker_{i + 1}",
         #randomly assign gender
        "gender": random.choice(["male", "female"]),
        #Randomly assign salary between $5,000 and $35,000
        "salary": random.randint(6000, 35000)  
    }
    Highridge_workers.append(worker)
   
#Step 5: Exception handling is implemented to manage potential errors
def generate_payment_slips(Highridge_workers):
    payment_slips = []
   
    for worker in Highridge_workers:
        try:
        #Step 4: Incorporate conditional statements within the loop  
         if 10000 < worker["Salary"] < 20000:
             Employee_level = "A1"
         elif 7500 < worker['Salary'] < 30000 and worker["Gender"] == "Female":
             Employee_level = "A5-F"
         else:
          Employee_level = "others"  
         
         # Generate the payment slip
         payment_slip = {
                "WorkerID": worker["WorkerID"],
                "Name": worker["Name"],
                "Gender": worker["Gender"],
                "Salary": worker["Salary"],
                "Employee Level": Employee_level
            }
         # Append the payment slip to the list
         payment_slips.append(payment_slip)
         
        except KeyError as ke:
            print(f"Key error while generating payment slips: {ke}")
        except Exception as e:
            print(f"An error occurred while generating payment slips: {e}")