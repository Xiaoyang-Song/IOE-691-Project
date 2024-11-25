from IP import *




if __name__ == '__main__':
    print("Driver")
    edges, root_id, D = read_files(sys)
    # Output
    tours = DVRP_on_tree(edges, root_id=root_id, D=D)
    if tours is not None:
        print(f"Number of Paths: {len(tours)}")

    # IP
    # TODO: resolve bugs in generate subtree function in IP
    nodes, root = build_tree(edges, root_id)
    opt = IP_DVRP(nodes, D)
    print(len(opt))