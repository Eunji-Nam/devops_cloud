# 화면에 Hello World 문자열을 출력
print('Hello World')

# 화면에 Mary's cosmetics을 출력
print("Mary's cosmetics")

# 신씨가 소리질렀다. "도둑이야". -> 출력
print('신씨가 소리질렀다. "도둑이야".')

# 화면에 "C:\Windows"를 출력
print('"C:\window"')

# naver;kakao;sk;samsung을 출력
print("naver", "kakao", "sk", "samsung", sep=';')

# naver/kakao/sk/samsung을 출력
print("naver", "kakao", "sk", "samsung", sep='/')

# 5/3의 결과를 화면에 출력
print(5/3)

# 삼성전자라는 변수로 50,000원을 바인딩한 후, 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력
삼성전자 = 50_000
print(삼성전자 * 10)


# 두 변수를 이용하여 아래와 같이 출력해보세요.
s = "hello"
t = "python"
# 실행 예: hello! python
print(s+"!", t)


# 문자열 '720'를 정수형으로 변환
num_str = "720"
print(type(int(num_str)))

# 정수 100을 문자열 '100'으로 변환
num = 100
print(type(str(num)))


# 월 48,584원/ 무이자 36개월로 판매되고 있는 에어컨의 총 금액을 계산한 후 출력(변수사용하기)
월_에어컨_금액 = 48_584
에어컨_총금액 = 월_에어컨_금액 * 36
print(에어컨_총금액)
