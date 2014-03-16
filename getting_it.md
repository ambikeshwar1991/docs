## Getting it
Sandhi, as mentioned earlier, is a free and open-source software, it can be downloaded and distributed freely under GNU GPL V3

### Pre-requisites

Sandhi is conglomeration of libraries and softwares. It uses GNU Radio at its core. For computational purposes, Scilab and Octave can be interfaced with Sandhi. Sandhi uses a special wrapper called Sciscipy which allows one to call scilab functions from python without having to worry about datatype conversion.

---------------------------
#### <a href='http://gnuradio.org/redmine/projects/gnuradio/wiki/UbuntuInstall#Install-the-Pre-Requisites'>Installing GNU Radio dependencies</a>

*If on Ubuntu 12.04, one can directly install using command*-


	sudo apt-get -y install git-core autoconf automake make libtool g++ python-dev swig \
	pkg-config libboost1.48-all-dev libfftw3-dev libcppunit-dev libgsl0-dev \
	libusb-dev sdcc libsdl1.2-dev python-wxgtk2.8 python-numpy \
	python-cheetah python-lxml doxygen python-qt4 python-qwt5-qt4 libxi-dev \
	libqt4-opengl-dev libqwt5-qt4-dev libfontconfig1-dev libxrender-dev \
	python-serial python-matplotlib

_Please note that Sandhi has been known to **not** work libboost1.49 available in Ubuntu 12.10 repositories._

-------------------------
#### <a href='http://forge.scilab.org/index.php/p/sciscipy/'> Sciscipy </a>
Sciscipy is _must_ for Sandhi's control blocks to work; to install:

Clone sciscipy-1.0.0 from our repository; run _install_ script from the directory with **sudo** privileges to automatically pull all dependencies for Sciscipy, build and install it<br>

	git clone https://github.com/manojgudi/sciscipy-1.0.0.git
	cd sciscipy-1.0.0/
	sudo ./install


-------------------------------------------------------------------------

### Build it

#### Downloading Source Code

    git clone http://github.com/gnu-sandhi/sandhi.git
    cd sandhi/
    git submodule init
    git submodule update

-- UPDATING FROM EXISTING CHECKOUT --

    cd sandhi/
    git pull origin master
    git submodule update

#### Compiling Source Code

    cd sandhi/
    mkdir build
    cd build/
    cmake ../
    make -j 2
    sudo make install
    sudo ldconfig

#### Current Build Status [![Build Status](https://travis-ci.org/manojgudi/sandhi.png)](https://travis-ci.org/gnu-sandhi/sandhi)

### Get Binary

Builds for Ubuntu 12.04 for 64bit Architecture is hosted [here](http://fossee.in/sandhi_builds/)


#### Packaging it for Ubuntu for other architecture
We use a package called [fpm](https://github.com/jordansissel/fpm/wiki) to roll-out .deb files for Ubuntu.

1. First install fpm for Ubuntu <br>
`sudo apt-get install rubygems`

2. Download [ffi package](http://rubygems.org/downloads/ffi-1.9.0.gem) <br>
Install that using gem<br>
`gem install ffi`

3. Similarly, download latest fpm.gem<br>
`gem install fpm`

Now packaging Sandhi using fpm we have to build Sandhi by changing _cmake_ option.<br>
`cmake -DCMAKE_INSTALL_PREFIX:PATH=out`

and then proceed as given in __Build it__ section from _make_ command.

`fpm -s dir -t deb -n "sandhi" -v 0.9 -C out/ -p sandhi-VERSION_ARCH.deb -d "git-core autoconf automake make libtool g++ python-dev swig pkg-config libboost1.48-all-dev libfftw3-dev libcppunit-dev libgsl0-dev libusb-dev sdcc libsdl1.2-dev python-wxgtk2.8 python-numpy python-cheetah python-lxml doxygen python-qt4 python-qwt5-qt4 libxi-dev libqt4-opengl-dev libqwt5-qt4-dev libfontconfig1-dev libxrender-dev" /usr/local/bin /usr/local/include/ /usr/local/lib /usr/local/libexec/ /usr/local/share/ /usr/local/etc/`

#### Final steps
- To run sandhi, path variables need to be set; even if one has installed through debian package.
- Set Path variables in /etc/environment 
`export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games`<br>
`export SCI=/usr/share/scilab`<br>
`export LD_LIBRARY_PATH=:/usr/lib/scilab:/usr/lib/jvm/java-6-openjdk-amd64/jre/lib/amd64/server/:/usr/lib/jvm/java-6-openjdk/jre/lib/amd64/native_threads/:/usr/local/lib`<br>
`export PYTHONPATH=/usr/local/lib/python2.7/dist-packages/`<br>

- Source /etc/environment in .bashrc<br>
`source /etc/environment`<br>
- Logout and login again, and you are done!

------------

