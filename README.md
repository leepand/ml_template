# template_ds_project

<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">ds_proj_v1</h3>

<div align="center">

  [![code coverage](coverage.svg "Code coverage")]()
</div>

---


## 🧐 About <a name = "about"></a>

ds project

## 🔖 Project structure

```
ds_proj_v1/
|- bin/          # contains scripts and main files that should be run
|- config/       # config files
|- notebooks/    # notebooks for EDA and exploration
|- secrets       # contains api keys and secret parameters. It should be ignored from git
|- src/          # source code - contains functions
|- tests/        # Test files should mirror the src folder
|- Makefile      # automatize taks through make utility
```

## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Clone the project 
```
git clone https
```

## Setup your environement and install project dependencies
```
conda create -n ds_proj_v1 python=1.0
source activate ds_proj_v1


python -m pip install pip-tools
pip-compile --output-file requirements.txt requirements.in requirements_dev.in
python -m pip install -r requirements.txt
```

### Installing

## 🔧 Running the tests
Tests are implemented in ./tests, you need to run the following command to run them.
```
make tests
```

## 🚀 Deployment
Add additional notes about how to deploy this on a live system.

## 🎈 Contributions
To contribute in this project, please setup locally the project following the steps  in Getting started section.
We use few packages to guarantee high quality code. Before commiting you can run:
To format you code using black
```
make black
```
To get warning message on non respect of pep8 code guidance:
(the command runs on all .py files in the project)
```
make lint
```
You can also run automatically, black, lint and few other packages to analyze and check your code base before commiting
```
make precommit
```

##  ✍️ Authors
ds_proj_v1 - leepand6@gmail.com