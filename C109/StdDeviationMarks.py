import statistics
import csv
import pandas as pd
import plotly_express as px
import plotly.figure_factory as pf
import plotly.graph_objects as pg

data = pd.read_csv("ExamMarks.csv")

Marks = data["math score"].tolist()

Mean = statistics.mean(Marks)
print("Mean of Math score: " + str(Mean))

Median = statistics.median(Marks)
print("Median of Math scores: " + str(Median))

Mode = statistics.mode(Marks)
print("Mode of Math scores: " + str(Mode))

StdDeviation = statistics.stdev(Marks)
print("Standard Deviation of Math scores: " + str(StdDeviation))

FirstStdDeviationStart, FirstStdDeviationEnd = Mean-StdDeviation, Mean+StdDeviation
SecondStdDeviationStart, SecondStdDeviationEnd = Mean-(2*StdDeviation), Mean+(2*StdDeviation)
ThirdStdDeviationStart, ThirdStdDeviationEnd = Mean-(3*StdDeviation), Mean+(3*StdDeviation)

#OneStdDeviation = [result for result in data if result > FirstStdDeviationStart and result < FirstStdDeviationEnd]
#TwoStdDeviation = [result for result in data if result > SecondStdDeviationStart and result < SecondStdDeviationEnd]
#ThirdStdDeviation = [result for result in data if result > ThirdStdDeviationStart and result < ThirdStdDeviationEnd]

#print("{}% of data lies within First standard deviation".format(len(OneStdDeviation)*100.0/len(data)))
#print("{}% of data lies within Second standard deviations".format(len(TwoStdDeviation)*100.0/len(data)))
#print("{}% of data lies within Third standard deviations".format(len(ThirdStdDeviation)*100.0/len(data)))

fig = pf.create_distplot([Marks], ["Math Scores"], show_hist=False)
fig.add_trace(pg.Scatter(x=[Mean, Mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(pg.Scatter(x=[FirstStdDeviationStart, FirstStdDeviationStart], y=[0, 0.17], mode="lines", name="Starting of 1st Standard Deviation"))
fig.add_trace(pg.Scatter(x=[FirstStdDeviationEnd, FirstStdDeviationEnd], y=[0, 0.17], mode="lines", name="End of 1st Standard Deviation"))
#fig.add_trace(pg.Scatter(x=[SecondStdDeviationStart, SecondStdDeviationStart], y=[0, 0.17], mode="lines", name="Starting of 2nd Standard Deviation"))
#fig.add_trace(pg.Scatter(x=[SecondStdDeviationEnd, SecondStdDeviationEnd], y=[0, 0.17], mode="lines", name="End of 2nd Standard Deviation"))
fig.show()