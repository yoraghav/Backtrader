#!/usr/bin/env python
# coding: utf-8

# In[21]:


import backtrader as bt
import datetime
import matplotlib
import math
import talib
import numpy as np
from RSI import RsiSignalStrategy
from goldencross import Cross

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000.0)

data = bt.feeds.YahooFinanceCSVData(
        dataname='1.csv',
        # Do not pass values before this date
        fromdate=datetime.datetime(2001, 1, 1),
        # Do not pass values after this date
        todate=datetime.datetime(2013, 12, 31),
        reverse=False)

cerebro.adddata(data)
cerebro.addstrategy(RsiSignalStrategy)
#cerebro.addstrategy(Cross)
    
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())


# In[65]:


cerebro.plot()





