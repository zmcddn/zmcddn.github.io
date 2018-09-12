---
Title:  The ultimate guide to setup multiple Python environment with Anaconda and Sublime Text
Tags: Python, Anaconda, Sublime Text
---

The need for setting up a virtual executing environment of Python has a lot of advantages and has been widely discussed over internet. Here I have a tutorial for setting up multiple environment with Anaconda and Sublime Text.  

- The reason I choose Anaconda over Virtualenv is because Anaconda is widely used in the industry, especially in the big data and machine learning field, and it covers most functions of Virtualenv.   
- I choose Sublime Text as my IDE because it is very simple yet powful with many plugins. It is way faster and more efficient than many other IDES.  
- The installation of Anaconda will not be covered here as there are many tutorials online already.  

The tutorial has the following steps:

* [Step 1: install Anaconda 2](#step1)
* [Step 2: setup python environment with Anaconda on Win 10](#step2)
* [Step 3: setup Sublime Text build file on Win 10](#step3)
* [Step 4: setup python environment with Anaconda on Mac](#step4)
* [Step 5: setup Sublime Text build file on Mac](#step5)
* [Summary of useful conda commands](#summary)


## <a name="step1"></a>Step 1: install Anaconda 3
1. Install [**Anaconda 3**](https://www.anaconda.com/download/). Choose the version that you use most frequently. 
	* For example, if you are working with python 3.6 most of the time, you should download the 3.6 version; otherwise, you can download the 2.7 version.
2. If you encounter any difficulties during installation, [google](www.google.com) and [stackoverflow](https://stackoverflow.com/) are your best friend:)

## <a name="step2"></a>Step 2: setup python environment with Anaconda on Win 10
1.	Open **Anaconda Prompt** to create new environment. Note that it is the Anaconda Prompt not the windows command line.   
<img height="500" src="https://github.com/zmcddn/zmcddn.github.io/raw/master/assets/tutorials/20180211_1.png"/>
2.	When the Anaconda Prompt opens, it is in the default directory with many packages pre-installed. Now you can install the missing packages that you need using ** `conda install \*package_name` **. 
	* For instance, you can install multiple packages at the same time using `conda install Django flask tornado twisted`
3.	If there are some packages that cannot be installed using `conda` command, you can use `pip` as described in the following steps.
4.	Once the packages are installed, you can create your own brand-new python 3.6 environment using `conda create -n py36 –clone base` as the following picture indicates.
	* Since it is a clone from the base, all the packages you installed can be used here. This will save a lot of time.     
	<img width="500" src="https://github.com/zmcddn/zmcddn.github.io/raw/master/assets/tutorials/20180211_2.png"/>
	* **NOTE** that you can also create the environment using `conda create -n \*environment_name` first and then install all the necessary packages
5.	Use `activate py36` to get into the environment you just created, and use pip to install the packages that cannot be installed with "conda". 
	* For example, wxpython can be install using pip command as follows (i.e. `pip install -U wxpython`):
	<img width="500" src="https://github.com/zmcddn/zmcddn.github.io/raw/master/assets/tutorials/20180211_3.png"/>
6.	You can use `python` command to check the version of python and `quit()` command to quit the python environment as follows:    
<img width="600" src="https://github.com/zmcddn/zmcddn.github.io/raw/master/assets/tutorials/20180211_4.png"/>
7.	Use `deactivate` to quit current environment
8.	Now the python 3.6 environment is fully prepared, we can add the python 2.7 environment using `conda create -n py27 python=2.7`
9.	Once the 2.7 environment is created, again you can use `activate py27` to get into the environment and use `conda install \*package_name` or `pip` to install packages as instructed above.
10.	When inside your base/root directory, you can use `conda info --envs` to check the current environments installed on your computer as follows:  
![Alt text](https://github.com/zmcddn/zmcddn.github.io/raw/master/assets/tutorials/20180211_5.png)  

## <a name="step3"></a>Step 3: setup Sublime Text build file on Win 10
1.	Navigate to the "New Build System"     
<img width="500" src="https://github.com/zmcddn/zmcddn.github.io/raw/master/assets/tutorials/20180211_6.png"/>
2.	Type the following JSON format code as follows. The path on the 4th line is the path to the python environment we created above.    
![Alt text](https://github.com/zmcddn/zmcddn.github.io/raw/master/assets/tutorials/20180211_7.png)
<!-- <img width="600" src="https://github.com/zmcddn/zmcddn.github.io/raw/master/assets/tutorials/20180211_7.png"/> -->
3.	Save the file with an extension `.sublime-build` into the default folder 
4.	Repeat steps 1 to 3 to setup for the other python environment.
5.	Now you can see the files you just saved have appeared in the "Build System". 
	* For example, I named as "Py27" and "Py36" and they have appeared as shown in step 1
6.	Now you can check the versions of python by run different build using the following codes.  
Run with Py36:  
<img width="500" src="https://github.com/zmcddn/zmcddn.github.io/raw/master/assets/tutorials/20180211_8.png"/>  
Run with Py27:  
<img width="500" src="https://github.com/zmcddn/zmcddn.github.io/raw/master/assets/tutorials/20180211_9.png"/>
7. **NOTE:** the anaconda path for Win 10 is usually `D:/Anaconda3/envs/\*environemnt_name/python`

## <a name="step4"></a>Step 4: setup python environment with Anaconda on Mac
1. Setting up python with Anaconda on Mac is pretty much the same as on Win 10, except that when you activate the environment, you have to use command "source activate" rather than "activate".    
![Alt text](https://github.com/zmcddn/zmcddn.github.io/raw/master/assets/tutorials/20180211_11.png)
2. For package installation, it is identical to the steps for Win 10 described above. You can simply follow the steps in [Step 2](#step2)

## <a name="step5"></a>Step 5: setup Sublime Text build file on Mac
1.	Navigate to the "New Build System"    
![Alt text](https://github.com/zmcddn/zmcddn.github.io/raw/master/assets/tutorials/20180211_10.png)
2. Find the Anaconda path of python environment. The following steps explains how to do it:
	1. Open a terminal, and activate the environment you would like to set up.
		* For example, `source activate py27`
	2. Use command `which python` to find out the path
	3. Don't close the terminal and remember the path. The above two steps canbe seen as follows:    
	![Alt text](https://github.com/zmcddn/zmcddn.github.io/raw/master/assets/tutorials/20180211_12.png)
3. Use the path find above and type the following code as follows:    
<img width="500" src="https://github.com/zmcddn/zmcddn.github.io/raw/master/assets/tutorials/20180211_13.PNG"/>
4. Save it to the default location with the `.sublime-build` extension. 
5. You can repeat steps 1 to 4 for other environment you have created.
6. To double check, run the following command and see the results:    
![Alt text](https://github.com/zmcddn/zmcddn.github.io/raw/master/assets/tutorials/20180211_14.png)
7. **NOTE:** the anaconda path for Mac is usually `/Users/\*user_name/anaconda3/envs/\*environemnt_name/bin/python`

## <a name="summary"></a>Summary of useful conda commands

|                   Commands                  |                              Description                              |
| ------------------------------------------- | --------------------------------------------------------------------- |
| conda list                                  | list all the packages installed                                       |
| conda info --envs                           | list all the environment created                                      |
| conda create -n \*environment_name          | create an environment                                                 |
| conda create --name \*name1 --clone \*name2 | create a new environment (name1) to be a clone of another (name2) one |
| conda install \*package1 \*package2         | install multipe packages at the same time                             |
| conda install \*package = version           | install a package with a particular version                           |

* For more environment management commands, you can find them [**HERE**](https://conda.io/docs/user-guide/tasks/manage-environments.html)