from pydep import *
import argparse

def debug():
    import pdb, traceback, code, sys
    def handle_exception(tp, val, tb):  # open up debugger on exception
        traceback.print_tb(tb)
        print 'ERROR:', val
        pdb.post_mortem(tb)
    sys.excepthook = handle_exception

def get_args():
    parser = argparse.ArgumentParser(description='Grab dependencies from a setup.py file')
    parser.add_argument('rootdir', help='path to root project directory')
    parser.add_argument('--debug', action='store_true', help='enable if you want to enable debugging stacktrace')
    parser.add_argument('--toplevel', action='store_true', help='enable if you want to print just top-level modules')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    if args.debug:
        print '##### DEBUG ENABLED #####'
        debug()

    deps = import_tree_for_project(args.rootdir, ignore_stdlib=True, ignore_internal=True)

    if args.toplevel:
        for k in sorted(deps.children.keys()):
            print k
    else:
        deps.print_tree()
