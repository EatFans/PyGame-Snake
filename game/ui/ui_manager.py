
class UIManager:
    """
    UI管理器

    每个场景应该都有一个独立的UI管理，负责每个场景的UI绘制、UI交互
    """

    def __init__(self):
        self.uis = []
        pass

    def register(self,ui,layer=0):
        """
        注册 UI
        :param ui: UI
        :param layer: UI所在图层
        :return:
        """
        ui.layer = layer
        self.uis.append(ui)
        # 根据图层进行排序
        self.uis.sort(key=lambda item: layer)
        # 将UI进行初始化
        ui.initialize()

    def remove(self, ui):
        """
        移除 UI
        """
        if ui in self.uis:
            ui.destroy()
            self.uis.remove(ui)


    def update(self,delta_time):
        """
        UI更新
        :param delta_time:
        :return:
        """
        for ui in self.uis:
            ui.update(delta_time)

    def handle_event(self,event):
        """
        UI事件处理
        :param event:
        :return:
        """
        for ui in reversed(self.uis):
            if ui.handle_event(event):
                return True
        return False


    def render(self, screen):
        """
        UI的渲染
        :param screen:
        :return:
        """
        for ui in self.uis:
            ui.render(screen)

    def destroy(self):
        """
        UI销毁
        :return:
        """
        for ui in self.uis:
            ui.destroy()
        self.uis.clear()
