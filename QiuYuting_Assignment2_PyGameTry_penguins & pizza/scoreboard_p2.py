import pygame.font

class Scoreboard_P2():
    """ 显示得分信息的类 """
    
    def __init__(self, pg_settings, screen, stats):
        """ 初始化显示得分涉及的属性 """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.pg_settings = pg_settings
        self.stats = stats
        
        #显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        #准备初始得分图像
        self.prep_score()
        
    def prep_score(self):
        """ 将得分转换为一幅渲染的图像 """
        score_str = str(self.stats.score2)
        self.score_image = self.font.render(score_str, True, self.text_color,self.pg_settings.bg_color)
        
        #将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20
        
    def show_score(self):
        '''屏幕显示得分'''
        self.screen.blit(self.score_image, self.score_rect)