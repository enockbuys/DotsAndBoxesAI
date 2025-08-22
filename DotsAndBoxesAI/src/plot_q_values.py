import pickle
import matplotlib.pyplot as plt

# Load the Q-table
with open("q_table_AI.pkl", "rb") as f:
    q_table = pickle.load(f)

# Flatten all Q-values
q_values = [q for state in q_table.values() for q in state.values()]

# Plot histogram
plt.hist(q_values, bins=30, color='skyblue', edgecolor='black')
plt.title("Q-Value Distribution")
plt.xlabel("Q-value")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()
