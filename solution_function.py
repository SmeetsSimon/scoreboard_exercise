def update_score(oldscore, team):
    """Deze functie berekent de nieuwe stand, vertrekkend van
    de oude stand "oldscore" als "team" net gescoord heeft.
    De nieuwe stand wordt als resultaat teruggegeven.

    oldscore: een tuple van 4 nummers, set thuis, set away, punten thuis, punten away
    team: de ploeg die net scoorde, "H" voor thuis, "A" voor away
    """
    sets_home = oldscore[0]
    sets_away = oldscore[1]
    points_home = oldscore[2]
    points_away = oldscore[3]

    # schrijf hier de nodige code om de testen te doen slagen

    return sets_home, sets_away, points_home, points_away
