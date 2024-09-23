import pandas as pd

# 예제 데이터 생성
data = {
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [25, 30, 22],
    '직업': ['학생', '개발자', '디자이너']
}

df = pd.DataFrame(data)

# 데이터 출력
print(df)

