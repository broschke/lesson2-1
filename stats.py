import pandas as pd
from scipy import stats

def print_output(stat, val):
	print("The {0} for the Alcohol and Tobacco dataset is {1}.".format(stat, val))

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()

data = [i.split(',') for i in data]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df_al = df['Alcohol'].astype(float)
df_to = df['Tobacco'].astype(float)

frames = [df_al, df_to]
result = pd.concat(frames)

val_mean = result.mean()
val_median = result.median()
val_mode = stats.mode(result)
val_range = max(result)-min(result)
val_variance = result.var()
val_std = result.std()

print_output('mean', val_mean)
print_output('median', val_median)
print_output('mode', val_mode)
print_output('range', val_range)
print_output('variance', val_variance)
print_output('stadard deviation', val_std)
