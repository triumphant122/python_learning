import pygame
class Ship:
    """管理飞船的类"""
    def __init__(self,ai_game):  # 第二个实参，指向当前AlienInvasion实例的引用
        """初始化飞船并设置其初始位置。"""
        self.screen = ai_game.screen  ## 将屏幕赋值给Ship的一个属性.
        self.screen_rect = ai_game.screen.get_rect()  ## 使用get_rect()获取屏幕的属性rect，赋值给screen_rect.

        # 加载飞船图像并获取其外接矩形。
        self.image = pygame.image.load('image/ship.bmp')  ## 创建image属性，使用pygame.image.load('地址')来获取图片并赋值给image属性.
        self.rect = self.image.get_rect() ## 使用get_rect()方法获取图片的rect并赋值给属性rect.

        # 对于每艘新飞船，都将其放在屏幕底部中央。
        self.rect.midbottom = self.screen_rect.midbottom  ## 设置一个属性，将飞船放置在屏幕的底部中央.
    
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
