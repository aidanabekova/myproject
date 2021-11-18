# Виртуальная среда и алгоритмы

import random

class Monty:
    def __init__(self, choices):
        self.choices = choices

    def choose_door(self):
        judge = random.choice(self.choices)
        print(f'Prize door is : {judge}')
        your_choice = int(input('your choice : '))
        for revealed_door in range(1, 4):
            if revealed_door != your_choice and revealed_door != judge:
                print(f'Revealed door: {revealed_door}')
                break
        option = input('one of the door revealed, and it is not prize door'
                       'do you want to change your mind: ')
        if option == 'n':
            print(judge)
            if judge == your_choice:
                print('You win auto')
            else:
                print('you loose, it is not prize door')
        if option == 'y':
            if judge != your_choice:
                print(f'your original choice was: {your_choice}')
                print(f'Your new choice is : {judge}')
                print(f'Prize door is : {judge}')
                print('you win auto! Congrats!')
            elif judge == your_choice:
                print(f'your original choice was: {your_choice}')
                print('Your original choice was right')
                print(f'Prize door is : {judge}')
                print('you loose, it is not prize door')


monty = Monty([1, 2, 3])
monty.choose_door()



