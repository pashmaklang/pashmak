.PHONY := compile install remove
PASHMAK = pashmak
INSTALLATION_PATH = /usr/bin/pashmiler

compile:
	$(PASHMAK) ./pashmiler.pashm ./pashmiler.pashm out.pashm
	chmod +x out.pashm

install: out.pashm
	cp ./out.pashm $(INSTALLATION_PATH)
	$(INSTALLATION_PATH) -v

remove: $(INSTALLATION_PATH)
	rm $(INSTALLATION_PATH)
