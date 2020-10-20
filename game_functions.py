import os
from PIL import Image
import random
import sys
import pygame
import numpy as np
import time

COUNT_TIME = pygame.USEREVENT + 1
pygame.time.set_timer(COUNT_TIME, 1000)

src_path = './resources/images'
dst_path = './resources/puzzle'

TOTAL = 35


def prepare(src, dst):
    def select_image(root):
        images = os.listdir(root)
        img = images[random.randint(0, TOTAL - 1)]
        path = os.path.join(root, img)
        return Image.open(path)

    def cut_and_save(img, root):
        w, _ = img.size
        sub_w = w // 3

        for i in range(3):
            for j in range(3):
                idx = 3 * i + j + 1
                box = (j * sub_w, i * sub_w, (j + 1) * sub_w, (i + 1) * sub_w)
                img.crop(box).save(''.join([root, '/{}.png'.format(idx)]))

    image = select_image(src)
    cut_and_save(image, dst)


def clear_cache():
    flist = os.listdir(dst_path)
    for f in flist:
        if f == '.gitignore':
            continue
        path = os.path.join(dst_path, f)
        os.remove(path)


def check_events(ai_settings, screen, stats, blocks,
                 play_button, reset_button, new_button, guide_button,
                 timepiece, step_record):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
                event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            clear_cache()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(stats, event, blocks)
            step_record.prep_step()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, blocks, play_button, timepiece, step_record, mouse_x, mouse_y)
            check_reset_button(stats, blocks, reset_button, timepiece, step_record, mouse_x, mouse_y)
            check_new_button(stats, blocks, new_button, timepiece, step_record, mouse_x, mouse_y)
            if check_guide_button(ai_settings, screen, stats, blocks,
                               play_button, [reset_button, new_button], guide_button,
                               timepiece, step_record, mouse_x, mouse_y):
                pygame.event.clear()
        elif event.type == COUNT_TIME and stats.game_active:
            stats.time += 1
            timepiece.prep_time()


def check_keydown_event(stats, event, blocks):
    """响应按键"""

    def check_swap(stats):
        stats.step += 1
#        if stats.step == blocks.step:
#            blocks.swap_blocks()

    if event.key == pygame.K_w:
        if blocks.move('w'):
            check_swap(stats)
    elif event.key == pygame.K_s:
        if blocks.move('s'):
            check_swap(stats)
    elif event.key == pygame.K_a:
        if blocks.move('a'):
            check_swap(stats)
    elif event.key == pygame.K_d:
        if blocks.move('d'):
            check_swap(stats)


def check_win(blocks):
    """判断是否恢复"""
    return blocks.status == blocks.goal


def check_play_button(stats, blocks, play_button, timepiece, step_record, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        prepare(src_path, dst_path)
        blocks.break_order()
        stats.game_active = True
        timepiece.prep_time()
        step_record.prep_step()


def check_reset_button(stats, blocks, reset_button, timepiece, step_record, mouse_x, mouse_y):
    """在玩家单击Reset按钮时重新开始游戏"""
    button_clicked = reset_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and stats.game_active:
        stats.reset_stats()
        blocks.reset_stats()
        timepiece.prep_time()
        step_record.prep_step()


def check_new_button(stats, blocks, new_button, timepiece, step_record, mouse_x, mouse_y):
    """在玩家单击New按钮时开始新游戏"""
    button_clicked = new_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and stats.game_active:
        stats.reset_stats()
        prepare(src_path, dst_path)
        blocks.break_order()
        timepiece.prep_time()
        step_record.prep_step()


def check_guide_button(ai_settings, screen, stats, blocks,
                       play_button, menu_buttons, guide_button,
                       timepiece, step_record, mouse_x, mouse_y):
    button_clicked = guide_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and stats.game_active:
        stats.game_show_guide = True
        ans = blocks.ans()
        cur_status_matrix = np.copy(blocks.status_matrix)
        cur_null_digit_no = blocks.null_digit_no
        cur_status = blocks.status[:]

        menu_buttons.append(guide_button)
        for op in ans:
            blocks.move(op)
            update_screen(ai_settings, screen, stats, blocks,
                          play_button, menu_buttons,
                          timepiece, step_record)
            time.sleep(0.5)

        blocks.null_digit_no = cur_null_digit_no
        blocks.status = cur_status[:]
        blocks.status_matrix = np.copy(cur_status_matrix)
        time.sleep(1)
        stats.game_show_guide = False
        update_screen(ai_settings, screen, stats, blocks,
                      play_button, menu_buttons,
                      timepiece, step_record)
        return True
    return False



def check_min_time(stats, timepiece):
    """检查是否产生了新的最少用时"""
    if stats.time < stats.min_time:
        stats.min_time = stats.time
        timepiece.prep_min_time()


def update_screen(ai_settings, screen, stats, blocks, play_button, menu_buttons, timepiece, step_record):
    """更新屏幕上的图像，并切换到新图像"""
    # 设置背景颜色
    screen.fill(ai_settings.bg_color)
    # 绘制数字方块
    blocks.blitme()
    # 显示计时
    # 如果游戏处于非活动状态,就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
        timepiece.show_time()
        step_record.show_step()
    else:
        if not stats.game_show_guide:
            for button in menu_buttons:
                button.draw_button()
            timepiece.show_time()
            step_record.show_step()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
