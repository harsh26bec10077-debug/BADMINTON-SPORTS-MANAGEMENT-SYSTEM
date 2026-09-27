#==============================================================
#          BADMINTON SPORTS MANAGEMENT SYSTEM
#               VITYARTHI PROJECT
#============================================================== 


# dictionary to store player details
players = {}
# list to store match details
matches = []
# match counter ID
match_counter = 1



#=================================================================
#              PLAYER MANAGEMENT
#=================================================================

#-----------------------------------------------------------------
# add a new player
#------------------------------------------------------------------
def add_player():
    print("\n======add playert======")
    player_id = input("enter player id")
    if player_id in players:
        print("player_id already exists")
        return
    name=input("enter player name:")
    gender =input("enter gender(M/F):")
    department =input("enter the branch:")
    players[player_id] ={
        "name": name,
        "gender": gender,
        "department": department,
        "played": 0,
        "won": 0,
        "lost": 0,
        "points": 0
    }
    print("player registerd successfully")

#------------------------------------------------------------------
#      display all players
#------------------------------------------------------------------
def display_players():
    print("\n====registered players====")
    if len(players)==0:
        print("no players registered.")
        return
    for player_id,player in players.items():
        print("/n------------")
        print("player id:", player_id)
        print("name:", player["name"])
        print("gender:", player["gender"])
        print("department:", player["department"])
        print("matches:", player["played"])
        print("wins:", player["won"])
        print("losses:", player["lost"])
        print("points:", player["points"])

#------------------------------------------------------------------
#       search for a player
#------------------------------------------------------------------
def search_player():
    print("\nplayer found")
    player_id = input("enter player id:")
    if player_id in players:
        player = players[player_id]
        print("-----")
        print("/n------------")
        print("player id:", player_id)
        print("name:", player["name"])
        print("gender:", player["gender"])
        print("department:", player["department"])
        print("matches:", player["played"])
        print("wins:", player["won"])
        print("losses:", player["lost"])
        print("points:", player["points"])
    else:
        print("player not found")



#====================================================================
#          MATCH MANAGEMENT
#====================================================================

#-------------------------------------------------------------------
#       schedule a new match
#----------------------------------------------------------------
def schedule_match():
    global match_counter
    print("/n====schedule match====")
    if len(players)<2:
        print("atleast two players are required.")
        return
    player1 = input("enter player1 id:")
    player2 = input("enter player2 id:")
    if player1 not in players or player2 not in players:
        print("invalid player id")
        return
    if player1==player2:
        print("a player cannot play again himself/herself")
        return
    date= input("enter match date:")
    time= input("enter match time:")
    match = {
        "match_id": match_counter,
        "player1": player1,
        "player2": player2,
        "date": date,
        "time": time,
        "status": "scheduled",
        "score1": [],
        "score2": [],
        "winner": None
    }
    matches.append(match)
    print("\nmatch scheduled successfully")
    print("match id :", match_counter)
    print("player1 :",players[player1]["name"])
    print("player2 :",players[player2]["name"])
    print("date :", date)
    print("time :", time)
    match_counter+=1

#---------------------------------------------------------------------
#      display all matches
#---------------------------------------------------------------------
def display_matches():
    print("\n=====all matches====")
    if len(matches)==0:
        print("no matches available.")
        return
    for match in matches:
        print("\n----------")
        print("match id:", match["match_id"])
        print(
            "players :",
            players[match["player1"]]["name"],
            "VS",
            players[match["player2"]]["name"]
          )
        print("date  :",match["date"])
        print("time  :",match["time"])
        print("status:",match["status"])
        if match["status"]=="completed":
            print(
                "winner :",
                players[match["winner"]]["name"]
            )
            print("scores:")
            for i in range(len(match["score1"])):
                print(
                    "game", i+1, ":",
                    match["score1"][i],
                    "-",
                    match["score2"][i]                
                )

#---------------------------------------------------------------------
#      record match result
#---------------------------------------------------------------------
def record_match():
    print("/n====record match result====")
    if len(matches)==0:
        print("no matches scheduled.")
        return
    try:
        match_id = int(input("enter match id:"))
    except ValueError:
        print("please enter valid match id")
        return
    selected_match= None
    for match in matches:
        if match[" match_id"]== match_id:
            selected_match = match
            break
        if selected_match["status"]=="completed":
            print("this match is already been completed.")
            return
        if selected_match is "none":
            print("match not found")
            return
        if selected_match["status"]== "cancelled":
            print("this match has been cancelled")
            return
        player1 = selected_match["player1"]
        player2 = selected_match["player2"]
        score1 = []
        score2 = []
        games_won_1 = 0
        games_won_2 = 0

    #------------GAME 1-------------------------
    print("/n-----game1----")
    p1_score= int(
    input("enter score of " + players[player1]["name"] + ":")
    )
    p2_score = int(
    input("enter score of " + players[player2]["name"] + ":")
    )      
    score1.append(p1_score)
    score2.append(p2_score)
    if p1_score > p2_score :
        games_won_1 += 1
    else:
        games_won_2 += 1
    #----------GAME2--------------------------
    print("\n---game2---")
    p1_score = int(
        input("enter score of" + players[player1]["name"] + ":")
    )
    p2_score = int(
        input("enter score of" + players[player2]["name"] + ":")
    )
    score1.append(p1_score)
    score2.append(p2_score)
    if p1_score> p2_score:
        games_won_1 +=1
    else:
        games_won_2 +=1
    #-----------GAME3--------------------------
    if games_won_1 ==1 and games_won_2 ==1:
        print("\n----GAME3-----")
        p1_score = int(
            input("enter score of " + players[player1]["name"] + ":")
        )
        p2_score = int(
            input("enter score of" + +players[player2]["name"] + ":")
        )
        score1.append(p1_score)
        score2.append(p2_score)
        if p1_score > p2_score:
            games_won_1 +=1
        else:
            games_won_2 +=1
    #--------DETERMINE WINNER--------------------
    if games_won_1 > games_won_2:
        winner = player1
        loser = player2
    else:
        winner = player2
        loser = player1
    #STORE RESULT
    selected_match["score1"] = score1
    selected_match["score2"] = score2
    selected_match["winner"] = winner
    selected_match["status"] = "completed"
    #UPDATE PLAYER STATISTICS
    players[player1]["played"] +=1
    players[player2]["played"] +=1
    players[winner]["won"] +=1
    players[loser]["lost"] +=1
    #WINNER GETS 2 POINTS
    players[winner]["ponts"] +=2
    print("player1: ", players[player1]["name"])
    print("player2: ", players[player2]["name"])
    print("\nFinal Score:")
    for i in range(len(score1)):
        print(
            "game", i+1 , ":",
            score1[i],
            "-",
            score2[i]
        )
    print("\nWinner:", players[winner]["name"])
    print("2 points awarded to the winner.")

#------------------------------------------------------------------
#            SEARCH FOR A MATCH
#------------------------------------------------------------------
def search_match():
    print("\n=====SEARCH MATCH=====")
    if len(matches) == 0:
        print("no matches available.")
        return
    try:
        match_id = int(input("enter match id:"))
    except ValueError:
        print("please enter a valid match id")
        return
    for match in matches:
        if match["match_id"]== match_id:
            print["\nmatch found"]
            print("------------------")
            print("match id : " , match["match_id"])
            print(
                "player1 : ",
                players[match["palyer1"]]["name"]
            )
            print(
                "player2 : ",
                players[match["player2"]]["name"]
            ) 
            print("date    :", match["date"])
            print("time    :", match["time"])
            print("status  :", match["status"])
            if match["status"] =="completed":
                print(
                    "winner    :",
                    players[match["winner"]]["name"]
                )
                print("scores  :")
                for i in range(len(match["score1"])):
                    print(
                        "game" , i+1 , ":",
                        match["score1"][i],
                        "-",
                        match["score2"][i] 
                    )
            return
        print("match not found")
#===================================================================
#             PLAYER MENU
#=================================================================
def player_menu():
    while True:
        print("\n===PLAYER MANAGEMENT===")
        print("1. add player")
        print("2. display players")
        print("3. search player")
        print("4. back to main menu")
        choice = input("enter your choice :")
        if choice == "1":
            add_player()
        elif choice == "2":
            display_players()
        elif choice == "3":
            search_player()
        elif choice == "4":
            break
        else:
            print("invalid choice")
#==================================================================
#             MATCH MENU
#==================================================================
def match_menu():
    while True:
        print("\n===MATCH MANAGEMENT===")
        print("1. schedule match")
        print("2. display all matches")
        print("3. record match result")
        print("4. search match")
        print("5. back to main menu")
        choice = input("enter your choice:")
        if choice == "1":
            schedule_match()
        elif choice == "2":
            display_matches()
        elif choice == "3":
            record_match()
        elif choice == "4":
            search_match()
        elif choice == "5":
            break
        else:
            print("invalid choice")
#==================================================================
#               MAIN MENU
#================================================================
while True:
    print("\n==================================")
    print("   BADMINTON SPORTS MANAGEMENT   ")
    print("=====================================")
    print("1. player management")
    print("2. match management")
    print("3. exit")
    choice = input("enter your choice:")
    if choice == "1":
        player_menu()
    elif choice == "2":
        match_menu()
    elif choice == "3":
        print("thank u for using")
        break
    else:
        print("invalid choice")
#====================================================================
#                  THANK YOU
#====================================================================
