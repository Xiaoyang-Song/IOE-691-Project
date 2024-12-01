import os
import argparse
import numpy as np
from matplotlib import pyplot as plt


def read_results(file_path, num_lines):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines[-num_lines:]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


parser = argparse.ArgumentParser(description="Process result files.")
parser.add_argument("-D", type=int, required=True, help="Value of D")
parser.add_argument("-n", type=int, required=True, help="Value of n")
parser.add_argument("-m", type=int, required=True, help="number of instances")
parser.add_argument("-mode", type=str, required=True, help="Mode (e.g., 'balanced')")
args = parser.parse_args()


mode=args.mode
D=args.D
n=args.n
m=args.m

summary = []

for i in range(m):
    file_path = os.path.join('out', mode, f'{n}-{D}', f"{i+1}.txt")

    results = read_results(file_path, 1)[0].rstrip("\n").split(" ")
    if results[0] != 'Terminated':
        results = np.array(results, dtype=np.float32)
        minTVR, IP, ratio, build_time, sol_time, tot_time, minTVR_time = results
        # if ratio==2:
        #     print(i)
        summary.append(results)

summary = np.array(summary)
print(summary)

x, y = summary[:,1], summary[:,0]
plt.scatter(x,y, color='black', label='instance', marker='x',s=15)

x_line = np.linspace(min(x), max(x), 100)  # Generate x values for the line
y_line_1 = x_line 
y_line_2 = 2 * x_line
plt.plot(x_line, y_line_1, color='green', label='LB')
plt.plot(x_line, y_line_2, color='red', label='UB')
plt.xticks(np.arange(int(np.floor(min(x))), int(np.ceil(max(x))) + 1, 1))

plt.xlabel('IP value')
plt.ylabel('minTVR value')
plt.title(f'Results on randomized instance (n={n} & D={D})')

plt.legend()
fname = os.path.join('figure', f"{mode}-{n}-{D}.png")
plt.savefig(fname)