#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
from pylab import rcParams
from scipy.stats import ttest_ind


# In[ ]:


def plot_distribution(inp):
    plt.figure()
    ax = sns.distplot(inp)
    plt.axvline(np.mean(inp), color="k", linestyle="dashed", linewidth=5)
    _, max_ = plt.ylim()
    plt.text(
        inp.mean() + inp.mean() / 10,
        max_ - max_ / 10,
        "Mean: {:.2f}".format(inp.mean()),
    )
    return plt.figure


# In[ ]:


def compare_2_groups(arr_1, arr_2, alpha, sample_size):
    stat, p = ttest_ind(arr_1, arr_2)
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    if p > alpha:
        print('Same distributions (fail to reject H0)')
    else:
        print('Different distributions (reject H0)')


# In[ ]:


#Test-errors on RandomForest and SVM-Linear
randForestError=[0.2505,0.2437,0.2431,0.2531,0.2539,0.2402,0.252,0.2412,0.2646]
svmError=[0.2357,0.2427,0.2531,0.2375,0.2544,0.2416,0.2564,0.2512,0.2342,0.2602]

randForestError=np.array(randForestError)
svmError=np.array(svmError)

print("Random Forest Error variance:  "+ str(randForestError.var()))
print("SVM - Linear Error variance:  " +str(svmError.var()))

compare_2_groups(randForestError, svmError, 0.05, 10)


# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(randForestError, shade=True)
sns.kdeplot(svmError, shade=True)
plt.axvline(np.mean(randForestError), color='b', linestyle='dashed', linewidth=5)
plt.axvline(np.mean(svmError), color='orange', linestyle='dashed', linewidth=5)
plt.title("Paired Sample T-Test.")


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
warnings.filterwarnings("ignore")
rcParams['figure.figsize'] = 20,10
rcParams['font.size'] = 30
sns.set()
np.random.seed(8)


# In[ ]:


plot_distribution(randForestError)
plot_distribution(svmError)
plt.figure()
ax1 = sns.distplot(randForestError)
ax2 = sns.distplot(svmError)
plt.axvline(np.mean(randForestError), color='b', linestyle='dashed', linewidth=5)
plt.axvline(np.mean(svmError), color='orange', linestyle='dashed', linewidth=5)

