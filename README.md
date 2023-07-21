# Movie-Recommendation-System
# Overview
The Movie Recommender System is a simple web application that provides movie recommendations based on the selected movie. It uses natural language processing techniques to analyze movie plots, genres, keywords, cast, and crew to find similar movies and recommend them to the user.

# How It Works
The system is built using Python and leverages the power of machine learning to create a movie similarity matrix. The data is preprocessed to extract relevant features from the movie dataset, and then the movie vectors are created using the CountVectorizer. Cosine similarity is calculated between the movie vectors to determine their similarity, and based on this similarity score, similar movies are recommended.

# Data Source
The movie data is sourced from the TMDB 5000 Movie Dataset, available on Kaggle. The dataset contains information about thousands of movies, including their titles, overviews, genres, keywords, cast, and crew.

# How to Use
Clone the repository to your local machine.
Install the required Python packages.
Download the dataset files (tmdb_5000_movies.csv and tmdb_5000_credits.csv) and place them in the same directory as the code files.
Execute the data preprocessing and model building code in a Jupyter notebook or any Python environment.
Run the frontend interface code using Streamlit in PyCharm or any Python environment.
Select a movie from the dropdown or type the movie name and press "Show Recommendation" to get similar movie suggestions.

# Frontend Interface
The frontend interface is developed using Streamlit, a Python library for building web applications with minimal effort. It allows users to interact with the system, select a movie, and view the recommended movies with their posters.

# Requirements
Python 3.7+
pandas
streamlit

# Customization
Feel free to customize the code and frontend interface according to your requirements. You can modify the CSS styles, add more features, or integrate it with a larger web application.

# Acknowledgments
Special thanks to Kaggle for providing the TMDB 5000 Movie Dataset, and to the Streamlit team for creating an amazing library for building interactive web apps with Python.
