import unittest
from tasks.task1.AVLTree import AVLTree

class TestAVLTree(unittest.TestCase):
    def test_insert_and_search(self):
        tree = AVLTree()
        tree.insert(10)
        tree.insert(20)
        tree.insert(5)

        self.assertIsNotNone(tree.search(10))
        self.assertIsNotNone(tree.search(20))
        self.assertIsNotNone(tree.search(5))
        self.assertIsNone(tree.search(15))

    def test_delete(self):
        tree = AVLTree()
        tree.insert(30)
        tree.insert(20)
        tree.insert(40)
        tree.insert(10)
        tree.insert(25)

        tree.delete(20)
        self.assertIsNone(tree.search(20))

        tree.delete(30)
        self.assertIsNone(tree.search(30))

    def test_balance_after_inserts(self):
        tree = AVLTree()
        tree.insert(10)
        tree.insert(20)
        tree.insert(30)  # Должен сработать левый поворот

        self.assertEqual(tree.root.key, 20)
        self.assertEqual(tree.root.left.key, 10)
        self.assertEqual(tree.root.right.key, 30)

    def test_balance_after_deletes(self):
        tree = AVLTree()
        tree.insert(50)
        tree.insert(30)
        tree.insert(70)
        tree.insert(20)
        tree.insert(40)
        tree.insert(60)
        tree.insert(80)

        tree.delete(30)  # Проверяем баланс после удаления
        self.assertTrue(tree.validate_avl())

    def test_inorder_traversal(self):
        tree = AVLTree()
        values = [40, 20, 60, 10, 30, 50, 70]
        for v in values:
            tree.insert(v)

        self.assertEqual(tree.inorder_traversal(), sorted(values))

    def test_bfs_traversal(self):
        tree = AVLTree()
        tree.insert(50)
        tree.insert(30)
        tree.insert(70)
        tree.insert(20)
        tree.insert(40)
        tree.insert(60)
        tree.insert(80)

        self.assertEqual(tree.breadth_first_search_traversal(), [50, 30, 70, 20, 40, 60, 80])

    def test_split(self):
        tree = AVLTree()
        for i in range(1, 8):
            tree.insert(i * 10)

        left_tree, right_tree = tree.split(30)

        self.assertEqual(left_tree.inorder_traversal(), [10, 20, 30])
        self.assertEqual(right_tree.inorder_traversal(), [40, 50, 60, 70])

    def test_merge(self):
        tree1 = AVLTree()
        tree2 = AVLTree()

        for i in range(1, 5):
            tree1.insert(i * 10)
        for i in range(5, 9):
            tree2.insert(i * 10)

        merged_tree = tree1.merge(tree2)

        self.assertEqual(merged_tree.inorder_traversal(), [10, 20, 30, 40, 50, 60, 70, 80])

    def test_count_nodes(self):
        tree = AVLTree()
        for i in range(1, 6):
            tree.insert(i * 10)

        self.assertEqual(tree.count_nodes(), 5)

    def test_validate_avl(self):
        tree = AVLTree()
        tree.insert(10)
        tree.insert(20)
        tree.insert(30)
        self.assertTrue(tree.validate_avl())

        tree.insert(40)
        self.assertTrue(tree.validate_avl())

if __name__ == '__main__':
    unittest.main()
