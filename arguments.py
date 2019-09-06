import argparse


def get():
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('--repeats', type=int, default=10, help='Requests repeats')
    parser.add_argument('--url', type=str, default='http://google.com', help='Request URL')

    args = parser.parse_args()
    return args
