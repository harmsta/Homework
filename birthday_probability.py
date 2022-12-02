import random


def did_anyone_have_a_birthday_match(people_in_room):
    birthdays_in_room_list = []
    for index in range(people_in_room):
        my_birthday = random.randint(1,367)
        birthdays_in_room_list.append(my_birthday)

    birthdays_in_room_set = set(birthdays_in_room_list)
    if (len(birthdays_in_room_set) != len(birthdays_in_room_list)):
        return True
    else:
        return False

if __name__ == '__main__':
    people_in_room = int(input('How many people are in the room? '))

    match_count = 0
    sample_size = 10000
    for index in range(sample_size):
        we_had_a_match = did_anyone_have_a_birthday_match(people_in_room)
        if(we_had_a_match):
            match_count += 1

    percent_match = (match_count / sample_size) * 100.0
    print(f'Out of a sample size of {sample_size}, we had {match_count} matches, or {percent_match:.2f}%. {people_in_room} people in the room.')
