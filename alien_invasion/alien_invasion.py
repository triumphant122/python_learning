import sys  ## 导入sys模块，用来退出游戏
import pygame  ## 导入pygame
from settings import Setting
from  ship import Ship 

class AlienInvasion:  ## 创建类
    """管理游戏资源和行为的类"""

    def __init__(self):  
        """初始化游戏并创建游戏资源"""
        pygame.init()  ## 初始化pygame

        self.settings = Setting()  ## 创建一个设置的实例并初始化Setting。
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))  ## screen是之前创建类的一个属性，对象是一个surface；设置一个1200*800的屏幕赋值给该属性
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self) ## 创建一个设置的实例并初始化Ship。

        # 设置背景色
        # self.bg_color = (230,230,230)

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            self._update_screen()
            # 每次循环是都重绘屏幕
    def _check_events(self):
        """响应按键和鼠标事件。"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                sys.exit()
    def _update_screen(self):
        """更新屏幕上的图像，并切换到最新绘制的屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()
    
if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()
