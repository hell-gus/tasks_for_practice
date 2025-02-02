import AVLNode

class AVLTree:
    """Класс для реализации АВЛ-дерева (сбалансированного бинарного дерева поиска)."""

    def __init__(self):
        """Инициализация АВЛ-дерева. Корень дерева изначально пуст."""
        self.root = None

    # === Базовые операции ===

    def insert(self, key):
        """Публичный метод для вставки ключа в дерево."""
        self.root = self._insert(self.root, key)

    def delete(self, key):
        """Публичный метод для удаления ключа из дерева."""
        self.root = self._delete(self.root, key)

    def search(self, key):
        """Публичный метод для поиска ключа в дереве."""
        return self._search(self.root, key)

    # === Вспомогательные методы (вставка, удаление, поиск) ===

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        return self._balance(node)

    def _delete(self, node, key):
        if not node:
            return node
        elif key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._get_min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        return self._balance(node)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # === Балансировка и повороты ===

    def _balance(self, node):
        """Балансировка узла."""
        if not node:
            return None
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        if balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        """Левый поворот вокруг узла z."""
        y = z.right
        T2 = y.left
        y.left, z.right = z, T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        """Правый поворот вокруг узла z."""
        y = z.left
        T3 = y.right
        y.right, z.left = z, T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    # === Вспомогательные методы ===

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _get_min_value_node(self, node):
        return self._get_min_value_node(node.left) if node and node.left else node

    def get_min_value(self):
        """Публичный метод для получения минимального значения в дереве."""
        return self._get_min_value_node(self.root).key if self.root else None

    # === Обходы дерева ===

    def inorder_traversal(self):
        """Обход дерева в порядке in-order."""
        elements = []
        self._inorder_traversal(self.root, elements)
        return elements

    def _inorder_traversal(self, node, elements):
        if node:
            self._inorder_traversal(node.left, elements)
            elements.append(node.key)
            self._inorder_traversal(node.right, elements)

    def breadth_first_search_traversal(self):
        """"Обход дерева в ширину (BFS)."""
        if not self.root:
            return []
        return self._breadth_first_search_traversal()

    def _breadth_first_search_traversal(self):
        if not self.root:
            return []
        queue, elements = [self.root], []
        while queue:
            node = queue.pop(0)
            elements.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return elements

    # === Валидация дерева ===

    def validate_avl(self):
        """Проверка, является ли дерево АВЛ-деревом."""
        return self._validate_avl(self.root)

    def _validate_avl(self, node):
        if not node:
            return True
        balance = self._get_balance(node)
        return abs(balance) <= 1 and self._validate_avl(node.left) and self._validate_avl(node.right)

    # === Операции с деревом ===

    def split(self, key):
        """Разделение дерева на два по ключу."""
        left_tree, right_tree = AVLTree(), AVLTree()
        self._split(self.root, key, left_tree, right_tree)
        return left_tree, right_tree

    def _split(self, node, key, left_tree, right_tree):
        if node:
            (left_tree if node.key <= key else right_tree).insert(node.key)
            self._split(node.right if node.key <= key else node.left, key, left_tree, right_tree)

    def merge(self, other_tree):
        """Слияние двух деревьев."""
        new_tree = AVLTree()
        self._merge_trees(self.root, new_tree)
        self._merge_trees(other_tree.root, new_tree)
        return new_tree

    def _merge_trees(self, node, new_tree):
        if node:
            new_tree.insert(node.key)
            self._merge_trees(node.left, new_tree)
            self._merge_trees(node.right, new_tree)
