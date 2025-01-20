### 자료형
  - 문자열 포매팅. % 사용하거나, .format() 함수, f'{}' 사용하는게 제일 편함.
  - 문자열 내장함수 : 문자열 뒤에 . 붙여서 사용하는 내장함수 count, find, index, replace, split, join, strip 등

---

### 제어문, 반복문	
- if문 : if 조건1 실행1 elif 조건2 실행2 else 실행3
- while문 : while 뒤에 조건을 만족할때까지 반복. while True 는 무한루프.
- Break는 반복문 즉시종료. Continue 는 반복문의 처음으로 돌아감 (건너뛰기). Pass 는 아무작업을 안함.

---

### 사용자함수 
- 매개변수(parameter)에 실제 할당하는 값은 인수(arguments)
- 매개변수가 몇 개일지 모를때 *args를 사용
- 매개변수에 key= value 쌍으로 입력값을 넣을때 **kwargs를 사용. 그러면 kwargs에 딕셔너리로 저장함
- 매개변수에 초기값을 줘도되는데, 그때는 맨 뒤에 놓을 것.
- Lambda 로 간단한 함수 만들기 가능. Lambda 매개변수 : 반환값 (여기 제어문,반복문 사용가능) 

---

### 파일읽고쓰기
- Open 함수로 열고, 모드를 r/w/a 중에 정해서 연다. W는 새로 새로 파일을 만들어 쓰는것
- Open으로 열면 close로 닫아줘야하기에 주로 with 함수를 이용해서 파일을 연다. With open() as f:
- 함수의 내용을 읽으려면 readline(), readlines(), read() 등의 함수사용, 쓰는데는 write() 사용
- 명령 프롬프트에서 실행시키려면 sys 모듈로 sys.argv에 인수전달

---

### 클래스
- 객체, 인스턴스, 매서드, 속성 개념의 이해
- 생성자(__init__) 을 통해 객체변수(속성; attribute)를 정의.
- 클래스의 상속 class Child(Parent): 부모 클래스의 속성과 매서드를 사용가능.
- __call__ 매서드를 활용하면 객체.매서드(인자) 대신 객체(인자)로 간단히 표현가능 

---

### 모듈, 패키지, 디렉터리, 피클
- 함수,변수,클래스의 모아둔 파이썬 파일(.py). 직접만든 파일일수도 있고 내장,외부 모듈일수도있음
- 불러올때는 import 모듈, from 모듈 import 매서드
- sys.path 는 파이썬 라이브러리 설치된 모든 디렉터리 목록. 여기 있는 모듈은 바로 불러오기 가능. 여기 없으면 sys.path.append 로 경로추가 후 모듈 불러오기
- 관련 모듈들의 집함. 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해줌.
- 패키지의 __init__.py 파일의 목적 ; 패키지 수준의 변수,함수 정의 및 초기화 코드.
- glob.glob 표준 라이브러리로 특정 디렉터리에 있는 모든파일(*) 특정파일(4*-*.py) 리스트 반환
- os 모듈의 os.path 서브모듈을 통해 파일과 디렉터리 경로를 확인하고, 일부를 뽑아내고, 합치는 등 기능함
- pathlib 을 이용하면 쉽게 파일과 디렉터리의 경로와 관련된 업무를 할수있음
- 피클(pickle)은 "객체의 형채를 그대로 유지"하면서 파일에 저장 (dump), 불러오는 (load) 모듈
- JSON 데이터는 json 모듈을 활용해 읽고쓰기 가능. json파일로 부터 load를 통해 딕셔너리로 받고, dump를 통해 딕셔너리를 저장함.
- 패키지 안에서 서로다른 서브 디렉터리의 모듈끼리 불러오기 ..
- shutil 모듈을 활용하여 파일을 복사하거나 이동시키기
- 본 모듈에서만 실행하고자 하는 경우 (스크립트로 직접 실행, 외부에서 import 시 실행 x), if __name__ == '__main__' 사용 

---

### 예외(오류)처리
- 예외(오류)가 발생했을때, try-except, try-except-else, try-except-finally 구문 사용
- Try: 실행문 except: 예외발생시 실행문
- Except (IndexError, ZeroDivisionError) as e: () 안에 에러 발생시에만 except 동작.
- finally: 오류발생 상관없이 항상 실행할 코드 / else : 오류발생 하지 않았을때 동작하는 절
- 파이썬 내장 클래스인 Exception 클래스를 상속해서 예외를 만들수도 있음
- 오류추적 : except 구문에 traceback.format_exc() 를 포함하면 오류추적 문자 반환함. 

---

### 내장함수
- Iterable 객체에서 all 과 any 사용. Enumerate로 iterable을 인덱스와 함께 반환.
- filter(함수, iterable) 는 iterable 을 각 함수 대입해 참인 값만 필터링 반환.
- map(함수, iterable) 는 iterable 을 각 함수에 대입한 값을 반환.
- map 과 filter 의 결과물은 보통 list 로 씌워서 출력함.
- zip(*iterable) 은 크기가 같은 여러 개 iterable 객체끼리 동일 인덱스 기준으로 묶음
- dir() 로 객체에 사용가능한 함수들 반환 / eval() 로 문자열로 된 표현식 실행
- isinstance(객체, 클래스)로 객체가 해당 클래스에 소속하는지 확인. 

---

### 🟩표준(내장)라이브러리
- datetime 라이브러리로 날짜와 시간 객체 생성 : datetime.date, datetime.datetime / timedelta 로 연산가능
- 그렇게 생성한 객체에서 월/일/시간/요일 등을 뽑기. 정수로 뽑기 -> .month, .minute 문자로뽑기 -> .strftime()
- time 모듈은 좀더 초단위, 시스템 시간관련 사용. Time.time() 으로 시간을 실수로 만들고 localtime(), asctime(), ctime(), strftime() 등으로 포맷을 변경가능함. Time.sleep() 을 사용하여 지연을 만들수도.
- math() 라이브러리를 통해 올림,내림,지수,로그 등 각종 연산기능 수행.
- random() 모듈을 통해 난수 행성. 리스트와 같은 객체의 값들을 섞거나 .shuffle 랜던뽑기 가능 .choice
- statistics 모듈을 통해 평균,중앙,편차,분위수 등 통계값을 구함
- itertools 라이브러리는 iterable 객체에 사용가능한 응용도구들 .zip_longest 는 zip인데 길이 안맞는 객체들 맞춰줌. .permutations 이나 .combinations 로 순열이나 조합 구함
- functools.reduce(function, iterable) 은 function 을 iterable 의 요소 왼쪽부터 오른쪽을 차례로 누적 적용
- operator.itemgetter 는 sorted 와 같은 함수의 key 매개변수로 사용하여 정렬 기준으로 사용
- os 모듈은 os자원 제어하는 모듈. 환경변수값, PATH 환경변수값 반환, chdir() 로 디렉터리 위치 변경, getcwd() 로 현재 디렉터리 위치 받기 등
- sys 모듈을 통해 인터프리터가 인수를 리스트로 받아 (sys.argv) 프로그래밍 하도록함. -> 명령줄에서 전달된 인자를 리스트로 받아 행하는 방법. (간단 스크립트에 적합)
- 보다 복잡한 명령줄에는 argparse 모듈이 적합.  argparse.ArgumentParser() 를 통해 명령줄 인자를 파싱하고 정의함. 인자별로 정의해주는 방식.

---
	
### 외부라이브러리
- faker 라이브러리의 Faker 사용하여 가짜 데이터 (사람이름,주소 등) 생성
- fractions 를 통해 유리수 만들기 fractions.Fraction(분자,분모) 로 유리수 생성
- sympy 를 통해 방정식 기호를 사용및 계산.  .symbols('x') 로 변수 생성, .Eq(x*Fraction(2,5), 1760) 과 같이 방정식 생성. .solve() 로 방정식 해 구하기 ()안에 리스트로 방정식 여러 개 넣으면 연립방정식 구함. 

---

### 유니코드, 인코딩
- 아스키코드(ASCII) 는 초기 표준으로 영어/숫자만 매핑. 현대는 유니코드(unicode; utf-8)가 세계 표준.
- 이 표준 코드는 우리의 문자열을 0,1 로 바꾸어 주는 표준체계.
- 파이썬 문자열은 모두 유니코드 문자열, 인코딩하면 바이트가 됨. 인코딩 = 문자열 → byte 전환과정 (↔디코딩)
- 문자열.encode('방식') 으로 인코딩 , 바이트.decode('방식') 으로 디코딩 

---

### 클로저, 데코레이터
- 함수안에 내부 함수를 구현하고, 그 내부함수를 리턴하는 외부함수를 클로저라고함.
- 데코레이터는 기존 함수를 바꾸지 않고 기능을 추가할 수 있도록하는 클로저. 인수로 함수를 받는 클로저
- @를 이용해서 데코레이터를 사용할 수도 있음. 

---

### 이터레이터, 제너레이터
- 이터레이터는, Iterable 하면서 next 함수로 계속 다음값을 반환하고, 한번 읽으면 사라지는 특징.
- iter() 함수를 통해 만들거나, 커스터마이징이 필요하면 클래스로 만들수 있음
- 제너레이터는, 이터레이터를 생성하는 '함수'.  return 대신 yield로 결과를 차례대로 반환
- 제너레이터를 리스트 컴프리헨션 처럼 제너레이터 표현식으로 만들수도 있음
	
---

### 정규표현식
- 정규 표현식을 사용하는 이유 ? 복잡한 문자열에서 특정 패턴을 효율적으로 검색, 추출, 변환하기 위해 사용
- 메타문자(. ^ * $ + 등 원래 그 문자가 가진 뜻이 아닌 특별한 의미를 가진 문자)를 사용하여 복잡한 문자열을 처리하는 방법.  re(regular expression) 모듈을 통해 실행됨
- [] 문자 클래스 : [a-d] [1-8] [a-zA-Z]
- 역슬래시 정규 표현식 \d \D \s \S \w \W
- .(dot)/*/+/?/{} 등을 이용한 정규표현식
- 여러가지 정규표현식을 통해 re.compile 매서드로  '컴파일한 객체(패턴)'를 만든다. p = re.compile('[a-z]+')
- '컴파일된 패턴 객체'는 4가지 매서드 제공 (match, search, findall, finditer) : 문자열에서 정규표현식과 매치되는 부분을 조사하고 반환. 그 리턴 결과를 '매치(match) 객체'라고 함. 또한 sub 매서드를 사용하여 정규식과 매치되는 부분을 다른문자로 바꿀 수 있음.
- '매치(match)객체' 는 4가지 매서드를 제공 (group, start, end, span) : 매치된 문자열 자체, 시작/끝 위치 인덱스를 반환.
- 컴파일(re.comiple) 할때 몇가지 옵션을 사용 가능 (DOTALL, IGNORECASE, MULTILINE, VERBOSE 등) 매치할때 대소문자 관계없이 하거나, 여러 줄과 매치될수 있게 해준다는 등..)
- 컴파일 할때 그루핑을 할 수 있음. p = re.compile(r'(\w+)\s+((\d+)[-]\d+[-]\d+)')
	
---

### 🔶표준 라이브러리 응용
- textwrap 모듈 (.shorten, .wrap, .fill) 을 활용해 문자열을 원하는 길이에 맞게 줄이거나, 잘라서 리스트 형태로 반환
- 정규표현식 re모듈을 활용해 특정 패턴으로 컴파일한 객체를 만들고 그 객체를 통해 문자열을 분석 및 변경
- collections 모듈을 활용
  - deque 라는 객체를 만들 수 있음. 리스트, 튜플등을 데크자료형으로 만들면 앞/뒤에서 데이터를 양방향으로 처리 가능.  rotate로 회전하거나, appendleft, popleft 등 가능.
  - namedtuple 을 만들 수 있음. 튜플은 인덱스를 통해 데이터에 접근, 네임드튜플은 인덱스뿐 아니라 키(key)로 접근이 가능.
  - Counter 를 활용하면, 리스트나 문자열과같은 자료형에서 각 요소가 몇 개인지 셀 수 있음. re 정규표현식과 같이 활용하면 문장내에 각 단어들의 빈도를 셀 수 있음.
- 우선순위 큐 구현.  heapq 모듈을 이용. 힙 데이터를 생성하면 데이터를 꺼낼 때 순위대로 꺼낼 수 있음.
- pprint(pretty print) 를 통해 데이터를 보기좋게 출력할 수 있음.
- 이진 탐색 알고리즘. bisect 모듈은 데이터를 구분할 기준점들을 만들어두고 인덱스를 반환하게함. 점수 리스트가 있을때 특정 점수 커트라인으로 A~F 학점 등급 매기기 등
- 위상 정렬 (topological sorting) 순환하지 않는.. 선수과목 문제와 같은 그래프 규칙을 구현하는 방법. TopologicalSorter 모듈을 이용함.
- csv 모듈을 이용하면 csv 파일을 리스트나 딕셔너리 형태로 읽거나, 리스트나 딕셔너리 객체를 csv 파일에 직접 쓸수도 있다.
- 시스템 정보를 확인하려면 (PC사양 등) platform 모듈을 활용
- sched 모듈을 활용하면, 지정된 시간(시차)로 원하는 이벤트(함수)를 실행하는 이벤트 스케쥴러를 만들 수 있음. 

---

### HTTP, API 
- requests 모듈을 활용하여 HTTP의 매서드 (GET, POST, PUT 등) 를 테스트함 : API 통신, 웹 페이지 요청 등
  - REST API (인터넷에 있는 컴퓨터=서버 와 대화하는 주소와 규칙의 모음)
- requests.get() 으로 조회, requests.post() 으로 포스팅 및 저장, requests.post() / .patch()로 수정

---

## 🔷넘파이와 판다스 


### Numpy
- 넘파이는 배열(array, numpy.ndarray) 이라는 객체를 만들고, 이를 통해 선형대수와 통계연산을 하는데 매우 유용한 라이브러리
- np.array() 혹은 np.arange() 로 배열을 만들고, 객체.shape 으로 차원을 확인하고, 객체.reshape() 으로 차원을 변경함
- 객체[2:5,:,[3,0,2]] 와 같은 방법으로 배열의 일부를 인덱싱 또는 슬라이싱하고, np.sort() 혹은 객체.sort()로 정렬함. np.argsort()로 정렬된 배열의 인덱스를 반환함
- 행렬 곱(내적) 이나 전치행렬과 같은 행렬계산 가능함. np.dot(), np.transpose()


### Pandas
- 데이터프레임(DataFrame) 과 시리즈(Series) 형태의 객체로 데이터를 다루기 위한 라이브러리
- csv 파일을 read_csv() 를 통해 dataframe 이나 series 형태로 받음.
- DataFrame의 구조는 info(), 통계값은 describe(), 항목별 개수는 value_counts() 를 통해 요약해서 볼 수 있음.
- 배열(ndarray), 리스트, 딕셔너리 → 데이터프레임 : pd.DataFrame() 을 통해 변환
- 데이터프레임 → 배열(ndarray), 리스트, 딕셔너리 : df.values , df.values.tolist() , df.to_dict() 를 통해 변환
- 데이터프레임의 칼럼 생성/수정/삭제(행,열). 특히 기존 컬럼을 이용해 수정/생성할때는 apply lambda 가 유용함 : df['age_cat'] = df['age'].apply(lambda x: 'child' if x <= 25 else 'Adult' )
- 데이터프레임의 데이터 셀렉션은 불린 인덱스 : df[ (df['Age']>=60) & (df['Sex'] == 1) ] 과 같이 사용. 넘파이의 인덱싱, 슬라이싱 방식은 잘 안씀.
- 인덱싱/슬라이싱은 loc[], iloc[] 를 통해서 함.  loc 는 명칭기반, iloc 는 인덱스 기반
- 특정 컬럼을 기준으로 내림/오름 차순 정렬 가능 .sort_values(by=, ascending=)
- 특정 컬럼을 기준으로 aggregation (min,max,sum,count 등) df.[[c1,c2]].sum() 을 할 수 있음. agg() 함수와 groupby()를 활용하면 특정 컬럼의 값을 기준으로 특정 컬럼마다 다른 기준으로 aggregation이 가능함.
- 결손 데이터 (NULL) 는 isna() 와 fillna()를 통해 컬럼별 결손값을 확인하거나 대체함.
