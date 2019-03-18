#This program converts an items masss in kg to weight in nt
#collects items mass
mass = float(input('Enter items mass: '))
#converts mass in kg to weight in nt
weight = mass*9.8
#displays if the object is too heavy(over 500 nt) or too light(under 100 nt)
if weight>500:
    print('The object is too heavy.')
elif weight<100:
    print('The object is too light.')
    
