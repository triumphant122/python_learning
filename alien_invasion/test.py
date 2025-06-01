import sys
import pygame  ## 导入pygame
from settings import Setting
from finger import Finger

class AlienInvasion:
    """创建练习的类，管理练习的资源"""
    def __init__(self):
        """初始化"""
        pygame.init()
        self.settings = Setting()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Test 1")

        self.finger = Finger(self)

    def run_game(self):
        """主循环"""
        while True:
            self._check_events()
            self._update_screen()  

    def _check_events(self):
        """响应鼠标键盘"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    def _update_screen(self):
        """更新屏幕上的画，并切换到最新绘制的屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.finger.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
