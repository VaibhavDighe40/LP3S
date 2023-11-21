import heapq

class node:
    def __init__(self, freq, symbol, left = None, right = None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    
def printnodes(node,val=''):
    newval = val + str(node.huff)

    if node.left:
        printnodes(node.left,newval)
    if node.right:
        printnodes(node.right,newval)
    if(not node.left and not node.right):
        print(f'{node.symbol} --> {newval}')



chars = ['a','b','c','d','e']
freq = [21,14,69,54,2]
nodes = []

for i in range(len(chars)):
    heapq.heappush(nodes, node(freq[i],chars[i]))

while len(nodes)>1:

    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    left.huff = 0
    right.huff = 1

    newnode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

    heapq.heappush(nodes, newnode)

printnodes(nodes[0])