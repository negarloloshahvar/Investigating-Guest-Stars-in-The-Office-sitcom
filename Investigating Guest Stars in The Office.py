from matplotlib import pyplot as plt
import pandas as pd
plt.rcParams['figure.figsize'] = [11, 7]

office_dataset = pd.read_csv('the_office_series2.csv')
print(office_dataset.columns)

colors = []
for ind, row in office_dataset.iterrows():
    if row['Ratings'] < 0.25:
        colors.append('red')
    elif row['Ratings'] < 0.50:
        colors.append('orange')
    elif row['Ratings'] < 0.75:
        colors.append('lightgreen')
    else:
        colors.append('darkgreen')

plt.scatter(x= office_dataset['Episode Number'], y= office_dataset['Viewership'], c= colors)
plt.title('Popularity, Quality, and Guest Appearances on the Office')
plt.xlabel('Episode Number')
plt.ylabel('Viewership (Millions)')
plt.show()
