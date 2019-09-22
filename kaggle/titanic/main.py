import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

surviver_df = pd.read_csv('data/gender_submission.csv')

train_df = pd.read_csv('data/train.csv')

print(train_df)