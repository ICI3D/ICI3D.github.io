## ICI3D/io

# http://localhost:4000/daidd
# http://ICI3D.github.io/daidd
# http://localhost:4000/MMED/schedule/shadow.html
# http://localhost:4000/MMED/team
# http://localhost:4000/MMED/apply
# http://localhost:4000/mmed/apply

current: target
-include target.mk

# include makestuff/perl.def

######################################################################

# Content

vim_session:
	bash -cl "vmt"

######################################################################

alldirs += futures

Sources += $(wildcard jdresources/*)

######################################################################

## daidd DAIDD Working with Pulliam 2022 Sep 08 (Thu)
## Maybe make a Makefile there later

Sources += daidd/*.md
Sources += mmed/*.md

######################################################################

Sources += _data/team/*

######################################################################

Sources += Gemfile.jd
Ignore += Gemfile Gemfile.lock

Sources += _config.yml $(wildcard *.config)
Ignore += _localconfig.yml

cerve: jekyll.log
	./run.sh > jekyll.log 2>&1 &
## jd.local:
%.local:
	/bin/ln -fs $*.config _localconfig.yml

## Gemfile is under revision control; have not tested whether it works on JD/ubuntu 2023 Aug 31 (Thu)

######################################################################

### Makestuff

Sources += Makefile

## Sources += content.mk
## include content.mk

Ignore += makestuff
msrepo = https://github.com/dushoff
Makefile: makestuff/Makefile
makestuff/Makefile:
	git clone $(msrepo)/makestuff
	ls $@

-include makestuff/os.mk
-include makestuff/git.mk
## -include makestuff/submod.mk
-include makestuff/visual.mk
-include makestuff/projdir.mk
