#Opens a text file, converts contents to a string, strips '/n', converts it to a float, adds the total of the numbers in the file, and displays the total.
def main():
    OpenInput = open('number_list.txt', 'r')
    line = OpenInput.readline()
    total = 0.0
    while line != '':
        amount = str(line)
        amount = amount.rstrip('\n')
        amount = float(amount)
        print(amount)
        total += amount
        line = OpenInput.readline()
    print("The total added count is: ",format(total,'.2f'))
    OpenInput.close()
main()
