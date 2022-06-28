## This is ICI3D's main web repo futures subdirectory
## http://www.ici3d.org/futures/
## http://www.ici3d.org/futures/shadow.html

current: target
-include target.mk
Ignore = target.mk

-include makestuff/perl.def

vim_session:
	bash -cl "vmt shadow.md README.md"

######################################################################

Sources += $(wildcard *.md *.pl)

index.md: shadow.md shadow.pl
	$(PUSHRO)

### Makestuff

Sources += Makefile

Ignore += makestuff
msrepo = https://github.com/dushoff

Makefile: makestuff/00.stamp
makestuff/%.stamp: | makestuff/Makefile
	- $(RM) makestuff/*.stamp
	touch $@

makestuff/Makefile:
	(cd .. && $(MAKE) $@) && /bin/ln -s ../makestuff .

-include makestuff/os.mk

## -include makestuff/pipeR.mk

-include makestuff/git.mk
-include makestuff/visual.mk
