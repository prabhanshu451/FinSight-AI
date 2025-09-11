from fastapi import FastAPI
from fastapi.responses import JSONResponse
from . import forecast

app = FastAPI(title='FinSightAI Forecasting')

@app.get('/health')
async def health():
    return JSONResponse({'status':'ok'})

@app.post('/forecast/{user_id}')
async def create_forecast(user_id: int, horizon_months: int = 6):
    res = forecast.run_forecast(user_id, horizon_months=horizon_months)
    return JSONResponse(res)
