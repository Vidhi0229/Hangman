import random
from Dictionary import Words

def Hangman(count, take):
    if(count == 1):
        print('___________________\n|\n|\n|\n|\n|\n|\n|')
        print("\nTry Again")
    elif(count == 2):
        print('___________________\n|     |\n|\n|\n|\n|\n|\n|\n|')
        print("\nTry Again")
    elif(count == 3):
        print('___________________\n|     |\n|   .;;;.\n|   (*_*)\n|\n|\n|\n|\n|')
        print("\nTry Again")
    elif(count == 4):
        print('___________________\n|     |\n|   .;;;.\n|   (*_*)\n|     |\n|\n|\n|\n|')
        print("\nTry Again")
    elif(count == 5):
        print('___________________\n|     |\n|   .;;;.\n|   (*_*)\n|     |\n|    /|\n|   / |\n|\n|')
        print("\nTry Again")
    elif(count == 6):
        print('___________________\n|     |\n|   .;;;.\n|   (*_*)\n|     |\n|    /|\ \n|   / | \ \n|\n|')
        print("\nTry Again")
    elif(count == 7):
        print('___________________\n|     |\n|   .;;;.\n|   (*_*)\n|     |\n|    /|\ \n|   / | \ \n|    /\n|   /')
        
    elif(count == 8):
        print('___________________\n|     |\n|   .;;;.\n|   (*_*)\n|     |\n|    /|\ \n|   / | \ \n|    / \ \n|   /   \ ')
        print("\nYOU LOSE :(\n The correct word was " + take)

def guess(take):
    s = '_'
    b = s * len(take);
    b = list(b)
    count = 0
    while(count != 8):
        choose = input("Guess letter or whole word: ").lower()
        low = take.lower();
        k = list(low)
        i = low.find(choose)
        if(choose == low or b == k):
            print("\nYOU WIN!!!\n" + choose + " is a right word")
            break
        if(i != -1):
            j = 0
            while(j != len(choose)):
                b[i] = choose[j]
                j += 1
                i += 1
            if(b == k):
                print("\nYOU WIN!!!\n" + low + " is a right word")
                break
            print(' '.join(map(str, b)))
        else:
            count += 1
            if(count < 9):
                Hangman(count, take)

def Randoms(Words):
    res = key, val = random.choice(list(Words.items()))
    print(res[0])
    choose = list(res[1])
    take = random.choice(choose);
    l = len(take)
    s = '_  '
    blank = l * s;
    print(blank, "\n")
    guess(take)

print('\nLets Play H.A.N.G.M.A.N!!!\n')
Randoms(Words);



