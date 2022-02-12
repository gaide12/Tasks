def rps_game_winner(players):
    if len(players)>2:
        raise Exception("WrongNumberOfPlayersError")
    rps=['R','P','S']
    pl2=players[1][1]
    pl1=players[0][1]
    if not ((pl1 and pl2) in rps):
        raise Exception('NoSuchStrategyError')
    if (pl1=='P' and pl2=='R')or(pl1=="S" and pl2=="P")or(pl1=="R" and pl2=="S"):
        return (f"Победил {players[0][0]}")
    elif pl1==pl2:
        return (f"Давай по новой)")
    else:
        return (f"Победил {players[1][0]}")
