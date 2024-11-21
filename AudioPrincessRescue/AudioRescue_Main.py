import pygame
import sys
from GuardCorps import AudioImage
from Warrior import ControlImage
from Hound import RandomImage
from states import States
from button import Button
from collision_detector import CollisionDetector
import random

def main():
    # 初始化 Pygame
    pygame.init()

    # 设置屏幕大小
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Audio Control Game by qyt,gjn & gy")

    # 加载字体
    font = pygame.font.Font(None, 74)
    font_small = pygame.font.Font(None, 36)

    # 创建对象
    begin_image = pygame.image.load('images/begin_image.jpg')
    audio_image = AudioImage('images/guardcorps.png')
    control_image = ControlImage('images/warrior.png')
    random_image = RandomImage('images/ghost.png')
    guardwin_image = pygame.image.load('images/guardwin.jpg')
    warriorwin_image = pygame.image.load('images/warriorwin.jpg')
    button_image = 'images/button.png'
    button_image_2 = 'images/button2.png'

    # 创建状态管理对象
    game_states = States()

    # 创建按钮
    begin_background = pygame.transform.scale(begin_image, (screen.get_width(), screen.get_height()))
    screen.blit(begin_background, (0, 0))
    play_button = Button(button_image, (330, 375))
    play_button_2 = Button(button_image_2, (330, 375))

    # 初始化游戏时间
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    # 创建碰撞检测器
    collision_detector = CollisionDetector(control_image, audio_image, random_image)

    # 主循环
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and game_states.get_state() == States.INIT:
                # 检查鼠标点击位置
                if play_button.is_clicked(event.pos):
                    game_states.set_state(States.PLAYING)
                    # 重新设置 random_image 的位置，确保不与 control_image 重合
                    while True:
                        random_image.x = random.randint(0, screen.get_width() - random_image.width)
                        random_image.y = random.randint(0, screen.get_height() - random_image.height)
                        random_rect = pygame.Rect(random_image.x, random_image.y, random_image.width, random_image.height)
                        control_rect = pygame.Rect(control_image.x, control_image.y, control_image.width, control_image.height)
                        if not random_rect.colliderect(control_rect):
                            break
            elif event.type == pygame.MOUSEBUTTONDOWN and game_states.get_state() == States.PLAYING:
                game_states.set_state(States.END)

        if game_states.get_state() == States.INIT:
            screen.blit(begin_background, (0, 0))
            play_button.draw(screen)
            pygame.display.flip()

        elif game_states.get_state() == States.PLAYING:
            # 更新位置
            audio_image.update_position()
            control_image.update_position()
            random_image.update_position()

            # 检测碰撞
            if collision_detector.detect_collision():
                end_background = pygame.transform.scale(guardwin_image, (screen.get_width(), screen.get_height()))
                screen.blit(end_background, (0, 0))
                pygame.display.flip()
                pygame.time.wait(3000)
                game_states.set_state(States.END)

            # 检测游戏时间
            elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

            # 清屏
            background_image = pygame.image.load('images/background.jpg')  # 加载背景图像
            background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))
            screen.blit(background_image, (0, 0))  # 绘制背景图像

            # 绘制图像
            audio_image.draw(screen)
            control_image.draw(screen)
            random_image.draw(screen)

            # 绘制游戏时间
            time_text = font_small.render(f"Time: {int(elapsed_time)}s", True, (255, 255, 255))
            screen.blit(time_text, (10, 10))

            # 检测游戏结束条件
            game_over_text = collision_detector.detect_game_over(elapsed_time)
            if game_over_text:
                if game_over_text == "Warrior Win!":
                    end_background = pygame.transform.scale(warriorwin_image, (screen.get_width(), screen.get_height()))
                else:
                    end_background = pygame.transform.scale(guardwin_image, (screen.get_width(), screen.get_height()))
                screen.blit(end_background, (0, 0))
                pygame.display.flip()
                pygame.time.wait(3000)
                game_states.set_state(States.END)
            else:
                # 更新屏幕
                pygame.display.flip()

        elif game_states.get_state() == States.END:
            end_background = pygame.transform.scale(pygame.image.load('images/begin_image.jpg'),
                                                    (screen.get_width(), screen.get_height()))
            screen.blit(end_background, (0, 0))
            play_button_2.draw(screen)
            pygame.display.flip()

            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        waiting = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        waiting = False
                        game_states.set_state(States.INIT)
                        # 重新设置 control_image 和 random_image 的位置
                        control_image.reset_position()
                        while True:
                            random_image.x = random.randint(0, screen.get_width() - random_image.width)
                            random_image.y = random.randint(0, screen.get_height() - random_image.height)
                            random_rect = pygame.Rect(random_image.x, random_image.y, random_image.width,
                                                      random_image.height)
                            control_rect = pygame.Rect(control_image.x, control_image.y, control_image.width,
                                                       control_image.height)
                            if not random_rect.colliderect(control_rect):
                                break
                        # 重新设置游戏时间
                        start_time = pygame.time.get_ticks()
        clock.tick(60)

    # 关闭资源
    audio_image.close()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()