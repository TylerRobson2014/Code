import numpy as np
import math
import csv
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

df = pd.read_csv('/home/steve/Downloads/results.csv',na_values=['.'])
df['DATE'] = pd.to_datetime(df['DATE'])
