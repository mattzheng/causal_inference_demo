'''
文档：
https://psmatching.readthedocs.io/en/latest/#

github:
https://github.com/rlirey/psmatching


模型使用的方法：glm广义估计
glm_binom = sm.formula.glm(formula = model, data = data, family = sm.families.Binomial())

Match的方式：
同时取K个结果，进行匹配

'''



import psmatching.match as psm
import pytest


path = "simMATCH.csv"
model = "CASE ~ AGE + TOTAL_YRS"
k = "3"

m = psm.PSMatch(path, model, k)


# Instantiate PSMatch object
# m = PSMatch(path, model, k)

# Calculate propensity scores and prepare data for matching
m.prepare_data()

# Perform matching
m.match(caliper = None, replace = False)

# Evaluate matches via chi-square test
m.evaluate()


# 一些数据
a = m.df # 打上PROPENSITY 潜力分
m.df['CASE'].value_counts()

b = m.matched_data   # 匹配之后的数据对
m.matched_data['CASE'].value_counts()

