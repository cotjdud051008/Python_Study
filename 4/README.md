# 문자열 다루기
## 1. 문자열

1.문자열은 문자들의 집합을 의미합니다</br>

2.파이썬에서는 작은따옴표 또는 큰따옴표로 감싸서 문자열임을 나타냅니다.</br>

3.문자열을 여러 줄에 거쳐 작성하는 경우 같은 종류의 여는 따옴표와 닫는 따옴표를 각각 3개씩 넣어 앞뒤로 감싸 주면 됩니다.</br>

## 2. 슬라이싱

1.원하는 만큼 데이터를 자르는 것을 슬라이싱이라고 합니다. 슬라이싱할 때는 데이터의 순서 또는 위치를 나타내는 인덱스를 이용합니다. 인덱스는 0부터 시작하며 변수명 뒤의 대괄호 안에 숫자를 넣어 표시합니다.</br>

<형식> 변수명[인덱스]

2.슬라이싱은 인덱스로 자르려는 시작 위치와 끝 위치를 정할 수 있습니다. 변수명 뒤 대괄호 안에 콜론(:)으로 구분해 시작 인덱스와 종료 인덱스를 넣으면 시작 인덱스로부터 종료 인덱스 직전 위치까지의 데이터를 잘라오게 됩니다.</br>

<형식> 변수명[시작 인덱스 : 종료 인덱스]

3.슬라이싱할 때 시작 인덱스나 종료 인덱스 또는 둘 다를 생략할 수 있는데, 의미는 각각 다음과 같습니다.</br>
ㆍ 변수명[:종료 인덱스]: 처음부터 종료 인덱스 직전까지 슬라이싱</br>

ㆍ 변수명[시작 인덱스:]: 시작 인덱스부터 끝까지 슬라이싱</br>

ㆍ 변수명[:]: 처음부터 끝까지 슬라이싱</br>

4.앞에서부터가 아니라 뒤에서부터 슬라이싱하려면 음수 인덱스를 사용하고, 음수 인덱스는 -1부터 시작합니다.

## 3. 문자열 처리 함수

1.파이썬에서는 문자열을 다루기 쉽도록 많은 함수를 제공합니다.</br>

<table border ="1">
    <tr>
        <th>함수</th>
        <th>의미</th>
    </tr>
    <tr>
        <td>lower()</td>
        <td>문자열을 소문자로 변환</td>
    </tr>
    <tr>
        <td>upper()</td>
        <td>문자열을 대문자로 변환</td>
    </tr>
    <tr>
        <td>islower()</td>
        <td>문자열이 소문자인지 확인</td>
    </tr>
    <tr>
        <td>isupper()</td>
        <td>문자열이 대문자인지 확인</td>
    </tr>
    <tr>
        <td>replace()</td>
        <td>문자열 바꾸기</td>
    </tr>
    <tr>
        <td>index()</td>
        <td>찾는 문자열의 인덱스(없으면 오류 발생)</td>
    </tr>
    <tr>
        <td>find()</td>
        <td>찾는 문자열의 인덱스(없으면-1 반환)</td>
    </tr>
    <tr>
        <td>count()</td>
        <td>문자열이 나온 횟수</td>
</table>

2.문자열 처리 함수는 다음과 같은 형식으로 사용합니다. 함수 종류에 따라 소괄호 사이에 값을 넣어야 하는 경우도 있습니다.</br>

<형식> 문자열.함수()

## 4. 문자열 포매팅

1.문자열 포매팅은 원하는 위치에 특정한 값(또는 변수)를 넣어서 하나의 문자열로 표현하는 방법입니다.</br>

2.<b>서식 지정자</b>: 자료형을 표현하는 방법으로 정수(%d), 실수(%c), 문자열(%s)과 같이 %뒤에 자료형을 나타내는 문자가 붙습니다.</br>

<형식> print("문자열 서식지정자 문자열" % 값)</br>

3.<b>format()함수</b>: 문자열에서 값을 넣을 위치에 중괄호({})를 표시하고 뒤에 format(값1, 값2, ...)형태로 값을 입력합니다. 인덱스를 생략하고 {}만 적으면 format() 함수 안 값들이 {} 위치에 순서대로 들어갑니다.</br>

<형식> print("문자열{인덱스}문자열{인덱스}...".format(값1, 값2,...))</br>

4.<b>f-문자열</b>: 문자열 앞에 f를 추가하면 앞에 정의한 변수의 값을 사용할 수 있습니다(파이썬 3.6 버전 이상)</br>

<형식> print(f"문자열{변수명1}문자열{변수명2}...")

## 5. 탈출 문자

큰따옴표(")나 작은따옴표(')와 같이 문자열 안에서 직접 사용하기 어려운 문자를 쓰거나 특정 동작을 수행하기 위해 사용하는 것이 탈출 문자입니다. 탈출 문자는 역슬래시(\)와 문자가 결합한 형태입니다.</br>

ㆍ \n : 줄 바꿈</br>

ㆍ \" : 큰따옴표</br>

ㆍ \' : 작은따옴표</br>

ㆍ \\ : 역슬래시</br>

ㆍ \r : 커서를 맨 앞으로 이동</br>

ㆍ \b : 백스페이스</br>

ㆍ \t : 탭