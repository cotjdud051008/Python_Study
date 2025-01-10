# 제어문

## 1. if 문

코드에서 조건에 따른 분기가 필요할 때 사용합니다. if 조건이 참일 때 실행할 명령들은 들여쓰기를 해서 구분합니다.</br>

<형식> if 조건:  
<p style="text-indent:70px">실행할 명령</br>

## 2. elis 문

코드에서 분기 조건이 여러 개일 때 사용합니다. if 문에 이어서 elif 문은 여러 번 사용할 수 있습니다.</br>

<형식> if 조건1: 
<p style="text-indent:70px"> 실행할 명령1</p>
<p style="text-indent:50px">elif 조건2:</p>
<p style="text-indent:70px"> 실행할 명령2</p>
<p style="text-indent:50px">elif 조건3:</p>
<p style="text-indent:70px"> 실행할 명령3</p>
<p style="text-indent:50px">. . .</p>

## 3. else 문

if 문과 elif 문의 조건에 모두 해당하지 않을 때 실행할 명령을 정의합니다. else 문은 생략할 수 있습니다.</br>

<형식> if 조건1:
<p style="text-indent:70px"> 실행할 명령1</p>
<p style="text-indent:50px">elif 조건2:</p>
<p style="text-indent:70px"> 실행할 명령2</p>
<p style="text-indent:50px">elif 조건3:</p>
<p style="text-indent:70px"> 실행할 명령3</p>
<p style="text-indent:50px">. . .</p>
<p style="text-indent:50px">else:</p>
<p style="text-indent:70px"> 실행할 명령n</p>

## 4. for 문

같은 동작을 여러 번 반복해서 수행하기 위해 사용합니다. 보통 반복 대상에 정해진 횟수만큼 반복합니다.</br>

<형식> for 변수 in 반복대상:
<p style="text-indent:70px"> 실행할 명령1</p>
<p style="text-indent:70px"> 실행할 명령2</p>
<p style="text-indent:70px"> . . .</p>

## 5. while 문

같은 동작을 여러 번 반복해서 수행하기 위해 사용합니다. 보통 주어진 조건을 만족하는 동안 끝없이 반복합니다.</br>

<형식> while 조건:
<p style="text-indent:70px"> 실행할 명령1</p>
<p style="text-indent:70px"> 실행할 명령2</p>
<p style="text-indent:70px"> . . .</p>

## 6. continue

반복문에서 해당 반복을 건너뛰고 다음 반복으로 넘어가기 위해 사용합니다. continue를 만나면 이후 문장들은 실행하지 않고 다음 반복으로 넘어갑니다.</br>

## 7. break

반복문을 탈출할 때 사용합니다. break를 만나면 이후 문장들은 실행하지 않고 즉시 반복문을 빠져나옵니다.