import pygame.font


class Timepiece:
    """显示计时的类"""

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示所有时间的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始计时图像
        self.time_image = None
        self.time_rect = None
        self.prep_time()
        self.min_time_image = None
        self.min_time_rect = None
        self.prep_min_time()

    def prep_time(self):
        """将所用时间转化为一幅渲染的图像"""
        time_str = str(self.stats.time) + 's'
        self.time_image = self.font.render(time_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.time_rect = self.time_image.get_rect()

        self.time_rect.right = self.screen_rect.right - 20
        self.time_rect.top = 20

    def prep_min_time(self):
        """将最少用时转换为图像"""
        min_time_str = 'Best Score: ' + str(self.stats.min_time)
        if self.stats.min_time != float('inf'):
            min_time_str += 's'
        self.min_time_image = self.font.render(min_time_str, True, self.text_color, self.ai_settings.bg_color)

        # 将最少用时放在屏幕顶部中央
        self.min_time_rect = self.min_time_image.get_rect()
        self.min_time_rect.centerx = self.screen_rect.centerx
        self.min_time_rect.top = self.time_rect.top

    def show_time(self):
        """在屏幕上显示计时"""
        self.screen.blit(self.time_image, self.time_rect)
        self.screen.blit(self.min_time_image, self.min_time_rect)
