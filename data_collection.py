# data_collection.py

import feedparser
import pandas as pd
from urllib.parse import quote

def collect_and_save_data(keyword, file_name='rss_data.xlsx'):
    """
    특정 키워드를 Google News RSS 피드에서 검색하고 결과를 엑셀 파일로 저장합니다.
    
    Parameters:
        keyword (str): 검색할 키워드.
        file_name (str): 저장할 엑셀 파일 이름.
    """
    # 공백이나 특수 문자가 포함된 키워드를 URL 인코딩
    encoded_keyword = quote(keyword)
    
    # 구글 뉴스 RSS URL에 인코딩된 키워드를 포함하여 생성
    url = f'https://news.google.com/rss/search?q={encoded_keyword}'
    
    # RSS 피드에서 데이터 가져오기
    feed = feedparser.parse(url)
    
    # 필요한 태그 추출
    data = []
    for entry in feed.entries:
        data.append({
            'Title': entry.title,
            'Link': entry.link,
            'Published': entry.published
        })
    
    # 데이터프레임으로 변환하고 엑셀 파일로 저장
    df = pd.DataFrame(data)
    df.to_excel(file_name, index=False)
    print(f"Data saved successfully to {file_name}")

if __name__ == "__main__":
    keyword = input("Enter a keyword for Google News search: ")
    collect_and_save_data(keyword)
