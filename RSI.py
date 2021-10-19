import backtrader as bt
import datetime
import matplotlib
import math
import talib
import numpy as np

class RsiSignalStrategy(bt.Strategy):
    params = dict(
		rsi_periods=14,
				  rsi_upper=70,
				  rsi_lower=30,
				  rsi_mid=50
	)

    def __init__(self):

        # add RSI indicator
        self.rsi = bt.indicators.RSI(period=self.p.rsi_periods,
                                upperband=self.p.rsi_upper,
                                lowerband=self.p.rsi_lower)

        # add RSI from TA-lib just for reference
        talib.RSI(np.array(self.data))

        # long condition (with exit)
        #rsi_signal_long = bt.ind.CrossUp(rsi, self.p.rsi_lower, plot=False)
        # Add long signal one, that is, the RSI value on the 14th will exceed 30
        #self.signal_add(bt.SIGNAL_LONG, rsi_signal_long)
        # LONGEXIT: short indications are taken to exit long positions
		 # Add long exit signal, the RSi value on the 14th is greater than 50
        #self.signal_add(bt.SIGNAL_LONGEXIT, -(rsi > self.p.rsi_mid))

        # short condition (with exit)
        #rsi_signal_short = -bt.ind.CrossDown(rsi, self.p.rsi_upper, plot=False)
                 # Add a short signal, that is, the RSI value crossed 70 on the 14th.
        #self.signal_add(bt.SIGNAL_SHORT, rsi_signal_short)
		# SHORTEXIT: long indications are taken to exit short positions
		 # Add short exit signal, the RSi value on the 14th is less than 50
        #self.signal_add(bt.SIGNAL_SHORTEXIT, rsi < self.p.rsi_mid)
    
    def next(self):
    
    
        if(self.rsi<self.params.rsi_lower):
            self.buy(size=100)
        
        if(self.rsi>self.params.rsi_mid):
            if(self.position.size>0):
                self.close()
        
        if(self.rsi>self.params.rsi_upper):
            self.sell(size=100)
            
        if(self.rsi<self.params.rsi_mid):
            if(self.position.size<0):
                self.close()
        
