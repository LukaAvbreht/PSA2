from ..AbstractTree import AbstractTree
from .Node import Node

__author__ = "Luka Avbreht"


class Avl(AbstractTree):
    """
    Clas that implements Avl tree on top of abstract tree class
    """
    def __init__(self, data=None):
        self.depth = 0
        if data is not None:
            self.root = Node(data[0])
            for i in data[:1]:
                self.insert(i)
        else:
            self.root = None
        super().__init__()

    def insert(self, T):
        if self.root is None:
            self.root = Node(T)
        else:
            dodali = False
            # Rebalance is the indicator parameter, that tells us if rebalancig is needet
            # and does the rebalacing of type rebalance[1]
            subroot = self.root
            while not dodali:
                # We go left
                if T < subroot.value:
                    # We need to go deeper into left tree
                    if subroot.right is not None and subroot.left is not None:
                        subroot = subroot.left
                    # we just add, we dont need to do any rebalancing
                    elif subroot.left is None:
                        subroot.left = Node(value=T, parent=subroot)
                        if self.depth < subroot.left.depth:
                            self.depth = subroot.left.depth
                        dodali = True
                    elif subroot.right is None and subroot.left is not None:
                        # We rebalance LL
                        if T < subroot.left.value:
                            self.LLRotation(subroot, T)
                            dodali = True
                        # We rebalance LR
                        else:
                            self.LRRotation(subroot, T)
                            dodali = True
                # We go right
                elif T >= subroot.value:
                    # We need to go deeper into right tree
                    if subroot.right is not None and subroot.left is not None:
                        subroot = subroot.right
                    elif subroot.right is None:
                        subroot.right = Node(value=T, parent=subroot)
                        if self.depth < subroot.right.depth:
                            self.depth = subroot.right.depth
                        dodali = True
                    elif subroot.right is not None and subroot.left is None:
                        # we rebalance RL
                        if T < subroot.right.value:
                            self.RLRotation(subroot, T)
                            dodali = True
                        # we rebalance RR
                        else:
                            self.RRRotation(subroot, T)
                            dodali = True
            self.rebalance(self.root)

    def remove(self, T):
        """
        Removes item T form Avl tree
        """
        pass

    def search(self, T):
        """
        Returns True if T is an item of Avl tree
        """
        subroot = self.root
        if T == self.root.value:
            return True
        else:
            raise NotImplementedError("Not yet done")

    # We always rebalance node with the noode that is in the root
    def rebalance(self, RebalanceNode):
        """
        Rebalances the tree with the root in RebalanceNode, it calls the sub method depending on type of rebalancing required
        """
        pass

    def LLRotation(self,RebalanceNode,addNode = None):
        """
        Does the Left-Left rebalancing od Subtree with root node RebalanceNode,
        if addNode is not none, it rotates and adds addNode into tree (add node is a value)
        """
        if addNode is not None:
            value1 = RebalanceNode.value
            value2 = RebalanceNode.left.value
            value3 = addNode
            parent = RebalanceNode.parent
            new_node = Node(value=value2, parent=parent)
            new_node.left = Node(value=value3, parent=new_node)
            new_node.right = Node(value=value1, parent=new_node)
        else:
            pass

    def LRRotation(self, RebalanceNode, addNode = None):
        """
        Does the Left-Right rebalancing od Subtree with root node RebalanceNode,
        if addNode is not none, it rotates and adds addNode into tree ( add node is a value)
        """
        if addNode is not None:
            value1 = RebalanceNode.value
            value2 = RebalanceNode.left.value
            value3 = addNode
            parent = RebalanceNode.parent
            new_node = Node(value=value3, parent=parent)
            new_node.left = Node(value=value2, parent=new_node)
            new_node.right = Node(value=value1, parent=new_node)
        else:
            pass

    def RLRotation(self,RebalanceNode,addNode = None):
        """
        Does the Right-Left rebalancing od Subtree with root node RebalanceNode,
        if addNode is not none, it rotates and adds addNode into tree ( add node is a value)
        """
        if addNode is not None:
            value1 = RebalanceNode.value
            value2 = RebalanceNode.right.value
            value3 = addNode
            parent = RebalanceNode.parent
            new_node = Node(value=value3, parent=parent)
            new_node.left = Node(value=value1, parent=new_node)
            new_node.right = Node(value=value2, parent=new_node)
        else:
            pass



    def RRRotation(self,RebalanceNode,addNode = None):
        """
        Does the Right-Right rebalancing od Subtree with root node RebalanceNode,
        if addNode is not none, it rotates and adds addNode into tree ( add node is a value)
        """
        if addNode is not None:
            value1 = RebalanceNode.value
            value2 = RebalanceNode.right.value
            value3 = addNode
            parent = RebalanceNode.parent
            new_node = Node(value=value2, parent=parent)
            new_node.left = Node(value=value1, parent=new_node)
            new_node.right = Node(value=value2, parent=new_node)
        else:
            pass