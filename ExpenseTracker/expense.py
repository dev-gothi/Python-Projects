import pandas as pd
import os
import json

class ExpenseTracker:
    def __init__(self,filename = "expense.csv"):
        self.filename = filename
        
        if os.path.exists(filename):
            self.dframe = pd.read_csv(filename)
        else:
            self.dframe = pd.DataFrame(columns=["Date","Category","Amount","Description"])
        self.loadbudget()

    def addexpense(self,date,category,amount,description):
        newrow = pd.DataFrame([{"Date" : date,
                                 "Category": category,
                                 "Amount" : amount,
                                 "Description": description
                                }])
        self.dframe = pd.concat([self.dframe,newrow],ignore_index = True)

        if category in self.budget:
            limit = self.budget[category]
            actual = self.dframe[self.dframe["Category"]==category]["Amount"].sum()
            if actual > limit:
                print("Budget exceed")
            else:
                print("Limit mot reached")
        else:
            print(f"There is no limit in {category}")

    def deleteexpense(self):
        print(self.dframe)
        inputindex = int(input("Enter the index of row to delete"))
        if isinstance(inputindex,int):
        
            self.dframe = self.dframe.drop(inputindex).reset_index(drop = True)
        else:
            print("Invalid Index")

    def budgetlim(self,category,limit):
        self.budget[category] = limit


    def savebudget(self):
        with open ("budget.json","w") as f:
            json.dump(self.budget,f)

    def loadbudget(self):
        if os.path.exists("budget.json"):
            with open("budget.json","r") as f:
                self.budget = json.load(f)
        else:
            self.budget = {}        

        
        

    def savedata(self):
        self.dframe.to_csv("expenses.csv",index=False)

    def viewexpense(self,category = None):
        if category==None:
            print(self.dframe)
        else:
            print(self.dframe[self.dframe["Category"]==category])


    def viewsummary(self):
        print(self.dframe["Amount"].sum())
        print(self.dframe.groupby("Category")["Amount"].sum())

    def exportsummary(self):
        total = self.dframe["Amount"].sum()
        categorysum = self.dframe.groupby("Category")["Amount"].sum()

        with open ("Summary Report.txt","w") as f:
            f.write(f"Total Spends : {total}")
            f.write(f"Category Spends : {categorysum}")
    
            

        