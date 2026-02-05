from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def content_based_recommend(movie_title, movies_df):
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(movies_df['genres'])

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    idx = movies_df.index[movies_df['title'] == movie_title][0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:4]

    return [movies_df.iloc[i[0]]['title'] for i in sim_scores]
