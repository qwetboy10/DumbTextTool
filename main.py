import sys, re, os
import inspect, pkgutil
from importlib import import_module
import tests

def run_tests(file_name, verbose):
    with open(file_name, mode='r') as file:
        contents = file.read()
    ret = []
    for (_, name, _) in pkgutil.iter_modules(['./tests']):
        try:
            ret.append('----- ' + name + ' -----')
            module = import_module('.' + name, package='tests')
            solve = getattr(module, 'solve')
            solve_verbose = getattr(module, 'solve_verbose')
            ret.extend(solve(contents))
            if verbose:
                ret.extend(solve_verbose(contents))
        except Exception as e:
            print('Exception when running test',name)
            print(e)
    return ret

if len(sys.argv) >= 2:
    flag_filter = None
    verbose = False
    file_name = sys.argv[1]
    for i in range(2,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            print('Usage: main.py file [--verbose] [--filter regex]')
            sys.exit(0)
        if sys.argv[i] == '-v' or sys.argv[i] == '--verbose':
            verbose = True
        if sys.argv[i] == '-f' or sys.argv[i] == '--filter':
            if i+1 < len(sys.argv):
                flag_filter = sys.argv[i+1]
            else:
                print('filter regex not specified')
                print('Usage: main.py file [--verbose] [--filter regex]')
    candidates = run_tests(file_name, verbose)
    if flag_filter is not None:
        p = re.compile(flag_filter)
        candidates = [ s for s in candidates if p.match(s) ]
    for candidate in candidates:
        if candidate is not None and candidate != '' and candidate != '\n':
            print(candidate.strip())
else:
    print('Usage: main.py file [--verbose] [--filter regex]')
    sys.exit(0)



