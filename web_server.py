import socket
import network

listen_s = None
client_s = None
req_handler_s = None

def setup_conn(port, accept_handler):
    global listen_s
    listen_s = socket.socket()
    listen_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ai = socket.getaddrinfo("0.0.0.0", port)
    addr = ai[0][4]

    listen_s.bind(addr)
    listen_s.listen(1)
    if accept_handler:
        listen_s.setsockopt(socket.SOL_SOCKET, 20, accept_handler)
    for i in (network.AP_IF, network.STA_IF):
        iface = network.WLAN(i)
        if iface.active():
            print("WebServer daemon started on http://%s:%d" % (iface.ifconfig()[0], port))
    return listen_s

def send_file(socket, file):
    cnt_file = 0
    cnt_write = 0
    with open(file, 'r') as f:
        while True:
            buf = f.read(1024)
            if not buf:
                break
            cnt_file += len(buf)
            cnt_write += socket.write(buf)
    
    print('Send:', file, cnt_file, cnt_write)
            
def accept_conn(listen_sock):
    global client_s
    global req_handler_s
    cl, remote_addr = listen_sock.accept()

    print("WebServer connection from:", remote_addr)
    client_s = cl
    cl.settimeout(2)
    try:
        recv_data = cl.recv(1*1024)
    except:
        pass
    else:
        recv_data = str(recv_data)
        print("RECIVED: %s" % recv_data)
        if recv_data != '':
            
            get_begin = recv_data.find('GET ')
            get_end = recv_data.find(' ', get_begin+4)
            get_val = recv_data[get_begin+4:get_end]
            
            path = get_val
            if get_val == '/':
                path = 'index.html'
            
            try:
                open(path, 'r')
            except:
                file = False
            else:
                file = True
            
            if file:
                print('Sending file:', path)
                send_file(cl, path)
            elif req_handler_s and req_handler_s(cl, get_val):
                pass
            else:
                print('File not found:', path)
                cl.write('404\n')
            
    cl.close()
    cl.setblocking(False)

def stop():
    global listen_s, client_s
    if client_s:
        client_s.close()
    if listen_s:
        listen_s.close()


def start(port=80, req_handler=None):
    global req_handler_s
    stop()
    req_handler_s = req_handler
    setup_conn(port, accept_conn)
    print("Started WebServer")

