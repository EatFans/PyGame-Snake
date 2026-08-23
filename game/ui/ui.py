class UI:
    """
    UI 基类

    所有场景 UI 都继承此类。
    """

    def __init__(self, layer=0):
        """
        :param layer: UI图层，数值越大，越晚渲染，显示在越上层
        """
        self.layer = layer
        self.visible = True
        self.enabled = True

    def initialize(self):
        """
        初始化 UI
        """
        pass

    def handle_event(self, event):
        """
        处理 UI 事件
        """
        return False

    def update(self, delta_time):
        """
        更新 UI
        """
        pass

    def render(self, screen):
        """
        渲染 UI
        """
        pass

    def destroy(self):
        """
        销毁 UI
        """
        pass