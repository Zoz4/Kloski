import pygame
import random
import numpy as np

class DigitalBlocks():
    def __init__(self, ai_settings, screen):
        '''初始化数字方块并设置其初始位置'''
        self.ai_settings = ai_settings
        self.screen = screen
        self.status = list(range(1, ai_settings.shape**2+1))
        self.null_digit = -1
        self.status_matrix = np.array(self.status).reshape((ai_settings.shape, ai_settings.shape))

    def blitme(self):
        for i in range(self.ai_settings.shape):
            for j in range(self.ai_settings.shape):
                digit = self.status_matrix[i][j]
                if digit is not 0:
                    color = pygame.Color(self.ai_settings.db_color)
                else:
                    color = pygame.Color(self.ai_settings.wb_color)

                x = self.ai_settings.margin*(j+1)+j*self.ai_settings.db_size
                y = self.ai_settings.margin*(i+1)+i*self.ai_settings.db_size
                pygame.draw.rect(self.screen, color, (x, y, self.ai_settings.db_size, self.ai_settings.db_size))
                if digit is not 0:
                    front_size = self.ai_settings.db_size - self.ai_settings.db_padding
                    font = pygame.font.Font(None, front_size)
                    font_width, font_height = font.size(str(digit))
                    self.screen.blit(font.render(str(digit), True, (255,255,255)),
                    (x+(self.ai_settings.db_size-font_width)/2, y + (self.ai_settings.db_size-font_height)/2+5))