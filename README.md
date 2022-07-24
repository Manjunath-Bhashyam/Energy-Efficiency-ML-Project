## Energy-Efficiency-ML-Project

[Deployed URL](https://energy-efficiency-predictor.herokuapp.com/predict)

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
each of the two responses - Heating Load & Cooling Load.

#### Specifically:
- X1 Relative Compactness
- X2 Surface Area
- X3 Wall Area
- X4 Roof Area
- X5 Overall Height
- X6 Orientation
- X7 Glazing Area
- X8 Glazing Area Distribution
- y1 Heating Load
- y2 Cooling Load

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

To setup CI/CD pipeline in heroku we need 3 information

HEROKU_EMAIL
HEROKU_API_KEY
HEROKU_APP_NAME

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase

To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```

Exploratory Data Analysis was performed on the Energy Efficiency Dataset and the observations, conclusions derived are under --> \notebook\Energy Efficiency EDA.ipynb

For train_test_split I have used StratifiedShuffleSplit to have the same kind of distribution for Train and Test Sets

#### Steps performed in Model Training
--> loading transformed training and testing dataset
--> reading model config file
--> getting best model on training dataset
--> evaluating models on both training & testing dataset --> model object
--> loading preprocessing object
--> custom model object by combining both preprocessing obj and model obj
--> saving custom model object
--> return model_trainer_artifact