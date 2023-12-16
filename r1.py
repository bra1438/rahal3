import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Sample data (replace this with your actual dataset)
data = {
    'TouristID': [1, 1, 2, 2, 3],
    'DriverID': [101, 102, 101, 103, 102],
    'Language': ['English', 'Spanish', 'French', 'English', 'Spanish'],
    'Gender': ['M', 'M', 'F', 'F', 'M'],
    'Age': [25, 30, 28, 35, 40],
    'Hobbies': ['Hiking', 'Cycling', 'Reading', 'Cycling', 'Photography']
}

df = pd.DataFrame(data)

# Collaborative Filtering - User-Item Matrix
user_item_matrix = df.pivot_table(index='TouristID', columns='DriverID', values='Age', fill_value=0)

# Content-Based Filtering - TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
hobbies_matrix = tfidf_vectorizer.fit_transform(df['Hobbies'])

# Calculate Cosine Similarity
cosine_similarities = cosine_similarity(hobbies_matrix, hobbies_matrix)

# Collaborative Filtering - Nearest Neighbors
knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(user_item_matrix)

# Streamlit App
st.title("Personalized Recommendation System")

# User Input Form
st.sidebar.header("User Preferences")
language = st.sidebar.selectbox("Select Language", df['Language'].unique())
gender = st.sidebar.radio("Select Gender", df['Gender'].unique())
age = st.sidebar.slider("Select Age", min_value=18, max_value=60, value=30)
hobbies = st.sidebar.text_input("Enter Hobbies (comma-separated)", "Cycling,Photography")

# Content-Based Filtering - Transform Input
input_vector = tfidf_vectorizer.transform([hobbies])

# Content-Based Filtering - Calculate Similarity
content_similarity = cosine_similarity(input_vector, hobbies_matrix).flatten()

# Content-Based Filtering - Recommend Drivers based on Similarity
content_based_recommendations = df.loc[content_similarity.argsort()[:-3:-1]]

# Collaborative Filtering - Recommend Drivers based on Nearest Neighbors
_, indices = knn.kneighbors([user_item_matrix.loc[1].values], n_neighbors=3)
collaborative_filtering_recommendations = df[df['DriverID'].isin(indices.flatten())]

# Display Recommendations
st.subheader("Content-Based Recommendations:")
st.table(content_based_recommendations)

st.subheader("Collaborative Filtering Recommendations:")
st.table(collaborative_filtering_recommendations)
