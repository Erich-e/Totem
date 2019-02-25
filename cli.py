#!/usr/bin/env python
"""
CLI interface for task management operations
"""
import argparse

import taskutils

dispatch = {}

def run_cli_command():
    base_parser = argparse.ArgumentParser()

    base_parser.add_argument("func", choices=dispatch)
    base_parser.add_argument("args", nargs=argparse.REMAINDER)

    base_args = base_parser.parse_args()


    dispatch[base_args.func](base_args.args)

def create(args):
    parser = argparse.ArgumentParser()

    parser.add_argument("name")
    parser.add_argument("--description")
    parser.add_argument("--due_date")
    parser.add_argument("--tags", nargs="+")
    parser.add_argument("--event", action="store_true")

    print(taskutils.create(parser.parse_args(args)))


def read(args):
    parser = argparse.ArgumentParser()

    parser.add_argument("--name")
    parser.add_argument("--tags", nargs="+")
    parser.add_argument("-v", "--verbose", action="store_true")

    print(taskutils.read(parser.parse_args(args)))

def update(args):
    parser = argparse.ArgumentParser()

    parser.add_argument("--name")
    parser.add_argument("--description")
    parser.add_argument("--add-tags", nargs="+", dest="add_tags")
    parser.add_argument("--del-tags", nargs="+", dest="del_tags")

    print(taskutils.update(parser.parse_args(args)))

def delete(args):
    parser = argparse.ArgumentParser()

    parser.add_argument("--name")
    parser.add_argument("--undo")

    print(taskutils.delete(parser.parse_args(args)))
def complete(args):
    parser = argparse.ArgumentParser()

    parser.add_argument("--name")
    parser.add_argument("--undo", action="store_true")

    print(taskutils.update(parser.parse_args(args)))

def repl(args):
    dispatch["exit"] = exit
    while(True):
        run_cli_command()


if __name__ == "__main__":

    dispatch = {
        "create": create,
        "read": read,
        "update": update,
        "delete": delete,
        "complete": complete,
        "repl": repl
    }

    run_cli_command()