import time
import random
import os

def clear_screen():
    """Ekranni tozalash."""
    os.system("cls" if os.name == "nt" else "clear")

def print_road(player_pos, obstacles):
    """Yo‘lni chizish."""
    road = ["|       |"] * 10
    for obs in obstacles:
        road[obs[1]] = road[obs[1]][:obs[0] + 1] + "#" + road[obs[1]][obs[0] + 2:]
    road[9] = road[9][:player_pos + 1] + "P" + road[9][player_pos + 2:]
    clear_screen()
    for line in road:
        print(line)
    print("=========")

def move_obstacles(obstacles):
    """To‘siqlarni pastga siljitish."""
    return [[obs[0], obs[1] + 1] for obs in obstacles if obs[1] < 9]

def check_collision(player_pos, obstacles):
    """To‘qnashuvni tekshirish."""
    for obs in obstacles:
        if obs[1] == 9 and obs[0] == player_pos:
            return True
    return False

def main():
    print("Trafik Rider: Mototsikl Versiyasi")
    print("O‘yinni boshlash uchun ENTER tugmasini bosing!")
    input()

    player_pos = 3  # O‘yinchi boshlang‘ich pozitsiyasi (yo‘lda)
    obstacles = []  # To‘siqlar ro‘yxati
    score = 0       # Ball

    try:
        while True:
            # To‘siqlarni qo‘shish
            if random.random() < 0.3:  # 30% ehtimollik bilan yangi to‘siq paydo bo‘ladi
                obstacles.append([random.randint(1, 5), 0])

            # To‘siqlarni harakatlantirish
            obstacles = move_obstacles(obstacles)

            # To‘qnashuvni tekshirish
            if check_collision(player_pos, obstacles):
                print("To‘qnashuv yuz berdi! O‘yin tugadi!")
                print

