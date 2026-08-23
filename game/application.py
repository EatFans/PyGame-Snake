import pygame

from game.audio_manager import AudioManager
from game.config import GameConfig
from game.scene.main_menu_scene import MainMenuScene
from game.scene.scene_manager import SceneManager
from game.utils.logger import Logger


class GameApplication:
    """
    游戏应用程序

    负责整个游戏的生命周期
    1、初始化
    2、创建窗口
    3、游戏循环
    4、处理事件
    5、更新游戏
    6、渲染游戏
    7、退出游戏
    """

    def __init__(self):
        # 游戏程序是否运行
        self.running = False
        # 游戏窗口
        self.screen = None
        # 游戏时钟
        self.clock = None
        # FPS
        self.fps = GameConfig.FPS

        # 游戏场景管理器
        self.scene_manager = SceneManager()

    def initialize(self):
        """
        初始化游戏程序
        :return:
        """
        Logger.info("游戏程序开始初始化加载...")
        pygame.init()
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(
            (
                GameConfig.WIDTH,
                GameConfig.HEIGHT
            )
        )
        # 设置窗口标题
        pygame.display.set_caption("贪吃蛇")
        self.clock = pygame.time.Clock()

        Logger.info("游戏窗口创建成功")

        # 初始化全局音频管理器
        AudioManager.initialize()
        Logger.info("游戏全局音频管理器初始化成功")

        # 设置游戏程序加载后默认的场景(主菜单场景）
        Logger.info("开始加载游戏默认场景（主菜单场景）")
        self.scene_manager.change_scene(MainMenuScene(self.scene_manager))

        Logger.info("游戏初始化加载完毕")


    def start(self):
        """
        启动游戏程序
        :return:
        """
        self.initialize()
        self.running = True
        self.run()
        self.shutdown()

    def run(self):
        """
        运行游戏主循环
        :return:
        """
        while self.running:
            # 计算 Delta Time 增量时间
            delta_time = self.clock.tick(self.fps) / 1000.0
            # 处理事件
            self.handle_event()
            # 执行场景切换
            self.scene_manager.process_scene_change()
            # 更新游戏
            self.update(delta_time)
            # 渲染游戏窗口游戏画面
            self.render()


    def handle_event(self):
        """
        处理游戏程序事件
        :return:
        """

        for event in pygame.event.get():
            # 处理场景管理器场景的事件
            self.scene_manager.handle_event(event)

            # 处理开发者工具调试

            # 点击窗口关闭按钮
            if event.type == pygame.QUIT:
                self.quit()


    def update(self, delta_time):
        # 处理场景管理器场景的更新
        self.scene_manager.update(delta_time)

    def render(self):
        """
        渲染游戏
        :return:
        """
        # 渲染场景管理器场景
        self.scene_manager.render(self.screen)
        # 刷新屏幕
        pygame.display.flip()


    def quit(self):
        """
        请求退出游戏
        """
        self.running = False
        self.scene_manager.destroy()

    def shutdown(self):
        """
        游戏退出后的资源释放
        """
        pygame.quit()
