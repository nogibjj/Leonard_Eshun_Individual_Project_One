[![Format](https://github.com/nogibjj/Leonard_Eshun_Individual_Project_One/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Leonard_Eshun_Individual_Project_One/actions/workflows/format.yml)
[![Test](https://github.com/nogibjj/Leonard_Eshun_Individual_Project_One/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Leonard_Eshun_Individual_Project_One/actions/workflows/test.yml)
[![Lint](https://github.com/nogibjj/Leonard_Eshun_Individual_Project_One/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Leonard_Eshun_Individual_Project_One/actions/workflows/lint.yml)
[![Install](https://github.com/nogibjj/Leonard_Eshun_Individual_Project_One/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Leonard_Eshun_Individual_Project_One/actions/workflows/install.yml)


## Data Engineering Individual Project One (also fulfilling Miniproject Two)

This repository is created to fulfill two assignments from the Data Engineering course, IDS 706. The aim is to create a python project that
1. has a Pandas Descriptive Statistics Script.
1. does Continuous Integration using Github Actions of Python Data Science

The requirements for assignment one are:
1. Python script using Pandas for descriptive statistics
1. Read a dataset (CSV or Excel)
1. Generate summary statistics (mean, median, standard deviation)
1. Create at least one data visualization

The requirements for assignment two are:
1. The project structure must include the following files:
1. Jupyter Notebook with: 
	1. Cells that perform descriptive statistics using Polars or Panda.
	1. Tested by using nbval plugin for pytest
1. Makefile with the following:
	1. Run all tests (must test notebook and script and lib)
	1. Formats code with Python black Links to an external site.
	1. Lints code with Ruff Links to an external site.
	1. Installs code via:  pip install -r requirements.txt
	1. test_script.py to test script
	1. test_lib.py to test library
	1. Pinned requirements.txt
1. Github Actions performs all four Makefile commands with badges for each one in the README.md

## This is what the python code does
It has the following functions:

1. **load_dataset** to read the dataset using Pandas
	```
	# Returns a data frame
	load_dataset()
	
	```
1. **calculate_summaries** to generate the summary statistics
	```
	# Returns a data frame
	calculate_summaries(data, column_one, column_one_heading, column_two, column_two_heading, set_first_column_index=False)
	```
1. **create_bar_chart** to create bar charts for visualization
	```
	# This either saves the chart as a file or displays it depending on the value of _save_chart_
	create_bar_chart(data: pd.DataFrame, save_chart: bool)
	```
1. **create_histogram** to add histograms for visualization
	```
	# This either saves the chart as a file or displays it depending on the value of _save_chart_
	create_histogram(data, column, title, save_chart: bool)
	```
1. **save_to_markdown(data)** to create a markdown file after a git push by github actions
	```
	# This creates and saves a markdown file with the results
	save_to_markdown(data)
	```

> [!TIP]
> Just clone the repository to your local machine or codespace and enjoy.



## Steps taken to meet the requirements
The code was pushed to Github and Github Actions did the following main things:

1. Setup the virtual environment according to the parameters in the workflow.yml
1. Packages were installed, including those in the requirements.txt file
1. All python files were formated by black
1. Code linting was done with ruf
1. All the tests in the test_main.py were executed
1. Finally, a markdown file summarizing the information was created during the pipeline runtime using Python. Prior to this the charts were generated in the pipeline runtime and used for visualization together with the descriptive statistics in the generated md file.

> [!IMPORTANT]
> All the above steps had to be successful to get a completed CI/CD.