class GameStats():
    ''' Track statistics for Alien Invasion '''

    def __init__(self, ui_settings):
        ''' Initialize statistics '''
        self.ui_settings = ui_settings
        self.reset_stats()

        # High score should never be reset
        self.high_score = 0

        # Start Alien Invasion in an active state
        self.game_active = False

    def reset_stats(self):
        ''' Initialize statistics that can change during the game '''
        self.ships_left = self.ui_settings.ship_limit
        self.score = 0