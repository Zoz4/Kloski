class Settings:
    """储存Kloski的所有设置的类"""

    def __init__(self):
        """ 初始化游戏设置 """
        self.fps = 300

        # 背景颜色
        self.bg_color = (230, 230, 230)
        # 数字方块颜色
        self.db_color = '#6485A7'
        # 空白方块颜色
        self.wb_color = '#FFFFFF'

        # 数字棋盘的形状和数字方块的大小
        self.shape = 3
        self.db_size = 200
        # 数字棋盘外白边的距离
        self.margin = 50

        # 数字方块间的间隔
        self.db_spacing = 20
        # 数字方块内数字内嵌的位置
        self.db_padding = 40

        # 屏幕大小
        self.screen_width = self.shape * (self.db_size + self.db_spacing) + self.db_spacing + 2 * self.margin
        self.screen_height = self.shape * (self.db_size + self.db_spacing) + self.db_spacing + 2 * self.margin

        # 按钮间的间隔
        self.bt_spacing = 20
        # 按钮大小
        self.bt_width = 150
        self.bt_height = 50
        # 按钮在屏幕上的位置
        self.play_button = {'center': 'center'}
        self.reset_button = {'bottom': ('bottom', '-10'), 'right': ('right', '-10')}
        self.new_button = {'bottom': ('bottom', '-10'), 'right': ('right', str(-10 - self.bt_width - self.bt_spacing))}

        # 答案文件路径
        self.ans_file_path = './game_data/123456780.json'
