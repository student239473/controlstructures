total_tasks = 20
tasks_ok = int(input('Enter the number of correctly completed tasks: '))
test_passed = False

if tasks_ok >= total_tasks * 0.5:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')