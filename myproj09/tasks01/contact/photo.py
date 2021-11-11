import telegram

def check_available(received_text: str) -> bool:
    return received_text == "고양이 사진"

def make_response(received_text: str) -> str:
    image = 'kitten.jpg'
    return sendPhoto(open(image,'rb'))
