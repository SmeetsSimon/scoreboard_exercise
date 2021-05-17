import pytest

from solution_function import update_score


def test_first_score_home():
    """Test dat de eerste score door de home-ploeg
    zorgt voor de volgende stand:
    sets: 0-0
    punten: 1-0
    """
    # de huidige score:
    # sets thuis, sets away, punten thuis, punten away
    score = (0, 0, 0, 0)
    # deze functie oproep geeft aan dat de thuisploeg
    # gescoord heeft ("H" van home, thuis dus)
    new_score = update_score(score, "H")
    # het resultaat van de oproep is de nieuwe stand
    # we controlleren nu, dat de nieuwe stand klopt:
    assert new_score == (0, 0, 1, 0)


def test_first_score_away():
    """Test dat de eerste score door de away-ploeg
    zorgt voor de volgende stand:
    sets: 0-0
    punten: 0-1
    """
    score = (0, 0, 0, 0)
    # deze functie oproep geeft aan dat de away-ploeg
    # gescoord heeft ("A" van home, away dus)
    new_score = update_score(score, "A")
    assert new_score == (0, 0, 0, 1)


def test_first_set_away():
    """Test dat de 25-ste score door de away-ploeg
    zorgt voor de volgende stand:
    sets: 0-1
    punten: 0-0

    De set wordt met andere woorden opgehoogd als de
    ploeg 25 bereikt heeft. De punten voor beide ploegen
    worden terug op 0 gereset.
    """
    score = (0, 0, 0, 24)
    new_score = update_score(score, "A")
    assert new_score == (0, 1, 0, 0)


def test_second_set_away():
    score = (0, 1, 0, 24)
    new_score = update_score(score, "A")
    assert new_score == (0, 2, 0, 0)


def test_1_1_away_scores():
    score = (1, 1, 24, 20)
    new_score = update_score(score, "A")
    assert new_score == (1, 1, 24, 21)


def test_1_1_home_scores():
    score = (1, 1, 24, 20)
    new_score = update_score(score, "H")
    assert new_score == (2, 1, 0, 0)


def test_25_difference_not_enough():
    """Test dat als de score 24-24 is, een score
    voor een ploeg niet kan zorgen voor set-winst.
    De stand is als de away-ploeg scoort nu als volgt:
    sets: 0-1
    punten: 24-25

    Er moet een verschil van 2 punten zijn voordat er
    sprake is van set winst.
    """
    score = (0, 1, 24, 24)
    new_score = update_score(score, "A")
    assert new_score == (0, 1, 24, 25)


def test_26_away_difference_not_enough():
    """Ook hier moet een verschil van 2 punten zijn,
    in dit geval is er ook dus ook geen setwinst.
    """
    score = (1, 1, 25, 25)
    new_score = update_score(score, "A")
    assert new_score == (1, 1, 25, 26)


def test_26_home_difference_not_enough():
    score = (0, 0, 25, 25)
    new_score = update_score(score, "H")
    assert new_score == (0, 0, 26, 25)


def test_27_home_difference_not_enough():
    score = (1, 0, 26, 26)
    new_score = update_score(score, "H")
    assert new_score == (1, 0, 27, 26)


def test_31_home_difference_not_enough():
    """Ook hier moet een verschil van 2 punten zijn,
    in dit geval is er ook dus ook geen setwinst.
    De punten kunnen dus ook oplopen tot ver boven
    de 25.
    """
    score = (1, 1, 30, 30)
    new_score = update_score(score, "H")
    assert new_score == (1, 1, 31, 30)


def test_31_away_difference_not_enough():
    score = (1, 1, 30, 31)
    new_score = update_score(score, "H")
    assert new_score == (1, 1, 31, 31)


def test_31_away_difference_enough():
    score = (1, 1, 30, 31)
    new_score = update_score(score, "A")
    assert new_score == (1, 2, 0, 0)


def test_14_away_difference_not_enough():
    """Ook in de 5de set moet een verschil van 2 punten zijn,
    in dit geval is er ook dus ook geen setwinst.
    De punten kunnen dus ook oplopen tot ver boven
    de 15 in de 5de set.
    """
    score = (2, 2, 14, 14)
    new_score = update_score(score, "A")
    assert new_score == (2, 2, 14, 15)


def test_14_away_difference_enough():
    score = (2, 2, 14, 15)
    new_score = update_score(score, "A")
    assert new_score == (2, 3, 0, 0)


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
    new_score = update_score(oldscore, team)
    assert new_score == expected
