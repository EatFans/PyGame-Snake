import pygame

from game.ui.ui import UI
from game.utils.logger import Logger


class GameButton(UI):
    """
    游戏按钮

    状态：
    NORMAL  : 普通状态
    HOVER   : 鼠标悬停
    PRESSED : 鼠标按下
    """

    STATUS_NORMAL = 0
    STATUS_HOVER = 1
    STATUS_PRESSED = 2

    def __init__(
            self,
            x,
            y,
            width,
            height,
            text="按钮",
            on_click=None
    ):
        super().__init__(layer=100)

        # ==========================================
        # 按钮区域
        # ==========================================

        self.rect = pygame.Rect(
            x,
            y,
            width,
            height
        )

        # ==========================================
        # 按钮属性
        # ==========================================

        self.text = text
        self.on_click = on_click

        # 当前视觉状态
        self.status = self.STATUS_NORMAL

        # 是否正在按下按钮
        self.pressed = False

        # 字体
        self.font = None

    # =====================================================
    # 初始化
    # =====================================================

    def initialize(self):
        """
        初始化按钮
        """

        # 获取系统字体
        font_path = pygame.font.match_font("sans")

        if font_path is None:
            self.font = pygame.font.Font(
                None,
                28
            )
        else:
            self.font = pygame.font.Font(
                font_path,
                28
            )
        Logger.debug(
            f"按钮初始化完成: {self.text}",
            "GameButton"
        )

    # =====================================================
    # 事件处理
    # =====================================================

    def handle_event(self, event):
        """
        处理按钮事件

        返回：
        True  -> 当前按钮消费了这个事件
        False -> 当前按钮没有消费这个事件
        """

        # =================================================
        # 鼠标移动
        # =================================================

        if event.type == pygame.MOUSEMOTION:

            # 如果当前正在按下按钮
            # 鼠标移动时不要修改 PRESSED 状态
            if self.pressed:
                return False

            if self.rect.collidepoint(event.pos):

                self.status = self.STATUS_HOVER

            else:

                self.status = self.STATUS_NORMAL

            # 鼠标移动事件一般不阻止其他 UI
            return False

        # =================================================
        # 鼠标按下
        # =================================================

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button != 1:
                return False

            # 鼠标没有点在按钮上
            if not self.rect.collidepoint(event.pos):

                return False

            # 记录按钮正在被按下
            self.pressed = True

            self.status = self.STATUS_PRESSED

            Logger.info(
                f"按钮按下: {self.text}",
                "GameButton"
            )

            # 鼠标按下事件已经被按钮消费
            return True

        # =================================================
        # 鼠标松开
        # =================================================

        if event.type == pygame.MOUSEBUTTONUP:

            if event.button != 1:
                return False

            # 如果之前没有按下这个按钮
            # 那么这次松开不算点击
            if not self.pressed:

                return False

            # 清除按下状态
            self.pressed = False

            # 鼠标松开时仍然在按钮内部
            if self.rect.collidepoint(event.pos):

                self.status = self.STATUS_HOVER

                Logger.info(
                    f"按钮点击: {self.text}",
                    "GameButton"
                )

                # 执行点击回调
                if self.on_click:

                    Logger.info(
                        f"执行按钮回调: {self.text}",
                        "GameButton"
                    )

                    self.on_click()

                else:

                    Logger.warning(
                        f"按钮没有设置 on_click: {self.text}",
                        "GameButton"
                    )

                # 非常重要：
                #
                # 当前按钮已经处理了这个事件
                # 后面的 UI 不应该继续处理
                return True

            else:

                # 鼠标按下按钮后，
                # 移动到了按钮外面再松开
                self.status = self.STATUS_NORMAL

                Logger.debug(
                    f"取消按钮点击: {self.text}",
                    "GameButton"
                )

                return True

        return False

    # =====================================================
    # 更新
    # =====================================================

    def update(self, delta_time):
        pass

    # =====================================================
    # 渲染
    # =====================================================

    def render(self, screen):
        """
        渲染按钮
        """

        # ==========================================
        # 根据状态选择颜色
        # ==========================================

        if self.status == self.STATUS_PRESSED:

            color = (30, 100, 180)

        elif self.status == self.STATUS_HOVER:

            color = (50, 150, 240)

        else:

            color = (40, 130, 220)

        # ==========================================
        # 绘制按钮
        # ==========================================

        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=10
        )

        # ==========================================
        # 绘制文字
        # ==========================================

        if self.font:

            text_surface = self.font.render(
                self.text,
                True,
                (255, 255, 255)
            )

            text_rect = text_surface.get_rect(
                center=self.rect.center
            )

            screen.blit(
                text_surface,
                text_rect
            )

    # =====================================================
    # 销毁
    # =====================================================

    def destroy(self):
        """
        销毁按钮
        """

        Logger.debug(
            f"销毁按钮: {self.text}",
            "GameButton"
        )

        self.font = None
        self.on_click = None

        self.pressed = False
        self.status = self.STATUS_NORMAL