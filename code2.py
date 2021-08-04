import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

#Change the School data here
df = pd.read_csv("mathScore.csv")
data = df["Math_score"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

std = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sd ",mean)
print("Standard deviation of sd ", std)


fstd_start, fstd_end = mean-std, mean+std
sstd, sstd_end = mean-(2*std), mean+(2*std)
tstd,  tstd_end = mean-(3*std), mean+(3*std)


# # finding the mean of THE STUDENTS WHO GAVE EXTRA TIME TO MATH LAB and plotting on graph
df = pd.read_csv("mathScore.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample1)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN "))
fig.add_trace(go.Scatter(x=[fstd_start, fstd_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[sstd, sstd_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[tstd,  tstd_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

zScore = (mean_of_sample1-mean)/std
print(zScore)