import pandas as pd
import numpy as np

df = pd.read_csv('/home/dhiraj/Documents/Code/AutomotiveSales/trainingData.csv')
training_set = df[:3000]
testing_set = df[3000:]