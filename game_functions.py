import sys
import pygame


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

def check_events(stats, blocks, play_button):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, blocks)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, blocks, play_button, mouse_x, mouse_y)
def check_win(blocks):
    '''判断是否恢复'''
    return  blocks.status == blocks.goal

def check_play_button(stats, blocks, play_button, mouse_x, mouse_y):
    '''在玩家单击Play按钮时开始新游戏'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        blocks.break_order()
        stats.game_active = True

def update_screen(ai_settings, screen, stats, blocks, play_button):
    '''更新屏幕上的图像，并切换到新图像'''
    # 设置背景颜色
    screen.fill(ai_settings.bg_color)
    # 绘制数字方块
    blocks.blitme()
    # 如果游戏处于非活动状态,就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

