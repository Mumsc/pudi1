Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> import matplotlib
>>> import matplotlib.pyplot as plt
>>> plt.rcParams['axes.labelsize'] = 14
>>> plt.rcParams['xtick.labelsize'] = 12
>>> plt.rcParams['ytick.labelsize'] = 12
>>> import seaborn as sns
>>> color = sns.color_palette()
>>> sns.set_style('darkgrid')
>>> import sklearn
>>> from sklearn.model_selection
SyntaxError: invalid syntax
>>> from sklearn.model_selection import train_test_split
>>> housing =pd.read_csv('housing.csv')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    housing =pd.read_csv('housing.csv')
  File "C:\Users\Admin\Anaconda3\lib\site-packages\pandas\io\parsers.py", line 685, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\Admin\Anaconda3\lib\site-packages\pandas\io\parsers.py", line 457, in _read
    parser = TextFileReader(fp_or_buf, **kwds)
  File "C:\Users\Admin\Anaconda3\lib\site-packages\pandas\io\parsers.py", line 895, in __init__
    self._make_engine(self.engine)
  File "C:\Users\Admin\Anaconda3\lib\site-packages\pandas\io\parsers.py", line 1135, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "C:\Users\Admin\Anaconda3\lib\site-packages\pandas\io\parsers.py", line 1917, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 382, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 689, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: [Errno 2] File b'housing.csv' does not exist: b'housing.csv'
>>> housing =pd.read_csv('C:\Users\Admin\Desktop\New folder\RICFiles\housing.csv')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> housing =pd.read_csv('C:\\Users\\Admin\\Desktop\\New folder\\RICFiles\\housing.csv')
>>> print(housing.head())
   longitude  latitude  ...  median_house_value  ocean_proximity
0    -122.23     37.88  ...            452600.0         NEAR BAY
1    -122.22     37.86  ...            358500.0         NEAR BAY
2    -122.24     37.85  ...            352100.0         NEAR BAY
3    -122.25     37.85  ...            341300.0         NEAR BAY
4    -122.25     37.85  ...            342200.0         NEAR BAY

[5 rows x 10 columns]
>>> print(housing.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20640 entries, 0 to 20639
Data columns (total 10 columns):
longitude             20640 non-null float64
latitude              20640 non-null float64
housing_median_age    20640 non-null float64
total_rooms           20640 non-null float64
total_bedrooms        20433 non-null float64
population            20640 non-null float64
households            20640 non-null float64
median_income         20640 non-null float64
median_house_value    20640 non-null float64
ocean_proximity       20640 non-null object
dtypes: float64(9), object(1)
memory usage: 1.6+ MB
None
>>> correlation_matrix = housing.corr()
>>> plt.subplots(figsize=(8,6))
(<Figure size 800x600 with 1 Axes>, <matplotlib.axes._subplots.AxesSubplot object at 0x0000019A65B74888>)
>>> sns.heatmap(correlation_matrix, center=0, annot=True, linewidths=.3)
<matplotlib.axes._subplots.AxesSubplot object at 0x0000019A65B74888>
>>> corr = housing.corr()
>>> print(corr['median_house_value'].sort_values(ascending=False))
median_house_value    1.000000
median_income         0.688075
total_rooms           0.134153
housing_median_age    0.105623
households            0.065843
total_bedrooms        0.049686
population           -0.024650
longitude            -0.045967
latitude             -0.144160
Name: median_house_value, dtype: float64
>>> sns.displot(housing.median_income)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    sns.displot(housing.median_income)
AttributeError: module 'seaborn' has no attribute 'displot'
>>> sns.distplot(housing.median_income)
<matplotlib.axes._subplots.AxesSubplot object at 0x0000019A65B74888>
>>> plt.show()
>>> 
