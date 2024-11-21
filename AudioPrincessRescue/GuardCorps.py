import pyaudio
import numpy as np
import pygame

class AudioImage:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.width, self.height = self.image.get_size()
        self.x = 500
        self.y = 0

        # 初始化 PyAudio
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=44100,
                                  input=True,
                                  frames_per_buffer=1024)

    def update_position(self):
        # 读取音频数据
        data = np.frombuffer(self.stream.read(1024), dtype=np.int16)
        # 计算音量大小
        volume = np.linalg.norm(data)
        # 将音量大小映射到屏幕高度
        max_volume = 80000
        self.y = int((volume / max_volume) * 480)
        # 限制音频控制的物体在屏幕内
        self.y = max(0, min(self.y, 480 - self.height))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()