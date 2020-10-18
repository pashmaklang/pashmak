SHELL = bash
PYTHON = python3
MANAGE_SCRIPT = $(PYTHON) ./scripts.py
INSTALLATION_PATH = /usr/bin/pashmak

.DEFAULT_GOAL := main
.PHONY := main compile clean update-headers test docs module all install uninstall pylint

GIT_IS_INSTALLED = 0
ifneq (,$(shell command -v git))
GIT_IS_INSTALLED = 1
endif

PYLINT_IS_INSTALLED = 0
ifneq (,$(shell command -v pylint3))
PYLINT_IS_INSTALLED = 1
endif

main: compile

compile:
	@$(PYTHON) -m PyInstaller ./src/pashmak.py --onefile

clean:
	@rm build/ dist/ pashmak.spec pylint.out -rf
	@echo -e "\033[32mall of build files cleaned successfuly\033[0m"

update-headers:
	@$(MANAGE_SCRIPT) update-headers

test:
	@$(PYTHON) ./tests/run.py

docs:
	@$(MANAGE_SCRIPT) build-doc

module:
	@$(MANAGE_SCRIPT) build-modules

all: module update-headers docs test
ifeq ($(GIT_IS_INSTALLED),1)
	-@git status
endif

install: ./dist/pashmak
	@cp ./dist/pashmak $(INSTALLATION_PATH)
	@echo -e "\033[32mPashmak installed successfuly in '$(INSTALLATION_PATH)'. now you can run it in terminal: pashmak\033[0m"

uninstall: $(INSTALLATION_PATH)
	@rm $(INSTALLATION_PATH)
	@echo -e "\033[32mpashmak has been removed from your system successfuly\033[0m"

pylint: all
ifeq (1,$(PYLINT_IS_INSTALLED))
	@pylint3 $(shell find src -type f -name '*.py') $(shell find tests -type f -name '*.py') |\
		grep -v '(invalid-name)' |\
		grep -v "Unused argument 'op' (unused-argument)"|\
		grep -v "(no-name-in-module)" > pylint.out
	@echo -e "\033[32mpylint saved output in pylint.out\033[0m"
else
	@echo -e "\033[31merror: pylint3 is not installed\033[0m"
endif
