# 자료구조
## 1. 리스트

1.리스트는 여러 값을 가질 수 있고 각 값의 자료형은 다를 수 있습니다. 값의 중복을 허용하며 순서를 보장합니다.</br>

<형식> 리스트명 = [값1, 값2, ...]</br>

2.리스트는 인덱스로 값에 접근할 수 있습니다.</br>

<형식> 리스트명[인덱스]</br>

3.리스트에서 제공하는 주요 함수는 다음과 같습니다. 이 중에서 값을 반환하는 함수는 print() 문 안에서 바로 실행해 값을 확인할 수 있습니다. 값을 반환하지 않는 함수는 별도 문장으로 실행해야 하고, print() 문 안에서 실행해도 None이라고만 출력합니다.</br>

<table border = "1">
    <tr>
        <th>함수</th>
        <th>설명</th>
        <th>값 반환 여부</th>
    </tr>
    <tr>
        <td>index()</td> 
        <td>리스트 내 특정 데이터의 위치 반환</td>
        <td>O</td>
    </tr>
    <tr>
        <td1>append()</td>
        <td>리스트 맨 뒤에 데이터 추가</td>
        <td>X</td>
    </tr>
    <tr>
        <td1>insert()</td>
        <td>리스트의 정해진 위치에 데이터 삽입</td>
        <td>X</td>
    </tr>
    <tr>
        <td1>pop()</td>
        <td>리스트 뒤에서부터 데이터를 하나씩 꺼내어 반환한 뒤 삭제</td>
        <td>O</td>
    </tr>
    <tr>
        <td1>clear()</td>
        <td>리스트의 모든 데이터 삭제</td>
        <td>X</td>
    </tr>
    <tr>
        <td1>count()</td>
        <td>리스트에 포함된 데이터 개수 반환</td>
        <td>O</td>
    </tr>
    <tr>
        <td1>sort()</td>
        <td>리스트 내 데이터를 오름차순 또는 내림차순으로 정렬</td>
        <td>X</td>
    </tr>
    <tr>
        <td>reverse()</td>
        <td>리스트 내 데이터 순서 뒤집기</td>
        <td>X</td>
    </tr>
    <tr>
        <td1>extend()</td>
        <td>서로 다른 리스트 합치기</td>
        <td>X</td>
    </tr>
</table>

## 2. 딕셔너리

1.딕셔너리는 key와 value 한 쌍으로 이루어진 값들을 담기 위한 자료구조입니다. key는 중복을 허용하지 않으며 파이썬 3.7 버전부터 순서를 보장합니다.</br>

<형식> 딕셔너리명 = {key1: value1, key2: value2, ...}</br>

2.딕셔너리의 값에는 key를 통해 접근할 수 있습니다.</br>

<형식> 딕셔너리명[key]</br>

3.딕셔너리에서 제공하는 주요 함수는 다음과 같습니다.</br>

<table border = "1">
    <tr>
        <th>함수</th>
        <th>설명</th>
        <th>값 반환 여부</th>
    </tr>
    <tr>
        <td>get()</td>
        <td>key에 해당하는 value 반환</td>
        <td>O</td>
    </tr>
    <tr>
        <td>keys()</td>
        <td>모든 key 반환환</td>
        <td>O</td>
    </tr>
    <tr>
        <td>values()</td>
        <td>모든 value 반환</td>
        <td>O</td>
    </tr>
    <tr>
        <td>items()</td>
        <td>모든 key, value 반환</td>
        <td>O</td>
    </tr>
    <tr>
        <td>clear()</td>
        <td>딕셔너리의 모든 데이터 삭제</td>
        <td>X</td>
    </tr>
</table>

## 3. 튜플

1.튜플은 리스트와 비슷하지만, 한 번 정의한 값은 변경할 수 없습니다. 값의 중복을 허용하며 순서를 보장합니다.</br>

<형식> 튜플명 = (값1, 값2, ...)</br>

2.튜플의 값에는 인덱스로 접근할 수 있습니다.</br>

<형식> 튜플명[인덱스]</br>

3.튜플을 이용하면 변수들의 값을 손쉽게 뒤바꿀 수 있습니다.</br>

## 4. 세트

1.세트는 집합을 표현하기 위한 자료구조로, 값의 중복을 허용하지 않고 순서도 보장하지 않습니다.</br>

<형식> 세트명 = {값1, 값2, ...}</br>

2.세트에서 제공하는 주요 함수는 다음과 같습니다.</br>

<table border = "1">
    <tr>
        <th>함수</th>
        <th>설명</th>
        <th>값 반환 여부</th>
    </tr>
    <tr>
        <td>intersection()</td>
        <td>두 집합에서 공통 값을 뽑아내는 교집합</td>
        <td>O</td>
    </tr>
    <tr>
        <td>union()</td>
        <td>두 집합을 합치는 합집합</td>
        <td>O</td>
    </tr>
    <tr>
        <td>difference()</td>
        <td>한 집합에서 다른 집합의 값을 뺀 차집합</td>
        <td>O</td>
    </tr>
    <tr>
        <td>add()</td>
        <td>세트에 데이터 추가</td>
        <td>X</td>
    </tr>
    <tr>
        <td>remove()</td>
        <td>세트에서 데이터 삭제</td>
        <td>X</td>
    </tr>
</table>

## 5. 자료구조의 변환

자료구조는 필요에 따라 다른 자료구조로 변환할 수 있습니다.