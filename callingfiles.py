def main():
    print('enter name3')
    name1=input('name')
    name2=input('name')
    name3=input('name')
    myfile=open('friends.txt', 'w')
    myfile.write(name1+'\n')
    myfile.write(name2+'\n')
    myfile.write(name3+'\n')
    myfile=open('friends.txt', 'a')
    myfile.write("bozo the clown")
    myfile.write("yozo the goof")
    myfile.write("fizzgig the clapper")

    myfile.close()
    marggg(myfile)
    print('the names friends txt')

def marggg(myfile):
    infile=open('friends.txt')
    line1=infile.readline()
    line2=infile.readline()
    line3=infile.readline()
    line4=infile.readline()
    line5=infile.readline()
    line6=infile.readline()
    line1=line1.rstrip('\n')
    line2=line2.rstrip('\n')
    line3=line3.rstrip('\n')
    infile.close()
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
main()
