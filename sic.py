import matplotlib.pyplot as plt
import fix_yahoo_finance as yf  
import datetime as dt
start = dt.datetime(2018, 1, 1)
end = dt.datetime.now()
data = yf.download('^DJI', start, end)
data.Close.plot()
plt.show()