default:
	@echo create - create a new env
	@echo setup - install dependencies in venv
	@echo prep - gather dependencies for git push
	@echo clean - removes serial/ - use with caution
create:
	python3 -m venv serial --prompt ser-mqtt
	@echo "Type '. ./serial/bin/activate'"

# this assumes Makefile is above folder created by venv
setup:
	# what happens if I activate when I'm already activated? no harm
	. ./serial/bin/activate
	# do I need to be in this dir?
	cd serial && pip install -r ../requirements.txt 

prep:  # prep for git push
	cd serial && pip freeze > ../requirements.txt

clean:
	rm -rf serial
