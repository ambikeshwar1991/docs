## Code Development

### Disruptive introduction to framework

This section is intended to be a quick introduction to architecture of Sandhi without getting into unnecessary details.

#### Sandhi Architecture
Sandhi is fork of GRAS(GNU Radio Advanced Scheduler) at core, but it also incorporates other modules like Sciscipy etc.
![Sandhi architecture](images/architecture.png)<br>
[GRAS](https://github.com/guruofquality/gras) is the application scheduler of Sandhi. It enables Sandhi to have closed-loop flowgraphs, dispatch threads, handle thread synchronization and much more.<br>
To know more, checkout it's [wiki](https://github.com/guruofquality/gras/wiki)

Essence of open-source development is to reuse the existing code and to build on top of it; several programs are generally written in high level programming languages such as Scilab/GNU-Octave since-
* It is easier to develop programs on them.
* Lot of libraries or toolboxes are availabe for such languages, which reduces the work.
Hence, Sandhi provides a way to reuse **Scilab** programs as functional blocks through a wrapper called _Sciscipy_. Sciscipy is essentially a wrapper written in C language to provide a mechanism to call Scilab's computational engine through Python while taking care of datatype conversion. <br>
To know more, here's link to it's [official page](http://forge.scilab.org/index.php/p/sciscipy/)






