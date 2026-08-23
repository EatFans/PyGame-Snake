import pygame

from game.scene.scene import Scene
from game.utils.logger import Logger


class SceneManager:
    """
    游戏场景管理器

    替游戏程序统一管理游戏中不同场景，管理当前场景、切换场景、调整场景生命周期
    """

    def __init__(self):
        self.current_scene = None
        self.pending_scene = None



    def change_scene(self, scene):
        """
        请求切换场景
        注意：
        这里不立即执行切换。
        而是把场景放入 pending_scene，
        等当前帧事件处理结束之后再真正切换。
        """
        if scene is None:
            Logger.warning(
                "尝试切换到空场景",
                "SceneManager"
            )
            return
        Logger.debug(
            f"请求切换场景: "
            f"{self._get_scene_name(scene)}",
            "SceneManager"
        )
        self.pending_scene = scene

    def process_scene_change(self):
        """
        执行待处理的场景切换
        应该在事件处理完成之后调用。
        """
        if self.pending_scene is None:
            return

        new_scene = self.pending_scene
        # 清空待处理场景
        self.pending_scene = None
        # ==========================================
        # 销毁旧场景
        # ==========================================
        if self.current_scene is not None:
            Logger.debug(
                f"销毁场景: "
                f"{self._get_scene_name(self.current_scene)}",
                "SceneManager"
            )
            self.current_scene.destroy()
        # ==========================================
        # 设置新场景
        # ==========================================
        self.current_scene = new_scene
        Logger.info(
            f"切换到场景: "
            f"{self._get_scene_name(self.current_scene)}",
            "SceneManager"
        )
        # ==========================================
        # 初始化新场景
        # ==========================================
        self.current_scene.initialize()
        Logger.info(
            f"场景加载完成: "
            f"{self._get_scene_name(self.current_scene)}",
            "SceneManager"
        )

    def handle_event(self, event):
        """
        处理场景事件
        :param event:
        :return:
        """
        if self.current_scene is None:
            return False
        return self.current_scene.handle_event(event)

    def update(self, delta_time):
        """
        更新场景
        :param delta_time:
        :return:
        """
        if self.current_scene is not None:
            self.current_scene.update(delta_time)

    def render(self,screen):
        """
        渲染场景
        :param screen:
        :return:
        """
        if self.current_scene is not None:
            self.current_scene.render(screen)


    def destroy(self):
        """
        销毁场景管理器
        """
        if self.current_scene is not None:
            Logger.debug(
                f"销毁当前场景: "
                f"{self._get_scene_name(self.current_scene)}",
                "SceneManager"
            )
            self.current_scene.destroy()
            self.current_scene = None
        self.pending_scene = None

    def get_current_scene(self):
        """
        获取当前场景
        """
        return self.current_scene

    def is_current_scene(self, scene_type):
        """
        判断当前是否为指定类型场景
        例如：
        scene_manager.is_current_scene(GameScene)
        """
        if self.current_scene is None:
            return False
        return isinstance(
            self.current_scene,
            scene_type
        )

    @staticmethod
    def _get_scene_name(scene):
        """
        获取场景名称
        """
        return scene.__class__.__name__
