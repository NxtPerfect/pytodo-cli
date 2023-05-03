import argparse
from .todo import todo
from .database import database
from .config import config


def main():
    argparse
    todo
    config
    id = 0
    if database.Database.get_all_tasks() is None:
        id = database.Database.data['tasks'][-1]['id']
    id += 1
