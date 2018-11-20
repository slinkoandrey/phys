import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

spots = sm.datasets.sunspots
print(spots.NOTE)
data = spots.load_pandas().data['SUNACTIVITY']
plt.plot(data)
plt.figure()
sm.graphics.tsa.plot_acf(data, lags=50, alpha=0.01)

ar = sm.tsa.ARMA(data.values, (12, 0))
model = ar.fit()
print(model.arparams)
plt.figure()
plt.plot(model.arparams)
forecast, f_err, f_conf = model.forecast(50, alpha=0.05)
plt.figure()
plt.plot(data.index[-100:], data.values[-100:])
plt.plot(np.arange(50) + data.index[-1], forecast, color='red')
plt.fill_between(np.arange(50) + data.index[-1], *f_conf.T, color='red', alpha=0.3)