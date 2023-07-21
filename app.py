import streamlit as st
import pickle
import pandas as pd
import requests
custom_css = f"""
<style>
div.stApp {{
    background-image: url('https://www.vshsolutions.com/wp-content/uploads/2020/02/recommender-system-for-movie-recommendation.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    opacity: 0.8; 
    color: white;
}}
</style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=4f247024a7ff29b7bcd58bc25eb21a50&language=en-US".format(movie_id))
    data = response.json()
    full_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return full_path
def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommended_movies = []
        recommended_movie_posters = []
        for i in movie_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movie_posters.append(fetch_poster(movie_id))
        return recommended_movies, recommended_movie_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox('"Type or select a movie from the dropdown",', movies['title'].values)

if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
