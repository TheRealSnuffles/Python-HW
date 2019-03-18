def main():
    outfile=open('numbers.txt', 'w')
    num1=int(input('Enter num'))
    num2=int(input('Enter num'))
    num3=int(input('Enter num'))
    outfile.write(str(num1)+'n')
    outfile.write(str(num2)+'n')
    outfile.write(str(num3)+'n')
    outfile.close()
    print('data written to numbers')
main()

