
class ExpenceTracker:  
    expence_list=[]     #list to store the expense
    def __init__(self):
        pass
    def add_expense(self):
        b=True
        while b:
            key = input("what you spend on: ")
            value = input("how much you spend: ")
            ExpenceTracker.expence_list.append({"what you spend on":key, "how much you spend":value})
            c=input("do you want to add more expense? (y/n)")
            if c == "y":
                b=True
            else:
                b=False

    def view_expense(self):
        print("Expense List: \n")
        for item in ExpenceTracker.expence_list:
            print( f"what you spend on: {item['what you spend on']} : how much you spend: {item['how much you spend']}\n")
    def recalculate_expense(self):
        total_expense=0
        for item in ExpenceTracker.expence_list:
            total_expense+=int(item["how much you spend"])
        print(f"Total expense: Rs. {total_expense}")







if __name__ == "__main__":
    et= ExpenceTracker()    #object of the class ExpenceTracker
    a=True
    while a:
        print("********Welcome to Tracker Program********")
        print("1. add the expense")
        print("2. view the expense")
        print("3. recalculate the expense")
        print("4. exit the program")
        choice= int(input("enter your choice :- \t"))
        if choice == 1:
            et.add_expense()
        elif choice == 2:
            et.view_expense()
        elif choice == 3:
            et.recalculate_expense()
        elif choice == 4:
            a=False
        else:
            print("invalid choice")



