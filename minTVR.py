# IOE 691 Project
# DVRP on tree metrics Algorithm Implementation
# Viswanath Nagarajan, R. Ravi: 
# Approximation algorithms for distance constrained vehicle routing problems Section2
import sys
class TreeNode:
    """
    Node class
    """
    def __init__(self, id):
        self.id = id
        self.children = []  # list of (child_node, edge_weight)
        self.parent = None  # parent node
        self.edge_weight = 0  # weight of edge from parent to this node
        self.subtree_size = 0  # total weight of subtree edges
        self.L = 0  # minimal tour length covering subtree rooted at this node
        self.depth = 0  # distance from root to this node
        self.level = 0  # level of this node (root has level 0)

def build_tree(edges, root_id):
    # Build adjacency list
    adj = {}
    for u, v, w in edges:
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append((v, w))
        adj[v].append((u, w))  # Since the tree is undirected

    # Create nodes
    nodes = {}
    for node_id in adj.keys():
        nodes[node_id] = TreeNode(node_id)

    # Build the tree using DFS
    visited = set()
    def dfs(u, parent, depth, level):
        visited.add(u)
        node_u = nodes[u]
        node_u.parent = nodes[parent] if parent is not None else None
        node_u.depth = depth
        node_u.level = level
        for v, w in adj[u]:
            if v not in visited:
                node_v = nodes[v]
                node_v.edge_weight = w
                node_u.children.append((node_v, w))
                dfs(v, u, depth + w, level+1)
    dfs(root_id, None, 0, 0)
    root = nodes[root_id]
    return nodes, root

def compute_L(node):
    # Base case: leaf node
    if not node.children:
        node.L = 2 * node.depth  # Go from root to leaf and back
        return

    total_L = 0
    for child_node, w in node.children:
        compute_L(child_node)
        total_L += child_node.L - 2 * node.depth  # Subtract extra root distance
    node.L = total_L + 2 * node.depth  # Add distance from root to this node and back

def minTVR(node, D, tours):
    if node.L <= D:
        # The subtree rooted at this node can be covered by one tour
        tour = generate_tour(node)
        tours.append(tour)
    else:
        if not node.children:
            raise ValueError(f"Cannot cover node {node.id} within distance D")
        # Find deepest child node(s) that cannot be covered within D
        for child_node, _ in node.children:
            minTVR(child_node, D, tours)

def get_path_to_node(node):
    # Get path from root to the given node
    path = []
    while node is not None:
        path.append(node.id)
        node = node.parent
    return path[::-1]  # Reverse to get path from root to node

def euler_tour(node):
    # Generate Euler tour of the subtree rooted at the given node
    tour = [node.id]
    for child_node, _ in node.children:
        tour.extend(euler_tour(child_node))
        tour.append(node.id)
    return tour

def generate_tour(node):
    # Generate the full tour including the path from root and back
    path_to_node = get_path_to_node(node)
    euler_sequence = euler_tour(node)
    # Combine paths to form the full tour
    full_tour = path_to_node[:-1] + euler_sequence + path_to_node[::-1][1:]
    return full_tour

def DVRP_on_tree(edges, root_id, D):
    nodes, root = build_tree(edges, root_id)
    compute_L(root)
    tours = []
    try:
        minTVR(root, D, tours)
    except ValueError as e:
        print(e)
        return None
    return tours


def read_files(sys):
    # Check if the user has provided the input file
    if len(sys.argv) < 2:
        print("Usage: python script_name.py edges_file.txt")
        sys.exit(1)

    edges_file = sys.argv[1]
    root_id = 1  # Default root node ID
    edges = []
    
    # input
    try:
        with open(edges_file, 'r') as f:
            lines = f.readlines()
            if not lines:
                print("Input file is empty.")
                sys.exit(1)
            D_line = lines[0].strip()
            if not D_line:
                print("The first line of the file must be the distance constraint D.")
                sys.exit(1)
            D = int(D_line)
            for line in lines[1:]:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue  # Skip empty lines and comments
                parts = line.split()
                if len(parts) != 3:
                    print(f"Invalid line in input file: {line}")
                    continue
                u, v, w = map(int, parts)
                edges.append((u, v, w))
    except FileNotFoundError:
        print(f"File not found: {edges_file}")
        sys.exit(1)
    return edges, root_id, D

if __name__ == "__main__":
    # Input handling
    edges, root_id, D = read_files(sys)

    # Output
    tours = DVRP_on_tree(edges, root_id=root_id, D=D)
    if tours is not None:
        print(f"Number of Paths: {len(tours)}")
        # uncomment it for path detail output 
        # for i, tour in enumerate(tours):
        #     tour_str = '->'.join(map(str, tour))
        #     print(f"Tour {i+1}: {tour_str}")
