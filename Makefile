SHELL = /bin/bash
PYTHON = /usr/bin/python3
DATADIR = /usr/share/ansible/roles
BUILDROOT =

install:
	mkdir -p $(BUILDROOT)$(DATADIR)/dci-sync-registry
	chmod 755 $(BUILDROOT)$(DATADIR)/dci-sync-registry

	cp -r defaults $(BUILDROOT)$(DATADIR)/dci-sync-registry
	cp -r files $(BUILDROOT)$(DATADIR)/dci-sync-registry
	cp -r tasks $(BUILDROOT)$(DATADIR)/dci-sync-registry
	cp -r templates $(BUILDROOT)$(DATADIR)/dci-sync-registry
	cp -r handlers $(BUILDROOT)$(DATADIR)/dci-sync-registry

	! type -p pathfix.py || pathfix.py -pni $(PYTHON) $(BUILDROOT)$(DATADIR)/dci-sync-registry/files/fetch_images.py
