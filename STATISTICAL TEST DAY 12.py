# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 16:32:22 2020

@author: APARNA S NAIR
"""


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt                              
dataset1=pd.read_excel("DS.xlsx",sheet_name=1)


# CHISQUARE TEST

# H(0):THERE IS NO SIGNIFICANT RELATION BETWEEN AGE & EDUCATION

dataset2=dataset1[['Age','Education']].head(40)
dataset3=dataset2.dropna()
from scipy.stats import chi2_contingency
chitable=pd.crosstab(dataset3.Age,dataset3.Education)
stats,p,dof,expected= chi2_contingency(chitable)
print(stats,p)
print("since p value greater than 0.05, accept null hypothesis,# H(0):THERE IS NO SIGNIFICANT RELATION BETWEEN AGE & EDUCATION")


# H(6):THERE IS NO SIGNIFICANT RELATION BETWEEN Education & TotalWorkingYears  

dataset2=dataset1[['Education','TotalWorkingYears']].head(40)
dataset3=dataset2.dropna()
from scipy.stats import chi2_contingency
chitable=pd.crosstab(dataset3.Education,dataset3.TotalWorkingYears)
stats,p,dof,expected= chi2_contingency(chitable)
print(stats,p)
print("since p value less than 0.05, REJECT null hypothesis & ACCEPT ALTERNATE HYPOTHESIS ,# H(A):THERE IS SIGNIFICANT RELATION Education & TotalWorkingYears")