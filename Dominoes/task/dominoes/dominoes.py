# Write your code here
import random

dominoes_list = []
player_dlist = []
ai_dlist = []
d_shake = []


def create_domino_set():
    d_list = [[a, b] for a in range(7) for b in range(a, 7)]
    random.shuffle(d_list)
    return d_list


def split_dominoes():
    global dominoes_list
    global player_dlist
    global ai_dlist
    player_dlist = dominoes_list[0:7]
    ai_dlist = dominoes_list[7:14]
    dominoes_list = dominoes_list[14:]
    player_dlist.sort()
    ai_dlist.sort()


def first_player():
    global player_dlist
    global ai_dlist
    global d_shake
    if player_dlist[-1] > ai_dlist[-1]:
        pstatus = "computer"
        d_shake = player_dlist[-1]
        player_dlist.pop()
    else:
        pstatus = "player"
        d_shake = ai_dlist[-1]
        ai_dlist.pop()
    return pstatus

def print_player_dominoes():
    for n in range(len(player_dlist)):
        print(f"{n+1}:{player_dlist[n]}")

dominoes_list = create_domino_set()
split_dominoes()
plai_status = first_player()


print("======================================================================")
print("Stock size:", len(dominoes_list))
print("Computer pieces:", len(ai_dlist))
print("")
print(d_shake)
print("")
print("Your pieces:")
print_player_dominoes()

print("")
if plai_status == "computer":
    print("Status: Computer is about to make a move. Press Enter to continue...")
if plai_status == "player":
    print("Status: It's your turn to make a move. Enter your command.")
