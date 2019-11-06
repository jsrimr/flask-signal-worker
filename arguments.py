import argparse


def argparser():
    parser = argparse.ArgumentParser()

    parser.add_argument('--host', type=str, default="cw.cloa.io",
                        help='type host')

    parser.add_argument('--port', type=int, default=4242,
                        help='type port')

    parser.add_argument('--query_time', type=int, default=1,
                        help='type query time')

    parser.add_argument('--db', type=str, default="maria",
                        help='type query time')

    args = parser.parse_args()
    return args