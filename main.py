from random import randint
from time import sleep
from data import *
from servise import *


name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = 0 
while True:
    action = input('''Выбери действие:
                   1 - в бой
                   2 - тренировка
                   3 - информация об игроке
                   4 - информация о противнике
                   5 - показать инвентарь
                   6 - магазин
                   7 - казино''')
    if action == "1":
        current_enemy = fight(current_enemy)
        if current_enemy == 3:
            break
    elif action == "2":
                trainType = input('''
                                    1 - тренировать атаку
                                    2 - тренировать оборону''')
                trainHero(trainType)
    elif action == "3":
          displayPlayer()
          print()
    elif action == "4":
          displayEnemy(current_enemy)
          print()
    elif action == "5":
          display_inventory()
    elif action == "6":
          shop()
    elif action == "7":
          earn()
          
