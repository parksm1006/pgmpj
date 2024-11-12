# main.py

from data_collection import collect_and_save_data
from data_preprocessing import load_data, preprocess_text, save_processed_data
from data_analysis import keyword_trend_analysis
from data_visualization import plot_keyword_trend, generate_wordcloud

def main():
    # 1단계: 데이터 수집
    collect_and_save_data(input("키워드를 입력하세요: "))
    # title_keyword = input("키워드를 입력하세요: ")
    # feed = fetch_rss_data(title_keyword)
    # df_feed = parse_rss(feed)
    # save_to_excel(df_feed)
    
    # 2단계: 데이터 전처리
    df = load_data('rss_data.xlsx')
    df = preprocess_text(df)
    save_processed_data(df)
    
    # 3단계: 데이터 분석
    keyword = input("분석할 연관 키워드를 입력하세요: ")
    trend_data = keyword_trend_analysis(df, keyword)
    
    # 4단계: 데이터 시각화
    plot_keyword_trend(trend_data, keyword)
    words = df['Processed Title'].explode().tolist()
    generate_wordcloud(words)

if __name__ == "__main__":
    main()
