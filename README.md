# Medicine_Recommendation_System

⚙️ How it works (based on the notebook):
1. Data Loading
 Imported a dataset of drug names and their tags (metadata) into a pandas DataFrame.

2. Preprocessing
 Cleaned the Drug_Name column by lowercasing, removing punctuation/symbols, and dropping nulls/duplicates.

3. Text Embedding (Vectorization)
 Used CountVectorizer to convert drug names into a bag-of-words sparse matrix — capturing word presence and frequency.

4. Similarity Matrix
 Computed cosine similarity between all drug name vectors using sklearn.metrics.pairwise.cosine_similarity. This creates a matrix of pairwise similarity scores.

5. Recommendation Logic
 For any given drug name, it:
• Finds the most similar known name
• Retrieves its row from the similarity matrix
• Sorts by similarity score and returns the top N similar drugs

6. Export for Deployment
 Saved both the cleaned dataframe and the similarity matrix using joblib for fast loading in a deployed environment.

🚀 App Highlights:
• Users can type or select a drug name
• Returns Top 5 similar drugs
• Designed with user-friendly UI and informative error handling

🌐 Try it Live:
 🔗 https://lnkd.in/eQRCGj4C
