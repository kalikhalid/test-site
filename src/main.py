from typing import Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse

app = FastAPI()

content = """
<h1>Здравствуйте! Это обращение предназначено сотрудникам модерации tome.ru.</h1>
<h2>Мой "магазин" работает на платформе Telegram как чат-бот, поэтому прошу проверить его по адресу:</h2>
<a href="https://t.me/kstudiopaybot">https://t.me/kstudiopaybot</a>
<h2>Если с магазином что-то не так прошу ответить мне на письмо которое я отправлял вам в поддержку 18.11.2024</h2>
"""

@app.get("/")
def read_root():
    return HTMLResponse(content=content)


@app.get("/verification.txt")
def read_item():
    return HTMLResponse(content="be19a4098d3d1fab16e7602d49296638e57f0411")
