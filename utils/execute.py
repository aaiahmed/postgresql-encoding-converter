"""
Executes a command in command line.
"""

import subprocess


def execute(command):
    """
    Executes the given command.
    :param command: command
    :return: output, error
    """
    return subprocess.run(command, check=True, stdin=subprocess.PIPE)


def main():
    """Main function."""
    command = ["ls", "-la"]
    result = execute(command)
    print(result.stdout)


if __name__ == '__main__':
    main()


