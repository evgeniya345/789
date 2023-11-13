from random import randint
from time import sleep
from data import *

def fight(current_enemy):
    round = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    print(f'Противник - {enemy["name"]} : {enemy["script"]}')
    input('Enter чтобы продолжить')
    print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            enemy_hp -= player['attack']
            sleep(1)
            print(f'''{player['name']} - {player['hp']}
            {enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}.')
            player['hp'] -= enemy['attack']
            sleep(1)
            print(f'''{player['name']} - {player['hp']}
            {enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
            round += 1
        if player['hp'] > 0:
            print(f'Противник - {enemy["name"]}: {enemy["win"]}')
            current_enemy += 1
        else:
            print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
        
def trainHero(trainType):
    skip = "2"
    if items["2"]["name"] in player[""]:
        skip = input('''Желаете пропустить тренировку?
                     1 - да
                     2 - нет''')
    if skip == "2":
        for i in range(0, 101, 20):
            print("тренировка завершена на {i}%")
            sleep(1.5)
    if trainType == "1":
        player["attack"] += 2
        print(f'Тренировка окончена! Теперь ваша атака равна {player["attack"]}')
    elif trainType == "2":
        player["armor"] -= .09
        print(f'Тренировка окончена! Теперь ваша броня поглощает {100 - player["armor"] * 100} % урона')

def displayPlayer():
    print(f'Игрок - {player["name"]}')
    print(f'Атака - {player["attack"]}, Шанс крита - {player["attack"]} равен {player["luck"]}')
    print(f'Броня поглощает {100 - player["armor"] * 100} % урона')

def displayEnemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Атака - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')
 
def display_inventory():
    print(f'У вас есть:')
    for value in player["inventory"]:
        print(value)
    print(f'{player["money"]} монет')
    print()
    if "Зелье удачи" in player["inventory"]:
        potion = input('''Хочешь выпить?
                       1 - да
                       2 - нет
                       :''')
        if potion == "":
            player["lack"] += 7
            print("Готово")
            player["inventory"].remove("Зелье удачи")

def shop():
    print("Добро пожаловать!")
    print(f'{player["money"]} монет')
    for key, value in items.items():
        print(f'{key} - {value["name"]} : {value["price"]}')
        item = input()
        if item in player["inventory"]:
            print(f'У тебя уже есть {items[item]["name"]}')
        elif player["money"] >= items[item]["price"]:
            print(f'Ты успешно приобрел предмет')
            player["inventory"].append(items[item]["name"])
            player["money"] -= items[item]["price"]
        else:
            print("Не хватает денег")
        print()
        print("Буду ждать снова!")
        print()

def earn():
    print(f'Добро пожаловать на завод! у тебя есть 66.66% шанс заработать деньги и 33.33% их потерять.')
    result = randint(1, 100)
    sleep(1.5)
    print("Результат...")
    if result < 67:
        print("Повезло")
        player["money"] += 500
    else:
        print("Не повезло")
        player["money"] -= 500
    print(f'Ваши деньги: {player["money"]}')