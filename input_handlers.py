from typing import Optional
import tcod.event
from actions import Action, EscapeAction, MovementAction

# 事件处理器


class EventHandler(tcod.event.EventDispatch[Action]):

    # 事件推出
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    # 事件按键
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        # Optional引入了可选值
        action: Optional[Action] = None

        key = event.sym

        # 处理移动
        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        return action
