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
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)
            
    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)

    def _get_height(self, node):
       if node == None:
            return 0
       else:
            left_height = self._get_height(node.left)
            right_height = self._get_height(node.right)
          
            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1
  
alien_catalog = {"venusian", "irken", "ashtar", "silurian", "mothman", "sleestak", "grey", "saiyan", "nam", "plejaren", "martian"}

alien_tree = BST()

for species in alien_catalog:
    alien_tree.insert(species)

for species in reversed(alien_tree):
    print(species)
    
print("Height: " + str(alien_tree.get_height())) # Will be 5.