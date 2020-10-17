import  sys
import  pygame

from settings import Settings
from  digital_blocks import DigitalBlocks
import  game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Kloski")
    blocks = DigitalBlocks(ai_settings,screen)
    
    fclock = pygame.time.Clock()

    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events()
        # 设置背景颜色
        screen.fill(ai_settings.bg_color)
        # 让最近绘制的屏幕可见
        blocks.blitme()
        pygame.display.flip()

        fclock.tick(ai_settings.fps)

if __name__ == '__main__':
    run_game()

