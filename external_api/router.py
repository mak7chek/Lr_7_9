from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse  # 1. Імпортуємо HTMLResponse
from .schemas import JokeModel, MemeModel, HumorCombinedModel
from .service import humor_service

router = APIRouter(prefix="/external", tags=["Humor API"])

@router.get("/joke", response_model=JokeModel)
async def get_joke():
    try:
        return await humor_service.get_joke()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/meme", response_model=MemeModel)
async def get_meme():
    try:
        return await humor_service.get_meme()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/combined", response_model=HumorCombinedModel)
async def get_combined():
    try:
        return await humor_service.get_combined_humor()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/view", response_class=HTMLResponse)
async def get_humor_html():
    try:
        result = await humor_service.get_combined_humor()

        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Humor API Lab</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify_content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f0f2f5;
                    margin: 0;
                }}
                .card {{
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box_shadow: 0 4px 8px rgba(0,0,0,0.1);
                    text-align: center;
                    max_width: 500px;
                }}
                img {{
                    max_width: 100%;
                    height: auto;
                    border-radius: 5px;
                    margin-bottom: 15px;
                }}
                p {{
                    font-size: 1.2em;
                    color: #333;
                }}
                .footer {{
                    margin-top: 10px;
                    font-size: 0.8em;
                    color: #888;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Random Humor</h1>

                <img src="{result.meme_url}" alt="Funny Meme" />

                <p>{result.joke_text}</p>

                <div class="footer">Source: {result.source}</div>
            </div>
        </body>
        </html>
        """
        return html_content

    except Exception as e:
        return f"<h3>Error loading humor: {e}</h3>"