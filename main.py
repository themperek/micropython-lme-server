from machine import Pin, SPI, PWM
import max7219, time

spi = SPI(1, baudrate=1000000)
display = max7219.Matrix8x8(spi, Pin(15))

def lcd_req_handler(socket, req):
    if req[:5] == '/led=':
        var = req[5:]
        print('Request:', var)
        lcd = eval(var)
        print(lcd)
        for i in lcd:
           display.buffer = bytearray(i);
           display.show();
           time.sleep(0.2)
            
        display.buffer = bytearray(lcd[0]);
        display.show();
            
        return True
    else:
        return False

import web_server
web_server.start(80, lcd_req_handler)
