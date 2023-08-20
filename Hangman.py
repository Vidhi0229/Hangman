import random

def Randoms(Words):
    res = key, val = random.choice(list(Words.items()))
    print(res[0])
    choose = list(res[1])
    take = random.choice(choose);
    l = len(take)
    s = '_ '
    print(l * s, "\n")

Words = {'COUNTRY': ['India', 'USA', 'Italy', 'New Zealand', 'Russia', 'Germany', 'Mexico', 'China', 'Canada', 'Japan'],
        'DAIRY': ['Milk', 'Butter', 'Cream', 'Cheese', 'Yoghurt', 'Ice-Cream', 'Ghee', 'Custard', 'Whipped Cream', 'Buttermilk'],
        'FRUIT': ['Apple', 'Banana', 'Papaya',	'Peach', 'Pomegranate',	'Pineapple', 'Raspberries', 'Strawberries', 'Watermelon', 'Mango'],
        'ANIMAL': ['Dog', 'Birds', 'Lion', 'Cat', 'Horse', 'Chicken', 'Bears', 'Monkey', 'Tiger', 'Giraffe'],
        'VEGETABLE': ['Carrots', 'Potato', 'Tomato', 'Onions', 'Broccoli', 'Mushroom', 'Lettuce', 'Capsicum', 'Pumpkin', 'Zucchini'],
        'PROFESSION': ['Teacher', 'Dentist', 'Physician', 'Architect', 'Lawyer', 'Software Developer', 'Artist', 'Police officer', 'Scientist', 'chef'],
        'PLANET': ['Earth', 'Jupiter', 'Saturn', 'Venus', 'Mars', 'Mercury', 'Neptune', 'Uranus'],
        'BRAND': ['Apple', 'Nike', 'Adidas', 'Google', 'Microsoft', 'Amazon', 'BMW', 'IBM', 'Starbucks', 'Disney']}

Randoms(Words)