class GameStats():
    '''跟踪游戏统计信息'''
    
    def __init__(self, pg_settings):
        self.pg_settings = pg_settings
        self.reset_stats()
        
        self.game_active = False
        
    def reset_stats(self):
        self.pizza_left = self.pg_settings.pizza_limit
        self.score = 0
        self.score2 = 0