#!/usr/bin/env python3
import tcod
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main() -> None:

    # 屏幕的高度
    screen_width = 80
    screen_height = 50

    # 角色位置
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # 加载字体
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # 创建一个窗口
    with tcod.context.new_terminal(screen_width, screen_height, tileset=tileset, title="游戏-Roguelike", vsync=True) as context:

        # 创建控制台
        root_console = tcod.Console(screen_width, screen_height, order="F")

        event_handler = EventHandler()

        # 游戏循环
        while True:
            # 消息
            for event in tcod.event.wait():
                action = event_handler.dispatch(event)
                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy
                elif isinstance(action, EscapeAction):
                    raise SystemExit()
            
            # 控制主角            
            root_console.print(x=player_x, y=player_y, string="@")

            # 渲染控制台
            context.present(root_console)
            # 清除屏幕
            root_console.clear()
         

if __name__ == "__main__":
    main()
