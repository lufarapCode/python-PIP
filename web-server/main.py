import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

# 1er recurso
@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    html_content = """
    <html>
        <head>
            <title>Python</title>
        </head>
        <body>
            <h1>Página en Python</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

def run():
    store.get_categories()

if __name__ == '__main__':
    run()