
import numpy as np
import IPython.display as display
from matplotlib import pyplot as plt
import io
import base64

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

fig = plt.figure(figsize=(4, 3), facecolor='w')
plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.title("Sample Visualization", fontsize=10)

data = io.BytesIO()
plt.savefig(data)
image = F"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Sample Visualization"
display.display(display.Markdown(F"""![{alt}]({image})"""))
plt.close(fig)

from collections import deque

def water_jug_bfs(jug1, jug2, target):

    visited = set()
    queue = deque()

    # start state
    queue.append((0, 0, []))

    while queue:
        x, y, path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        # Goal condition
        if x == target or y == target:
            return path

        # Possible actions
        next_states = [
            (jug1, y),      # Fill Jug1
            (x, jug2),      # Fill Jug2
            (0, y),         # Empty Jug1
            (x, 0)          # Empty Jug2
        ]

        # Pour Jug1 -> Jug2
        pour = min(x, jug2 - y)
        next_states.append((x - pour, y + pour))

        # Pour Jug2 -> Jug1
        pour = min(y, jug1 - x)
        next_states.append((x + pour, y - pour))

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    return None


# ---- User Input ----
jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

solution = water_jug_bfs(jug1, jug2, target)

if solution:
    print("\nSteps to reach the target:")
    for step in solution:
        print(step)
else:
    print("No solution possible.")
