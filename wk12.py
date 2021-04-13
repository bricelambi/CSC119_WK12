
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker



def change_me(myvar):
    myvar[0] = '1'

myvar = '0,1,2'
print ("starting with:", myvar)
change_me(myvar)
print ("ending with:", myvar)