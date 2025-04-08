from random import randint
import os
import time
from datetime import datetime 

history_game = [
    ['Pasha','23.11.2024 11:58','Bot'],
    ['Dima','23.11.2024 11:58','Dima'],
]

while True:
    os.system('cls')

    print("Меню игры:")
    print("1 - Начать игру ")
    print("2 - Посмотреть историю игр ")
    print("3 - Выйти ")

    menu = int(input("Enter: "))

    if menu == 1:
        field = []

        for _ in range(9):
            field.append("*")

        last_step = 'bot'
        user_name = input("Как тебя зовут: ")

        while True:
            os.system('cls')
            print("=========")
            print(f"= {field[0]} {field[1]} {field[2]} =")
            print(f"= {field[3]} {field[4]} {field[5]} =")
            print(f"= {field[6]} {field[7]} {field[8]} =")
            print("=========")

            if field[0] == field[1] and field[1] == field[2] and field[0] != "*":
                time_now = datetime.now().strftime("%d.%m.%Y %H:%M")
                if field[0] == "X":
                    print(f"Победил: {user_name}")
                    h = [user_name, time_now, user_name]
                else:
                    print("Победил: Бот")
                    h = [user_name, time_now, "Bot"]
                history_game.append(h)
                time.sleep(2)
                break
            
            if last_step == "bot":
                print(f"Ходит: {user_name}")
                choice = int(input(f"Координата: "))
                if 1 <= choice <= 9:
                    idx_coord = choice - 1
                    if field[idx_coord] == "*":
                        field[idx_coord] = "X"
                        last_step = 'user'
                    else:
                        print("Поле уже занято! Попробуйте снова.")
                        time.sleep(2)
                else:
                    print("Неверная координата! Попробуйте снова.")
                    time.sleep(2)

            else:
                print(f"Ходит: Бот")
                while True:
                    idx_coord = randint(3, 8)
                    if field[idx_coord] == "*":
                        field[idx_coord] = "0"
                        print(f"Координата: {idx_coord+1}")
                        last_step = 'bot'
                        time.sleep(2)
                        break

    elif menu == 2:
        print("История игр")
        search_name = input("Введи имя игрока, чьи игры ты хочешь посмотреть: ")
        find = False
        num = 1
        for hisrory in history_game:
            [user_name, time_now, winner] = hisrory
            if search_name == user_name:
                find = True
                print(f"{num}) игра {time_now} {user_name} VS Bot -> Win {winner}")
                num += 1 
        if find == False:
            print("Такой истории игры нет")

        input("Нажмите enter, чтобы вернуться в меню")


    elif menu == 3:
        print("До скорых встреч!")
        break