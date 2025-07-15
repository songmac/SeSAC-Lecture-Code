# 모듈과 패키지를 찾는 경로
import sys

print(sys.path) # 출력된 경로 목록을 순서대로 검색하여 모듈을 찾음


# 필요시 수행
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # 현재 파일의 디렉토리를 기준으로 상위 디렉토리를 PYTHONPATH에 추가
