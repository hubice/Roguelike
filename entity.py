from typing import Tuple

# 实体对象 表示游戏中的所有事物
class Entity:
    
    # 描述实体
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    # 移动
    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy

        