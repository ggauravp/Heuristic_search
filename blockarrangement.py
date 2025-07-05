# The goal state for the block arrangement
GOAL_STATE = ['A', 'B', 'C', 'D']

def calculate_heuristic(state):
   
    misplaced_blocks = 0
    for i in range(len(state)):
        if state[i] != GOAL_STATE[i]:
            misplaced_blocks += 1
    return misplaced_blocks

def get_neighbors(state):
    neighbors = []
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            # Create a copy of the state to modify
            neighbor = state[:]
            # Swap blocks at positions i and j
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def hill_climbing(initial_state):
    current_state = initial_state
    path = [current_state]

    while True:
        current_heuristic = calculate_heuristic(current_state)
        print(f"Current State: {current_state}, Heuristic (Misplaced): {current_heuristic}")

        # Goal reached if heuristic is 0
        if current_heuristic == 0:
            print("\n Goal State Reached!")
            return path

        neighbors = get_neighbors(current_state)
        best_neighbor = None
        # Start with the current heuristic as the best one so far
        best_heuristic = current_heuristic

        # Find the best neighbor
        for neighbor in neighbors:
            neighbor_heuristic = calculate_heuristic(neighbor)
            if neighbor_heuristic < best_heuristic:
                best_heuristic = neighbor_heuristic
                best_neighbor = neighbor
        
        # If no neighbor is better, we are stuck
        if best_neighbor is None:
            print("\n Stuck at a local optimum. No better neighbors found.")
            return path
        
        # Move to the best neighbor found
        print(f"-> Moving to a better state.\n")
        current_state = best_neighbor
        path.append(current_state)

# --- Main Execution ---
if __name__ == "__main__":
    # Input: Initial stack of blocks
    initial_stack = ['C', 'A', 'D', 'B']
    
    solution_path = hill_climbing(initial_stack)
    
    print("-" * 35)
    print("## Final Path Taken")
    for i, state in enumerate(solution_path):
        print(f"Step {i}: {state}")