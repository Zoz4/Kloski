import sys
import pygame

COUNT_TIME = pygame.USEREVENT + 1
pygame.time.set_timer(COUNT_TIME, 1000)

def check_events(stats, blocks, play_button, timepiece):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, blocks)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, blocks, play_button, mouse_x, mouse_y)
        if event.type == COUNT_TIME and stats.game_active:
            stats.time += 1
            timepiece.prep_time()

def check_keydown_event(event, blocks):
    '''响应按键'''
    if event.key == pygame.K_w:
        blocks.move('w')
    elif event.key == pygame.K_s:
        blocks.move('s')
    elif event.key == pygame.K_a:
        blocks.move('a')
    elif event.key == pygame.K_d:
        blocks.move('d')

def check_win(blocks):
    '''判断是否恢复'''
    return  blocks.status == blocks.goal

def check_play_button(stats, blocks, play_button, mouse_x, mouse_y):
    '''在玩家单击Play按钮时开始新游戏'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        blocks.break_order()
        stats.game_active = True

def check_min_time(stats, timepiece):
    '''检查是否产生了新的最少用时'''
    if stats.time < stats.min_time:
        stats.min_time = stats.time
        timepiece.prep_min_time()
def update_screen(ai_settings, screen, stats, blocks, play_button, timepiece):
    '''更新屏幕上的图像，并切换到新图像'''
    # 设置背景颜色
    screen.fill(ai_settings.bg_color)
    # 绘制数字方块
    blocks.blitme()
    # 显示计时
    timepiece.show_time()
    # 如果游戏处于非活动状态,就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

