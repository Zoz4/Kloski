import sys
import pygame

COUNT_TIME = pygame.USEREVENT + 1
pygame.time.set_timer(COUNT_TIME, 1000)

def check_events(stats, blocks, play_button, reset_button, timepiece, step_record):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
                event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(stats, event, blocks)
            step_record.prep_step()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, blocks, play_button, timepiece, step_record, mouse_x, mouse_y)
            check_reset_button(stats, blocks, reset_button, timepiece, step_record, mouse_x, mouse_y)
        elif event.type == COUNT_TIME and stats.game_active:
            stats.time += 1
            timepiece.prep_time()

def check_keydown_event(stats, event, blocks):
    '''响应按键'''
    if event.key == pygame.K_w:
        if(blocks.move('w')):
            stats.step += 1
    elif event.key == pygame.K_s:
        if(blocks.move('s')):
            stats.step += 1
    elif event.key == pygame.K_a:
        if(blocks.move('a')):
            stats.step += 1
    elif event.key == pygame.K_d:
        if(blocks.move('d')):
            stats.step += 1
def check_win(blocks):
    """判断是否恢复"""
    return blocks.status == blocks.goal


def check_play_button(stats, blocks, play_button, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
def check_play_button(stats, blocks, play_button, timepiece, step_record, mouse_x, mouse_y):
    '''在玩家单击Play按钮时开始新游戏'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        blocks.break_order()
        stats.game_active = True
        timepiece.prep_time()
        step_record.prep_step()
def check_reset_button(stats, blocks, reset_button, timepiece, step_record, mouse_x, mouse_y):
    button_clicked = reset_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and stats.game_active:
        blocks.break_order()
        stats.reset_stats()
        timepiece.prep_time()
        step_record.prep_step()



def update_screen(ai_settings, screen, stats, blocks, play_button):
    """更新屏幕上的图像，并切换到新图像"""

def check_min_time(stats, timepiece):
    '''检查是否产生了新的最少用时'''
    if stats.time < stats.min_time:
        stats.min_time = stats.time
        timepiece.prep_min_time()
def update_screen(ai_settings, screen, stats, blocks, play_button, reset_button, timepiece, step_record):
    '''更新屏幕上的图像，并切换到新图像'''
    # 设置背景颜色
    screen.fill(ai_settings.bg_color)
    # 绘制数字方块
    blocks.blitme()
    # 显示计时
    # 如果游戏处于非活动状态,就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    else:
        reset_button.draw_button()

    timepiece.show_time()
    step_record.show_step()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
