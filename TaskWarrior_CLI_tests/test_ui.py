import os 


def test_addlist():

    #add list and assert list contents, then cleanup list 
    os.system('task list')
    os.system('yes')
    os.system('task add test scripts')
    os.system('task add push to repo')
    stream = os.popen('task list')
    output = stream.read()
    assert 'test scripts' in output
    assert 'push to repo' in output
    assert '2 tasks' in output
    #cleanup
    os.system('task 1 done')
    os.system('task 2 done')
    stream = os.popen('task list')
    output = stream.read()
    assert output == ''


def test_modify_list():

    #add a list, modify the contents, expect the modified list then cleanup
    os.system('task add test scripts')
    os.system('task modify 1 push to repo')
    stream = os.popen('task list')
    output = stream.read()
    assert 'push to repo' in output
    assert 'test scripts' not in output
    #cleanup
    os.system('task 1 done')
    output = stream.read()
    assert output == ''

def test_modify_due_date():

    #add a list, modify the due date column, expect the modified list then cleanup
    os.system('task add test scripts due:2023-04-03')
    os.system('task list')
    os.system('task modify 1 due:2025-05-12')
    stream = os.popen('task list')
    output = stream.read()
    assert '2025-05-12' in output
    assert '2023-04-03' not in output
    assert 'test scripts' in output
    #cleanup
    os.system('task 1 done')
    output = stream.read()
    assert output == ''

def test_skip_filters():
    #Runtime error in cli; hangs on attempting to list with filters, command works manually. Debugging TODO
 #   #add multiple junk lists, filter to a specific list, expect list then cleanup
    os.system('task add holy_grail')
    os.system('task add junklist1')
    os.system('task add junklist2')
    stream = os.popen('task holy_grail list')
    output = stream.read()
    assert 'holy_grail' in output
    assert 'junklist' not in output
 
    #cleanup - 'task delete' and 'task purge' seem to cause errors during runtime; cleanup needs to be manual using task completion commands for now 
    os.system('task 1 done')
    os.system('task 2 done')
    os.system('task 3 done')
    output = stream.read()
    assert output == ''
 #   os.system('task delete all')
 #   os.system('yes')
 #   os.system('all')
 #   os.system('task purge')
 #   os.system('yes')
 #   os.system('all')
 #   stream = os.popen('task list')
 #   output = stream.read()
 #   assert output == ''

