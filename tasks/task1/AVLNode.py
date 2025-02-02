from typing import Union

class AVLNode:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left: Union[AVLNode, None] = left
        self.right: Union[AVLNode, None] = right
        self.height: int = 1