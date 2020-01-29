import random
n=random.choice(range(10))
for i in range(5):
    c=int(input('guess a number:'))
    if c==n:
        print('win')
        exit(0)
    else:
         print('try again')
         print('lost')
