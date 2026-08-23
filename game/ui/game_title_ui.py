import pygame

from game.config import GameConfig
from game.ui.ui import UI
from game.utils.logger import Logger


class GameTitleUI(UI):
    """
    游戏菜单标题 UI
    """

    def __init__(self):
        super().__init__(layer=10)

        self.image = None
        self.rect = None

    def initialize(self):
        Logger.info("游戏标题UI开始加载...")
        # 通过pygame加载图片素材
        image = pygame.image.load(
            "assets/images/game_logo.png"
        ).convert_alpha()

        # 根据游戏窗口大小计算 LOGO 最大显示尺寸
        max_width = int(GameConfig.WIDTH * 0.70)
        max_height = int(GameConfig.HEIGHT * 0.30)

        image_width, image_height = image.get_size()

        # 计算缩放比例
        scale = min(
            max_width / image_width,
            max_height / image_height
        )

        # 计算缩放后的图片尺寸
        new_width = int(image_width * scale)
        new_height = int(image_height * scale)

        self.image = pygame.transform.smoothscale(image, (new_width, new_height))

        # 设置LOGO位置
        self.rect = self.image.get_rect()
        self.rect.centerx = GameConfig.WIDTH // 2
        self.rect.top = 100

        Logger.info("游戏标题UI加载成功")

    def handle_event(self, event):
        pass

    def update(self, delta_time):
        pass

    def render(self, screen):
        """
        渲染
        :param screen:
        :return:
        """
        if not self.visible:
            return

        screen.blit(
            self.image,
            self.rect
        )

    def destroy(self):
        self.image = None
        self.rect = None