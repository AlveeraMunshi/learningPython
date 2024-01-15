class Node:
    def __init__(self, name, children):
        self.children = children
        self.name = name

    def __repr__(self) -> str:
        return f"Node({self.name})"

def dfs(u): #preorder
    ans.append(str(u))
    for v in u.children:
        if v not in visited:
            visited.add(v)
            dfs(v)

def dfs2(u): #postorder
    for v in u.children:
        if v not in visited:
            visited.add(v)
            dfs2(v)
    ans.append(str(u))

def bfs(u):
    q = [u]
    while (len(q) != 0):
        u = q.pop(0)
        ans.append(str(u))
        for v in u.children:
            if v not in visited:
                visited.add(v)
                q.append(v)

def hasPath(u1, u2):
    if u1 == u2:
        return True
    bfs(u1)
    return u2 in visited
    




leaf_1 = Node(3, ())
leaf_2 = Node(5, ())
parent_1 = Node(2, (leaf_1,))
parent_2 = Node(4, (leaf_1, leaf_2))
root = Node(1, (parent_1, parent_2))
#       1
#   2       4
#       3       5

#visited = set()
#ans = []
#dfs(root)

#visited = set()
#ans = []
#bfs(root)

visited = set()
ans = []
print(hasPath(root, leaf_2))


