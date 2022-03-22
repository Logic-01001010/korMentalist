from jamo import h2j, j2hcj

kordic = { 'ㄺ':'fr', 'ㅄ':'qt', 'ㅆ':'T', 'ㅖ': 'P', 'ㄶ':'sg', 'ㄸ':'E', 'ㅉ':'W', 'ㅃ':'Q', 'ㄲ':'R', 'ㅂ':'q', 'ㅈ':'w', 'ㄷ':'e', 'ㄱ':'r', 'ㅅ':'t', 'ㅛ':'y', 'ㅕ':'u', 'ㅑ':'i', 'ㅐ':'o', 'ㅔ':'p', 'ㅁ':'a', 'ㄴ':'s', 'ㅇ':'d', 'ㄹ':'f', 'ㅎ':'g', 'ㅗ':'h', 'ㅓ':'j', 'ㅏ':'k', 'ㅣ':'l', 'ㅋ':'z', 'ㅌ':'x', 'ㅊ':'c', 'ㅍ':'v', 'ㅠ':'b', 'ㅜ':'n', 'ㅡ':'m', 'ㅝ':"nj", 'ㅘ':"hk", 'ㅢ':"ml", 'ㅙ':"ho", 'ㅚ':"hl", 'ㅟ':"nl" }
특수기호 = {'1':'!', '2':'@', '3':'#', '4':'$', '5':'%', '6':'^', '7':'&', '8':'*', '9':'(', '0':')'}

start = []
mid = []
end = []

print("\n<KOR Mentalist: the password maker>\n")

print("\n상대방의 한글 성씨를 적으세요. 예) 김, 장, 박")
한글_성씨 = input("성씨 입력 > ")

print("\n상대방의 한글 이름을 적으세요. 예) 용환, 준혁, 미현")
한글_이름 = input("이름 입력 > ")

print("\n상대방의 영문 성씨를 적으세요. 예) jang, park, kim")
영어_성씨 = input("성씨 입력 > ")

print("\n상대방의 영문 이름을 적으세요. 예) minji, jisung")
영어_이름 = input("이름 입력 > ")

print("\n상대방의 전화번호를 적으세요. 예) 010-1234-5678")
전화번호 = input("이름 입력 > ")
전화번호1, 전화번호2 = 전화번호.split('-')[1], 전화번호.split('-')[2],


print("\n상대방의 생년월일을 적으세요. 예) 980214, 951224")
생년월일 = input("이름 입력 > ")
생년월일1, 생년월일2 = 생년월일, 생년월일[2:]


k1 = ""
k2 = ""
e1 = 영어_성씨
e2 = 영어_이름

for jamo in j2hcj(h2j(한글_성씨)):
	k1 += kordic[jamo]
for jamo in j2hcj(h2j(한글_이름)):
	k2 += kordic[jamo]	

k1 = k1.lower()
k2 = k2.lower()
e1 = e1.lower()
e2 = e2.lower()

성이름 = k1 + k2
	
# 이름
start.append(k1)
start.append(k2)	
start.append(성이름)
start.append(e1)
start.append(e2)

start.append( k1[0].upper() + k1[1:] )
start.append( k2[0].upper() + k2[1:] )
start.append( 성이름[0].upper() + 성이름[1:] )
start.append( e1[0].upper() + e1[1:] )
start.append( e2[0].upper() + e2[1:] )

# 전화번호 / 생년월일
mid.append(전화번호1)
mid.append(전화번호2)
mid.append(생년월일1)
mid.append(생년월일2)
if 생년월일2[0] == '0':
	mid.append(생년월일2[1:])


# 특수기호
end.append("")
end.append("!")
end.append("@")
end.append("#")

if 특수기호[ 전화번호1[-1] ] not in end:
	end.append(특수기호[ 전화번호1[-1] ])
if 특수기호[ 생년월일[-1] ] not in end:
	end.append(특수기호[ 생년월일[-1] ])
	
	
count = 0
f = open('output_passwords.txt', 'a')



for s in start:

	for m in mid:
	
		for e in end:
		
			count += 1
			f.write( s + m + e + "\n" )
			
			
print( "\n" + str(count) + "개의 패스워드 생성.\a")
print("출력된 파일 이름: " + "output_passwords.txt\n")
