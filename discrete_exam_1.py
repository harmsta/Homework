import random

user_num = int(input('Please enter number:\n'))

pattern = random.randint(1,4)


if pattern == 1:
    difference = random.randint(0,10)
    output_1 = user_num + difference
    output_2 = output_1 + difference
    output_3 = output_2 + difference
    output_4 = output_3 + difference
    output_5 = output_4 + difference
    print(output_1, output_2, output_3, output_4)

    user_answer = int(input('What is the next number in the pattern?:\n'))
    if user_answer == output_5:
        print('Correct')
    else:
         print('Incorrect')




if pattern == 2:
    difference = random.randint(0,10)
    output_1 = user_num - difference
    output_2 = output_1 - difference
    output_3 = output_2 - difference
    output_4 = output_3 - difference
    output_5 = output_4 - difference
    print(output_1, output_2, output_3, output_4)

    user_answer = int(input('What is the next number in the pattern?:\n'))
    if user_answer == output_5:
        print('Correct')
    else:
        print('Incorrect')


if pattern == 3:
    difference = random.randint(0,10)
    output_1 = user_num * difference
    output_2 = output_1 * difference
    output_3 = output_2 * difference
    output_4 = output_3 * difference
    output_5 = output_4 * difference
    print(output_1, output_2, output_3, output_4)

    user_answer = int(input('What is the next number in the pattern?:\n'))
    if user_answer == output_5:
        print('Correct')
    else:
        print('Incorrect')


if pattern == 4:
    output_1 = user_num
    output_2 = output_1 * user_num
    output_3 = output_2 * user_num
    output_4 = output_3 * user_num
    output_5 = output_4 * user_num
    print(output_1, output_2, output_3, output_4)

    user_answer = int(input('What is the next number in the pattern?:\n'))
    if user_answer == output_5:
        print('Correct')
    else:
        print('Incorrect')
