# Write your code here
import random

dominoes_list = []
player_dlist = []
ai_dlist = []
d_shake = []
pstatus = ""

def create_domino_set():
    global player_dlist
    global ai_dlist
    global dominoes_list

    d_list = [[a, b] for a in range(7) for b in range(a, 7)]
    random.shuffle(d_list)

    player_dlist = d_list[0:7]
    ai_dlist = d_list[7:14]
    dominoes_list = d_list[14:]
    player_dlist.sort()
    ai_dlist.sort()



def first_player():
    global player_dlist
    global ai_dlist
    global d_shake
    global pstatus
    if player_dlist[-1] > ai_dlist[-1]:
        pstatus = "computer"
        d_shake = [player_dlist[-1]]
        player_dlist.pop()
    else:
        pstatus = "player"
        d_shake = [ai_dlist[-1]]
        ai_dlist.pop()
    return pstatus

def print_player_dominoes():
    for n in range(len(player_dlist)):
        print(f"{n+1}:{player_dlist[n]}")

def print_ontable():
    if len(d_shake) < 6:
        print(''.join(str(x) for x in d_shake))
    else:
        print(f"{''.join(str(x) for x in d_shake[0:3])}...{''.join(str(x) for x in d_shake[-3:])}")

def print_game_endmsg(msg):
    print("Status:", msg)

def check_user_input():
    # while True:
    #     input_data = int(input())
    #     if -len(player_dlist) <= input_data <= len(player_dlist):
    #             return input_data
    #     else:
    #         print("Invalid input. Please try again.")
    while True:
        input_data = input()
        if input_data.isdigit() == True:
            input_data = int(input_data)
            if -len(player_dlist) <= input_data <= len(player_dlist):
                return input_data
        else:
            print("Invalid input. Please try again.")

        # try:
        #     input_data = int(input())
        # except:
        #     print("Invalid input. Please try again.")
        # else:
        #     if -len(player_dlist) <= input_data <= len(player_dlist):
        #         return input_data
        #     else:
        #         print("2.Invalid input. Please try again.")

def print_table():
    print("======================================================================")
    print("Stock size:", len(dominoes_list))
    print("Computer pieces:", len(ai_dlist))
    print("")
    print_ontable()
    print("")
    print("Your pieces:")
    print_player_dominoes()
    print("")


# setup the game
create_domino_set()
plai_status = first_player()

# main game cycle
game_run = True
while game_run == True:

    print_table()

    if plai_status == "computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")
        input()
        ai_choice = random.choice(ai_dlist)
        d_shake.append(ai_choice)
        ai_dlist.remove(ai_choice)
        plai_status = "player"
    else:
        print("Status: It's your turn to make a move. Enter your command.")
        cmd = check_user_input()
        if cmd == 0:
            player_dlist.append(dominoes_list[0])
            dominoes_list.remove(dominoes_list[0])
        else:
            sel_dominoe = player_dlist[abs(cmd)-1]
            if cmd > 0: d_shake.append(sel_dominoe)
            if cmd < 0: d_shake.insert(0, sel_dominoe)
            player_dlist.remove(sel_dominoe)
            plai_status = "computer"

    if len(ai_dlist) == 0 and len(player_dlist) == 0:
        # print_table()
        print_game_endmsg("The game is over. It's a draw!")
        game_run = False
    elif len(ai_dlist) == 0:
        # print_table()
        print_game_endmsg("The game is over. The computer won!")
        game_run = False
    elif len(player_dlist) == 0:
        # print_table()
        print_game_endmsg("The game is over. You won!")

        game_run = False
    elif d_shake[0][0] == d_shake[len(d_shake)-1][1]:
        counter = 0
        for n in d_shake:
            counter += n.count(1)
        if counter == 8:
            print_game_endmsg("The game is over. You won!")
            game_run = False










    # if plai_status == "computer":
    #     print("Status: Computer is about to make a move. Press Enter to continue...")
    #     plai_status = "player"
    #     input()
    #     ai_choice = random.choice(ai_dlist)
    #     d_shake.append(ai_choice)
    #     ai_dlist.remove(ai_choice)
    #     plai_status = "player"
    # elif plai_status == "player":
    #     print("Status: It's your turn to make a move. Enter your command.")
    #     plai_status = "computer"
    #     cmd = int(input())
    #     if cmd == 0:
    #         player_dlist.append(dominoes_list[0])
    #         dominoes_list.remove(dominoes_list[0])
    #     else:
    #         sel_dominoe = player_dlist[abs(cmd)-1]
    #         if cmd > 0: d_shake.append(sel_dominoe)
    #         if cmd < 0: d_shake.insert(0, sel_dominoe)
    #         player_dlist.remove(sel_dominoe)
    #         plai_status = "computer"