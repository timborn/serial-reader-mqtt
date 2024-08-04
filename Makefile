default:
	echo create - create a new env
	echo setup - install dependencies in venv
	echo prep - gather dependencies for git push
create:
	python3 -m venv serial --prompt ser-mqtt

# this assumes Makefile is above folder created by venv
setup:
	. ./serial/bin/activate
	# do I need to be in this dir?
	cd serial && pip install -r ../requirements.txt 

prep:  # prep for git push
	cd serial && pip freeze > ../requirements.txt
