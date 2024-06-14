import web_scraping
import model
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import starlette.status as status

app = FastAPI(
    title="Planirana isključenja na mreži",
    version="0.0.1",
    terms_of_service="https://elektrodistribucija.rs/planirana-iskljucenja/planirana-bgd",
)
test = web_scraping.Web_scraping()


# Redirect to home
@app.get("/")
async def main():
    # Redirect to /docs (relative URL)
    return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)


@app.get("/beograd")
async def get_data(day=0):
    if int(day) > 5:
        raise HTTPException(
            status_code=400,
            detail="Mozete izabrat 4 dana unapred"
        )
    else:
        data = test.web_scraping(day)
        headers = data[0]
        json_data = [dict(zip(headers, row)) for row in data[1:]]
        return json_data


@app.get("/novisad")
async def get_data(day=0):
    if int(day) > 5:
        raise HTTPException(
            status_code=400,
            detail="Mozete izabrat 4 dana unapred"
        )
    else:
        data = test.web_scraping(day, "novi_sad")
        headers = data[0]
        json_data = [dict(zip(headers, row)) for row in data[1:]]
        return json_data


@app.get("/kraljevo")
async def get_data(day=0):

    if int(day) > 5:
        raise HTTPException(
            status_code=400,
            detail="Mozete izabrat 4 dana unapred"
        )
    else:
        data = test.web_scraping(day, "kraljevo")
        headers = data[0]
        json_data = [dict(zip(headers, row)) for row in data[1:]]
        return json_data


@app.get("/nis")
async def get_data(day=0):
    if int(day) > 5:
        raise HTTPException(
            status_code=400,
            detail="Mozete izabrat 4 dana unapred"
        )
    else:
        data = test.web_scraping(day, "nis")
        headers = data[0]
        json_data = [dict(zip(headers, row)) for row in data[1:]]
        return json_data


@app.get("/kragujevac")
async def get_data(day=0):
    if int(day) > 5:
        raise HTTPException(
            status_code=400,
            detail="Mozete izabrat 4 dana unapred"
        )
    else:
        data = test.web_scraping(day, "kragujevac")
        headers = data[0]
        json_data = [dict(zip(headers, row)) for row in data[1:]]
        return json_data
