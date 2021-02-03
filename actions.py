
# 事件基类
class Action:
    pass

# esc事件
class EscapeAction(Action):
    pass

# 移动事件
class MovementAction(Action):

    def __init__(self, dx: int, dy: int):
        super().__init__()
        self.dx = dx
        self.dy = dy
