## Installation
this installation guide is for GNU/Linux/UNIX systems. if you are windows user, you can run program with python. also compile process needs `pyinstaller`.

compile & install:

```bash
# checkout to latest release
git branch installation v1.2.3
git checkout installation

# compile and install
make all
make
sudo make install

# back to master branch and delete installation branch
git checkout master
git branch -D installation
```

run above commands in terminal to install pashmak interpreter on your GNU/Linux/UNIX system.

also if you want install latest version (in development), do not run above git commands and just run it:

```bash
make all
make
sudo make install
```

above commands installs latest (development) state of program

now you can run interpreter in terminal:

```bash
pashmak --info # shows info about pashmak
pashmak -v # --version, shows version of pashmak
pashmak app.pashm
pashmak /path/to/script.pashm # runs file
pashmak - # gets code from stdin and run that
```

IF YOU DON'T WANT TO INSTALL IT, you can run this with python3 in terminal:

```bash
cd /path/to/project/folder
python3 src/pashmak.py
# or
./src/pashmak.py
```

windows users can use this way.

#### uninstallation
to uninstall pashmak, run this make command in terminal:

```bash
sudo make uninstall
```

pashmak will be remove from your system.
