.PHONY: install-dev
install-dev: dev.txt
	pip-sync $^

dev.txt: dev.in
	pip-compile $<

.PHONY: clean
clean:
	- rm *.txt
