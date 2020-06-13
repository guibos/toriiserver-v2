import argparse

from src.application.common.enums.environment_enum import EnvironmentEnum
from src.main import create_app


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='ToriiServer',
        epilog="And that's how you'd foo a bar",
    )
    parser.add_argument(
        '--environment',
        metavar='environment',
        nargs='?',
        help='Environment to choice',
        dest='environment',
        type=EnvironmentEnum,
        choices=EnvironmentEnum.__members__.values(),
    )

    return parser.parse_args()


if __name__ == '__main__':
    arguments = parse_arguments()
    app = create_app(arguments=arguments)
    app.run()  # debug=True
