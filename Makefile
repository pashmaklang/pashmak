SHELL = bash
PYTHON = python3
SCRIPTS = $(PYTHON) ./src/pashmak.py scripts/
INSTALLATION_PATH = /usr/bin/pashmak

.DEFAULT_GOAL := main
.PHONY := main compile clean update-headers test module all install uninstall pylint speed-test

GIT_IS_INSTALLED = 0
ifneq (,$(shell command -v git))
GIT_IS_INSTALLED = 1
endif

main: compile

compile:
	@$(PYTHON) -m PyInstaller ./src/pashmak.py --onefile

clean:
	@rm build/ dist/ pashmak.spec pylint.out -rf
	@echo -e "\033[32mall of build files cleaned successfuly\033[0m"

update-headers:
	@$(SCRIPTS)update-headers.pashm

test:
	@$(PYTHON) ./tests/run.py

module:
	@$(SCRIPTS)module-build.pashm

all: module update-headers test speed-test
ifeq ($(GIT_IS_INSTALLED),1)
	-@git status
endif

install: ./dist/pashmak
	@cp ./dist/pashmak $(INSTALLATION_PATH)
	@echo -e "\033[32mPashmak installed successfuly in '$(INSTALLATION_PATH)'. now you can run it in terminal: pashmak\033[0m"

uninstall: $(INSTALLATION_PATH)
	@rm $(INSTALLATION_PATH)
	@echo -e "\033[32mpashmak has been removed from your system successfuly\033[0m"

speed-test:
	@$(PYTHON) ./src/pashmak.py ./scripts/speed-test.pashm
	@echo

pylint:
	@$(PYTHON) -m pylint $(shell find src -type f -name '*.py') \
	| grep -v '(no-member)' \
	| grep -v '(relative-beyond-top-level)' \
	| grep -v '(no-name-in-module)' > pylint.out
	@echo -e "\033[32mpylint output was saved in pylint.out\033[0m"
