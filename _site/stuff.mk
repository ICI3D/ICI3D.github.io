msrepo = https://github.com/dushoff
gitroot = ./
export ms = $(gitroot)/makestuff
Drop = ~/Dropbox

-include local.mk
-include $(gitroot)/local.mk
export ms = $(gitroot)/makestuff
-include $(ms)/os.mk

Makefile: $(ms) $(subdirs)

$(ms):
	cd $(dir $(ms)) && git clone $(msrepo)/$(notdir $(ms)).git
