# Installation

## GNU/Linux/Unix
This installation guide is for GNU/Linux/UNIX systems. Also compile process needs `pyinstaller` pip library.
If you don't have Pyinstaller, run `pip3 install pyinstaller` command in terminal.

Compile & Install:

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

Run above commands in terminal to install Pashmak interpreter on your GNU/Linux/UNIX system.

Also if you want install latest version(development state), do not run above git commands and just run it:

```bash
make all
make
sudo make install
```

Above commands install latest (development) state of the program.

Now you can run Interpreter in terminal:

```bash
pashmak --info # shows info about Pashmak
pashmak -v # --version, shows version of Pashmak
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

### uninstallation
To uninstall Pashmak, run this make command in terminal:

```bash
sudo make uninstall
```

Or manually remove `/usr/bin/pashmak`.

Pashmak will be remove from your system.

## Windows
In Windows, you can run program with python interpreter without compiling:

```bash
cd \path\to\project
python src\pashmak.py
```

But also you can compile it with `pyinstaller`. If you don't have Pyinstaller, run `pip install pyinstaller` in command line.

Compile:

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
