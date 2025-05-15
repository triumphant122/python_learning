import sys  ## 导入sys模块，用来退出游戏
import pygame  ## 导入pygame
from settings import Setting

class AlienInvasion:  ## 创建类
    """管理游戏资源和行为的类"""

    def __init__(self):  
        """初始化游戏并创建游戏资源"""
        pygame.init()  ## 初始化pygame

        self.settings = Setting()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))  ## screen是之前创建类的一个属性，对象是一个surface；设置一个1200*800的屏幕赋值给该属性
        pygame.display.set_caption("Alien Invasion")

        # 设置背景色
        # self.bg_color = (230,230,230)

    def run_game(self):
        """开始游戏主循环"""
        while True:
            # 监视键盘和鼠标事件。
            for event in pygame.event.get():  ## 该行代码返回一个列表
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环是都重绘屏幕
            self.screen.fill(self.settings.bg_color)

            # 让最近绘制的屏幕可见。
            pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()
