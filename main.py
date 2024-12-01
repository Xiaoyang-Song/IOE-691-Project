from IP import *
import sys
import os
import time




if __name__ == '__main__':
    # print("Driver")
    print("Instance: ",  " ".join(sys.argv))
    edges, root_id = read_files(sys)
    D = int(sys.argv[2])
    # Output
    sol_minTVR_s=time.time()
    tours = DVRP_on_tree(edges, root_id=root_id, D=D)
    sol_minTVR_e=time.time()
    if tours is not None:
        print(f"Number of Paths: {len(tours)}")
    else:
        exit(0)

    # IP
    nodes, root = build_tree(edges, root_id)
    opt, build_time, sol_time = IP_DVRP(nodes, D)

    # Soln
    print("-"*80)
    print(f"minTVR: {len(tours)}")
    print(f"IP: {len(opt)}")
    ratio = len(tours) / len(opt)
    print(f"Ratio: {ratio:.4}")
    # Runtime comparison
    print("-"*80)
    print(f"IP runtime: {build_time + sol_time:.4}")
    print(f"-- Build Instance: {build_time:.4}")
    print(f"-- Solve: {sol_time:.4}")
    print(f"minTVR runtime: {sol_minTVR_e - sol_minTVR_s:.4}")
    print(f"{len(tours)} {len(opt)} {ratio:.4} {build_time:.4} {sol_time:.4} {build_time + sol_time:.4} {sol_minTVR_e - sol_minTVR_s:.4}")