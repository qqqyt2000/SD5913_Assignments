import sys
import pygame
import time
import os

def check_keydown_events(event,pg1,pg2):
    #P1上下左右控制
    if  event.key == pygame.K_RIGHT:
        pg1.moving_right = True
    if event.key == pygame.K_LEFT:
        pg1.moving_left = True
    if event.key == pygame.K_UP:
        pg1.moving_up = True
    if event.key == pygame.K_DOWN:
        pg1.moving_down = True
    #P2 AWDS控制
    if  event.key == pygame.K_d:
        pg2.moving_right = True
    if event.key == pygame.K_a:
        pg2.moving_left = True
    if event.key == pygame.K_w:
        pg2.moving_up = True
    if event.key == pygame.K_s:
        pg2.moving_down = True
    
def check_keyup_events(event,pg1,pg2):
    if event.key == pygame.K_RIGHT:
        pg1.moving_right = False
    if event.key == pygame.K_LEFT:
        pg1.moving_left = False
    if event.key == pygame.K_UP:
        pg1.moving_up = False
    if event.key == pygame.K_DOWN:
        pg1.moving_down = False
    if event.key == pygame.K_d:
        pg2.moving_right = False
    if event.key == pygame.K_a:
        pg2.moving_left = False
    if event.key == pygame.K_w:
        pg2.moving_up = False
    if event.key == pygame.K_s:
        pg2.moving_down = False

def check_events(stats, play_button, score_button, pg1, pg2, pizza,rule):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, pg1,pg2)
                
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, pg1,pg2)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, pizza, mouse_x, mouse_y)
            check_score_button(score_button, mouse_x, mouse_y)
            check_rules(rule, mouse_x, mouse_y)

def check_play_button(stats, play_button, pizza, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        #重置游戏信息
        stats.reset_stats()
        
        stats.game_active = True
        
        #清空pizza重置pg位置
        '''pizza.empty()'''
        
def check_score_button(score_button, mouse_x, mouse_y):
    if score_button.rect.collidepoint(mouse_x, mouse_y):
        os.system('notepad records.txt')

def check_rules(rule, mouse_x, mouse_y):
     if rule.rect.collidepoint(mouse_x, mouse_y):
         os.system('notepad rules.txt')
    

def collisions(pg1,pg2,pizza):
    flag1 = False
    flag2 = False
    if pizza.rect.left <= pg1.rect.centerx and pg1.rect.centerx<=pizza.rect.right and pizza.rect.top <= pg1.rect.centery and pg1.rect.centery <= pizza.rect.bottom:
        flag1 = True
    if pizza.rect.left <= pg2.rect.centerx and pg2.rect.centerx<=pizza.rect.right and pizza.rect.top <= pg2.rect.centery and pg2.rect.centery <= pizza.rect.bottom:
        flag2 = True
    return flag1,flag2

def update_screen(pg_settings, screen, stats, sb, sb2, pg1, pg2, pizza, play_button, score_button,ranking):
    screen.fill(pg_settings.bg_color)
    pg1.blitme()
    pg2.blitme()
    pizza.blitme()
    
    #显示得分
    sb.show_score()
    sb2.show_score()
    
    if not stats.game_active:
        play_button.draw_button()
        score_button.draw_button()
        ranking.draw_button()
    #使最近绘制的屏幕可见
    pygame.display.flip()    
    
def recording(pg1_scores, pg2_scores):
    winner = 0
    winnerdata = '0'
    if pg1_scores > pg2_scores:
        winner = 'Penguin ONE'
        winnerdata = '1'
    elif pg1_scores == pg2_scores:
        winner = 'Matches'
    else:
        winner = 'Penguin TWO'
        winnerdata = '2'
        
    fp = open('records.txt', 'a+')
    fp1 = open('winner.txt', 'a+')
    localtime = time.asctime( time.localtime(time.time()) )
    fp.writelines([ '★Play time:  ', localtime, '     ', '★result:  ', str(pg1_scores), ' vs ', str(pg2_scores), '     ★winner is:  ', winner,  '\n'])
    fp1.writelines([winnerdata])
    fp.close()
