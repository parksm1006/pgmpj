# app.py

import streamlit as st
import pandas as pd
from data_analysis import load_data, keyword_trend_analysis
from data_visualization import plot_keyword_trend, generate_wordcloud

st.title("Google News Keyword Trend Analysis")

# 키워드 입력
keyword = st.text_input("Enter a keyword to analyze:")

# 데이터 로드
df = load_data()

# 키워드 분석 실행
if st.button("Analyze") and keyword:
    trend_data = keyword_trend_analysis(df, keyword)
    st.write("Keyword Trend Data:")
    st.dataframe(trend_data)
    
    # 시각화
    st.write(f"Daily Trend of '{keyword}'")
    plot_keyword_trend(trend_data, keyword)
    
    # 워드클라우드 생성
    st.write(f"Word Cloud for '{keyword}'")
    words = df['Processed Title'].explode().tolist()
    generate_wordcloud(words)
