import numpy as np
from tcod.console import Console
import tile_types


class GameMap:

    # 初始化地图
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full(
            (width, height), fill_value=tile_types.floor, order="F")

        self.tiles[30:33, 22] = tile_types.wall

    # 检测是否在地图里面
    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    # 渲染地图
    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]