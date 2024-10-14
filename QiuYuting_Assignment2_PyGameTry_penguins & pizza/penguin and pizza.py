import pygame
import time
from settings import Settings
from pg import PG1
from pg import PG2
from pizza import Pizza
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from scoreboard_p2 import Scoreboard_P2
from button import Button
from s_button import S_Button
import music as mu
from rules import  Rules


def run_game():
    pygame.init()
    pg_settings = Settings()
    screen = pygame.display.set_mode((pg_settings.screen_width, pg_settings.screen_height))
    pygame.display.set_caption("Penguin and pizza")
    
    #stats存疑
    stats = GameStats(pg_settings)
    sb = Scoreboard(pg_settings, screen, stats)
    sb2 = Scoreboard_P2(pg_settings, screen, stats)
    
    #创建按钮
    play_button = Button(pg_settings, screen, "Play")
    score_button = S_Button(pg_settings, screen, "Records")
    rule = Rules(pg_settings, screen, 'Click to Read Rules!!')

    #创建企鹅和披萨
    pg1 = PG1(screen)
    pg2 = PG2(screen)
    pizza = Pizza(screen)
    
    mu.music_play_whole()#载入全局背景音乐
    
    pg1_scores = 0
    pg2_scores = 0
    n = 0

    t1 = time.time()
    
    flag = True
    
    while True:
        gf.check_events(stats, play_button, score_button, pg1, pg2, pizza,rule)
        if stats.game_active:
            pg1.update()
            pg2.update()
            a,b = gf.collisions(pg1,pg2,pizza)
            if a and not b:
                stats.pizza_left -= 1
                stats.score += pg_settings.pizza_points
                pg1_scores += 1
                sb.prep_score()
                n += 1
                print("Penguin 1 win a point")
                mu.music_play_eat()#吃pizza音效
            if b and not a:
                stats.pizza_left -= 1
                stats.score2 += pg_settings.pizza_points
                pg2_scores += 1
                sb2.prep_score()
                n += 1
                print("Penguin 2 win a point")
                mu.music_play_eat()#吃pizza音效
            else:
                pass
	
        #每次循环重绘屏幕
        gf.update_screen(pg_settings, screen, stats, sb, sb2, pg1, pg2, pizza, play_button, score_button, rule)
        if stats.game_active:
            t2 = time.time()
            if t2-t1 >= 1:
                pizza.update()
                t1 = t2
            if a or b:
                pizza.update()
                t1 = t2
		
        if stats.pizza_left == 0:
            stats.game_active = False
            if flag:
                print(pg1_scores, pg2_scores)
                gf.recording(pg1_scores, pg2_scores)
                flag = False#第二次进行游戏以后因为flag==false所以不会再显示二者得分比
            

run_game()
