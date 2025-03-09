import numpy as np
import streamlit as st

st.title("Self-Organizing Map (SOM) Training")

# Step 1: Get user inputs
num_vectors = st.number_input("Enter Number of Vectors:", min_value=1, step=1, value=4)
vector_dim = st.number_input("Enter Dimension of Each Vector:", min_value=1, step=1, value=5)
num_clusters = 2  # Fixed to match the lab problem (2 weight vectors)

# Step 2: Get vectors from user
st.subheader("Enter Vector Values")
vectors = []
for i in range(num_vectors):
    vector = st.text_input(f"Vector {i+1} (space-separated values):", " ".join(["0"] * vector_dim))
    vectors.append(list(map(float, vector.split())))

vectors = np.array(vectors)

# Step 3: Get weight matrix from user
st.subheader("Enter Initial Weights")
weights = []
for i in range(vector_dim):
    weight = st.text_input(f"Weight Row {i+1} (space-separated {num_clusters} values):", " ".join(["0.0"] * num_clusters))
    weights.append(list(map(float, weight.split())))

weights = np.array(weights)

# Step 4: Get learning rate
eta = st.number_input("Enter Initial Learning Rate:", min_value=0.01, max_value=1.0, value=0.8)

# Step 5: Train the SOM
if st.button("Compute"):
    st.subheader("Initial Weights:")
    st.write(weights)

    # Training loop
    for cycle in range(num_vectors):  # One iteration per cycle
        st.subheader(f"Cycle {cycle + 1}")

        x = vectors[cycle]  # Process one vector per cycle

        # Step 1: Compute Euclidean distances
        distances = np.linalg.norm(weights - x.reshape(-1, 1), axis=0)

        # Step 2: Determine the winning neuron
        winner_idx = np.argmin(distances)
        st.write(f"Winner Neuron: {winner_idx + 1}")

        # Step 3: Compute weight update
        old_weights = weights[:, winner_idx].copy()
        weights[:, winner_idx] += eta * (x - weights[:, winner_idx])

        # Step 4: Show only updated values
        st.write(f"Updated Weights for Neuron {winner_idx + 1}:")
        for i in range(len(weights)):
            if old_weights[i] != weights[i, winner_idx]:  # Show only changed values
                st.write(f"{np.round(weights[i, winner_idx], 3)}")

        # Reduce learning rate
        eta /= 2

    # Display final weights
    st.subheader("Final Weights:")
    st.write(np.round(weights, 3))
