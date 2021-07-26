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

Para que los programas necesarios sean iniciados automáticamente se deben agregar los comandos de inicialización a ``/etc/rc.local``.

```
sudo fluidsynth -i -s -a alsa -o audio.alsa.device=hw:1 -g 3 -c 4 -z 64 /home/pi/bandonberry_simple/bandoneon_v2.sf2 &
python /home/pi/bandonberry_simple/bandonberry.py &
```

El mecanismo de apagado es el de [RaspiATX](https://github.com/LowPowerLab/ATX-Raspi).

Un script que corre en la raspberry monitorea el estado de un pin para enviar una señal de apagado en el sistema cuando se detecta un cambio en su estado. Una señal es enviada por otro pin para indicar el correcto booteo del sistema. Solo utilizamos los scripts provistos e implementamos en el BMS la funcionalidad del manejo de la energía.

Se copia el script de instalación: 
```
sudo wget https://raw.githubusercontent.com/LowPowerLab/ATX-Raspi/master/shutdownchecksetup.sh
```
Se editan los pines a usar ```sudo nano shutdownchecksetup.sh```:
```Python
SHUTDOWN = 12     # GPIO used for shutdown signal
BOOT = 16         # GPIO used for boot signal
```
Se instala eligiendo la opción 1:
```
sudo bash shutdownchecksetup.sh
sudo rm shutdownchecksetup.sh
sudo reboot
```
