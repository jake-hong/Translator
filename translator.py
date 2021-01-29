from googletrans import Translator

# 번역기 생성
translator = Translator()
# 언어감지
sentence = input("번역을 원하는 문장을 입력하세요 : ")
dest = input("어떤 언어로 번역을 원하시나요?")
result = translator.translate(sentence, dest)
detected = translator.detect(sentence)

print("\n============= 번역 결과 ============\n")
print(detected.lang, ":", result.origin)
print(result.dest, ":", result.text)
print("\n====================================\n")
