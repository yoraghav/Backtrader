import backtrader as bt
import datetime
import matplotlib
import math
import talib
import numpy as np


class Cross(bt.Strategy):
    params = (('fast',50),('slow',200),('order_percentage',0.95),('ticker','SPY'))
    
    def __init__(self):
        self.fast_moving_average = bt.indicators.SMA(
            self.data.close,period = self.params.fast,plotname= '50days'
        )
        
        self.slow_moving_average = bt.indicators.SMA(
            self.data.close,period = self.params.slow,plotname= '200days'
        )
        
        self.crossover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)
    
    def next(self):
        if self.position.size == 0:
            if self.crossover > 0:
                #amount_to_invest = (self.params.order_percentage * self.broker.cash)
                #self.size = math.floor(amount_to_invest / self.data.close)
                self.buy(size=1000)
                
        if self.position.size > 0:
            if self.crossover < 0:
                self.close()
                 

