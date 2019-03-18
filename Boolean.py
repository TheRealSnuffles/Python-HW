test1=float(input('What was your 1st test score?'))
test2=float(input('What was your 2nd test score?'))
test3=float(input('What was your 3rd test score?'))
HIGH_SCORE=95
average=(test1+test2+test3)/3
print('The average score is', average)
if average >= HIGH_SCORE:
    print('Congratulations!')
    print('that is a great average!')
