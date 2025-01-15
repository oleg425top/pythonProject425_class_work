import unittest
from inspect import stack

from module_10_06_узлы import Node, Stack

class TestNode(unittest.TestCase):
    node_1 = Node(5)

    def test_01_node(self):
        self.assertEqual(TestNode.node_1.data, 5)
        self.assertEqual(TestNode.node_1.next_node, None)
        node_2 = Node(3,TestNode.node_1)
        self.assertEqual(node_2.data, 3)
        self.assertEqual(node_2.next_node, TestNode.node_1)
        self.assertEqual(node_2.next_node.data, 5)

class TestStack(unittest.TestCase):
    stack = Stack()

    def test_init(self):
        self.assertEqual(self.stack.top, None)

    def test_push(self):
        self.stack.push('test_data1')
        self.assertEqual(TestStack.stack.top.data, 'test_data1')