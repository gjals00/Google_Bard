import bardapi
import os


os.environ['_BARD_API_KEY'] = "YQh7pcL2ubupO5q8lUsrlbkkyzKNBcEAPc_7dPzYvep67HzN22yFKrloub0OrIyxAewlAQ."


# 질문작성
input_text = "대한민국 일산 이번주 날씨"

# 바드 대답
response = bardapi.core.Bard().get_answer(input_text)

for i, choice in enumerate(response['choices']):
    print(f"Choice {i+1}:\n", choice['content'][0], "\n")



# 0. sudo apt update -> sudo apt install python3 -> python3 --version

# 1. pip install bardapi

# 2. os.environ['_BARD_API_KEY'] = "xxxxxxxxx.......xx"

# 3. F12 -> Application -> Cookies -> https://www.bard.google.com -> _Secure-1PSID -> KEY 값 입력