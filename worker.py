import sys
import signal
import socket
import threading
import pymysql
from arguments import argparser

COMMANDS = ["PUB", "SUBN", "SUB", "UNSUB", "GET", "SET"]


def count(result):
    count = [0 for _ in range(len(COMMANDS))]
    for i, res in enumerate(result[:-1]):
        ok, id_person, count_res = res.split()
        count[i] = int(count_res)
    return count


def record_db_maria(conn, result, ):
    c = conn.cursor()

    result = result.split('\r\n')[:-1]

    count_res = count(result)
    c.execute(f"INSERT INTO status_statuslog( cmd_id, value, created ) VALUES ( 1, {count_res[0]}, NOW() )")
    c.execute(f"INSERT INTO status_statuslog( cmd_id, value, created ) VALUES ( 2, {count_res[1]}, NOW() )")
    c.execute(f"INSERT INTO status_statuslog( cmd_id, value, created ) VALUES ( 3, {count_res[2]}, NOW() )")
    c.execute(f"INSERT INTO status_statuslog( cmd_id, value, created ) VALUES ( 4, {count_res[3]}, NOW() )")
    c.execute(f"INSERT INTO status_statuslog( cmd_id, value, created ) VALUES ( 5, {count_res[4]}, NOW() )")
    c.execute(f"INSERT INTO status_statuslog( cmd_id, value, created ) VALUES ( 6, {count_res[5]}, NOW() )")
    conn.commit()


def get_status(sock):
    cmd = "STATUS 1 PUB\r\nSTATUS 2 SUBN\r\nSTATUS 3 SUB\r\nSTATUS 4 UNSUB\r\nSTATUS 5 GET\r\nSTATUS 6 SET\r\n"
    sock.sendall(cmd.encode())

    result = ""
    continue_recv = True
    while continue_recv:
        res = sock.recv(1024)
        result += res.decode()

        if result.count('\r\n') == len(COMMANDS):
            continue_recv = False

    return result


def on_stop_handler(signum, frame):
    print('Exiting application...')
    sock.close()
    conn.close()
    sys.exit(0)

def listen_stop_signal():
    signal.signal(signal.SIGINT, on_stop_handler) #sigint : ctrl + c
    signal.signal(signal.SIGTERM, on_stop_handler) #sigterm : termination signal

def main():
    listen_stop_signal()
    result = get_status(sock)
    record_db_maria(conn, result)

    print("hello worker is working")
    print(f"query time : {args.query_time}")
    threading.Timer(args.query_time, main).start()

if __name__ == "__main__":
    args = argparser()
    sock = socket.socket()
    conn = pymysql.connect(host=args.host,
                           user="admin",
                           password="cloa2514",
                           db="cloaweb",
                           )
    main()
