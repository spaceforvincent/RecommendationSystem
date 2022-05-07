# -*- coding: utf-8 -*-
"""1. movies.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/107F33TzGMlNSegnV6Iv0yJ44RiTPtOCL
"""

import pandas as pd

"""# Read Data"""

movies = pd.read_csv('/content/drive/MyDrive/추천시스템 입문/data/movies.csv', index_col = 'movieId')

movies.shape

#movies.head()
#movies.tail()
movies.sample(10)

movies.columns

"""### 개봉연도 데이터 정제하기"""

movies['year'] = movies['title'].str.extract('(\(\d\d\d\d\))') #제목에서 연도추출

movies['year'] = movies['year'].str.extract('(\d\d\d\d)')# 연도에서 괄호제거

movies.head()

"""### 결측값 핸들링하기"""

movies[movies['year'].isnull()] #결측값 행만 보기

movies['year'] = movies['year'].fillna('2050') #2050으로 일괄적으로 결측값 채움
movies

### 가장 많이 출현하는 개봉연도를 찾기
movies['year'].value_counts()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt #seaborn figure 크기 조절을 위해서

plt.figure(figsize = (100,50))
sns.countplot(data = movies, x='year')

"""### genres 분석"""

movies['genres']

sample_genre = movies['genres'][1]
sample_genre

sample_genre.split("|")

genres_list = list(movies['genres'].apply(lambda x:x.split("|"))) #x : movies['genres']
genres_list[:3]

flat_list = []
for sublist in genres_list:
  for item in sublist:
    flat_list.append(item) #flat_list에는 모든 레코드의 장르가 담김

genres_unique = list(set(flat_list)) #중복제거

len(genres_unique) #총 20개의 장르가 있음

"""### 장르데이터 숫자형으로 변환하기"""

movies['Adventure'] = movies['genres'].apply(lambda x:'Adventure' in x)

movies

genres_dummies = movies['genres'].str.get_dummies(sep='|') #영화의 장르 여부를 1과 0으로 구분
genres_dummies

#difference between csv and pickle when saving pandas?
genres_dummies.to_pickle('/content/drive/MyDrive/추천시스템 입문/data/ml-latest-small/genres.p')

# 두 장르의 관계가 1에 가깝다는 것은 두 장르가 자주 같이 출현한다는 것
plt.figure(figsize=(30,15))
sns.heatmap(genres_dummies.corr(), annot = True)