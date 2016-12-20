# micropython-lme-server
LED matrix 8x8 online editor with self-hosted server for [Micropython](https://micropython.org/).

Tested on [ESP8266](https://en.wikipedia.org/wiki/ESP8266) [Wemos D1 mini](https://www.wemos.cc/product/d1-mini.html) module.

Project based on [LED matrix 8x8 online editor](https://github.com/xantorohara/led-matrix-editor) using [Adafruit MAX7219 driver](https://github.com/adafruit/micropython-adafruit-max7219).

##Installation

Install [Node.js](https://nodejs.org/)

```bash
wget http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.css
wget http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.css
wget http://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.js
wget http://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.js
wget http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.js

npm install uglify-js -g
npm install --save purify-css

uglifyjs jquery.js jquery-ui.js bootstrap.js script.js --compress --mangle -o script.min.js 
node purify_css.js

wget https://raw.githubusercontent.com/adafruit/micropython-adafruit-max7219/master/max7219.py
```

Upload `style.min.css` `main.py` `web_server.py` `script.min.js` `index.html` `max7219.py` and restart.

###TODO:
- save the animation to file and reply after boot
- configure speed and repetition
- reduce size
- mobile friendly
