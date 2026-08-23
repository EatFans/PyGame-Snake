import pygame


class AudioManager:
    """
    全局音频管理器

    负责：
    - 背景音乐
    - 音效
    - 音量控制
    - 音乐停止
    - 音效停止
    """

    _initialized = False

    @classmethod
    def initialize(cls):
        """
        初始化音频系统
        """
        if cls._initialized:
            return

        pygame.mixer.init()

        cls._initialized = True

    @classmethod
    def play_music(
        cls,
        path,
        loops=-1,
        volume=1.0,
        fade_ms=0
    ):
        cls._check_initialized()
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(
            loops=loops,
            fade_ms=fade_ms
        )

    @classmethod
    def stop_music(cls):
        """
        停止背景音乐
        """
        cls._check_initialized()
        pygame.mixer.music.stop()

    @classmethod
    def pause_music(cls):
        """
        暂停背景音乐
        """
        cls._check_initialized()
        pygame.mixer.music.pause()

    @classmethod
    def resume_music(cls):
        """
        恢复背景音乐
        """
        cls._check_initialized()
        pygame.mixer.music.unpause()

    @classmethod
    def set_music_volume(cls, volume):
        """
        设置背景音乐音量

        :param volume: 0.0 ~ 1.0
        """
        cls._check_initialized()
        pygame.mixer.music.set_volume(volume)


    @classmethod
    def play_sound(
        cls,
        path,
        volume=1.0
    ):
        """
        播放音效

        :param path: 音效文件路径
        :param volume: 0.0 ~ 1.0
        """
        cls._check_initialized()
        sound = pygame.mixer.Sound(path)
        sound.set_volume(volume)
        sound.play()

    @classmethod
    def stop_all(cls):
        """
        停止所有音频
        """
        cls._check_initialized()
        pygame.mixer.music.stop()
        pygame.mixer.stop()

    @classmethod
    def _check_initialized(cls):
        """
        检查音频系统是否初始化
        """
        if not cls._initialized:
            raise RuntimeError(
                "AudioManager 尚未初始化，请先调用 AudioManager.initialize()"
            )