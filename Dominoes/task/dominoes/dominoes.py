# Write your code here
import random

dominoes_list, player_dlist, ai_dlist, d_shake, r_list, t_list = [], [], [], [], [], []
weight_of_aidom = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}


def create_domino_set():
    global player_dlist
    global ai_dlist
    global dominoes_list
    # set and shuffle the dominoes
    d_list = [[a, b] for a in range(7) for b in range(a, 7)]
    random.shuffle(d_list)
    # give dominoes to players
    player_dlist = d_list[0:7]
    ai_dlist = d_list[7:14]
    dominoes_list = d_list[14:]
    player_dlist.sort()
    ai_dlist.sort()


def first_player():
    global player_dlist
    global ai_dlist
    global d_shake
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
    for num in range(len(player_dlist)):
        print(f"{num + 1}:{player_dlist[num]}")


def print_ontable():
    if len(d_shake) < 6:
        print(''.join(str(x) for x in d_shake))
    else:
        print(f"{''.join(str(x) for x in d_shake[0:3])}...{''.join(str(x) for x in d_shake[-3:])}")


def print_game_endmsg(msg):
    print("Status:", msg)


def check_user_input(msg=""):
    while True:
        try:
            if msg != "":
                print(msg)
            input_data = int(input())
        except ValueError:
            print("Invalid input. Please try again.")
        else:
            if -len(player_dlist) <= input_data <= len(player_dlist):
                return input_data
            else:
                print("Invalid input. Please try again.")


def get_dominoes_variants(ai_or_player_dlist):
    temp_list = []
    for item in ai_or_player_dlist:
        if item[0] == d_shake[0][0] or item[0] == d_shake[len(d_shake) - 1][1] or \
                item[1] == d_shake[0][0] or item[1] == d_shake[len(d_shake) - 1][1]:
            temp_list.append(item)
    return temp_list


def run_dominoe_magnet(dom, board_snake):
    r_vars, l_vars = [], []

    for item in dom:
        if board_snake[0][1] == item[0]:
            r_vars.append(item)
        if board_snake[0][1] == item[1]:
            r_vars.append([item[1], item[0]])
        if board_snake[0][0] == item[0]:
            l_vars.append([item[1], item[0]])
        if board_snake[0][0] == item[1]:
            l_vars.append(item)

    # calculate dominoes weigts
    temp_list = dom + d_shake
    for x in temp_list:
        for i in range(7):
            weight_of_aidom[i] = weight_of_aidom[i] + x.count(i)

    # select best dominoe to use (for AI)
    temp_list = l_vars + r_vars
    max_weight = 0
    best_choice = []
    for n in temp_list:
        if (weight_of_aidom[n[0]] + weight_of_aidom[n[1]]) > max_weight:
            max_weight = weight_of_aidom[n[0]] + weight_of_aidom[n[1]]
            best_choice.clear()
            best_choice.append(n)

    if len(best_choice) > 0:
        if best_choice[0] in l_vars:
            return best_choice[0], 0
        if best_choice[0] in r_vars:
            return best_choice[0], 1
    return [[-1, -1], 0]


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
while game_run:
    t_list = []
    print_table()
    # AI turn
    if plai_status == "computer":
        input("Status: Computer is about to make a move. Press Enter to continue...")

        # get variants from current list of player dominoes
        t_list, lr_flag = run_dominoe_magnet(ai_dlist, [[d_shake[0][0], d_shake[len(d_shake) - 1][1]]])

        # if no right dominoes in the AI List
        if t_list == [-1, -1]:
            if len(dominoes_list) > 0:
                ai_dlist.append(dominoes_list[0])
                dominoes_list.remove(dominoes_list[0])
            plai_status = "player"
        # if AI have dominoe
        else:
            if lr_flag == 0:
                d_shake.insert(0, t_list)
            else:
                d_shake.append(t_list)
            for item in ai_dlist:
                if item == t_list:
                    ai_dlist.remove(item)
                elif [item[1], item[0]] == t_list:
                    ai_dlist.remove(item)
        plai_status = "player"
    # Player Turn
    else:
        print("Status: It's your turn to make a move. Enter your command.")
        r_list = get_dominoes_variants(player_dlist)

        cmd = check_user_input()
        if cmd == 0:
            if len(dominoes_list) > 0:
                player_dlist.append(dominoes_list[0])
                dominoes_list.remove(dominoes_list[0])
            plai_status = "computer"
        else:
            sel_dominoe = player_dlist[abs(cmd) - 1]
            while sel_dominoe not in r_list:
                cmd = check_user_input("Illegal move. Please try again.")
                sel_dominoe = player_dlist[abs(cmd) - 1]

                if cmd == 0:
                    if len(dominoes_list) > 0:
                        player_dlist.append(dominoes_list[0])
                        dominoes_list.remove(dominoes_list[0])
                        pass_mode = 1
                        print("PASS and add", dominoes_list[0])
                    plai_status = "computer"
                    break

            if cmd > 0:
                if sel_dominoe[0] == d_shake[len(d_shake) - 1][1]:
                    d_shake.append([sel_dominoe[0], sel_dominoe[1]])
                elif sel_dominoe[1] == d_shake[len(d_shake) - 1][1]:
                    d_shake.append([sel_dominoe[1], sel_dominoe[0]])
            if cmd < 0:
                if sel_dominoe[0] == d_shake[0][0]:
                    d_shake.insert(0, [sel_dominoe[1], sel_dominoe[0]])
                elif sel_dominoe[1] == d_shake[0][0]:
                    d_shake.insert(0, [sel_dominoe[0], sel_dominoe[1]])
            player_dlist.remove(sel_dominoe)
            plai_status = "computer"

    # end of game conditions check
    if ai_dlist == [] and player_dlist == []:
        print_table()
        print_game_endmsg("The game is over. It's a draw!")
        game_run = False
    elif not ai_dlist:
        print_table()
        print_game_endmsg("The game is over. The computer won!")
        game_run = False
    elif not player_dlist:
        print_table()
        print_game_endmsg("The game is over. You won!")
        game_run = False

    if d_shake[0][0] == d_shake[len(d_shake) - 1][1] and game_run is not False:
        counter = 0
        for n in d_shake:
            counter += n.count(d_shake[0][0])
        if counter == 8:
            print_table()
            print_game_endmsg("The game is over. It's a draw!")
            game_run = False
