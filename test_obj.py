import pytest

from solution_obj import Game


def test_score_0():
    """Test dat de initiele score 0-0 is:
    punten: 0-0
    """
    game = Game()

    assert game.points_home == 0
    assert game.points_away == 0


def test_scoreset_0():
    """Test dat de initiele set stand 0-0 is:
    set: 0-0
    """
    game = Game()

    assert game.sets_home == 0
    assert game.sets_away == 0


def test_update_setnr():
    """Test dat de initiele set nummer 1 is:"""
    game = Game()

    assert game.set_nr == 1


def test_get_max_points():
    """Test dat er een functie `get_max_points` is
    die het maximale aantal punten in de huidige set aangeeft:
    """
    game = Game()

    assert game.get_max_points() == 25


def test_get_max_points_set_1():
    """Test dat er een functie `get_max_points` is
    die het maximale aantal punten in de huidige set aangeeft
    en dat deze 25 geeft voor de eerste set.
    """
    game = Game()
    game.set_nr = 1
    assert game.get_max_points() == 25


def test_get_max_points_set2():
    """Test dat er een functie `get_max_points` is
    die het maximale aantal punten in de huidige set aangeeft
    en dat deze 25 geeft voor de 2de set.
    """
    game = Game()
    game.set_nr = 2
    assert game.get_max_points() == 25


def test_get_max_points_set3():
    """Test dat er een functie `get_max_points` is
    die het maximale aantal punten in de huidige set aangeeft
    en dat deze 25 geeft voor de 3de set.
    """
    game = Game()
    game.set_nr = 3
    assert game.get_max_points() == 25


def test_get_max_points_set4():
    """Test dat er een functie `get_max_points` is
    die het maximale aantal punten in de huidige set aangeeft
    en dat deze 25 geeft voor de 4de set.
    """
    game = Game()
    game.set_nr = 4
    assert game.get_max_points() == 25


def test_get_max_points_set5():
    """Test dat er een functie `get_max_points` is
    die het maximale aantal punten in de huidige set aangeeft
    en dat deze 15 geeft voor de 2de set.
    """
    game = Game()
    game.set_nr = 5
    assert game.get_max_points() == 15


def test_score_home():
    game = Game()
    game.score("H")

    assert game.sets_away == 0
    assert game.sets_home == 0
    assert game.points_away == 0
    assert game.points_home == 1


def test_score_away():
    game = Game()
    game.score("A")

    assert game.sets_away == 0
    assert game.sets_home == 0
    assert game.points_away == 1
    assert game.points_home == 0


def test_three_points():
    game = Game()
    game.score("A")
    game.score("H")
    game.score("A")

    assert game.sets_away == 0
    assert game.sets_home == 0
    assert game.points_away == 2
    assert game.points_home == 1


def test_set_home():
    game = Game()
    game.points_home = 24
    game.points_away = 21
    game.score("H")

    assert game.points_home == 0
    assert game.points_away == 0
    assert game.sets_home == 1
    assert game.sets_away == 0
    assert game.set_nr == 2


def test_set_away():
    game = Game()
    game.points_home = 20
    game.points_away = 24
    game.score("A")

    assert game.points_away == 0
    assert game.points_home == 0
    assert game.sets_away == 1
    assert game.sets_home == 0
    assert game.set_nr == 2


def test_third_set():
    game = Game()
    game.sets_home = 0
    game.sets_away = 2
    game.set_nr = 3
    game.points_home = 20
    game.points_away = 24
    game.score("A")

    assert game.points_away == 0
    assert game.points_home == 0
    assert game.sets_home == 0
    assert game.sets_away == 3
    assert game.set_nr == 4


def test_fifth_set():
    game = Game()
    game.sets_home = 2
    game.sets_away = 2
    game.set_nr = 5
    game.points_home = 10
    game.points_away = 14
    game.score("A")

    assert game.points_away == 0
    assert game.points_home == 0
    assert game.sets_home == 2
    assert game.sets_away == 3


# Pytest voorziet mogelijkheden om zeer veel
# testen heel compact te omschrijven.
# Onderstaande tabel geeft telkens het volgende weer:
# oude stand, ploeg die scoort, nieuwe stand
testdata = [
    ((0, 0, 0, 0), "H", (0, 0, 1, 0)),
    ((0, 0, 1, 0), "H", (0, 0, 2, 0)),
    ((0, 0, 2, 0), "H", (0, 0, 3, 0)),
    ((0, 0, 23, 0), "H", (0, 0, 24, 0)),
    ((0, 0, 24, 3), "H", (1, 0, 0, 0)),
    ((1, 0, 24, 5), "H", (2, 0, 0, 0)),
    ((1, 1, 24, 20), "H", (2, 1, 0, 0)),
    ((1, 2, 24, 20), "H", (2, 2, 0, 0)),
    ((2, 2, 14, 10), "H", (3, 2, 0, 0)),
    ((0, 0, 18, 24), "A", (0, 1, 0, 0)),
    ((0, 1, 20, 24), "A", (0, 2, 0, 0)),
    ((0, 2, 17, 24), "A", (0, 3, 0, 0)),
    ((0, 0, 10, 24), "A", (0, 1, 0, 0)),
    ((0, 1, 24, 22), "H", (1, 1, 0, 0)),
    ((1, 1, 12, 24), "A", (1, 2, 0, 0)),
    ((1, 2, 22, 24), "A", (1, 3, 0, 0)),
    ((0, 0, 24, 23), "H", (1, 0, 0, 0)),
    ((1, 0, 21, 24), "A", (1, 1, 0, 0)),
    ((1, 1, 23, 24), "A", (1, 2, 0, 0)),
    ((1, 2, 24, 17), "H", (2, 2, 0, 0)),
    ((2, 2, 14, 10), "H", (3, 2, 0, 0)),
    ((0, 0, 22, 24), "A", (0, 1, 0, 0)),
    ((0, 1, 30, 29), "H", (1, 1, 0, 0)),
    ((1, 1, 21, 24), "A", (1, 2, 0, 0)),
    ((1, 2, 21, 24), "A", (1, 3, 0, 0)),
    ((0, 0, 26, 27), "A", (0, 1, 0, 0)),
    ((0, 0, 25, 24), "H", (1, 0, 0, 0)),
]


# Onderstaande functie hoeven jullie niet te begrijpen.
@pytest.mark.parametrize("oldscore,team,expected", testdata)
def test_update_scores(oldscore, team, expected):
    game = Game()
    game.sets_home = oldscore[0]
    game.sets_away = oldscore[1]
    game.set_nr = oldscore[0] + oldscore[1] + 1
    game.points_home = oldscore[2]
    game.points_away = oldscore[3]
    game.score(team)

    assert game.points_away == expected[3]
    assert game.points_home == expected[2]
    assert game.sets_home == expected[0]
    assert game.sets_away == expected[1]
