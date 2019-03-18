#Mod 5-2. Creating "global constants"
STATE_TAX_RATE=0.05
COUNTY_TAX_RATE=0.025
#defining main, creating variables, calculating tax rates and sale prices
def main():
    itemPrice=0.0
    stateTax=0.0
    countyTax=0.0
    totalTax=0.0
    totalSale=0.0
    itemPrice=float(input("Enter item's price: "))
    stateTax=itemPrice*STATE_TAX_RATE
    countyTax=itemPrice*COUNTY_TAX_RATE
    totalTax=stateTax+countyTax
    totalSale=itemPrice+totalTax
    output(itemPrice,stateTax,countyTax,totalTax,totalSale)
#Defining output, printing calculations of item price and sales tax 
def output(a,b,c,d,e):
    print("The item's price is: $ ",format(a, '.2f'))
    print("State tax is 5%: $ ", format(b, '.2f'))
    print("County tax is 2.5%: $ ", format(c, '.2f'))
    print("Total tax is: $", format(d, '.2f'))
    print("The total sale price is: $", format(e, '.2f'))
main()
