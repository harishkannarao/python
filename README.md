# python

## Tools Required

* `git` (any version)
* `python` (3.9.0)

## Bootstrap Commands

	source venv/bin/activate

	pip install pybuilder
	
    pyb --start-project

## Build Commands

#### Full Build (unit and integration tests)

    pyb clean install_dependencies analyze publish
    
#### Run unit and integration tests

    pyb clean run_unit_tests    
    
## Generate tar ball with version

    BUILD_VERSION="1.0.0" pyb clean install_dependencies analyze publish
    
## PyCharm / Idea Integration

#### Generate modules

    pyb pycharm_generate
    
#### Install dependencies as pip packages

    pyb install_dependencies
    
## pyb commands

#### List Tasks

    pyb --list-tasks