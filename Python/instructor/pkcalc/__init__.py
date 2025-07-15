"""
1. __init__.py 란?
pkcalc 폴더가 패키지로 인식되기 위한 파일
- 패키지 외부로 노출하고 싶은 모듈이나 함수들을 정의할 수 있음
- 이렇게 하면 패키지를 사용할 때, pkcalc.add 또는 pkcalc.sub와 같은 형태로 함수를 호출할 수 있게 됨

2. 패키지를 사용하는 예시
    - 패키지를 사용할 때 내부 모듈 경로를 신경 쓰지 않고, 바로 필요한 함수를 import하여 사용할 수 있음
        # 패키지를 사용하고 싶은 다른 파일에서
        from pkcalc import add, sub

        result1 = add(3, 5)  # 8을 반환
        result2 = sub(10, 4)  # 6을 반환

        print(result1)  # 8 출력
        print(result2)  # 6 출력
"""

from .calc import add, sub
