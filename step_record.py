import pygame.font


class StepRecord:
    """显示当前步数的类"""

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        # 显示步数的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始记录步数对象
        self.step_image = None
        self.step_rect = None
        self.prep_step()

    def prep_step(self):
        """将步数转换为一幅渲染的图像"""
        step_str = 'Step: ' + str(self.stats.step)
        self.step_image = self.font.render(step_str, True, self.text_color, self.ai_settings.bg_color)

        # 将步数放在左上角
        self.step_rect = self.step_image.get_rect()

        self.step_rect.left = self.screen_rect.left + 20
        self.step_rect.top = 20

    def show_step(self):
        """在屏幕上显示步数"""
        self.screen.blit(self.step_image, self.step_rect)
