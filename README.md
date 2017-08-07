# PYTB
Post-Yafte Telegram bot

Post-Yafte URL: http://postyafteh.post.ir/

Setting up development Environment on Linux
----------------------------------

### Installing Dependencies

    $ sudo apt-get install libass-dev build-essential

### Setup Python environment

    $ sudo apt-get install python3-pip python3-dev
    $ sudo pip3 install virtualenvwrapper
    $ echo "export VIRTUALENVWRAPPER_PYTHON=`which python3.5`" >> ~/.bashrc
    $ echo "alias v.activate=\"source $(which virtualenvwrapper.sh)\"" >> ~/.bashrc
    $ source ~/.bashrc
    $ v.activate
    $ mkvirtualenv --python=$(which python3.5) --no-site-packages pytb

#### Activating virtual environment

    $ workon pytb

#### Upgrade pip, setuptools and wheel to the latest version

    $ pip install -U pip setuptools wheel

### Installing Project (edit mode)

So, your changes will affect instantly on the installed version

#### pytb

    $ cd /path/to/workspace
    $ git clone git@github.com:Carrene/pytb.git
    $ cd pytb
    $ pip install -e .
