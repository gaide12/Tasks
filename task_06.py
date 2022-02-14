def rps_game_winner(players):
    if len(players)!=2:
        raise Exception("WrongNumberOfPlayersError")
    rps=['R','P','S']
    pl2=players[1][1]
    pl1=players[0][1]
    if not ((pl1 and pl2) in rps):
        raise Exception('NoSuchStrategyError')
    if (pl1=='P' and pl2=='R')or(pl1=="S" and pl2=="P")or(pl1=="R" and pl2=="S"):
        return (f"{players[0][0]} {pl1}")
    elif pl1==pl2:
        return (f"{players[0][0]} {pl1}")
    else:
        return (f"{players[1][0]} {pl2}")
print(rps_game_winner([['player1', 'P'], ['player2', 'S']])) # 'player2 S'
print(rps_game_winner([['player1', 'S'], ['player2', 'S']])) #  'player1 P'
print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])) # WrongNumberOfPlayersError
print(rps_game_winner([['player1', 'P'], ['player2', 'A']])) # NoSuchStrategyError