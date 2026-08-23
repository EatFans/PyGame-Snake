import pygame

from game.audio_manager import AudioManager
from game.scene.game_scene import GameScene
from game.scene.scene import Scene
from game.ui.game_background_ui import GameBackGroundUI
from game.ui.game_start_menu_ui import GameStartMenuUI
from game.ui.game_title_ui import GameTitleUI
from game.utils.logger import Logger


class MainMenuScene(Scene):
    """
    游戏主菜单场景
    """

    def __init__(self, scene_manager):
        super().__init__(scene_manager)


    def initialize(self):

        Logger.info("游戏主菜单场景开始加载...")

        # 注册游戏背景UI
        self.ui_manager.register(
            GameBackGroundUI(),
            0
        )

        # 注册游戏标题UI
        self.ui_manager.register(
            GameTitleUI(),
            10
        )

        # 注册开始菜单UI
        self.ui_manager.register(
            GameStartMenuUI(
                self.start_game,
                self.exit_game
            ),
            10
        )

        # 开始播放背景音乐
        AudioManager.play_music(
            "assets/audio/background_bgm.wav",
            loops=-1,
            volume=0.5
        )
        Logger.info("开始播放游戏背景音乐")

        Logger.info("游戏主菜单场景加载完成")

        pass

    def handle_event(self, event):
        """
        监听处理本场景事件
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

    def destroy(self):
        """
        销毁场景
        :return:
        """
        self.ui_manager.destroy()

    def start_game(self):
        """
        开始游戏按钮被点击后
        :return:
        """
        Logger.info("开始游戏按钮被点击")
        Logger.debug("准备跳转到游戏主场景中...")
        self.scene_manager.change_scene(GameScene())

    def exit_game(self):
        """
        退出游戏
        :return:
        """
        Logger.info("正在退出游戏")
        pygame.event.post(
            pygame.event.Event(pygame.QUIT)
        )

