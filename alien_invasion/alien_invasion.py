import sys
import pygame
from ship import Ship
from alien import Alien
from settings import Settings
from pygame.sprite import Group
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))  # 屏幕对象
    pygame.display.set_caption("Alien Invasion")  # 字幕

    # play按钮
    play_button = Button(ai_settings, screen, "Play")

    ship = Ship(ai_settings, screen)  # 飞船

    alien = Alien(ai_settings, screen)  # 外星人

    # 子弹编组
    bullets = Group()

    # 外星人编组
    aliens = Group()

    # 绘制外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个用于存储游戏统计信息的实例，并创建计分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            # 更改飞船位置
            ship.update()

            # 所有子弹位置更新，并删除已消失的子弹(这里选择遍历副本，因为无法一边遍历一边删除)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens ,bullets)

            # 更新外星人群位置
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # 重绘屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()