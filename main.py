from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return ("""<h1 id="h1">Hello, world!</h1>
    <h2>Hello, Again</h2>
    <script>document.getElementById("h1").style.color="red";</script>""")
