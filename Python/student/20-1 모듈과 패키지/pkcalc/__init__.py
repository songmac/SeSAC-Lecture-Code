"""
__init__.py 란?
pkcalc 폴더가 패키지로 인식되기 위한 파일
- 패키지 외부로 노출하고 싶은 모듈이나 함수들을 정의할 수 있음
- 이렇게 하면 패키지를 사용할 때, pkcalc.add 또는 pkcalc.sub와 같은 형태로 함수를 호출할 수 있게 됨
"""

from .calc import add, sub
