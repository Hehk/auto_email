from transformers import pipeline

sentiment_analysis = pipeline('sentiment-analysis')
res = sentiment_analysis('we love you!')
print(res)