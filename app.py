import streamlit as st
import pandas as pd
import numpy as np
import os
import random
from PIL import Image

# Set up page configuration
st.set_page_config(page_title="Cluster Visualization", layout="wide")

# Sidebar: Cluster type selection
st.sidebar.title("Cluster Type Selection")
cluster_type = st.sidebar.radio("Choose Clustering Method:", ["Euclidean", "Cosine"])

# Load corresponding data based on cluster type
if cluster_type == "Euclidean":
    cluster_labels = np.load("cluster_labels_euclidean.npy")
    image_cluster_map = pd.read_csv("image_cluster_map_euclidean.csv", quotechar='"')
else:
    cluster_labels = np.load("cluster_labels_cosine.npy")
    image_cluster_map = pd.read_csv("image_cluster_map_cosine.csv", quotechar='"')

# Sidebar: Cluster Selection
st.sidebar.title("Cluster Selection")
clusters = sorted(image_cluster_map["Cluster"].unique())
selected_cluster = st.sidebar.selectbox("Select a cluster:", clusters)

# Display images in selected cluster
st.title(f"Images in Cluster {selected_cluster} ({cluster_type} Distance)")

# Get all image paths in the selected cluster
cluster_images = image_cluster_map[image_cluster_map["Cluster"] == selected_cluster]["Image"].tolist()

# Randomly sample images (limit to 10 for display)
random.shuffle(cluster_images)
display_images = cluster_images[:10]

# Display images
cols = st.columns(4)  # Display images in 4 columns
image_folder = "images/"  # Adjust to your image folder path

for i, image_name in enumerate(display_images):
    image_path = os.path.join(image_folder, image_name)
    if os.path.exists(image_path):
        image = Image.open(image_path)
        with cols[i % 4]:  # Rotate through columns
            st.image(image, caption=image_name, use_container_width=True)

# Info on toggle button
st.sidebar.info("Use the toggle above to switch between Euclidean and Cosine clusters.")
