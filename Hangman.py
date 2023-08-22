import random

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
        print("\nYOU LOSE :(\n the write word was " + take)

        
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
    
    

Words = {'COUNTRY': ['India', 'USA', 'Italy', 'New Zealand', 'Russia', 'Germany', 'Mexico', 'China', 'Canada', 'Japan'],
        'DAIRY': ['Milk', 'Butter', 'Cream', 'Cheese', 'Yoghurt', 'Ice-Cream', 'Ghee', 'Custard', 'Whipped Cream', 'Buttermilk'],
        'FRUIT': ['Apple', 'Banana', 'Papaya',	'Peach', 'Pomegranate',	'Pineapple', 'Raspberries', 'Strawberries', 'Watermelon', 'Mango'],
        'ANIMAL': ['Dog', 'Birds', 'Lion', 'Cat', 'Horse', 'Chicken', 'Bears', 'Monkey', 'Tiger', 'Giraffe'],
        'VEGETABLE': ['Carrots', 'Potato', 'Tomato', 'Onions', 'Broccoli', 'Mushroom', 'Lettuce', 'Capsicum', 'Pumpkin', 'Zucchini'],
        'PROFESSION': ['Teacher', 'Dentist', 'Physician', 'Architect', 'Lawyer', 'Software Developer', 'Artist', 'Police officer', 'Scientist', 'chef'],
        'PLANET': ['Earth', 'Jupiter', 'Saturn', 'Venus', 'Mars', 'Mercury', 'Neptune', 'Uranus'],
        'BRAND': ['Apple', 'Nike', 'Adidas', 'Google', 'Microsoft', 'Amazon', 'BMW', 'IBM', 'Starbucks', 'Disney']}


print('\nLets Play H.A.N.G.M.A.N!!!\n')
Randoms(Words);



