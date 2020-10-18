import pygame.font


class Button:
    def __init__(self, ai_settings, screen, msg, **kwargs):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性值
        self.width, self.height = ai_settings.bt_width, ai_settings.bt_height
        self.button_color = (123, 139, 111)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect对象， 并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.set_position(kwargs)

        # 按钮的标签只需要创建一次
        self.msg_image = None
        self.msg_image_rect = None
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制一个用颜色填充的按钮，再绘制文本"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def set_position(self, kwargs):
        """确定按钮在屏幕上的位置"""

        # 特判以屏幕中心为参照点的位置信息
        if len(kwargs) == 1:
            self.rect.center = self.screen_rect.center
            return

        for kw in kwargs:
            pos1 = ''.join(['self.rect.', kw])
            pos2 = ''.join(['self.screen_rect.', kwargs[kw][0]])
            p = compile(''.join([pos1, '=', pos2, kwargs[kw][1]]), '', 'exec')
            exec(p)

    # TODO(Tomspiano): add AI button
    '''
    def set_button_lower_left(self):
        """将按钮位置和字体设置为左下"""
        self.rect.bottom = self.screen_rect.bottom - 10
        self.rect.left = self.screen_rect.left + 10
        self.msg_image_rect.center = self.rect.center
    '''