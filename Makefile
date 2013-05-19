clean:
	rm -f *~ *.pyc \#*
count:
	printf "%d lines of python code\n  \t%d lines in main.py\n \t%d lines in vm.py\n" `cat *.py| wc -l` `cat main.py| wc -l` `cat vm.py| wc -l` 
run:
	python -tt test.py

.PHONY: clean count run
