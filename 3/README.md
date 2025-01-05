# 연산자
## 1. 연산자

연산자는 프로그래밍에서 연산할 때 사용하는 기호입니다.</br>

ㆍ산술 연산자: 덧셈, 뺄셈, 곱셈, 나눗셈 등 수를 연산하는 데 사용합니다.</br>

ㆍ비교 연산자: 값의 크기를 비교할 때 사용합니다.</br>

ㆍ논리 연산자: 수식, 조건 등에서 값이 참인지 거짓인지 판단할 때 사용합니다.</br>

## 2. 연산자의 우선순위

연산자에는 우선순위가 있어서 수식을 어떻게 작성하느냐에 따라 연산 순서가 달라질 수 있습니다.</br>
<table border = "1">
    <tr> 
        <th>우선순위</th>
        <th>연산자</th>
        <th>설명</th> 
        </tr>
    <tr>
        <td rowspan = "7"> 높음 -> 낮음</td>
        <td> [], {}, ()</td>
        <td> 리스트, 딕셔너리, 세트, 튜플</td>
        </tr>
    <tr>
        <td> ** </td>
        <td> 거듭제곱 </td>
        </tr>
    <tr>
        <td> *, /, //, % </td>
        <td> 곱셈, 나눗셈, 정수 나눗셈, 나머지 </td>
    <tr>
        <td> +, - </td>
        <td> 덧셈, 뺄셈 </td>
    <tr>
        <td> not, in, <, <=, >, >=, !=, == </td>
        <td> 부정, 비교 연산자 </td>
        </tr>
    <tr>
        <td> and, or </td>
        <td> 논리 연산자 </td>
        </tr>
    <tr>
        <td> = </td>
        <td> 대입 연산자 </td>
        </tr>

</table>

## 3. 변수로 연산하기

연산을 쉽게 하기 위해 변수에 연산 결과를 저장한 뒤 새로운 연산에 활용할 수 있습니다. 이때 복합 대입 연산자를 사용하면 더욱 간소한 형태로 연산이 가능합니다. 

<table border="1">
    <tr>
        <th>연산자</th>
        <th>의미</th>
        <th>예</th>
    </tr>
    <tr>
        <td>+=</td>
        <td>연산자 왼쪽 값에 오른쪽 값을 더한 후 왼쪽 값에 대입</td>
        <td>number = number + 2 -> number += 2</td>
    </tr>
    <tr>
        <td>-=</td>
        <td>연산자 왼쪽 값에서 오른쪽 값을 뺀 후 왼쪽 값에 대입</td>
        <td>number = number - 2 -> number -= 2</td>
    </tr>
    <tr>
        <td>*=</td>
        <td>연산자 왼쪽 값에 오른쪽 값을 곱한 후 왼쪽 값에 대입</td>
        <td>number = number * 2 -> number *= 2</td>
    </tr>
    <tr>
        <td>/=</td>
        <td>연산자 왼쪽 값을 오른쪽 값으로 나눈 후 왼쪽 값에 대입</td>
        <td>number = number / 2 -> number /= 2</td>
    </tr>
    <tr>
        <td>**=</td>
        <td>연산자 왼쪽 값을 오른쪽 값으로 거듭제곱한 후 왼쪽 값에 대입</td>
        <td>number = number ** 2 -> number **= 2</td>
    </tr>
    <tr>
        <td>//=</td>
        <td>연산자 왼쪽 값을 오른쪽 값으로 나눈 후 몫을 왼쪽 값에 대입</td>
        <td>number = number // 2 -> number //= 2</td>
    </tr>
    <tr>
        <td>%=</td>
        <td>연산자 왼쪽 값을 오른쪽 값으로 나눈 후 나머지를 왼쪽 값에 대입</td>
        <td>number = number % 2 -> number %= 2</td>
</table>

## 4. 함수로 연산하기

파이썬에서는 다양한 연산을 편리하게 할 수 있도록 여러 함수를 제공합니다.
<table border="1">
    <tr>
        <th>함수</th>
        <th>의미</th>
    </tr>
    <tr>
        <td>abs(x)</td>
        <td>x의 절대값</td>
    </tr>
    <tr>
        <td>pow(x, y)</td>
        <td>x를 y만큼 거듭제곱한 값</td>
    </tr>
    <tr>
        <td>max()</td>
        <td>가장 큰 값</td>
    </tr>
    <tr>
        <td>min()</td>
        <td>가장 작은 값</td>
    </tr>
    <tr>
        <td>round(x,d)</td>
        <td>x를 반올림한 값, d는 표시할 소수점 이하 자릿수, d가 없으면 소수점 이하 첫째 자리에서 반올림한 정수</td>
</table>

## 5. math 모듈

1. math 모듈에도 숫자 연산을 수행하는 함수들이 들어 있습니다.

<table border = "1">
    <tr>
        <th>함수</th>
        <th>의미</th>
    </tr>
    <tr>
        <td>floor()</td>
        <td>내림</td>
    </tr>
    <tr>
        <td>ceil()</td>
        <td>올림</td>
    </tr> 
    <tr>
        <td>sqrt()</td>
        <td>제곱근</td>
</table>

2. 모듈의 기능을 사용하려면 다음과 같이 import를 먼저 해야 합니다.

<형식> from 모듈명 import 기능

## 6. random 모듈

random 모듈에는 난수가 필요한 경우에 사용하는 함수들이 있습니다. 함수에 따라 마지막 값을 포함하는지 아닌지가 달라질 수 있으니 주의해야 합니다.

<table border = "1">
    <tr>
        <th>함수</th>
        <th>의미</th>
    </tr>
    <tr>
        <td>random()</td>
        <td>0 이상 1 미만의 실수인 난수 생성</td>
    </tr>
    <tr>
        <td>randrange(시작 숫자, 끝 숫자)</td>
        <td>주어진 범위 안에서 정수인 난수 생성(끝 숫자 미포함)</td>
    </tr>
    <tr>
        <td>randint(시작 숫자, 끝 숫자)</td>
        <td>주어진 범위 안에서 정수인 난수 생성(끝 숫자 포함)</td>
</table>