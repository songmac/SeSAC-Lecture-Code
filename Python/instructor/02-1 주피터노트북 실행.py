# -*-coding: utf-8 -*-

# matplotlib.pyplot 모듈을 plt로 가져오기
# anaconda prompt에서 conda install matplotlib 로 설치 후 실행

import matplotlib.pyplot as plt

#Jupyter Notebook Test
#주피터 처음 실행해보기
#주피터의 기본기능 익혀보기
print('Hello World')
print('저는 송은채입니다')

# 간단한 선 그래프 그리기
x_values = [1, 2, 3, 4]  # x값으로 사용할 리스트
y_values = [1, 2, 3, 4]  # y값으로 사용할 리스트

plt.plot(x_values, y_values)  # x값과 y값을 플로팅
plt.xlabel('Index')           # x축 레이블을 'Index'로 설정
plt.ylabel('Number')          # y축 레이블을 'Number'로 설정
plt.title('Simple Line Plot') # 그래프 제목 추가
plt.show()                    # 그래프를 화면에 표시
