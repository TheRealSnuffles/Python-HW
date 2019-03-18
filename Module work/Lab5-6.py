#Mod 5-6 Calculating calories from fat and carbs
#Define main, getting grams of fat and carb intake, calcluating calories from
#fat and carb intake
FAT_G_CALC=9
CARB_G_CALC=4
def main():
    fatGrams=0.0
    carbGrams=0.0
    fatCals=0.0
    carbCals=0.0
    fatGrams=float(input('Enter grams of daily fat intake: '))
    carbGrams=float(input('Enter grams of daily carbohydrate intake: '))
    fatCals=fatGrams*FAT_G_CALC
    carbCals=carbGrams*CARB_G_CALC
    output(fatCals,carbCals)
#prints calories from fat and carbs
def output(a,b):
    print("Calories from fat are: ", format(a, '.2f'))
    print("Calories from carbs are: ", format(b, '.2f'))
main()
                                            
    
    
    
    
