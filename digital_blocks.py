import pygame
import random
import os
import json
import numpy as np

img_path = './resources/puzzle'


class DigitalBlocks:
    def __init__(self, ai_settings, screen):
        """初始化图片方块并设置其初始位置"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.status = list(range(1, ai_settings.shape**2 + 1))
        self.status[ai_settings.shape**2 - 1] = 0
        self.goal = self.status[:]
        self.null_digit_no = ai_settings.shape**2
        self.status_matrix = np.array(self.status).reshape((ai_settings.shape, ai_settings.shape))
        self.null_digit_no_cache = None
        self.status_cache = None

    def blitme(self):
        """在指定位置加载图片方块"""
        for i in range(self.ai_settings.shape):
            for j in range(self.ai_settings.shape):
                x = self.ai_settings.db_spacing * (j + 1) + j * self.ai_settings.db_size + self.ai_settings.margin
                y = self.ai_settings.db_spacing * (i + 1) + i * self.ai_settings.db_size + self.ai_settings.margin

                if len(os.listdir(img_path)) == 1:
                    color = pygame.Color(self.ai_settings.wb_color)
                    pygame.draw.rect(self.screen, color, (x, y, self.ai_settings.db_size, self.ai_settings.db_size))
                    continue

                digit = self.status_matrix[i][j]
                if digit == 0:
                    color = pygame.Color(self.ai_settings.wb_color)
                    pygame.draw.rect(self.screen, color, (x, y, self.ai_settings.db_size, self.ai_settings.db_size))
                else:
                    img = pygame.image.load(''.join([img_path, '/{}.png'.format(digit)])).convert()
                    img = pygame.transform.smoothscale(img, (self.ai_settings.db_size, self.ai_settings.db_size))
                    self.screen.blit(img, (x, y))

    def move(self, op):
        """移动图片方块"""
        _next = {'s': [-1, 0], 'w': [1, 0], 'd': [0, -1], 'a': [0, 1]}
        location = [[-1, -1]]
        for i in range(self.ai_settings.shape):
            for j in range(self.ai_settings.shape):
                location.append([i, j])
        x, y = location[self.null_digit_no]
        nx = x + _next[op][0]
        ny = y + _next[op][1]
        if nx < 0 or ny < 0 or nx > self.ai_settings.shape - 1 or ny > self.ai_settings.shape - 1:
            return False
        else:
            n_no = location.index([nx, ny])
            self.status_matrix[x][y], self.status_matrix[nx][ny] = \
                self.status_matrix[nx][ny], self.status_matrix[x][y]

            self.status[self.null_digit_no - 1], self.status[n_no - 1] = \
                self.status[n_no - 1], self.status[self.null_digit_no - 1]
            self.null_digit_no = n_no

            return True

    def break_order(self):
        cnt = 0
        operations = ['w', 's', 'a', 'd']
        while cnt < 100:
            operation = random.choice(operations)
            self.move(operation)
            cnt += 1
        self.status_cache = np.copy(self.status_matrix)
        self.null_digit_no_cache = self.null_digit_no

    def ans(self):
        with open(self.ai_settings.ans_file_path, 'r') as json_file:
            ans_dict = json.load(json_file)
        status_str = ''
        for i in self.status:
            status_str += str(i)

        return ans_dict[status_str][::-1]

    def reset_stats(self):
        self.status_matrix = np.copy(self.status_cache)
        self.null_digit_no = self.null_digit_no_cache
