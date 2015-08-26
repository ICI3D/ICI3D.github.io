### Hooks for the editor to set the default target
current: target

target pngtarget pdftarget vtarget acrtarget: notarget

##################################################################

# make files

Sources = Makefile 

##################################################################

md = ../make/
rrd = ../RR/

local = default
-include $(md)/local.mk
-include $(md)/$(local).mk
-include $(rrd)/inc.mk

