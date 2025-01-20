''' 
명령 프롬프트에서는 아래와 같이 파일이름을 인수로 받아 파일 내용을 출력받는다. 
G:\내 드라이브\파이썬공부> type 새파일.txt
이러한 기능을 파이썬 프로그램에도 적용할 수 있다. 
4.3장-프로그램의 입출력
'''
# sys모듈을 통한 프로그램에 인수 전달 
import sys

# argv는 프로그램(=지금 만들고 있는 파일) 실행 시 전달된 인수를 의미함
args_origin = sys.argv    # argv = argument value 
print(args_origin)
print(111111)

args = sys.argv[1:]
for i in args:
    print(i, end=' ')
    print(i.upper(), end=' ')

'''
본 파일(=프로그램)을 cmd에서 실행해보면 이해할 수 있다
cmd 창에 아래와 같이 입력 
python "G:\내 드라이브\파이썬공부>python 4.3장-프로그램입출력.py" life is good
'''

