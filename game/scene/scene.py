from game.ui.ui_manager import UIManager


class Scene:
    """
    游戏场景基类

    所有游戏场景都应该继承这个类
    """
    def __init__(self, scene_manager):
        self.scene_manager = scene_manager
        # 每个场景都自动注册 UI 管理器
        self.ui_manager = UIManager()

    def initialize(self):
        """
        初始化场景
        :return:
        """
        pass


    def handle_event(self, event):
        """
        处理场景的事件操作
        :param event:
        :return:
        """
        return False


    def update(self,delta_time):
        """
        更新场景
        :return:
        """
        self.ui_manager.update(delta_time)
        pass

    def render(self, screen):
        """
        渲染场景
        :return:
        """
        pass

    def destroy(self):
        """
        销毁场景
        :return:
        """
        self.ui_manager.destroy()
        pass