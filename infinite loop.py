todos = []
while True:
    user_choice = int(input("select 1 to add:\n"
                            "select 2 to update:\n"
                            "select 3 to delete:\n"
                            "select 4 to view:\n"
                            "select 5 to exit:\n"))
    
    #comparing user's 
    if user_choice == 1:
        activity = input("Enter activity you want to add: \n")
        todos.append(activity)
        print(f"{activity} added successfully.")

    elif user_choice == 2:
        if not todos:
            print("Nothing to update, Please add something")
        else:
            update = input("Please enter your choice to update:\n")
            if update in todos:
                new_update = input("Enter update: \n")
                update = new_update

    elif user_choice == 3:
        index = int(input("Enter the index activity you wish to delete:\n"))
        if index < len(todos):
            del todos[index]
            print("Activity deleted successfully")
        else:
            print("invalid activity or empty list")

    elif user_choice == 4:
        if not todos:
            print("Nothing to view,please add an activity")
        else:
         print(todos)

    elif user_choice == 5:
        print("Exit successfully")

        exit(1)
    else:
        print("Choose an option between 1 - 5 ")
        
        


