from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from actions import EscapeAction, MovementAction
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

# 游戏引擎
class Engine:
    # 初始化
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player

    # 事件方法
    def handler_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            if isinstance(action, MovementAction):
                if self.game_map.tiles["walkable"][self.player.x + action.dx, self.player.y + action.dy] :
                    self.player.move(dx=action.dx, dy=action.dy)


            elif isinstance(action, EscapeAction):
                raise SystemExit()


    # 渲染方法    
    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)

        for entity in self.entities:
            console.print(x=entity.x, y=entity.y, string=entity.char, fg=entity.color)

        # 渲染控制台
        context.present(console)
        # 清除屏幕
        console.clear()
