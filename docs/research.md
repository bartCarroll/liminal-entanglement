## Components

- [Raspberry Pi 4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/specifications/)
- [AlfaZeta XY5 Flip-Dot display](https://flipdots.com/en/products-services/flip-dot-boards-xy5/)
- [USB to RS485 Module](https://www.amazon.com/JBtek-Converter-Adapter-ch340T-Supported/dp/B00NKAJGZM/ref=sr_1_3?keywords=USB+to+RS485&qid=1562355433&s=gateway&sr=8-3)
- [12v to 5v Step-Down Converter](https://www.amazon.com/Converter-DROK-Regulator-Inverter-Transformer/dp/B01NALDSJ0/ref=sr_1_6?keywords=12+volt+to+5+volt+power+regulator&qid=1562112182&s=gateway&sr=8-6)
- [12v to 24v Step-Up Converter](https://www.amazon.com/Converter-Regulator-Reducer-Waterproof-SupplyTransformer/dp/B0756W6V4F/ref=sr_1_13?keywords=12v+to+24v+dc+step+up+converter&qid=1562356872&s=gateway&sr=8-13)
- [PiEZ Connect GPIO Breakout](https://www.adafruit.com/product/2711)

## Sample Projects

- [AlfaZeta Flip-Dot with Raspberry Pi](https://www.instructables.com/id/Howto-Flipdot-With-a-Raspi/)
- [AlfaZeta Flip-Dot with Arduino](https://create.arduino.cc/projecthub/iizukak/flip-dot-clock-3dd850)
- [Hanover Flip Dot Display - Raspberry Pi](https://engineer.john-whittington.co.uk/2017/11/adventures-flippy-flip-dot-display/)
- [Raspberry Pi Christmas Light Show](https://www.youtube.com/watch?v=uBKYJW1PBSI)

## Code
- [Flip Dot board driver](https://github.com/dcreemer/flipdot)
- [Raspbian Lite OS](https://www.raspberrypi.org/downloads/raspbian/)
- **Raspberry Pi Flip-Dot driver:** [flipdot_demon.py](https://github.com/vwyf/vwyf_door_sensor/blob/2a281e274d4d14e7d020158d55fd5dc94bfccd13/flipdot_demon.py)
- [Python Daemon Library](https://www.python.org/dev/peps/pep-3143/)

## Software 

### Simulation on Windows

In order to run the simulated terminal on Windows, the curses library needs to be installed. 
If you're on a *nix system you just need to run `pip install curses`
  - [Python Wheels](https://pythonwheels.com/)
  - [Curses Library](https://www.lfd.uci.edu/~gohlke/pythonlibs/)
  - [Installing curses on windows](https://stackoverflow.com/questions/32417379/what-is-needed-for-curses-in-python-3-4-on-windows7)

### Useful Tools

Below is a list of tools needed to build and work with the project.
- [MRemoteNG](https://mremoteng.org/) - For SSH / VNC connection to Raspberry PI
- [pycharm](https://www.jetbrains.com/pycharm/) - Python IDE
- [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) - VNC Client

## Questions

- Will 2 12V 60ah batteries with 150W solar panel be sufficient to power the terminal?
  - Additional batteries can be added in parallel if needed. 
- Any additional need for output besides 2 columns, door lock, sound and the display?
- What will we display? 
  - We have the ability to show gifs
- Should we have alternative input besides a keyboard?
  - Is a keyboard interesting enough for input?
  - If no, prefer USB input. Requires less engineering time.
- We will need airflow to keep they pi cool. if it overheats ??

 


