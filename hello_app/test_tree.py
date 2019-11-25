import node


def evaluate_tree(tree,expected):
    print(f"Find Max: {tree.find_max_id()} and {expected}")
    assert tree.find_max_id() == expected

def test_tree1():
    print("Test1")
    tree=node.Node(23)
    tree.left=node.Node(18)
    tree.right=node.Node(2)
    tree.right.left=node.Node(34)
    tree.right.right=node.Node(12)
    tree.left.right=node.Node(4)
    tree.left.left=node.Node(11)


    evaluate_tree(tree,34)

def test_tree2():
    print("Test2")
    tree=node.Node(23)
    tree.left=node.Node(18)
    tree.right=node.Node(2)
    tree.right.left=node.Node(34)
    tree.right.right=node.Node(12)
    tree.left.right=node.Node(4)

    evaluate_tree(tree,34)

def test_tree3():
    print("Test3")
    tree=node.Node(23)
    tree.left=node.Node(18)
    tree.right=node.Node(2)
    tree.right.right=node.Node(12)
    tree.left.right=node.Node(4)

    evaluate_tree(tree,23)

def test_tree3b():
    print("Test3b")
    tree=node.Node(4)
    tree.left=node.Node(18)
    tree.right=node.Node(2)
    tree.right.right=node.Node(12)
    tree.left.right=node.Node(23)

    evaluate_tree(tree,23)

def test_tree3c():
    print("Test3c")
    tree=node.Node(4)
    tree.left=node.Node(18)
    tree.right=node.Node(23)
    tree.right.right=node.Node(12)
    tree.left.right=node.Node(2)

    evaluate_tree(tree,23)

def test_tree3d():
    print("Test3d")
    tree=node.Node(4)
    tree.left=node.Node(18)
    tree.right=node.Node(12)
    tree.right.right=node.Node(23)
    tree.left.right=node.Node(2)

    evaluate_tree(tree,23)

def test_tree4():
    print("Test4")
    tree=node.Node(23)
    tree.left=node.Node(18)
    tree.right=node.Node(2)
    tree.right.right=node.Node(12)
    tree.left.right=node.Node(4)

    evaluate_tree(tree,23)

def test_tree5():
    print("Test5")
    tree=node.Node(23)
    tree.left=node.Node(18)
    tree.right=node.Node(2)
    tree.right.right=node.Node(12)

    evaluate_tree(tree,23)

def test_tree6():
    print("Test6")
    tree=node.Node(23)
    tree.right=node.Node(2)
    tree.right.right=node.Node(12)

    evaluate_tree(tree,23)

def test_tree7():
    print("Test7")
    tree=node.Node(23)
    tree.right=node.Node(2)

    evaluate_tree(tree,23)

def test_tree8():
    print("Test8")
    tree=node.Node(23)

    evaluate_tree(tree,23)