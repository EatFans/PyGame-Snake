import pygame

from game.config import GameConfig
from game.ui.ui import UI
from game.utils.logger import Logger


class GameBackGroundUI(UI):
    """
    游戏主要背景图UI
    """

    def __init__(self):
        super().__init__(layer=0)

        self.image = None
        self.rect = None

    def initialize(self):
        Logger.info("游戏背景图UI开始加载...")
        # 加载背景图片
        self.image = pygame.image.load(
            "assets/images/background.png"
        ).convert()

        # 缩放到游戏窗口大小
        self.image = pygame.transform.smoothscale(
            self.image,
            (
                GameConfig.WIDTH,
                GameConfig.HEIGHT
            )
        )
        # 获取背景图片矩形
        self.rect = self.image.get_rect(
            topleft=(0, 0)
        )

        Logger.info("游戏背景图UI加载成功")


    def handle_event(self, event):
        pass

    def update(self, delta_time):
        pass

    def render(self, screen):
        if self.image is not None:
            screen.blit(
                self.image,
                self.rect
            )

    def destroy(self):
        self.image = None
        self.rect = None