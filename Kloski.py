import os
import pygame
import random
from PIL import Image

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

UPPER = 20
TOTAL = 35

src_path = './resources/images'
dst_path = './resources/puzzle'


def prepare(src, dst):
    def generate_step():
        return random.randint(0, UPPER)

    def select_block():
        return random.randint(1, 9)

    def generate_swap():
        a = select_block()
        while True:
            b = select_block()
            if b != a:
                return [a, b]

    def select_image(root):
        images = os.listdir(root)
        img = images[random.randint(0, TOTAL - 1)]
        path = os.path.join(root, img)
        return Image.open(path)

    def cut_and_save(img, root):
        w, _ = img.size
        sub_w = w // 3

        blank = select_block()

        for i in range(3):
            for j in range(3):
                idx = 3 * i + j + 1
                box = (j * sub_w, i * sub_w, (j + 1) * sub_w, (i + 1) * sub_w)
                img.crop(box).save(''.join([root, '/{}.png'.format(idx)]))

        return blank

    image = select_image(src)
    index = cut_and_save(image, dst)

    return [generate_step(), generate_swap(), index]


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
    play_button = Button(ai_settings, screen, "Play")
    reset_button = Button(ai_settings, screen, "Reset")
    reset_button.set_button_lower_right()
    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(stats, blocks, play_button, reset_button, timepiece, step_record)
        if stats.game_active:
            if gf.check_win(blocks):
                stats.game_active = False
                gf.check_min_time(stats, timepiece)

        gf.update_screen(ai_settings, screen, stats, blocks, play_button, reset_button, timepiece, step_record)
        fclock.tick(ai_settings.fps)


if __name__ == '__main__':
    prepare(src_path, dst_path)
    run_game()
