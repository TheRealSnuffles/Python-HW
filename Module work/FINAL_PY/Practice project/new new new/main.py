import month
import pickle
import setters_getters
LOOK_UP = 1
ADD = 2
EXIT = 3

def main():
    
    
    input_file = open('Game_Releases.dat','rb')
    end_of_file = False
    while not end_of_file:
        try:
            Releases = pickle.load(input_file)
        except EOFError:
            end_of_file = True
        except:
            TypeError
    input_file.close()
    
    choice = 0
    while choice != EXIT:
        choice = menu_choice()
        if choice == LOOK_UP:
            look_up(month)
        if choice == ADD:
            add_game(setters_getters)



    output_file = open('Game_Releases.dat','wb')        
    name_email = pickle.dump(games,output_file)
    output_file.close()
            

def menu_choice():
    
    print()
    print("Menu")
    print("-----------------")
    print("1. Look up releases by month")
    print("2. Add new release by month")#and publisher?
    print("3. Exit")
    
    try:
        choice = int(input("Enter a choice: "))
        if choice < LOOK_UP or choice > EXIT :
            print(choice,"is not a valid choice")
            choice = int(input("Please enter a valid choice: "))
    
    except ValueError:
        print("Entry was not a valid choice")
        choice = int(input("Enter a valid choice: "))
        
    return choice
    
   


def look_up(month):
    gameMonth = input(str('Input a month: ')).lower()
    if gameMonth == 'january':
        print("The games coming out in January are: ")
        for key in month.January:
            print('\n',"Publisher: ",key,'\n',"Titles:",month.January[key],
                    '\n', sep='')
    elif gameMonth == "february":
        print("The games coming out in February are: ")
        for key in month.February:
            print('\n',"Publisher: ",key,'\n',"Titles:",month.February[key],
                    '\n', sep='')
            
    
    
def add_game(setters):
    month = input(str("What month is the game you would like'",
                      "to add being released in?")).lower()
    publisher = input(str("Enter the name of the game publisher: ")).lower()
    title = input(str("Enter the title of the game: "))
    #if month == 'january':
        #if publisher == 'activision':
            

    
    #x=setters_getters.game_class(month,publisher,title)
    #print("You entered the following data")
    #print("Game release month:",x.get_release_month())
    #print("Publisher name:",x.get_publisher_name())
    #print("Game title:",x.get_game_title())
    
    
    


                  
        
            
        
main()
    
    
