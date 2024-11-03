import random

def decision_maker():
    user_prompt = input("would you like me to make a choice?: ")
    choices = []
    if user_prompt == "yes":
        user_choice = input('option(type stop when done): ')
        while user_choice != 'stop':
            user_choice = input('option: ')
            choices.append(user_choice)
        else:
            choices.remove('stop')
            random_choice = random.choice(choices)
            print(f'your choice should be {random_choice}!')
    else:
        print('okay, have a good day!')


decision_maker()