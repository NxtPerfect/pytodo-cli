import argparse
import config


class Cli():
    pass


class ArgParser():
    def __init__(self):
        self.parser = argparse.ArgParser(
            prog='Pytodo',
            description='Simple python program to organize your work, add and complete tasks, set due date',)
        self.parser.add_argument('taskname')
        self.parser.add_argument('-c', '--complete')


class Config():
    pass


def run():
    argparse
    config
