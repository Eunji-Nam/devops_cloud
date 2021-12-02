# 다음 문자열에서 첫번째와 세번째 문자를 출력
letters = 'python'
# 실행 예 : p t
print(letters[0], letters[2])


# 자동차 번호 뒤에 4자리만 출력
license_plate = "24가 2210"
# 실행 예: 2210
print(license_plate[-4:])


# '홀' 만 출력
string = "홀짝홀짝홀짝"
# 실행 예: 홀홀홀
print(string[::2])


# 문자열을 거꾸로 뒤집어 출력
string1 = "PYTHON"
# 실행 예: NOHTYP
print(string1[::-1])


# 아래의 전화번호에서 하이푼('-')을 제거하고 출력
phone_number = "010-1111-2222"
# 실행 예 : 010 1111 2222
phone_number1 =phone_number.replace("-", " ")
print(phone_number1)


# 위 전화번호를 모두 붙여 출력
# 실행 예 : 01011112222
phone_number2 = phone_number.replace("-", "")
print(phone_number2)


# 웹 페이지 주소에서 도메인을 출력/split사용
url = "http://sharebook.kr"
# 실행 예: kr
url_do = url.split(".")
print(url_do[-1])


# 소문자 'a'를 대문자 'A'로 변경/replace 사용
string2 = 'abcdfe2a354a32a'
# 실행 예: Abcdfe2A354A32A
string3 = string2.replace("a", "A")
print(string3)

# '-'를 80개 출력
print("-"*80)


# 다음 문자열을 아래와 같이 출력
# python java python java python java python java
t1 = 'python'
t2 = 'java'
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)

# 변수에 다음과 같이 문자열과 정수를 % formatting을 사용해서 다음과 같이 출력
# 문자열의 format( ) 메서드를 사용
# f-string을 사용
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print()
print()
print()

# 삼성전자의 상장주식수의 컴마를 제거한 후 이를 정수 타입으로 변환
상장주식수 = "5,969,782,550"


# '2020/03'만 출력
분기 = "2020/03(E) (IFRS연결)"

# 문자열 좌우의 공백 제거
data = "   삼성전자    "

# 대문자 BTC_KRW로 변경
ticker = "btc_krw"

# 소문자 btc_krw로 변경
ticker = "BTC_KRW"

# 공백을 기준으로 문자열 나누기
a = "hello world"

# btc와 krw로 나누기
ticker = "btc_krw"

# 연도, 월, 일로 나누기
date = "2020-05-01"

# 문자열의 오른쪽에 공백 제거
data = "039490     "