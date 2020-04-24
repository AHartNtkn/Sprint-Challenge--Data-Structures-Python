import sys

# Canonical endofunctor map
# Here, the endofunctor is modeled as a type which is either
# None, modeling an empty leaf, or a tuple consisting of
# the left tree recurse, the value, and the right tree recurse.
def bst_efmap(f, nF):
    if nF is None:
        return None
    elif isinstance(nF, tuple):
        return (f(nF[0]), nF[1], f(nF[2]))

# Canonical coalgebra out of the tree
def bst_out(tr):
    if tr is None:
        return None
    else:
        return (tr.left, tr.value, tr.right)

# Canonical algebra into the tree
def bst_in(Ftr):
    if nF is None:
        return None
    elif isinstance(nF, tuple):
        bst = BinarySearchTree(nF[1])
        bst.left = nF[0]
        bst.right = nF[2]
        return bst

# Generic catamorphism over BSTs
def bst_cata(alg, a):
    return alg(bst_efmap(lambda x: bst_cata(alg, x), bst_out(a)))

# Algebra for creating a list of items in the tree, in order.
def in_order_alg(trF):
    if trF is None:
        return []
    elif isinstance(trF, tuple):
        return trF[0] + [trF[1]] + trF[2]

def in_order(tr):
    return bst_cata(in_order_alg, tr)

# Algebra for creating a list of items in the tree, depth first (pre-order).
def depth_first_alg(trF):
    if trF is None:
        return []
    elif isinstance(trF, tuple):
        return [trF[1]] + trF[0] + trF[2]

def debth_first(tr):
    return bst_cata(depth_first_alg, tr)

# riffle two lists together
def riffle(l1, l2):
    m = min(len(l1), len(l2))
    return [ x for p in zip(l1, l2) for x in p ] + l1[m:] + l2[m:]

# Algebra for creating a list of items in the tree, breadth first.
def breadth_first_alg(trF):
    if trF is None:
        return []
    elif isinstance(trF, tuple):
        return [trF[1]] + riffle(trF[2], trF[0])

def breadth_first(tr):
    return bst_cata(breadth_first_alg, tr)

# Algebra for creating a list of items in the tree, depth first (post-order).
def post_order_dft_alg(trF):
    if trF is None:
        return []
    elif isinstance(trF, tuple):
        return trF[0] + trF[2] + [trF[1]]

def post_order(tr):
    return bst_cata(post_order_dft_alg, tr)

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None    

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        self.value = cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        [ print(x) for x in in_order(self) ] 

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        [ print(x) for x in breadth_first(self) ] 

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        [ print(x) for x in debth_first(self) ] 

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        [ print(x) for x in debth_first(self) ] 

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        [ print(x) for x in post_order(self) ] 
