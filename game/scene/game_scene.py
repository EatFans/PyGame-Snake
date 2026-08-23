from game.map.game_map import GameMap
from game.scene.scene import Scene
from game.ui.game_area_background_ui import GameAreaBackgroundUI
from game.utils.logger import Logger


class GameScene(Scene):
    """
    游戏主要场景
    """

    def __init__(self):
        super().__init__(None)
        self.map = None


    def initialize(self):
        Logger.info("游戏主要场景加载中...")

        # 注册游戏场景背景UI
        self.ui_manager.register(
            GameAreaBackgroundUI(),
            0
        )

        # 开始计算游戏地图
        self.map = GameMap()

        Logger.info("游戏主要场景加载完毕")


    def handle_event(self, event):
        """
        监听处理本场景时间
        :param event:
        :return:
        """
        return self.ui_manager.handle_event(event)

    def update(self,delta_time):
        """
        更新场景数据
        :param delta_time:
        :return:
        """
        self.ui_manager.update(delta_time)

    def render(self, screen):
        """
        绘制场景
        :param screen:
        :return:
        """
        self.ui_manager.render(screen)
        self.map.debug_render(screen)

    def destroy(self):
        """
        销毁场景
        :return:
        """
        self.ui_manager.destroy()