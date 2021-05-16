import pytest

from main import update_score


def test_update_score():
    score = (0, 0, 0, 0)
    new_score = update_score(score, "H")
    assert new_score == (0, 0, 1, 0)


def test_update_score2():
    score = (0, 0, 0, 0)
    new_score = update_score(score, "A")
    assert new_score == (0, 0, 0, 1)


def test_update_score3():
    score = (0, 0, 0, 24)
    new_score = update_score(score, "A")
    assert new_score == (0, 1, 0, 0)


def test_update_score4():
    score = (0, 1, 0, 24)
    new_score = update_score(score, "A")
    assert new_score == (0, 2, 0, 0)


def test_update_score5():
    score = (1, 1, 24, 20)
    new_score = update_score(score, "A")
    assert new_score == (1, 1, 24, 21)


def test_update_score6():
    score = (1, 1, 24, 20)
    new_score = update_score(score, "A")
    assert new_score == (1, 1, 24, 21)


testdata = [
    ((0, 0, 0, 0), "H", (0, 0, 1, 0)),
    ((0, 0, 1, 0), "H", (0, 0, 2, 0)),
    ((0, 0, 2, 0), "H", (0, 0, 3, 0)),
    ((0, 0, 23, 0), "H", (0, 0, 24, 0)),
    ((0, 0, 24, 3), "H", (1, 0, 0, 3)),
    ((1, 0, 24, 5), "H", (2, 0, 0, 5)),
    ((1, 1, 24, 20), "H", (2, 1, 0, 20)),
    ((1, 2, 24, 20), "H", (2, 2, 0, 20)),
]


@pytest.mark.parametrize("oldscore,team,expected", testdata)
def test_update_scores(oldscore, team, expected):
    new_score = update_score(oldscore, team)
    assert new_score == expected
