import datetime
import numpy as np
import pandas as pd
def run_forecast(user_id:int, horizon_months=6):
    # generate synthetic monthly expense data for last 24 months
    periods = 24
    end = datetime.datetime.utcnow().replace(day=1)
    dates = [end - datetime.timedelta(days=30*(periods - i)) for i in range(periods)]
    np.random.seed(42)
    values = 1000 + np.linspace(0, 400, periods) + 150 * np.sin(np.linspace(0, 3*np.pi, periods)) + np.random.normal(0,50,periods)
    df = pd.DataFrame({'ds': pd.to_datetime(dates), 'y': values})

    try:
        from prophet import Prophet
        m = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
        m.fit(df)
        future = m.make_future_dataframe(periods=horizon_months, freq='M')
        forecast = m.predict(future)
        preds = forecast[['ds','yhat','yhat_lower','yhat_upper']].tail(horizon_months)
        data = []
        for _, row in preds.iterrows():
            data.append({
                'ds': pd.to_datetime(row['ds']).isoformat(),
                'yhat': float(row['yhat']),
                'yhat_lower': float(row['yhat_lower']),
                'yhat_upper': float(row['yhat_upper'])
            })
        source = 'prophet'
    except Exception as e:
        df2 = df.copy()
        df2['t'] = range(len(df2))
        coeffs = np.polyfit(df2['t'], df2['y'], 1)
        data = []
        last_t = df2['t'].iloc[-1]
        for i in range(1, horizon_months+1):
            t = last_t + i
            yhat = float(coeffs[0]*t + coeffs[1])
            data.append({
                'ds': (end + datetime.timedelta(days=30*i)).isoformat(),
                'yhat': yhat,
                'yhat_lower': yhat * 0.9,
                'yhat_upper': yhat * 1.1
            })
        source = f'fallback_linear ({str(e)})' if e else 'fallback_linear'

    return {
        'user_id': user_id,
        'generated_at': datetime.datetime.utcnow().isoformat(),
        'horizon_months': horizon_months,
        'source': source,
        'data': data
    }
