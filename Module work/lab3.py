#Defines infant child teenager and adult
infant=1
child=12
teen=19
adult=20
#This gets the users age
age=int(input('Enter your age: '))
#displays the age catagory
if age<=infant:
    print('You are an infant.')
elif age>infant and age<=child:
    print('You are a child.')
elif age>child and age<=teen:
    print('You are a teen.')
else:
    print('You are an adult.')

