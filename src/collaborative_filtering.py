import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def collaborative_filter(user_id, ratings_df, movies_df):
    df = pd.merge(ratings_df, movies_df, on="movie_id")

    user_movie_matrix = df.pivot_table(index="user_id",columns="title",values="rating").fillna(0)
    similarity = cosine_similarity(user_movie_matrix)

    sim_df = pd.DataFrame(similarity,index=user_movie_matrix.index,columns=user_movie_matrix.index)

    similar_users = sim_df[user_id].sort_values(ascending=False)
    top_user = similar_users.index[1]

    user_seen = set(df[df['user_id'] == user_id]['title'])
    top_user_seen = df[df['user_id'] == top_user]['title']

    return [m for m in top_user_seen if m not in user_seen][:3]
