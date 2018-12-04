

class Node():
	def __init__(self, val, left=None, right=None):
		self.val=val
		self.left=left
		self.right=right

class Tree():
	def __init__(self, nodes):
		self.root=nodes[0]
		self.create_btree(nodes)
	
	def create_btree(self, nodes):
		i=0;j=1
		while j < len(nodes):
			nodes[i].left=nodes[j]
			j=j+1
			nodes[i].right=nodes[j]
			i=i+1
			j=j+1

	def print_tree(self):
		queue=[self.root]
		while len(queue):
			node=queue.pop()
			if node.left is not None or node.right is not None:
				print node.val, 'left: ', node.left.val, 'right: ', node.right.val
				queue.append(node.left)
				queue.append(node.right)
			else:
				print node.val, 'left: None', 'right: None'

def main():
	nodes=[]
	for val in li:
		nodes.append(Node(val))
	t = Tree(nodes)
	t.print_tree()

if __name__ == "__main__":
	li=[5,2,1,4,3,9,8]
	main()
