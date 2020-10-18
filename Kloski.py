import sys
import pygame

from settings import Settings
from digital_blocks import DigitalBlocks
from button import Button
from game_stats import GameStats
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    blocks = DigitalBlocks(ai_settings, screen)
    pygame.display.set_caption("Kloski")
    
    fclock = pygame.time.Clock()
    play_button = Button(ai_settings, screen, "Play")

    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(stats, blocks, play_button)
        if stats.game_active:
            if(gf.check_win(blocks)):
                stats.game_active = False
        gf.update_screen(ai_settings, screen, stats, blocks, play_button)
        fclock.tick(ai_settings.fps)

if __name__ == '__main__':
    run_game()

