```python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalysis:
    def __init__(self):
        self.sid = SentimentIntensityAnalyzer()
    
    def analyze_sentiment(self, text):
        sentiment_scores = self.sid.polarity_scores(text)
        sentiment = sentiment_scores['compound']
        
        if sentiment >= 0.05:
            return 'Positive'
        elif sentiment <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'
```
