import sys
import pygame


def check_keydown_event(event, blocks):
    '''响应按键'''
    if event.key == pygame.K_w:
        blocks.move(1)
    elif event.key == pygame.K_s:
        blocks.move(0)
    elif event.key == pygame.K_a:
        blocks.move(3)
    elif event.key == pygame.K_d:
        blocks.move(2)

def check_events(blocks):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, blocks)


def update_screen(ai_settings, screen, blocks):
    '''更新屏幕上的图像，并切换到新图像'''
    # 设置背景颜色
    screen.fill(ai_settings.bg_color)
    # 绘制数字方块
    blocks.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

