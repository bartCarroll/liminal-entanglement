This page holds the design for the 2019 Burning Man Project Liminal Entanglement. 

## Design Decisions

Initially, we wanted multiple terminals in which users could interact with terminals spread across the playa. These 
terminals would interact via wifi. However, technical limitations on the distance of wifi and possibly congested RF spectrum
made us re-focus on a single terminal design. We have settled on having a single "terminal" located with the door which 
will reduce cost, and provide for a more meaningful interaction with the door. 

- Power will be provided by deep cycle batteries with solar panels. 
- The flip-dot board requires 2 x 24V DC power. Initially it was thought that we should connect the batteries in series
to get 24V out, however research has shown that this may negatively affect the ability to charge the batteries. Instead 
the batteries will be connected in parallel. 
- Raspberry Pi was chosen over arduino due to the number of inputs and outputs required, along with the ease of using
on-board USB, audio out, and on-board storage. 
- We will leverage existing libraries to control the flip-dot board. 

Open questions are located [here](research.md).

## Required Packages 

- `sudo apt-get install python-gst-1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools`

## Terminal With Door Flow

Below is the logic flow assuming the door is co-located with the terminal.

![flow](diagrams/terminal_flowchart.png)

### Circuit Diagram

![raspberry pi](diagrams/raspberry-pi-circuit.png)

### Components

- [14 x 28 Flip-Dot Display](https://flipdots.com/en/products-services/flip-dot-boards-xy5/)
- [Raspberry Pi 4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/specifications/)
- [AlfaZeta XY5 Flip-Dot display](https://flipdots.com/en/products-services/flip-dot-boards-xy5/)
- [USB to RS485 Module](https://www.amazon.com/JBtek-Converter-Adapter-ch340T-Supported/dp/B00NKAJGZM/ref=sr_1_3?keywords=USB+to+RS485&qid=1562355433&s=gateway&sr=8-3)
- [12v to 5v Step-Down Converter](https://www.amazon.com/Converter-DROK-Regulator-Inverter-Transformer/dp/B01NALDSJ0/ref=sr_1_6?keywords=12+volt+to+5+volt+power+regulator&qid=1562112182&s=gateway&sr=8-6)

### Original Diagram

![circuit diagram](diagrams/terminal_diagram.PNG)

