from typing import Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return RedirectResponse(url='https://taplink.cc/kfreelance')

@app.get("/verification.txt")
def read_item():
    return HTMLResponse(content="be19a4098d3d1fab16e7602d49296638e57f0411")
