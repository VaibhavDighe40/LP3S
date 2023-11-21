# Define a Node class to represent nodes in the Huffman tree
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''  # Attribute to store Huffman code for the node

# Define the less than (__lt__) method for Node class for sorting
    def __lt__(self, nxt):
        return self.freq < nxt.freq

# Function to recursively print nodes and their Huffman codes
def print_nodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left:
        print_nodes(node.left, newVal)
    if node.right:
        print_nodes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")

# Function to perform Huffman coding and return the root of the Huffman tree
def huffman_coding(chars, freq):
    # Create initial nodes for each character and frequency
    nodes = [Node(freq[i], chars[i]) for i in range(len(chars))]
    
    # Build the Huffman tree by merging nodes with the lowest frequencies
    while len(nodes) > 1:
        # Sort nodes based on frequencies
        nodes.sort(key=lambda x: x.freq)
        
        # Pop two nodes with the lowest frequencies
        left = nodes.pop(0)
        right = nodes.pop(0)
        
        # Assign Huffman codes (0 for left, 1 for right)
        left.huff = '0'
        right.huff = '1'
        
        # Create a new internal node with the sum of frequencies
        # and concatenate symbols of the left and right nodes
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        
        # Append the new internal node back to the list
        nodes.append(new_node)

    # Return the root of the Huffman tree
    return nodes[0]

# Example data (characters and their frequencies)
chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]

# Perform Huffman coding and get the root of the Huffman tree
root = huffman_coding(chars, freq)

# Print nodes and their Huffman codes
print_nodes(root)
