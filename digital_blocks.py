import pygame
import random
import numpy as np

class DigitalBlocks():
    def __init__(self, ai_settings, screen):
        '''初始化数字方块并设置其初始位置'''
        self.ai_settings = ai_settings
        self.screen = screen
        self.status = list(range(1, ai_settings.shape**2+1))
        self.status[ai_settings.shape**2-1] = 0
        self.goal = self.status[:]
        self.null_digit_no = ai_settings.shape**2
        self.status_matrix = np.array(self.status).reshape((ai_settings.shape, ai_settings.shape))

    def blitme(self):
        for i in range(self.ai_settings.shape):
            for j in range(self.ai_settings.shape):
                digit = self.status_matrix[i][j]
                if(digit != 0):
                    color = pygame.Color(self.ai_settings.db_color)
                else:
                    color = pygame.Color(self.ai_settings.wb_color)

                x = self.ai_settings.db_spacing*(j+1)+j*self.ai_settings.db_size
                y = self.ai_settings.db_spacing*(i+1)+i*self.ai_settings.db_size
                pygame.draw.rect(self.screen, color, (x, y, self.ai_settings.db_size, self.ai_settings.db_size))
                if (digit != 0):
                    front_size = self.ai_settings.db_size - self.ai_settings.db_padding
                    font = pygame.font.Font(None, front_size)
                    font_width, font_height = font.size(str(digit))
                    self.screen.blit(font.render(str(digit), True, (255, 255, 255)),
                    (x+(self.ai_settings.db_size-font_width)/2, y + (self.ai_settings.db_size-font_height)/2))

    def move(self, op):
        next = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        location = [[-1, -1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0],[2,1], [2, 2], [2, 2]]
        x,y = location[self.null_digit_no]
        nx = x+next[op][0]
        ny = y+next[op][1]
        if(nx < 0 or ny < 0 or nx > 2 or ny >2 ):
            return
        else:
            n_no = location.index([nx,ny])
            self.status_matrix[x][y], self.status_matrix[nx][ny] = \
            self.status_matrix[nx][ny], self.status_matrix[x][y]

            self.status[self.null_digit_no-1], self.status[n_no-1] = \
            self.status[n_no-1], self.status[self.null_digit_no-1]
            self.null_digit_no = n_no

    def win(self):
        if (self.status == self.goal):
            return True






