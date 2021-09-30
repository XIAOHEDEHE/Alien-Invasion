class Settings():
    """A class to store all settings for A_I"""

    def __init__(self):
        """Init the game's settings"""
        # Screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (253, 253, 253)

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Ship settings
        self.ship_speed_factor = 1.5
