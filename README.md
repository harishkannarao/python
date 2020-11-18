# python

## Tools Required

* `git` (any version)
* `python` (3.9.0)

## Bootstrap Commands

	source venv/bin/activate

	pip install pybuilder
	
	pip install pip-tools

    pyb --start-project

## Build Commands

    pyb clean publish
    
## PyCharm / Idea Integration

#### Generate modules

    pyb pycharm_generate
    
#### Install dependencies as pip packages

    pyb pip_sync