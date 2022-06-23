
To set up makestuff (once per repo copy), it should work to:
* go to the futures subdirectory
* `make Makefile`

To change the schedule, it should work to:
* edit shadow.md
* `make index.md`
* sync the repo

The shortcut way is:
* edit shadow.md
* `make up.time`

to take care of updating and syncing in one step (this may or may not work depending on editor setup).

__Note that it may take time for github to rebuild this giant site.__

The rules for how to control what is shown in [the schedule](http://www.ici3d.org/futures/) are at the top of [the shadow](http://www.ici3d.org/futures/shadow.html)
