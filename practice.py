def main():
    num_days=int(input("Enter number sale days: "))
    sales_file=open("sales.txt", 'w')
    for count in range(1,num_days+1):
        sales=float(input("enter sales for day#"+str(count)+":"))
        sales_file.write(str(sales)+'\n')
    sales_file.close()
    print('data written to sales')
    second()
def second():
    sales_file=open("sales.txt", 'r')
    line=sales_file.readline()
    while line!='':
        amount=float(line)
        print(format(amount, '.2f'))
        line=sales_file.readline()
    sales_file.close()


main()
