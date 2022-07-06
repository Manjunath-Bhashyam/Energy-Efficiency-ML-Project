## Energy-Efficiency-ML-Project

### End-to-End Machine Learning Project;

### Problem Statement:
The effect of eight input variables (relative compactness, surface area, wall area, roof
area, overall height, orientation, glazing area, glazing area distribution) on two output
variables, namely heating load (HL) and cooling load (CL) of residential buildings is
investigated using a statistical machine learning framework. We have to use a number
of classical and non-parametric statistical analytic tools to carefully analyse the strength
of each input variable's correlation with each of the output variables in order to discover
the most strongly associated input variables. We need to estimate HL and CL, we can
compare a traditional linear regression approach to a sophisticated state-of-the-art
nonlinear non-parametric method, random forests.

#### Data Set Information:

We perform energy analysis using 12 different building shapes simulated in Ecotect. The buildings differ
with respect to the glazing area, the glazing area distribution, and the orientation, amongst other parameters.
We simulate various settings as functions of the afore-mentioned characteristics to obtain 768 building shapes.
The dataset comprises 768 samples and 8 features, aiming to predict two real valued responses. It can also be
used as a multi-class classification problem if the response is rounded to the nearest integer.

#### Attribute Information:

The dataset contains eight attributes (or features, denoted by X1...X8) and
two responses (or outcomes, denoted by y1 and y2). The aim is to use the eight features to predict
each of the two responses.

#### Specifically:
X1 Relative Compactness
X2 Surface Area
X3 Wall Area
X4 Roof Area
X5 Overall Height
X6 Orientation
X7 Glazing Area
X8 Glazing Area Distribution
y1 Heating Load
y2 Cooling Load

#### Software and account requirement

1. [GitHub Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)

Creating virtual environment

```
conda create -p venv python==3.7 -y
```

```
conda activate venv/
```

setup setup.py file

&

```
pip install -r requirements.txt
```

for ipynb files
```
pip install ipykernel
```

For train_test_split we have used StratifiedShuffleSplit to have the same kind of distribution for Train and Test Sets

