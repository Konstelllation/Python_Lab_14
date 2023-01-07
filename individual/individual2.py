#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import pathlib
import colorama
from colorama import Fore, Style


def tree(directory):
    print(Fore.RED + f'>>> {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = ' ' * depth
        print(Fore.MAGENTA + Style.BRIGHT + f'{spacer} >> {path.name}')
        for new_path in sorted(directory.joinpath(path).glob('*')):
            depth = len(new_path.relative_to(directory.joinpath(path)).parts)
            spacer = '\t' * depth
            print(Fore.CYAN + f'{spacer} > {new_path.name}')

def main(command_line=None):
    colorama.init()
    path = pathlib.Path.cwd()
    file_parser = argparse.ArgumentParser(add_help=False)

    parser = argparse.ArgumentParser("tree")
    parser.add_argument(
        "--version",
        action="version",
        help="The main parser",
        version="%(prog)s 0.1.0"
    )

    subparsers = parser.add_subparsers(dest="command")

    create = subparsers.add_parser(
        "file",
        parents=[file_parser]
    )
    create.add_argument(
        "filename",
        action="store"
    )

    create = subparsers.add_parser(
        "directory",
        parents=[file_parser]
    )
    create.add_argument(
        "filename",
        action="store"
    )

    create = subparsers.add_parser(
        "how",
        parents=[file_parser]
    )
    create.add_argument(
        "filename",
        action="store"
    )

    args = parser.parse_args(command_line)
    if args.command == "file":
        directory_path = path / args.filename
        directory_path.touch()
        tree(path)
    elif args.command == 'directory':
        directory_path = path / args.filename
        directory_path.mkdir()
        tree(path)
    else:
        tree(path)


if __name__ == "__main__":
    main()