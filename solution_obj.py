class Game:
    """Deze class houdt de stand bij, en voorziet een functie
    om de nieuwe stand te berekenen.
    """

    def __init__(self):
        """Zet de stand op de beginstand bij aanvang van de wedstrijd"""
        # TODO: Gebruik onderstaande member variables,
        # maar corrigeer de initiele waardes:
        self.points_home = 99
        self.points_away = 99
        self.sets_home = 99
        self.sets_away = 99
        self.set_nr = 99

    def get_max_points(self):
        """Geef het maximaal aantal punten voor deze set terug."""
        # TODO: Geef de correcte waarde terug afhankelijk van
        # de set_nr.
        return 99

    def score(self, team):
        """Bereken de nieuwe stand als team `team` gescoord heeft.
        team: kan "A" of "H" zijn, voor "away" en "home".
        """
        # TODO: Pas hier de punten, set punten en set nummer aan.
        # Gebruik `get_max_points` om te weten bij hoeveel punten je
        # in de set de set gewonnen hebt.
