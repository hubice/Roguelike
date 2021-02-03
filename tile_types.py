from typing import Tuple
import numpy as np

# 这个是tcod需要的渲染结构
graphic_dt = np.dtype(
    [
        ("ch", np.int32), #字符
        ("fg", "3B"), #前景色 3个无符号字节 表示字符颜色
        ("bg", "3B"), #背景色 表示背景颜色
    ]
)

# 这个是我们的逻辑结构
tile_dt = np.dtype(
    [
        ("walkable", np.bool), #是否可以行走
        ("transparent", np.bool), #是否透明
        ("dark", graphic_dt), #区分在视场中和不在视场中的图块
    ]
)

# 一个快捷方法
def new_title(*, walkable: bool, transparent: bool, dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]]) -> np.ndarray:
    return np.array((walkable, transparent, dark), dtype=tile_dt)

# 生成的两种类型
floor = new_title(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
)
wall = new_title(
    walkable=False, transparent=False, dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
)