🎬 Movie Recommendation System

A simple yet powerful Movie Recommendation System using:

Content-Based Filtering (genre similarity)

Collaborative Filtering (user–user similarity)

This project is ideal for AI/ML learning, internships, and portfolio building.

📌 Project Structure
movie-recommender/
│
├── data/
│   ├── movies.csv
│   └── ratings.csv
│
├── src/
│   ├── data_loader.py
│   ├── content_based.py
│   ├── collaborative_filtering.py
│   └── main.py
│
├── notebooks/
│   └── Movie_Recommender.ipynb
│
├── README.md
└── requirements.txt

🚀 Features
✔ 1. Content-Based Filtering

Recommends movies by comparing genre similarity using:

TF-IDF Vectorizer

Cosine Similarity

Example:
If a user likes Inception, the system suggests movies with similar genres.

✔ 2. Collaborative Filtering

Recommends movies based on similar users’ preferences using:

User–Movie rating matrix

Cosine similarity between users

Example:
If User A and User B like similar movies, the system recommends movies that User B has seen but User A hasn’t.

📂 Dataset Description
movies.csv
movie_id	title	genres
1	Inception	Sci-Fi Thriller
2	Interstellar	Sci-Fi Adventure Drama
...	...	...
ratings.csv
user_id	movie_id	rating
1	1	5
1	3	4
...	...	...
🧠 Technologies Used

Python

Pandas

NumPy

Scikit-learn

Matplotlib

Cosine Similarity

TF-IDF Vectorizer

📝 Installation
1. Clone the repo:
git clone https://github.com/Sambit0228/movie-recommendation-system.git

2. Install dependencies:
pip install -r requirements.txt

3. Run the project:
python src/main.py

🧪 Output Example
Content-Based Filtering
Movies similar to Inception:
['Interstellar', 'Iron Man', 'Avengers']

Collaborative Filtering
Recommendations for User 1:
['Interstellar']

🧩 Future Improvements

Add matrix factorization (SVD)

Build web app using Flask/Streamlit

Use IMDb/TMDb API for real movie data

Implement Neural Collaborative Filtering

👨‍💻 Author

Sambit Kumar Panda

LinkedIn: https://www.linkedin.com/in/sambit-kumar-panda-853201293

GitHub: https://github.com/Sambit0228

⭐ Show Your Support!

If you like this project, don’t forget to ⭐ the repository on GitHub.
