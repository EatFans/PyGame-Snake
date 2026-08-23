from game.ui.game_button_ui import GameButton
from game.ui.ui import UI
from game.utils.logger import Logger


class GameStartMenuUI(UI):
    """
    游戏开始菜单UI
    """

    def __init__(
            self,
            on_start_button_click=None,
            on_exit_button_click=None
    ):
        super().__init__(layer=10)
        self.buttons = []
        # 当开始按钮被点击后的指针函数
        self.on_start_button_click = on_start_button_click
        self.on_exit_button_click = on_exit_button_click

    def initialize(self):
        """
        初始化游戏开始菜单UI
        :return:
        """
        Logger.info("游戏开始菜单UI加载中...")
        start_button = GameButton(
            x=500,
            y=400,
            width=280,
            height=70,
            text="开始游戏",
            on_click=self.on_start_button_click
        )
        start_button.initialize()
        self.buttons.append(start_button)

        exit_button =  GameButton(
            x = 500,
            y = 490,
            width=280,
            height=70,
            on_click=self.on_exit_button_click
        )
        exit_button.initialize()
        self.buttons.append(exit_button)
        Logger.info("游戏开始菜单UI加载成功")


    def handle_event(self, event):
        """
        处理按钮事件
        :param event:
        :return:
        """

        for button in reversed(self.buttons):
            if button.handle_event(event):
                return True
        return False

    def update(self, delta_time):
        """
        更新菜单按钮
        :param delta_time:
        :return:
        """
        for button in self.buttons:
            button.update(delta_time)

    def render(self, screen):
        """
        渲染菜单
        :param screen:
        :return:
        """
        for button in self.buttons:
            button.render(screen)

    def destroy(self):
        """
        销毁菜单
        :return:
        """
        for button in self.buttons:
            button.destroy()

