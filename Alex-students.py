#Opens a text file to write a students name and score to the file
def main():
    students = open('students_file.txt', 'w')
    keep_going = 'y'
    while keep_going == 'y' or keep_going == 'Y':
        names = input("Enter student's name: ")
        scores = int(input("Enter student's score: "))
        students.write(names+'\n')
        students.write(str(scores) + '\n')
        keep_going=input("To Enter another student's information type y: ")
    students.close()
main()
