import streamlit as st
import numpy as np
import pandas as pd

# Fixed dataset
x1 = np.array([1.4, 1.6, -1.4, -2, -3, 2.4, 1.5, 2.3, -3.2, -4.1])
x2 = np.array([1.65, 1.975, -1.775, -2.525, -3.95, 3.075, 2.025, 2.75, -4.05, -4.85])

# Compute mean
mean_x1, mean_x2 = np.mean(x1), np.mean(x2)

# Compute centered data
centered_x1 = x1 - mean_x1
centered_x2 = x2 - mean_x2
cov_product = centered_x1 * centered_x2

# Compute covariance matrix
cov_x1 = np.sum(centered_x1**2) / (len(x1) - 1)
cov_x2 = np.sum(centered_x2**2) / (len(x2) - 1)
covariance = np.sum(centered_x1 * centered_x2) / (len(x1) - 1)
cov_matrix = np.array([[cov_x1, covariance], [covariance, cov_x2]])

# Compute eigenvalues and eigenvectors
a = 1
b = -(cov_x1 + cov_x2)
c = (cov_x1 * cov_x2) - (covariance**2)
eigenvalue1 = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)
eigenvalue2 = (-b - np.sqrt(b**2 - 4*a*c)) / (2*a)
eigenvalues = np.array([eigenvalue1, eigenvalue2])

# Compute eigenvectors
eigenvector1 = np.array([covariance, eigenvalue1 - cov_x1])
eigenvector2 = np.array([covariance, eigenvalue2 - cov_x1])
eigenvector1 = eigenvector1 / np.linalg.norm(eigenvector1)
eigenvector2 = eigenvector2 / np.linalg.norm(eigenvector2)
eigenvectors = np.column_stack((eigenvector1, eigenvector2))

# Transform data
transformed_data = np.column_stack((centered_x1, centered_x2)) @ eigenvectors

# Streamlit UI
st.title("PCA Calculator")

# Display Data Table
data_df = pd.DataFrame({
    "X1": x1,
    "X2": x2,
    "X1 - Mean": centered_x1,
    "X2 - Mean": centered_x2,
    "(X1 - Mean) * (X2 - Mean)": cov_product
})
st.subheader("Input and Centered Data")
st.write(data_df)

st.subheader("Mean Values")
st.write(f"X1 Mean: {mean_x1}, X2 Mean: {mean_x2}")

st.subheader("Variance and Covariance")
st.write(f"Variance X1: {cov_x1}")
st.write(f"Variance X2: {cov_x2}")
st.write(f"Covariance: {covariance}")

st.subheader("Covariance Matrix")
st.write(pd.DataFrame(cov_matrix, columns=["Var X1", "Cov(X1,X2)"], index=["Var X1", "Var X2"]))

st.subheader("Eigenvalues Calculation Steps")
st.write(f"Equation: λ² - {cov_x1 + cov_x2}λ + {cov_x1 * cov_x2 - covariance**2} = 0")
st.write(f"Eigenvalues: {eigenvalues}")

st.subheader("Eigenvectors")
st.write(pd.DataFrame(eigenvectors, columns=["PC1", "PC2"]))

st.subheader("Transformed Data")
st.write(pd.DataFrame(transformed_data, columns=["PC1", "PC2"]))
