from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI(title="OAuth Callback API", version="1.0.0")


@app.get("/oauth/callback", response_class=HTMLResponse)
async def oauth_callback(request: Request):
    code = request.query_params.get("code")
    state = request.query_params.get("state")
    print(f"Received code: {code}")
    print(f"Received state: {state}")
    return f"""
    <html>
        <body>
            <h2>OAuth code received!</h2>
            <p>Code: {code}</p>
            <p>State: {state}</p>
        </body>
    </html>
    """

@app.get("/oauth/callback", response_class=HTMLResponse)
async def oauth_callback(request: Request):
    code = request.query_params.get("code")
    state = request.query_params.get("state")
    print(f"Received OAuth code: {code}")
    print(f"Received state: {state}")
    return f"""
    <html>
        <body>
            <h2>OAuth code received!</h2>
            <p>Code: {code}</p>
            <p>State: {state}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
