# System board app (WIP)

Masonite web app to drive climbing climbing boards such as the Tension board, the Moonboard and the Kilter board.

## Requirements

- Python 3.4 +
- OpenSSL (latest version)
- Pip

## Linux

If you are running on a Linux flavor, you’ll need a few extra packages before you start. You can download these packages by running:

```
$ sudo apt-get install python-dev libssl-dev
```

Instead of `python-dev` you may need to specify your Python version

```
$ sudo apt-get install python3.6-dev libssl-dev
```

## Windows

With windows you will need to have the latest OpenSSL version. Install [OpenSSL 32-bit or 64-bit](https://slproweb.com/products/Win32OpenSSL.html).

## Mac

If you do not have the latest version of OpenSSL you will encounter some installation issues with creating new applications since we need to download a zip of the application via GitHub.

With Mac you can install OpenSSL through `brew`.

```
brew install openssl
```

Python 3.6 does not come preinstalled with certificates so you may need to install certificates with this command:

```
/Applications/Python\ 3.6/Install\ Certificates.command
```

You should now be good to install new Masonite application of Mac :)

## Installation:

```
pip install -r requirements.txt
python craft serve
```

Go to `http://localhost:8000/`
## Installation

The best way to install Masonite is by starting in a virtual environment first. This will avoid any issues with filesystem permissions.

```
python3 -m venv venv
```

Then activate the virtual environment:

```
WINDOWS: $ ./venv/Scripts/activate
MAC: $ source venv/bin/activate
```

