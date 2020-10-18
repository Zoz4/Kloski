import pygame
import random
import numpy as np
import json

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
        '''在指定位置绘制数字方块'''
        for i in range(self.ai_settings.shape):
            for j in range(self.ai_settings.shape):
                digit = self.status_matrix[i][j]
                if(digit != 0):
                    color = pygame.Color(self.ai_settings.db_color)
                else:
                    color = pygame.Color(self.ai_settings.wb_color)

                x = self.ai_settings.db_spacing*(j+1)+j*self.ai_settings.db_size+self.ai_settings.margin
                y = self.ai_settings.db_spacing*(i+1)+i*self.ai_settings.db_size+self.ai_settings.margin
                pygame.draw.rect(self.screen, color, (x, y, self.ai_settings.db_size, self.ai_settings.db_size))
                if (digit != 0):
                    front_size = self.ai_settings.db_size - self.ai_settings.db_padding
                    font = pygame.font.Font(None, front_size)
                    font_width, font_height = font.size(str(digit))
                    self.screen.blit(font.render(str(digit), True, (255, 255, 255)),
                    (x+(self.ai_settings.db_size-font_width)/2, y + (self.ai_settings.db_size-font_height)/2))

    def move(self, op):
        '''移动数字方块'''
        next = {'s':[-1, 0], 'w':[1, 0], 'd':[0, -1], 'a':[0, 1]}
        location = [[-1, -1]]
        for i in range(self.ai_settings.shape):
            for j in range(self.ai_settings.shape):
                location.append([i,j])
        x,y = location[self.null_digit_no]
        nx = x+next[op][0]
        ny = y+next[op][1]
        if(nx < 0 or ny < 0 or nx > self.ai_settings.shape-1 or ny >self.ai_settings.shape-1 ):
            return
        else:
            n_no = location.index([nx,ny])
            self.status_matrix[x][y], self.status_matrix[nx][ny] = \
            self.status_matrix[nx][ny], self.status_matrix[x][y]

            self.status[self.null_digit_no-1], self.status[n_no-1] = \
            self.status[n_no-1], self.status[self.null_digit_no-1]
            self.null_digit_no = n_no
    def break_order(self):
            cnt = 0
            operations = ['w', 's', 'a', 'd']
            while(cnt < 100):
                operation = random.choice(operations)
                self.move(operation)
                cnt += 1









