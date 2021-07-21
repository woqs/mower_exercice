run:
	python3.7 run.py lawn.txt

test-unit:
	python3.7 -m unittest discover -s test/ . "*Test.py"

test-behavioural:
	behave

test: test-unit
test: test-behavioural

