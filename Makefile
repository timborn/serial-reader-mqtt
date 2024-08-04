default:
	@echo create - create a new env
	@echo setup - install dependencies in venv
	@echo prep - gather dependencies for git push
	@echo clean - removes serial/ - use with caution
	@echo
	@echo test - run our program and see what happens
create:
	python3 -m venv serial --prompt ser-mqtt
	@echo "Type '. ./serial/bin/activate'"

# this assumes Makefile is above folder created by venv
# When Make starts up, it transforms every environment variable into 
# a Make variable with the same name and value. 
# we need to confirm we are in venv
setup:
ifdef VIRTUAL_ENV_PROMPT
	cd serial && pip install -r ../requirements.txt 
else
	@echo source ./serial/bin/activate and try again
endif

prep:  # prep for git push
ifdef VIRTUAL_ENV_PROMPT
	cd serial && pip freeze > ../requirements.txt
else
	@echo source ./serial/bin/activate and try again
endif

clean:
	rm -rf serial

test:
ifdef VIRTUAL_ENV_PROMPT
	python ./reader.py
else
	@echo source ./serial/bin/activate and try again
endif
