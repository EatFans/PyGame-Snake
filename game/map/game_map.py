import pygame

from game.config import GameConfig


class GameMap:
    """
    游戏地图

    统一负责：
    地图区域定义
    地图边界
    网格坐标转换
    地图范围碰撞检查
    """

    def __init__(self):
        # 游戏区域矩形
        self.area_rect = pygame.Rect(
            GameConfig.AREA_X,
            GameConfig.AREA_Y,
            GameConfig.AREA_WIDTH,
            GameConfig.AREA_HEIGHT
        )

        # 每列竖线
        self.grid_x = [74, 147, 222, 297, 370, 444, 519, 594, 670, 748]
        # 每行横线
        self.grid_y = [68]

    def debug_render(self, screen):
        """
        调试渲染
        :param screen:
        :return:
        """
        # 绘制地图边界
        pygame.draw.rect(
            screen,
            (255,0,0),
            self.area_rect,
            2
        )

        # 绘制每一个网格
        grid_color = (255, 255, 255)
        # 绘制竖线
        for x in self.grid_x:
            pygame.draw.line(
                screen,
                grid_color,
                (
                    self.area_rect.x + x,
                    self.area_rect.y
                ),
                (
                    self.area_rect.x + x,
                    self.area_rect.bottom
                ),
                1
            )
        # 绘制横线
        for y in self.grid_y:
            pygame.draw.line(
                screen,
                grid_color,
                (
                    self.area_rect.x,
                    self.area_rect.y + y
                ),
                (
                    self.area_rect.right,
                    self.area_rect.y + y
                ),
                1
            )