user_string = input()
reverse_string = user_string[::-1]

if user_string == reverse_string:
    print('You have a palindrome')
    print(f'{user_string} = {reverse_string}')
else:
    print('That was not a palindrome')
    print(f'{user_string} is not the same as {reverse_string}')
