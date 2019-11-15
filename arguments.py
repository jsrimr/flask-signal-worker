import argparse


def argparser():
    parser = argparse.ArgumentParser()

    parser.add_argument('--broker', type=str, default="34.84.41.232",
                        help='type host')

    parser.add_argument('--broker_port', type=int, default=6380,
                        help='type port')

    parser.add_argument('--query_time', type=int, default=1,
                        help='type query time')

    parser.add_argument('--db_host', type=str, default="cw.cloa.io",
                        help='type query time')

    args = parser.parse_args()
    return args