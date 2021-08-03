import pandas as pd
import csv
from pandas.core.algorithms import mode
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go


df = pd.read_csv('data.csv')
data = df['Math_score'].tolist()

mean = statistics.mean(data)
std = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

print(mean)
print(std)
print(median)
print(mode)

first_std_diviesion_start, first_std_diviesion_end = mean - std, mean + std
second_std_diviesion_start, second_std_diviesion_end = mean - \
    2*(std), mean + 2*(std)
third_std_diviesion_start, third_std_diviesion_end = mean - \
    3*(std), mean + 3*(std)

list_of_data_within_first_std = [result for result in data if result >
                                 first_std_diviesion_start and result < first_std_diviesion_end]
list_of_data_within_second_std = [result for result in data if result >
                                  second_std_diviesion_start and result < second_std_diviesion_end]
list_of_data_within_third_std = [result for result in data if result >
                                 third_std_diviesion_start and result < third_std_diviesion_end]

fig = ff.create_distplot([data], ["data"], show_hist=False)

fig.add_trace(go.Scatter(x=[mean, mean], y=[
              0, 0.17], mode="lines", name='mean'))
fig.add_trace(go.Scatter(x=[first_std_diviesion_start, first_std_diviesion_start], y=[
              0, 0.17], mode="lines", name='first_std_diviesion_start'))
fig.add_trace(go.Scatter(x=[first_std_diviesion_end, first_std_diviesion_end], y=[
              0, 0.17], mode="lines", name='first_std_diviesion_end'))
fig.add_trace(go.Scatter(x=[second_std_diviesion_start, second_std_diviesion_start], y=[
              0, 0.17], mode="lines", name='second_std_diviesion_start'))
fig.add_trace(go.Scatter(x=[second_std_diviesion_end, second_std_diviesion_end], y=[
              0, 0.17], mode="lines", name='second_std_diviesion_end'))
fig.add_trace(go.Scatter(x=[third_std_diviesion_start, third_std_diviesion_start], y=[
              0, 0.17], mode="lines", name='third_std_diviesion_start'))
fig.add_trace(go.Scatter(x=[third_std_diviesion_end, third_std_diviesion_end], y=[
              0, 0.17], mode="lines", name='third_std_diviesion_end'))
fig.show()

print("{}% of data lies within 1 standard deviation".format(
    len(list_of_data_within_first_std)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(
    len(list_of_data_within_second_std)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(
    len(list_of_data_within_third_std)*100.0/len(data)))
