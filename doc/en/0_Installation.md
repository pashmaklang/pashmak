## Installation

### GNU/Linux/Unix
this installation guide is for GNU/Linux/UNIX systems. also compile process needs `pyinstaller`.
if you don't have pyinstaller, type `pip3 install pyinstaller` in terminal

compile & install:

```bash
# checkout to latest release
git branch installation $(git describe --abbrev=0)
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

above commands install latest (development) state of the program

now you can run interpreter in terminal:

```bash
pashmak --info # shows info about pashmak
pashmak -v # --version, shows version of pashmak
pashmak app.pashm
pashmak /path/to/script.pashm # runs file
pashmak - # gets code from stdin and run that
pashmak -r "<you code...>" # run code from cli arguments with `-r` option
```

IF YOU DON'T WANT TO INSTALL IT, you can run this with python3 in terminal:

```bash
cd /path/to/project/folder
python3 src/pashmak.py
# or
./src/pashmak.py
```

#### uninstallation
to uninstall pashmak, run this make command in terminal:

```bash
sudo make uninstall
```

pashmak will be remove from your system.

### Windows
in windows, you can run program with python interpreter without compiling:

```bash
cd \path\to\project
python src\pashmak.py
```

but also you can compile it with `pyinstaller`. if you don't have pyinstaller, enter `pip install pyinstaller` in command line

compile:

```bash
# install pyinstaller with pip
pip install pyinstaller

# configure & compile
.\win-configure.bat
python -m PyInstaller src\pashmak.py --onefile
```

now executable file is created in `dist\pashmak.exe`:

```bash
dist\pashmak.exe -v
```
