from datetime import datetime


class Logger:
    """
    全局日志工具

    用于开发阶段输出游戏运行日志
    """

    @staticmethod
    def _log(level, message, tag=None):
        """
        输出日志
        """

        time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        if tag:
            print(
                f"[{time}] "
                f"[{level}] "
                f"[{tag}] "
                f"{message}"
            )
        else:
            print(
                f"[{time}] "
                f"[{level}] "
                f"{message}"
            )

    @classmethod
    def debug(cls, message, tag=None):
        """
        调试日志
        """
        cls._log(
            "DEBUG",
            message,
            tag
        )

    @classmethod
    def info(cls, message, tag=None):
        """
        普通信息
        """
        cls._log(
            "INFO",
            message,
            tag
        )

    @classmethod
    def warning(cls, message, tag=None):
        """
        警告
        """
        cls._log(
            "WARNING",
            message,
            tag
        )

    @classmethod
    def error(cls, message, tag=None):
        """
        错误
        """
        cls._log(
            "ERROR",
            message,
            tag
        )