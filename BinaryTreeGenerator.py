import random
import argparse

def generate_balanced_binary_tree(n, min_weight, max_weight):
    edges = []
    for i in range(1, n // 2 + 1):
        left = 2 * i
        right = 2 * i + 1
        if left <= n:
            weight = random.randint(min_weight, max_weight)
            edges.append((i, left, weight))
        if right <= n:
            weight = random.randint(min_weight, max_weight)
            edges.append((i, right, weight))
    return edges

def generate_unbalanced_binary_tree(n, L, min_weight, max_weight):
    edges = []
    node_id = 1  # Root node ID
    current_id = node_id
    node_id += 1

    # Validate L
    if L < 0 or L > n - 1:
        raise ValueError("L must be between 0 and N-1.")

    # Number of nodes on the right side
    R = n - L - 1

    # Generate left subtree
    left_nodes = L
    if left_nodes > 0:
        left_child = node_id
        weight = random.randint(min_weight, max_weight)
        edges.append((current_id, left_child, weight))
        node_id += 1
        edges.extend(build_subtree(left_child, left_nodes, node_id, min_weight, max_weight))
        node_id += left_nodes - 1

    # Generate right subtree
    right_nodes = R
    if right_nodes > 0:
        right_child = node_id
        weight = random.randint(min_weight, max_weight)
        edges.append((current_id, right_child, weight))
        node_id += 1
        edges.extend(build_subtree(right_child, right_nodes, node_id, min_weight, max_weight))
        node_id += right_nodes - 1

    return edges

def build_subtree(parent_id, num_nodes, node_id_start, min_weight, max_weight):
    edges = []
    nodes = [parent_id]
    node_id = node_id_start
    num_nodes -= 1  # Subtract the parent node

    while num_nodes > 0 and nodes:
        current_parent = nodes.pop(0)
        # Decide how many children to add: 1 or 2
        children = min(2, num_nodes)
        for _ in range(children):
            child_id = node_id
            node_id += 1
            weight = random.randint(min_weight, max_weight)
            edges.append((current_parent, child_id, weight))
            nodes.append(child_id)
            num_nodes -= 1
            if num_nodes == 0:
                break
    return edges

def write_edges_to_file(edges, filename, D):
    with open(filename, 'w') as f:
        f.write(f"{D}\n")
        f.write("# Edges (u,v,w)\n")
        for u, v, w in edges:
            f.write(f"{u} {v} {w}\n")

def main():
    parser = argparse.ArgumentParser(description='Generate a random binary tree and save it to a file.')
    parser.add_argument('-n', '--nodes', type=int, required=True, help='Number of nodes in the tree.')
    parser.add_argument('-D', '--distance', type=int, required=True, help='Distance constraints for the first line')
    parser.add_argument('-b', '--balanced', action='store_true', help='Generate a balanced tree.')
    parser.add_argument('-L', '--left_nodes', type=int, default=0,
                        help='Number of nodes on the left of the root (excluding root). Applicable only if unbalanced.')
    parser.add_argument('--min', type=int, required=True, help='Minimum edge weight.')
    parser.add_argument('--max', type=int, required=True, help='Maximum edge weight.')
    parser.add_argument('-o', '--output', type=str, default='source/binary_tree.txt', help='Output file name.')
   
    args = parser.parse_args()

    n = args.nodes
    D = args.distance
    min_weight = args.min
    max_weight = args.max
    output_file = args.output

    if args.balanced:
        edges = generate_balanced_binary_tree(n, min_weight, max_weight)
    else:
        L = args.left_nodes
        edges = generate_unbalanced_binary_tree(n, L, min_weight, max_weight)

    write_edges_to_file(edges, output_file, D)
    print(f"Binary tree has been generated and saved to '{output_file}'.")

if __name__ == "__main__":
    main()
