import pygame

import game_functions as gf
from button import Button
from digital_blocks import DigitalBlocks
from game_stats import GameStats
from settings import Settings
from step_record import StepRecord
from timepiece import Timepiece

description = """
    操作指南:
        w: 向上移动白块
        s: 向下移动白块
        a: 向左移动白块
        d: 向右移动白块

        q: 退出游戏
    
    如何开始：
        点击“Play”即可开始游戏
        
    游戏目标：
        移动白块，使所有方块回到正确位置，一起组成字母
"""
print(description)


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))

    stats = GameStats(ai_settings)
    timepiece = Timepiece(ai_settings, screen, stats)
    step_record = StepRecord(ai_settings, screen, stats)

    blocks = DigitalBlocks(ai_settings, screen)
    pygame.display.set_caption("Kloski")

    fclock = pygame.time.Clock()
    play_button = Button(ai_settings, screen, "Play", **ai_settings.play_button)
    reset_button = Button(ai_settings, screen, "Reset", **ai_settings.reset_button)
    new_button = Button(ai_settings, screen, "New", **ai_settings.new_button)
    guide_button = Button(ai_settings, screen, "Guide", **ai_settings.guide_button)

    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, blocks,
                        play_button, reset_button, new_button, guide_button,
                        timepiece, step_record)
        if stats.game_active:
            if gf.check_win(blocks):
                stats.game_active = False
                gf.check_min_time(stats, timepiece)

        gf.update_screen(ai_settings, screen, stats, blocks,
                         play_button, [reset_button, new_button, guide_button],
                         timepiece, step_record)
        fclock.tick(ai_settings.fps)


if __name__ == '__main__':
    run_game()
