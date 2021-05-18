class Layout:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Methods for calculating the title position

    def _get_x_center_position_title(self):
        """Get the X position of the center of the title"""
        return self.width / 2

    def _get_y_center_position_title(self):
        """Get the Y position of the center of the title"""
        return self.height / 20

    def _get_x_position_title(self, surface):
        """Get the X position of the top left of the title"""
        return self._get_x_center_position_title() - surface.get_width() / 2

    def _get_y_position_title(self, surface):
        """Get the Y position of the top left of the title"""
        return self._get_y_center_position_title() - surface.get_height() / 2

    def get_position_title(self, surface):
        """Get the X and Y coordinates of the top left of the title

        surface: the image rendered with pygame font rendering
        These are the coordinates at which we will blit the image using pygame:
        screen.blit(surface, (x, y))
        """
        return self._get_x_position_title(surface), self._get_y_position_title(
            surface
        )

    # Methods for calculating the clock position

    def _get_x_center_position_clock(self):
        return 0

    def _get_y_center_position_clock(self):
        return 0

    def _get_x_position_clock(self, surface):
        return 0

    def _get_y_position_clock(self, surface):
        return 0

    def get_position_clock(self, surface):
        """The position of the clock showing the game time"""
        return 0, 0

    # Methods for calculating the X-position of the
    # columns of both teams

    def _get_x_center_position_home(self):
        return 0

    def _get_x_position_home(self, surface):
        return 0

    def _get_x_center_position_away(self):
        return 0

    def _get_x_position_away(self, surface):
        return 0

    # Methods for calculating the logo position

    def _get_team_logo_x_center_position(self):
        return 0

    def _get_team_logo_y_center_position(self):
        return 0

    def _get_team_logo_y_position(self, surface):
        return 0

    def get_position_team_logo_home(self, surface):
        """The position of the home team logo"""
        return 0, 0

    def get_position_team_logo_away(self, surface):
        """The position of the away team logo"""
        return 0, 0

    # Methods for calculating the set score position

    def _get_team_set_score_x_center_position(self):
        return 0

    def _get_team_set_score_y_center_position(self):
        return 0

    def _get_team_set_score_y_position(self, surface):
        return 0

    def get_position_team_set_score_home(self, surface):
        """The position of the home team set score"""
        return 0, 0

    def get_position_team_set_score_away(self, surface):
        """The position of the away team set score"""
        return 0, 0

    # Methods for calculating the score position

    def _get_team_score_x_center_position(self):
        return 0

    def _get_team_score_y_center_position(self):
        return 0

    def _get_team_score_y_position(self, surface):
        return 0

    def get_position_team_score_home(self, surface):
        """The position of the home team score"""
        return 0, 0

    def get_position_team_score_away(self, surface):
        """The position of the away team score"""
        return 0, 0

    # Methods for calculating the team name position

    def _get_team_name_y_center_position(self):
        return 0

    def _get_team_name_y_position(self, surface):
        return 0

    def get_position_team_name_home(self, surface):
        """The position of the home team name"""
        return 0, 0

    def get_position_team_name_away(self, surface):
        """The position of the away team name"""
        return 0, 0
