# data_preprocessing.py

import pandas as pd
from konlpy.tag import Okt

def load_data(file_name='rss_data.xlsx'):
    """
    엑셀 파일에서 데이터를 로드합니다.
    
    Parameters:
        file_name (str): 로드할 파일 이름.
    
    Returns:
        DataFrame: 로드된 데이터를 담은 DataFrame.
    """
    df = pd.read_excel(file_name)
    print("Data loaded successfully.")
    return df

def preprocess_text(df):
    """
    텍스트 데이터를 전처리합니다.
    
    Parameters:
        df (DataFrame): 전처리할 데이터를 담은 DataFrame.
    
    Returns:
        DataFrame: 전처리된 데이터를 담은 DataFrame.
    """
    okt = Okt()
    
    # 각 문서의 title에 대해 토큰화 처리
    df['Processed Title'] = df['Title'].apply(lambda x: okt.morphs(x))
    
    # 각 문서의 title에서 불용어를 제거하고, 필요시 명사만 추출하기
    # (불용어는 기본적인 예시이며, 프로젝트에 맞게 추가적으로 정의 가능)
    stopwords = set(['있다', '하다', '되다', '않다'])  # 불용어 예시
    
    df['Processed Title'] = df['Processed Title'].apply(lambda words: [word for word in words if word not in stopwords])
    
    print("Text preprocessing completed.")
    return df

def save_processed_data(df, file_name='processed_rss_data.xlsx'):
    """
    전처리된 데이터를 엑셀 파일로 저장합니다.
    
    Parameters:
        df (DataFrame): 저장할 전처리된 데이터프레임.
        file_name (str): 저장할 파일 이름.
    """
    df.to_excel(file_name, index=False)
    print(f"Processed data saved to {file_name}")

if __name__ == "__main__":
    # 데이터 로드
    df = load_data()
    
    # 데이터 전처리
    df = preprocess_text(df)
    
    # 전처리된 데이터 저장
    save_processed_data(df)
