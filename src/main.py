from data_loader import load_movies, load_ratings
from content_based import content_based_recommend
from collaborative_filtering import collaborative_filter

movies_df = load_movies()
ratings_df = load_ratings()

print("\n--- CONTENT BASED RECOMMENDATIONS ---")
print(content_based_recommend("Inception", movies_df))

print("\n--- COLLABORATIVE FILTERING RECOMMENDATIONS ---")
print(collaborative_filter(1, ratings_df, movies_df))
