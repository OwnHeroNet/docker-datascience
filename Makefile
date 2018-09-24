TOPTARGETS := clean push

#SUBDIRS := $(wildcard */.)
SUBDIRS := $(wildcard minimal shell jupyter complete)

$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBDIRS)
.DEFAULT: all

complete: jupyter
jupyter: shell
shell: minimal
