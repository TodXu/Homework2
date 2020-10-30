# INF560

 This repository is for the homework1 of INF 560  
 Here is to host the 3 required scripts:  
 The 1st script is for generating 1000 random numbers from 0-100  
 The 2nd script is for generating new numbers from the original 1000 using the equation y=3x+6  
 The 3rd scipt is for visualizing the results of the 1st and 2nd steps    

Zenodo badge with the DOI:  [![DOI](https://zenodo.org/badge/298433408.svg)](https://zenodo.org/badge/latestdoi/298433408)






## Homework 4  

A binder badge to click and open the Binder tree:    
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/TodXu/Homework2/master)

A binder badge to click and open the Notebook (Homework4.ipynb) directly:  
[![Binder](https://mybinder.org/badge_logo.svg)](https://hub.gke2.mybinder.org/user/todxu-homework2-4q1kb9lx/notebooks/Homework4.ipynb)


### Question 1:  Create a blank virtual environment in the local repository from homework 2  

At first, I used Github Desktop to clone the Homework2 Repository to local.  
I've done the project by using Python version of 3.7.8.  
Then I installed the virtualenv package by:  
`pip install virtualenv`  
Then I changed the directory to my local clone and created the new environment named dsci560H4:  
`cd C:\Users\Tod Xu\Documents\GitHub\Homework2`  
`py -m venv dsci560H4`  
  
### Question 2: Activate the environment and install the dependencies to run the scripts  

I activated the environment by  
`py -m .\Script\activate`  
I used numpy and matplotlib in my scripts so that I installed 2 of the dependencies in my virtual environment:  
`py -m pip install numpy`  
`py -m pip install matplotlib`  

### Question 3: Run the scripts and screenshot of my terminal with the activated environment after running the script for the number generator.  
Run the 3 scripts from homework2  
`py Random_Number_Generator.py`  
`py Equation_Number_Generator.py`  
`py Visualization.py`  
And here is the screenshot of my terminal:  
![image](https://github.com/TodXu/Homework2/blob/master/Terminal1.JPG)
![image](https://github.com/TodXu/Homework2/blob/master/Terminal2.JPG)  

### Question 4: Extract the dependencies of your virtual environment  
#### a).Compare the packages that I manually installed versus the dependency list I extracted.  
I've check the dependecies by running:  
`py -m pip freeze`  
At the very beginning of my virtual environment, the dependency list is all empty.  
After I installed the numpy and matplotlib library,  
I ran `py -m pip freeze` again.  
And here is the dependencies list:  
![image](https://github.com/TodXu/Homework2/blob/master/Freeze.JPG)  

I noticed that I only manually installed numpy and matplotlib package, but the dependency list I've extracted has several more dependencies.  
I think that is other dependencies associated with either the numpy or the matplotlib.  
When I installed numpy and matplotlib dependency, other dependencies are part of numpy or matplotlib so that they're installed to my environment, too.  

#### b). gitignore  
I've created a hidden file named ".gitignore" under the local Homework 2 folder.  
![image](https://github.com/TodXu/Homework2/blob/master/ignore1.JPG)  
![image](https://github.com/TodXu/Homework2/blob/master/ignore2.JPG)  
And I edited it by notepad and write `dsci560H4/` into it.  
This is to exclude dsci560H4 environment folder from github commit.  

#### c). Upload extracted dependencies to GitHub  
I downloaded the dependencies by `py -m pip freeze > requirements.txt` into the requirements.txt file.  
Then I uploaded it to my Github.  

### Question 5: Binder  
I've updated the jupyter notebook (Homework4.ipynb) to include visualizations of the initial, intermediate and final results.  
And I have uploaded the notebook to my Github repository.  
To make sure it is executable in Binder, I uploaded the requirements.txt(In Question 4 c).) to meet all the required dependencies.  

A binder badge to click and open the Binder tree:  
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/TodXu/Homework2/master)  
  
  
A binder badge to click and open the Notebook (Homework4.ipynb) directly:  
[![Binder](https://mybinder.org/badge_logo.svg)](https://hub.gke2.mybinder.org/user/todxu-homework2-4q1kb9lx/notebooks/Homework4.ipynb)









