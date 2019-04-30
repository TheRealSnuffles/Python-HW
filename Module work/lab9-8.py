#This program creates a menu for a user to look up, add, change, or delete
#an email address from a dictionary
#creates main
def main():
    import pickle
    #creates menu choices
    LOOK_UP = 1
    ADD = 2
    CHANGE = 3
    DELETE = 4
    QUIT = 5
    #creates dictionary
    name_email = {'Alex':'@Lenzen'}
    #sets choice to zero
    choice = 0
    #while loop to iterate while user wants to use the program
    while choice != QUIT:
        #creates variable for menu choice
        choice = user_choice()
        #if statement to open file to search for email, and call lookup def
        #while statement to read pickled file
        if choice == LOOK_UP:
            input_file = open('name_email.dat','rb')
            end_of_file = False
            while not end_of_file:
                try:
                    name_email = pickle.load(input_file)
                except EOFError:
                    end_of_file = True
            look_up(name_email)
            input_file.close()
        #else if statement to add email to list by calling add def
        #and pickle.dump contents  
        elif choice == ADD:
            output_file = open('name_email.dat','wb')
            add(name_email)
            name_email = pickle.dump(name_email,output_file)
            output_file.close()
        #else if statement to change an existing email address
        #and pickle.dump contents
        elif choice == CHANGE:
            output_file = open('name_email.dat','wb')
            change(name_email)
            name_email = pickle.dump(name_email,output_file)
            output_file.close()
        #else if statement to delete existing email address and pickle.dump    
        elif choice == DELETE:
            output_file = open('name_email.dat','wb')
            delete(name_email)
            name_email = pickle.dump(name_email,output_file)
            output_file.close()
    #quits program   
    if choice == QUIT:
        quit 
#creates menu function to present options for user to choose
def user_choice():
    print()
    print("Names and E-Mail addresses")
    print("--------------------------")
    print("1.Look up email address")
    print("2.Add new name and email address")
    print("3.Change existing email address")
    print("4.Delete an existing name and email address")
    print("5.Quit")
    choice = int(input("Enter your choice:"))
    while choice < 0 or choice > 5:
        choice = int(input("enter a valid choice:"))
    return choice
#function for looking up an email in a dictionary
def look_up(name_email):
    name = input("Enter a name to look up users email:")
    print("Email address:",name_email.get(name,"Not Found"))
    
#function to add an email to a dictionary   
def add(name_email):
    name = input("Enter a name to add:")
    email = input("Enter an email to add:")
    if name not in name_email:
        name_email[name]=email
    else:
        print("That entry already exists")
    return name_email[name]

#function to change an email by looking up pickeled contents and replacing it
#with new contents 
def change(name_email):
    input_file = open('name_email.dat','rb')
    end_of_file = False
    while not end_of_file:
        try:
            name_email = pickle.load(input_file)
        except EOFError:
            end_of_file = True   
    name = input("Enter a name to change:")
    if name in name_email:
        email = input("Enter the new email address:")
        name_email[name] = email
    else:
        print("That name is not found")
    return name_email[name]
    input_file.close()
    
#function to delete email in a dictionary    
def delete(name_email):
    name = input("Enter a name to delete:")
    if name in name_email:
        del name_email[name]
        print(name,"deleted")
    else: 
        print(name, "not found")
    
#calls main
main()
        
               
        
        



