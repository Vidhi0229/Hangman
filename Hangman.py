import random

def guess(take , blank):
    Dash = len(blank)
    
    while(1):
        choose = input("Guess letter or whole word: ").lower()
        low = take.lower();
        c_len = len(choose)
        i = low.find(choose)
        if(i != -1):
            if(i == 0):
                b = blank[c_len-1 : ]
                V = choose+b;
                print(V)
            # else:
            #     b1 = blank[ : i-2]
            #     b = blank[c_len-1 : ] 
            #     V = b1 + choose + b
            #     print(V)
            if(low == V):
                print("You Won!!")
                break


    


def Randoms(Words):
    res = key, val = random.choice(list(Words.items()))
    print(res[0])
    choose = list(res[1])
    take = random.choice(choose);
    l = len(take)
    s = '_ '
    blank = l * s;
    print(blank, "\n")
    guess(take, blank)
    
    

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



