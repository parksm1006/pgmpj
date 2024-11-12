# data_analysis.py

import pandas as pd

def load_data(file_name='processed_rss_data.xlsx'):
    """
    전처리된 데이터를 엑셀 파일에서 로드합니다.
    
    Parameters:
        file_name (str): 로드할 파일 이름.
    
    Returns:
        DataFrame: 로드된 데이터를 담은 DataFrame.
    """
    df = pd.read_excel(file_name)
    print("Data loaded successfully.")
    return df

def keyword_trend_analysis(df, keyword):
    """
    특정 키워드의 일자별 빈도수를 분석합니다.
    
    Parameters:
        df (DataFrame): 분석할 데이터를 담은 DataFrame.
        keyword (str): 분석할 키워드.
    
    Returns:
        DataFrame: 일자별 키워드 빈도수를 담은 DataFrame.
    """
    # 'Processed Title'에서 키워드가 포함된 행을 필터링
    df['Date'] = pd.to_datetime(df['Published']).dt.date
    keyword_df = df[df['Processed Title'].apply(lambda x: keyword in x)]
    
    # 일자별 키워드 빈도수 계산
    trend = keyword_df.groupby('Date').size().reset_index(name='Count')
    print("Keyword trend analysis completed.")
    return trend

if __name__ == "__main__":
    df = load_data()
    keyword = 'example_keyword'
    trend_data = keyword_trend_analysis(df, keyword)
    print(trend_data)
