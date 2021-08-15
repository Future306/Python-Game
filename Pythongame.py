print('Hello welecome')

ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 4

if  ans.lower() =='yes':
    ans = input('1. Which programming I am learing at present? ')
    if ans.lower() == 'python':
        score += 1
        print('Correct')
    else:
        print('Incorrect')



    ans = input('2. From where am I learning python at present? ')
    if ans.lower == 'great learning':
        score += 1
        print('Correct')
    else:
        print('Incorrect')



    ans = input('3.What is the time I am studing ? ')
    if ans == '10:00 PM':
        score += 1
        print('Correct')
    else:
        print('Incorrect')
