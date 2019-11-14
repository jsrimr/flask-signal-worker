import sys
import signal
import socket
import threading
import pymysql
from arguments import argparser

cmd_list = ["PUBLISH",
"message",
"SUBSCRIBE",
"UNSUBSCRIBE",
"SET",
"GET",
"RPUSH",
"LPOP",
"PING",
"STATUS"]

cmd = ""
for cmd_ in cmd_list:
    tmp = "status "+cmd_+"\r\n"
    cmd += tmp


def record_db_maria(conn, result, ):
    c = conn.cursor()

    count_res = result.replace("\r\n", "").split(':')[1:]

    c.execute(f"INSERT INTO status_statuslog( cmd_id, value, created ) VALUES ( 1, {count_res[0]}, NOW() )")
    c.execute(f"INSERT INTO status_statuslog( cmd_id, value, created ) VALUES ( 2, {count_res[1]}, NOW() )")
    c.execute(f"INSERT INTO status_statuslog( cmd_id, value, created ) VALUES ( 3, {count_res[2]}, NOW() )")
    c.execute(f"INSERT INTO status_statuslog( cmd_id, value, created ) VALUES ( 4, {count_res[3]}, NOW() )")
    c.execute(f"INSERT INTO status_statuslog( cmd_id, value, created ) VALUES ( 5, {count_res[4]}, NOW() )")
    c.execute(f"INSERT INTO status_statuslog( cmd_id, value, created ) VALUES ( 6, {count_res[5]}, NOW() )")
    c.execute(f"INSERT INTO status_statuslog( cmd_id, value, created ) VALUES ( 6, {count_res[6]}, NOW() )")
    c.execute(f"INSERT INTO status_statuslog( cmd_id, value, created ) VALUES ( 6, {count_res[7]}, NOW() )")
    c.execute(f"INSERT INTO status_statuslog( cmd_id, value, created ) VALUES ( 6, {count_res[8]}, NOW() )")
    c.execute(f"INSERT INTO status_statuslog( cmd_id, value, created ) VALUES ( 6, {count_res[9]}, NOW() )")
    conn.commit()
    print("wrote status to db")


def get_status(cmd, sock):
    sock.sendall(cmd.encode())

    result = ""
    continue_recv = True
    while continue_recv:
        res = sock.recv(1024)
        result += res.decode()

        if result.count('\r\n') == len(cmd_list):
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

    result = get_status(cmd, sock)
    record_db_maria(conn, result)

    print("hello worker is working")
    print(f"query time : {args.query_time}")
    threading.Timer(args.query_time, main).start()

if __name__ == "__main__":
    listen_stop_signal()
    args = argparser()
    sock = socket.socket()
    sock.connect((args.host, args.port))
    conn = pymysql.connect(host=args.host,
                           user="admin",
                           password="cloa2514",
                           db="cloaweb",
                           )
    main()
