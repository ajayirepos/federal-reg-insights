from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import metrics

app = FastAPI()
templates = Jinja2Templates(directory="templates")

data = metrics.load_data()

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    word_counts = metrics.word_count_by_agency(data)
    checksums = metrics.checksum_by_agency(data)
    custom_metric = metrics.custom_metric_parts_per_agency(data)
    clarity_scores = metrics.avg_sentence_length_by_agency(data)
    historical = metrics.historical_word_count_by_agency(data)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "word_counts": word_counts,
        "checksums": checksums,
        "custom_metric": custom_metric,
        "clarity_scores": clarity_scores,
        "historical": historical,
    })

@app.get("/word-count")
async def word_count():
    return metrics.word_count_by_agency(data)

@app.get("/checksum")
async def checksum():
    return metrics.checksum_by_agency(data)

@app.get("/historical")
async def historical():
    return metrics.historical_word_count_by_agency(data)

@app.get("/clarity-score")
async def clarity_score():
    return metrics.avg_sentence_length_by_agency(data)

