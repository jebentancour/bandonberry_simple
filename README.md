# bandonberry_simple

Habiliar la interfaz SPI con el comando ``sudo raspi-config``.

Ir a Interfacing Options, seleccionar SPI.
Responder YES cuando pregunte si queremos habilitar SPI.

Reiniciar con ``sudo reboot`` para que se realicen los cambios.

Descargar este repositorio con el comando ``git clone https://github.com/jebentancour/bandonberry_simple.git``.

Ir a la carpeta descargada ``cd bandonberry_simple`` y correr el programa de test de las botoneras ``python botoneras.py``.

Presionar los botones y observar la salida de texto.
Presionar ctrl-c para salir del programa.

Instalar las dependencias.

```
sudo apt-get install fluidsynth
sudo apt-get install build-essential
sudo apt-get install libasound2-dev
sudo apt-get install libjack-jackd2-dev
sudo apt-get install python-dev python-pip
sudo pip install rtmidi-python
sudo pip install gpiozero
```
Abrir el sintetizador y dejarlo corriendo en segundo plano.

```
sudo fluidsynth -i -s -a alsa -o audio.alsa.device=hw:1 -g 3 -c 4 -z 64 /home/pi/bandonberry_simple/bandoneon_v2.sf2 &
```

Correr el programa principal del bandonberry.

```
python bandonberry.py
```

Para que los programas necesarios sean inicados en automáticamente se deben agregar los comandos de inicialización a ``/etc/rc.local``.

```
sudo fluidsynth -i -s -a alsa -o audio.alsa.device=hw:1 -g 3 -c 4 -z 64 /home/pi/bandonberry_simple/bandoneon_v2.sf2 &
python /home/pi/bandonberry_simple/bandonberry.py &
```
