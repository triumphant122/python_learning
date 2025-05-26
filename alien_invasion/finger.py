import pygame
class Finger:
    """管理人物图像的类"""
    def __init__(self,ai_game):
        self.screen = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形。
        self.image = pygame.image.load('image/finger.bmp')