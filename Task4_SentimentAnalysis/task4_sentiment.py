# Task 4: Sentiment Analysis using TextBlob and Matplotlib
# Internship: CodeAlpha Data Analytics

import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# 1. Sample dataset containing customer reviews / text feedback
data = {
    'Review': [
        "I absolutely love this product! It exceeded my expectations.",
        "Terrible experience. The service was slow and unhelpful.",
        "It's okay, nothing special, but gets the job done.",
        "Amazing quality and fast delivery! Highly recommended.",
        "Worst purchase I have ever made. Completely disappointed.",
        "Good value for money. Very satisfied with the overall quality.",
        "Average product, neither too good nor too bad."
    ]
}

df = pd.DataFrame(data)

# 2. Function to determine sentiment polarity using TextBlob
def get_sentiment(text):
    analysis = TextBlob(text)
    # polarity ranges from -1.0 (negative) to 1.0 (positive)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# 3. Apply sentiment analysis to the dataframe
df['Polarity'] = df['Review'].apply(lambda x: TextBlob(x).sentiment.polarity)
df['Sentiment'] = df['Review'].apply(get_sentiment)

print("--- Sentiment Analysis Results ---")
print(df[['Review', 'Sentiment', 'Polarity']])

# 4. Count the sentiments for visualization
sentiment_counts = df['Sentiment'].value_counts()

# 5. Visualize the sentiment distribution
plt.figure(figsize=(7, 5))
sentiment_counts.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Sentiment Analysis Distribution')
plt.xlabel('Sentiment Category')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot
plt.savefig('sentiment_distribution.png', bbox_inches='tight')
print("\n[INFO] Sentiment distribution plot saved successfully as 'sentiment_distribution.png'!")

plt.show()