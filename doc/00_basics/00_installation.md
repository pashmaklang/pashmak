# Installation

## GNU/Linux/Unix
This installation guide is for GNU/Linux/UNIX systems and requires Python >= 3.8. Also the compile process needs the `pyinstaller` pip library.
If you don't have PyInstaller, run the `pip3 install pyinstaller` command in the terminal.

Compile & Install:

```bash
# checkout to latest release
git branch installation $(git describe --abbrev=0)
git checkout installation

# compile and install
make all
make
sudo make install

# go back to the master branch and delete the installation branch
git checkout master
git branch -D installation
```

Run the above commands in the terminal to install the Pashmak interpreter on your GNU/Linux/UNIX system.

Also if you want to install the latest version (development state), do not run the above git commands and just run this:

```bash
make all
make
sudo make install
```

The above commands install the latest (development) state of the program.

Now you can run the interpreter in the terminal:

```bash
$ pashmak --info # shows info about Pashmak
$ pashmak -v # --version, shows version of Pashmak
$ pashmak app.pashm
$ pashmak /path/to/script.pashm # runs file
$ pashmak - # gets code from stdin and runs it
$ pashmak -r "<your code...>" # runs code from cli arguments with the `-r` option

# interactive shell
# to run your code in an interactive shell in the terminal:
$ pashmak @shell
```

If you don't want to install it, you can run it with python3 in the terminal:

```bash
cd /path/to/project/folder
python3 src/pashmak.py
# or
./src/pashmak.py
```

### Uninstallation
To uninstall Pashmak, run this make command in the terminal:

```bash
sudo make uninstall
```

Or manually remove `/usr/bin/pashmak`.

Pashmak will be removed from your system.

## Windows
On Windows, you can run the program with the Python interpreter without compiling:

```bash
cd \path\to\project
python src\pashmak.py
```

But also you can compile it with `pyinstaller`. If you don't have PyInstaller, run `pip install pyinstaller` on the command line.

Compile:

```bash
# install pyinstaller with pip
pip install pyinstaller

# configure & compile
.\win-configure.bat
python -m PyInstaller src\pashmak.py --onefile
```

Now the executable file is created in `dist\pashmak.exe`:

```bash
dist\pashmak.exe -v
```

## Other tools

### Syntax highlighters

- [VSCode](https://github.com/pashmaklang/vscode-pashmak)
- [Nano editor](https://github.com/sami2020pro/pashmak-nanorc)

