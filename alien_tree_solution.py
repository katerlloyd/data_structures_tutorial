class BST:
    class Node:

        # Initializes the node with the data and empty child nodes.
        def __init__(self, data):       
            self.data = data
            self.left = None
            self.right = None

    # Initializes the BST to be empty.
    def __init__(self):
        self.root = None

    # Inserts the data into the next open node unless the root is empty.
    def insert(self, data):
        # inserts the data into the root if it is empty.
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    # Locates the next empty node and inserts the data into it.
    def _insert(self, data, node):
        # Data is smaller so goes on the left.
        if data < node.data:
            if node.left is None:
                # Inserts data into empty spot.
                node.left = BST.Node(data)
            else:
                # Keeps searching for empty spot recursively.
                self._insert(data, node.left)
        # Data is larger so it goes on the right.
        else:
            if node.right is None:
                # Inserts data into empty spot.
                node.right = BST.Node(data)
            else:
                # Keeps searching for empty spot recursively.
                self._insert(data, node.right)
    
    # Iterates forward starting at the root, like in a for loop.
    def __iter__(self):
        yield from self._traverse_forward(self.root)
    
    # Keeps iterating forwared until runs into an empty node.
    def _traverse_forward(self, node):
        if node is not None:
            # Returns the left node location.
            yield from self._traverse_forward(node.left)
            # Returns the data value.
            yield node.data
            # Remembers the right node location.
            yield from self._traverse_forward(node.right)
    
    # Iterates backward starting at the root, like in a reversed for loop.
    def __reversed__(self):
      yield from self._traverse_backward(self.root)

    # Keeps iterating backward until runs into an empty node.  
    def _traverse_backward(self, node):      
        if node is not None:
            # Remembers the right node location.
            yield from self._traverse_backward(node.right)
            # Returns the data value.
            yield node.data
            # Returns the left node location.
            yield from self._traverse_backward(node.left)
    
    # Calculates height of BST starting at the root.
    def get_height(self):
        # Returns 0 if root is empty.
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)

    # Calcuates height of each node subtree plus 1 to account for the root.
    def _get_height(self, node):
        # An empty node will return 0.
        if node == None:
            return 0
        # Recursively goes through each left and right node subtree until.
        else:
            left_height = self._get_height(node.left)
            right_height = self._get_height(node.right)

            # Adds 1 to the height that is greatest and returns that height.
            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1
  
alien_catalog = {"venusian", "irken", "ashtar", "silurian", "mothman", "sleestak", "grey", "saiyan", "nam", "plejaren", "martian"}

# Creates a BST.
alien_tree = BST()

# Inserts each species into the BST.
for species in alien_catalog:
    alien_tree.insert(species)

# Iterates over tree backwards.
for species in reversed(alien_tree):
    print(species)
    
print("Height: " + str(alien_tree.get_height())) # Will be 5.
