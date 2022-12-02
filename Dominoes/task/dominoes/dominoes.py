# Write your code here
import random

dominoes_list = []
player_dlist = []
ai_dlist = []
first_player = ""


def create_domino_set():
    for a in range(7):
        for b in range(7):
            if [b, a] not in dominoes_list:
                dominoes_list.append([a, b])

    random.shuffle(dominoes_list)


def split_dominoes():
    for a in range(7):
        player_dlist.append(dominoes_list[a])
        dominoes_list.pop(a)
        ai_dlist.append(dominoes_list[a])
        dominoes_list.pop(a)
    player_dlist.sort()
    ai_dlist.sort()


create_domino_set()
split_dominoes()

def first_player():
    global player_dlist
    global ai_dlist
    if player_dlist[-1] > ai_dlist[-1]:
        plai_status = "computer"
        d_shake = [player_dlist[-1]]
        player_dlist.pop()
    else:
        plai_status = "player"
        d_shake = [ai_dlist[-1]]
        ai_dlist.pop()

print("Stock pieces:", dominoes_list)
print("Computer pieces:", ai_dlist)
print("Player pieces:", player_dlist)
print("Domino snake:", d_shake)

print("Status:",plai_status)