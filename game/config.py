
class GameConfig:
    """
    游戏全局配置
    """

    # 游戏窗口配置
    WIDTH = 1280
    HEIGHT = 720

    # 游戏 FPS 帧数配置
    FPS = 60

    # 游戏区域左上角
    AREA_X = 65
    AREA_Y = 55
    # 游戏区域尺寸
    AREA_WIDTH = 1180
    AREA_HEIGHT = 615
    # 地图砖块大小
    TILE_SIZE = 75
    # 地图砖块列数
    COLS = 16
    # 地图砖块行数
    ROWS = 9


    SNAKE_MOVE_INTERVAL = 0.15


    # 地图背景颜色
    BACKGROUND_COLOR = (0, 0, 0)
    # 墙壁颜色
    WALL_COLOR = (255, 255, 255)

    # 蛇头颜色
    SNAKE_HEAD_COLOR = (50, 255, 50)
    # 蛇身颜色
    SNAKE_COLOR = (144, 238, 144)

    # 食物颜色
    FOOD_COLOR = (70, 190, 240)