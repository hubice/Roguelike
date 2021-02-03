#!/usr/bin/env python3
import tcod

from entity import Entity
from input_handlers import EventHandler
from game_map import GameMap
from engine import Engine

# 启动器
def main() -> None:

    # 屏幕的高度
    screen_width = 80
    screen_height = 50

    # map
    map_width = 80
    map_height = 45

    # 加载字体
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # 消息处理器
    event_handler = EventHandler()

    # 生成实体(这个只是显示,没有逻辑)
    player = Entity(int(screen_width / 2),
                    int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5),
                 int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    # 生成地图
    game_map = GameMap(map_width, map_height)

    # 游戏引擎
    engine = Engine(entities=entities,
                    event_handler=event_handler,
                    game_map=game_map, 
                    player=player)

    # 创建一个窗口
    with tcod.context.new_terminal(screen_width, screen_height, tileset=tileset, title="游戏-Roguelike", vsync=True) as context:

        # 创建控制台
        root_console = tcod.Console(screen_width, screen_height, order="F")

        # 游戏循环
        while True:
            # 消息
            engine.handler_events(events=tcod.event.wait())
            # 渲染
            engine.render(console=root_console, context=context)


if __name__ == "__main__":
    main()
