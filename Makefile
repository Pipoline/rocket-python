.PHONY: clean-pyc clean-build docs clean


docs:
	rm -f docs/rocketchat.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ rocketchat
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
