'''Guess a number game'''

import numpy as np

number = np.random.randint(1, 101) # загадываем число

# Количество попыток
count = 0

while True:
    count += 1
    predict_number = int(input('Guess a number from 1 to 100: '))
    
    if predict_number > number:
        print("Number should be less")
        
    elif predict_number < number:
        print('Number should be larger')
        
    else:
        print(f'You have guessed the number: {number} in {count} attempts')
        break 
    