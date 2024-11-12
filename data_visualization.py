# data_visualization.py

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

def plot_keyword_trend(trend_df, keyword):
    """
    키워드의 일자별 빈도수를 시각화합니다.
    
    Parameters:
        trend_df (DataFrame): 일자별 키워드 빈도수를 담은 DataFrame.
        keyword (str): 분석할 키워드.
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=trend_df, x='Date', y='Count')
    plt.title(f"Daily Trend of '{keyword}'")
    plt.xlabel("Date")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print("Keyword trend plot generated.")

def generate_wordcloud(words):
    """
    키워드와 연관된 단어들로 워드클라우드를 생성합니다.
    
    Parameters:
        words (list): 워드클라우드에 사용할 단어 리스트.
    """
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(words))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    print("Wordcloud generated.")
