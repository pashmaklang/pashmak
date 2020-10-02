PYTHON = python3
MANAGE_SCRIPT = $(PYTHON) ./scripts.py

.DEFAULT_GOAL := main
.PHONY := main compile clean update-headers test docs module all install

GIT_IS_INSTALLED = 0
ifneq ("",$(shell command -v git))
GIT_IS_INSTALLED = 1
endif

PYINSTALLER_IS_INSTALLED = 0
ifneq ("",$(shell command -v pyinstaller))
PYINSTALLER_IS_INSTALLED = 1
endif

main: compile

compile:
ifeq (1,$(PYINSTALLER_IS_INSTALLED))
	@$(MANAGE_SCRIPT) build
else
	@echo error: the pyinstaller for python is required for compile the program. run \"pip3 install -r requirements.txt\" to install it
endif

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
ifeq ($(GIT_IS_INSTALLED),1)
	@git status
endif

install: ./dist/pashmak
	@cp ./dist/pashmak /usr/bin/pashmak
	@echo Pashmak installed successfuly in '/usr/bin/pashmak'. now you can run it in terminal: '$ pashmak'
