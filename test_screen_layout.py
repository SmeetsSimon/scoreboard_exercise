from solution_screen_layout import Layout


class Surface:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_size(self):
        return self.width, self.height

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width


def test_get_x_center_position_title():
    layout = Layout(width=1600, height=800)
    x = layout._get_x_center_position_title()
    assert x == 800


def test_get_y_center_position_title():
    layout = Layout(width=1600, height=800)
    x = layout._get_y_center_position_title()
    assert x == 40


def test_get_position_title():
    layout = Layout(width=1600, height=800)
    text = Surface(100, 50)
    x, y = layout.get_position_title(text)
    assert x == (1600 / 2 - 100 / 2)
    assert y == (800 / 20 - 50 / 2)


def test_get_position_clock():
    layout = Layout(width=1600, height=800)
    text = Surface(100, 50)
    x, y = layout.get_position_clock(text)
    assert x == (1600 / 2 - 100 / 2)
    assert y == (2 * 800 / 8 - 50 / 2)


def test_get_x_center_position_home():
    layout = Layout(width=1600, height=800)
    x = layout._get_x_center_position_home()
    assert x == 400


def test_get_x_center_position_away():
    layout = Layout(width=1600, height=800)
    x = layout._get_x_center_position_away()
    assert x == 1200


def test_get_x_position_home():
    layout = Layout(width=1600, height=800)
    text = Surface(100, 50)
    x = layout._get_x_position_home(text)
    assert x == (400 - 100 / 2)


def test_get_x_position_away():
    layout = Layout(width=1600, height=800)
    text = Surface(200, 50)
    x = layout._get_x_position_away(text)
    assert x == (1200 - 200 / 2)


def test_get_team_name_y_center_position():
    layout = Layout(width=1000, height=800)
    y = layout._get_team_name_y_center_position()
    assert y == 350


def test_get_team_logo_y_center_position():
    layout = Layout(width=1000, height=800)
    y = layout._get_team_logo_y_center_position()
    assert y == 200


def test_get_team_score_y_center_position():
    layout = Layout(width=1000, height=800)
    y = layout._get_team_score_y_center_position()
    assert y == 500


def test_get_team_set_score_y_center_position():
    layout = Layout(width=1000, height=800)
    y = layout._get_team_set_score_y_center_position()
    assert y == 700


def test_get_team_name_y_position():
    layout = Layout(width=1000, height=800)
    text = Surface(100, 50)
    y = layout._get_team_name_y_position(text)
    assert y == (350 - 50 / 2)


def test_get_team_logo_y_position():
    layout = Layout(width=1000, height=800)
    logo = Surface(200, 100)
    y = layout._get_team_logo_y_position(logo)
    assert y == (200 - 100 / 2)


def test_get_team_score_y_position():
    layout = Layout(width=1000, height=800)
    text = Surface(100, 80)
    y = layout._get_team_score_y_position(text)
    assert y == (500 - 80 / 2)


def test_get_team_set_score_y_position():
    layout = Layout(width=1000, height=800)
    text = Surface(100, 40)
    y = layout._get_team_set_score_y_position(text)
    assert y == (700 - 40 / 2)


def test_get_x_position_team_name_away():
    layout = Layout(1000, 1000)
    text = Surface(100, 50)
    x, y = layout.get_position_team_name_away(text)
    assert x == (3 * 1000 / 4 - 100 / 2)


def test_get_y_position_team_name_away():
    layout = Layout(1000, 800)
    text = Surface(100, 50)
    x, y = layout.get_position_team_name_away(text)
    expected = 3.5 * 800 / 8 - 50 / 2
    assert y == expected


def test_get_x_position_team_name_home():
    layout = Layout(1000, 1000)
    text = Surface(100, 50)
    x, y = layout.get_position_team_name_home(text)
    assert x == (1000 / 4 - 100 / 2)


def test_get_y_position_team_name_home():
    layout = Layout(1000, 1000)
    text = Surface(100, 50)
    x, y = layout.get_position_team_name_home(text)
    assert y == (3.5 * 1000 / 8 - 50 / 2)


def test_get_position_team_logo_home():
    layout = Layout(1000, 1000)
    text = Surface(100, 50)
    x, y = layout.get_position_team_logo_home(text)
    assert x == (1000 / 4 - 100 / 2)
    assert y == (1000 / 4 - 50 / 2)


def test_get_position_team_logo_away():
    layout = Layout(1000, 1000)
    text = Surface(100, 50)
    x, y = layout.get_position_team_logo_away(text)
    assert x == (3 * 1000 / 4 - 100 / 2)
    assert y == (1000 / 4 - 50 / 2)


def test_get_position_team_set_score_home():
    layout = Layout(1000, 1000)
    text = Surface(100, 50)
    x, y = layout.get_position_team_set_score_home(text)
    assert x == (1000 / 4 - 100 / 2)
    assert y == (7 * 1000 / 8 - 50 / 2)


def test_get_position_team_set_score_away():
    layout = Layout(1000, 1000)
    text = Surface(100, 50)
    x, y = layout.get_position_team_set_score_away(text)
    assert x == (3 * 1000 / 4 - 100 / 2)
    assert y == (7 * 1000 / 8 - 50 / 2)


def test_get_position_team_score_home():
    layout = Layout(1000, 1000)
    text = Surface(100, 50)
    x, y = layout.get_position_team_score_home(text)
    assert x == (1000 / 4 - 100 / 2)
    assert y == (5 * 1000 / 8 - 50 / 2)


def test_get_position_team_score_away():
    layout = Layout(1000, 1000)
    text = Surface(100, 50)
    x, y = layout.get_position_team_score_away(text)
    assert x == (3 * 1000 / 4 - 100 / 2)
    assert y == (5 * 1000 / 8 - 50 / 2)
