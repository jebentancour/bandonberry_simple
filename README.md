# bandonberry_simple

Habiliar la interfaz SPI con el comando ``sudo raspi-config``.

Ir a Interfacing Options, seleccionar SPI.
Responder YES cuando pregunte si queremos habilitar SPI y listo.

Reiniciar con ``sudo reboot`` para que se realicen los cambios.

Descargar este repositorio con el comando ``git clone https://github.com/jebentancour/bandonberry_simple.git``.

Ir a la carpeta descargada ``cd bandonberry_simple`` y correr el programa de test de las botoneras ``python botoneras.py``.

Presionar los botones y observar la salida de texto.
Presionar ctrl-c para salir del programa.

sudo apt-get install fluidsynth
sudo apt-get install build-essential
sudo apt-get install libasound2-dev
sudo apt-get install libjack-jackd2-dev
sudo apt-get install python-dev python-pip
sudo pip install rtmidi-python
sudo pip install gpiozero

sudo fluidsynth -i -s -a alsa -g 3 -c 2 -z 64 /home/pi/bandonberry_simple/bandoneon_v2.sf2 &

python send_midi_test.py

python bandonberry.py
