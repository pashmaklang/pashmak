PYTHON = python3
MANAGE_SCRIPT = $(PYTHON) ./scripts.py

.DEFAULT_GOAL := main
.PHONY := main compile clean update-headers test docs module all install

main: compile

compile:
	@$(MANAGE_SCRIPT) build

clean:
	@rm build/ dist/ pashmak.spec -rf
	@echo all of build files cleaned successfuly

update-headers:
	@$(MANAGE_SCRIPT) update-headers

test:
	@$(MANAGE_SCRIPT) test

docs:
	@$(MANAGE_SCRIPT) build-doc

module:
	@$(MANAGE_SCRIPT) build-modules
	@echo all of modules mixed in 'src/core/modules.py' successfuly

all: module update-headers docs test
	@git status

install: ./dist/pashmak
	@cp ./dist/pashmak /usr/bin/pashmak
	@echo Pashmak installed successfuly in '/usr/bin/pashmak'. now you can run it in terminal: '$ pashmak'

