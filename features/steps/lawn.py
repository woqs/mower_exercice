from behave import *
from subprocess import PIPE, Popen


@given('I have a file with')
def step_impl(context):
    f = open("test.txt", "a")
    for row in context.table:
        f.write(row['boundaries'] + "\n")
        f.write(row['starting_position'] + "\n")
        f.write(row['directions'] + "\n")
    f.close()


@when('I run the program')
def step_impl(context):
    sp = Popen(['./run.py', 'test.txt'], stdout=PIPE, stderr=PIPE)
    out, err = sp.communicate()
    context.result = out.decode('utf-8').strip()


@then('I should have {result} as a result')
def step_impl(context, result):
    assert context.result == result, context.result + " != " + result
