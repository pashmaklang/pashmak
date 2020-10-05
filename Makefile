SHELL = bash
PYTHON = python3
MANAGE_SCRIPT = $(PYTHON) ./scripts.py
INSTALLATION_PATH = /usr/bin/pashmak

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
	@$(PYTHON) $(shell which pyinstaller) ./src/pashmak.py --onefile
else
	@echo -e "\033[31merror: the pyinstaller for python is required for compile the program. run \"pip3 install pyinstaller\" to install it\033[0m"
endif

clean:
	@rm build/ dist/ pashmak.spec -rf
	@echo -e "\033[32mall of build files cleaned successfuly\033[0m"

update-headers:
	@$(MANAGE_SCRIPT) update-headers

test:
	@$(PYTHON) ./tests/run.py

docs:
	@$(MANAGE_SCRIPT) build-doc

module:
	@$(MANAGE_SCRIPT) build-modules
	@echo -e "\033[32mall of modules mixed in 'src/core/modules.py' successfuly\033[0m"

all: module update-headers docs test
ifeq ($(GIT_IS_INSTALLED),1)
	@git status
endif

install: ./dist/pashmak
	@cp ./dist/pashmak $(INSTALLATION_PATH)
	@echo -e "\033[32mPashmak installed successfuly in '$(INSTALLATION_PATH)'. now you can run it in terminal: pashmak\033[0m"

uninstall: $(INSTALLATION_PATH)
	@rm $(INSTALLATION_PATH)
	@echo -e "\033[32mpashmak has been removed from your system successfuly\033[0m"
