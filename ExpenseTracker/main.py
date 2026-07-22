from  expense import ExpenseTracker

def main():
    tracker = ExpenseTracker()

    while True:
        print("""

            Welcome to DG Expense Tracker
              1. Add Expense
              2. View Expenses
              3. View Summary
              4. Delete Expense
              5. Set Budget
              6. Export Summary
              7. Exit
            



 """)
        userinput = input("Choose : " )

        if userinput=="1":
            date = input("Enter Date : ")
            category = input("Enter Category : ")
            amount = float(input("Enter Amount : "))
            description = input("Enter Description of Expense : ")
            tracker.addexpense(date,category,amount,description)
            tracker.savedata()
        
        elif userinput=="2":
            category = input("Which Category Expense : ")
            tracker.viewexpense(category)

        elif userinput=="3":
            tracker.viewsummary()
        
        

        elif userinput=="4":
            tracker.deleteexpense()
            tracker.savedata()

        elif userinput=="5":
            category = input("Enter Category : ")
            limit = float(input("Enter Limit : "))
            tracker.budgetlim(category,limit)
            tracker.savebudget()

        elif userinput=="6":
            tracker.exportsummary()
            print("Summary Exported Succesfully")

        elif userinput=="7":
            print("Thank You for using DG Software")
            break
        
        else:
            print("Invalid Input Please Try Again")



main()
