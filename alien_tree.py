class BST:
    class Node:
        def __init__(self, data):       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)
                
    def __iter__(self):
        yield from self._traverse_forward(self.root)
        
    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
            
    def __reversed__(self):
      yield from self._traverse_backward(self.root)
      
    def _traverse_backward(self, node):
    
        # TODO: Reverse the _traverse_forward() function to iterate backwards.
            
    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)

    def _get_height(self, node):
    
      # TODO: Check the height of the tree using the left and right node heights.
      
        if node == None:
            return 0
        # Recursively call the _get_height() function on the left and right nodes.
        else:
            left_height = None # Change this.
            right_height = None # Change this.
          
            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1
  
alien_catalog = {"venusian", "irken", "ashtar", "silurian", "mothman", "sleestak", "grey", "saiyan", "nam", "plejaren", "martian"}

alien_tree = BST()

for species in alien_catalog:
    
    # TODO: Insert the species into the alien_tree.

for species in reversed(alien_tree):
    print(species)
    
print("Height: " + str(alien_tree.get_height())) # Will be 5.
