# Check if a given Binary Tree is symmetric or not

# Node structure
class Node:
	def __init__(self, key):
		self.key = key			# Key of the node to compare with other nodes
		self.left = None		# left node
		self.right = None		# right node

# Function to check if is mirror
def isMirror(root1, root2):
    if root1 is None and root2 is None:				# If we came to the end, is mirror
        return True

    if (root1 is not None and root2 is not None):	# If we have roots in the actual node
        if root1.key == root2.key:					# Check if key are the same
            return (isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left))	# Recursive option to check if left and right are equal

    return False		# If any root are different, then return False


# Check if tree is mirror
def isSymmetric(root):
	return isMirror(root, root)


# Tree creation
root = Node(1) # First level

root.left = Node(2) # Second level
root.right = Node(2)

root.left.left = Node(3) # Third level
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

root.left.left.left = Node(5) # Fourth level
root.left.left.right = Node(6)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
root.right.left.left = Node(7)
root.right.left.right = Node(6)
root.right.right.left = Node(6)
root.right.right.right = Node(5)

print("Mirror" if isSymmetric(root) == True else "Not mirror")

