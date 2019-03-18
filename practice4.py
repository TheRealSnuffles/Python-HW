def main():
    x=open('sales.txt', 'r')
    line=x.readline()
    while line !='':
        amount=float(line)
        print(format(line, '.2f'))
        line=x.readline()
    x.close()
