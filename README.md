# SNIFFER v1.3.1 hardware 

| View | Top | Bottom |
| ---- | --- | ------ |
| <img src="doc/t-view.png" alt="drawing" width="300"> | <img src="doc/t-view-top.png" alt="drawing" width="300"/> | <img src="doc/t-view-bottom.png" alt="drawing" width="300"/> |
|  | <img src="doc/r-view-top.jpg" alt="drawing" width="300"/> | <img src="doc/r-view-bottom.jpg" alt="drawing" width="300"/> |

## Features

# Wiring

Schematic features. Schematic can be provided via issue.

**Connectors**

The node has connectors which are described in the table below.

| N | Connector | Description |
| - | - | - |
| 1 | CAN1, CAN2, TARGET SWD |  |
| 2 | CAN3 |  |
| 3 | J1 |  |
| 4 | SWD1, SWD2 |  |
| 5 | TARGET SWD1 |  |

[Here](https://docs.raccoonlab.co/guide/wires/) you can find manufacturer part number of connectors it self and its mates.

## Pin configuration and functions

| Pin N | CAN1 | Pin N | CAN2 | Pin N | TARGETSWD | Pin N | CAN3 | Pin N | J1 | Pin N | SWD1 | Pin N | SWD2 | Pin N | TARGETSWD1 |
| ----- | ---------------- | ----- | ---------------- | ----- | ---------------- | ----- | ---------------- | ----- | ---------------- | ----- | ---------------- | ----- | ---------------- | ----- | ---------------- |
| 1 | VBUS | 1 | VBUS | | | 1 | Vin | A1 | GND | 1 | GND | 1 | GND | | |
| 2 | CAN_H | 2 | CAN_H | | | 2 | Vin | A12 | GND | 2 | SWLK | 2 | SWLK_p | | |
| 3 | CAN_L | 3 | CAN_L | | | 3 | CAN_H | A4 | VBUS | 3 | SWDIO | 3 | SWDIO_p | | |
| 4 | GND | 4 | GND | | | 4 | CAN_L | A5 | IP0 | 4 | 3.3 | 4 | 3.3 | | |
| SH1 | GND | SH1 | GND | | | 5 | GND | A6 | D+ | | | | | | |
| SH2 | GND | SH2 | GND | 6 | GND | A7 | D- | | | | | | |
| P1 | GND | A9 | VBUS | | | | | | |
| P2 | GND | B1 | GND | | | | | | |
| B12 | GND | | | | | | |
| B4 | VBUS | | | | | | |
| B5 | IP1 | | | | | | |
| B6 | D+ | | | | | | |
| B7 | D- | | | | | | |
| B9 | VBUS | | | | | | |
| SH1 | GND | | | | | | |
| SH2 | GND | | | | | | |
| SH3 | GND | | | | | | |
| SH4 | GND | | | | | | |
| SH5 | GND | | | | | | |
| SH6 | GND |


Here you can see all connections of MCU.

<img src="doc/pinout.png" alt="pinout"/>

| MCU PIN         | PIN Numer | NET Name | Description |
| ---------- |  -- | --------------  | - |
| PA0-WKUP       |  10 | WAKE        |  |
| PA12           |  33 | USB_DP      |  |
| PA11           |  32 | USB_DM      |  |
| PA0-WKUP       |  7  | TX2/B2      |  |
| PA2            |  9  | TX2/B2      |  |
| PA10           |  31 | T_SWO_OUT   |  |
| PB0            |  18 | T_NRST_OUT  |  |
| PB14           |  27 | T_JTMS      |  |
| PA5            |  15 | T_JTCK      |  |
| PB13           |  26 | T_JTCK      |  |
| PB1            |  16 | T3CH4/ADC9  |  |
| PB0            |  15 | T3CH3/ADC8  |  |
| PA7            |  14 | T3CH2/ADC7  |  |
| PA6            |  13 | T3CH1/ADC6  |  |
| PA14           |  37 | SWLK_p      |  |
| PA14/JTCK/SWCLKI/O |  28 | SWLK        |  |
| PA13           |  34 | SWDIO_p     |  |
| PB12           |  25 | SWDIO_IN    |  |
| PA13/JTMS/SWDIOI/O |  25 | SWDIO       |  |
| NRST           |  7  | STM_RST     |  |
| PA8            |  20 | STLINK_RX   |  |
| PA9            |  21 | STLINK_RX   |  |
| PA3            |  13 | STLINK_RX   |  |
| PA15/JTDI      |  29 | SPI1_SS     |  |
| PB3/JTDO       |  30 | SPI1_SCK    |  |
| PB5            |  32 | SPI1_MOSI   |  |
| PB4/JNTRST     |  31 | SPI1_MISO   |  |
| PB7            |  34 | SDA/A1      |  |
| PB6            |  33 | SCL/A2      |  |
| PA3            |  10 | RX2/B1      |  |
| PA10           |  22 | RX1/C1      |  |
| PA2            |  12 | RX1/C1      |  |
| NRST           |  4  | NRST        |  |
| PD1-OSC_OUT    |  6  | NetU4_6     |  |
| PD0-OSC_IN     |  5  | NetU4_5     |  |
| PC14-OSC32_IN  |  3  | NetR23_2    |  |
| PC13-TAMPER-RTCI/O |  2  | NetR22_1    |  |
| BOOT0          |  44 | NetR21_1    |  |
| OSC_OUT/PD1    |  3  | NetDD1_3    |  |
| OSC_IN/PD0     |  2  | NetDD1_2    |  |
| PA9            |  30 | LED_STLINK  |  |
| PA5            |  12 | LED_BLUE    |  |
| PA4            |  11 | LED         |  |
| VSSA           |  5  | GND         |  |
| PB2/BOOT1      |  17 | GND         |  |
| VSS_2          |  18 | GND         |  |
| VSS_3          |  26 | GND         |  |
| VSS_1          |  36 | GND         |  |
| VSSA           |  8  | GND         |  |
| PB2            |  20 | GND         |  |
| VSS_1          |  23 | GND         |  |
| VSS_2          |  35 | GND         |  |
| VSS_3          |  47 | GND         |  |
| PA12           |  24 | CAN_TXD     |  |
| PA11           |  23 | CAN_RXD     |  |
| BOOT0          |  35 | BOOT0       |  |
| PA1            |  8  | ADC_5V      |  |
| VDD_1          |  1  | 3.3         |  |
| VDDA           |  6  | 3.3         |  |
| VDD_2          |  19 | 3.3         |  |
| VDD_3          |  27 | 3.3         |  |
| VBAT           |  1  | 3.3         |  |
| VDDA           |  9  | 3.3         |  |
| VDD_1          |  24 | 3.3         |  |
| VDD_2          |  36 | 3.3         |  |
| VDD_3          |  48 | 3.3         |  |


## Specifications

**Mechanical**

Scheme is shown on the picture below. CAN model can be provided via email request or issue on github or downloaded on GrabCAD (opens new window).

<img src="doc/drw.png" alt="drawing" height="400"/>

|       | Width, mm | Length, mm | Height, mm |
| ----- | --------- | ---------- | ---------- |
|Outline|      51.9 |       31.9 |        8.1 |
|PCB    |     51.88 |      31.88 |        1.6 |

Total weight of device less than 50 g.

### Housing

Information about case presented here.

### Absolute Maximum Ratings

### Recommended operating conditions

### ESD ratings

### MTFF

## Integration

**Recommended mechanical mounting**

**Connection example diagram**

### Power Supply Recommendations

Device is designed to operate from an input voltage supply range between 4.5 V and 5.5 V over CAN2 or CAN3 connector, or 5.5 - 30 V from CAN1. This input supply must be able to withstand the maximum input current and maintain a stable voltage. The resistance of the input supply rail should be low enough that an input current transient does not cause a high enough drop that can cause a false UVLO fault triggering and system reset. The amount of bulk capacitance is not critical, but a 47-uF or 100-uF electrolytic capacitor is a typical choice.

## Revision history

|View |Version| Date| Description|
|-    |-      |-    |-           |



## Order details

### PCB Specification Selection

- Board type : Panel by PCBWay
- Break-away rail: Yes
- Instructions:
~~~
Final size is larger ( 51.9 x 31.9 mm ) than board it self ( 51.88 x 31.88 mm), 
take a look at the picure in attachements. 
Panel should be designed to be able to install PWM1, PWM2 while assembly.
~~~
- Route Process: Panel as PCBWay prefer
- X-out Allowance in Panel:  Accept

- Size (single): 51.88 x 31.88 mm
- Quantity (single): 200
- Layers: 2 -   ['Top Layer', 'Bottom Layer'] check [PCBway layer stack](https://www.pcbway.com/multi-layer-laminated-structure.html)

- Material: FR-4
- FR4-TG: TG 150-160
- Thickness: 1.6
- Min Track/Spacing: 7/7mil (0.17 mm)
- Min Hole Size: 0.3 mm
- Solder Mask: Black
- Silkscreen: White
- Edge connector: No
- Surface Finish: HASL with lead
- Yes - Tick means you accept we might change "HASL" to "ENIG" at our discretion without extra charge.
- Via Process: Tenting vias
- Finished Copper: 1 oz Cu
- Other Special request:
~~~
Final size is larger ( 51.9 x 31.9 mm ) than board it self ( 51.88 x 31.88 mm )
~~~

### Assembly Service

- Turnkey
- Board type : Panelized PCBs
-  Assembly Side(s): Both sides
- Quantity: 200
- Contains Sensitive components/parts - No; 
- Do you accept alternatives/substitutes made in China? - Yes

- Number of Unique Parts: 0
- Number of SMD Parts: 0
- Number of BGA/QFP Parts: 0
- Number of Through-Hole Parts: 0

### Additional Options

- Firmware loading: Yes
- Detailed information of assembly:
~~~
Firmware is in attachements in folder 'firmware', programming should be done in the part directly before assembly.
'can-uart.bin' is for DD1 (STM32F103T8U6)
'Protected-2-1-Bootloader.bin' is for U4 (STM32F103CBT6)
~~~

## Device and Documentation Support

- [User manual]()
- [Hardware docs](doc/doc.pdf)

## Device Support

- [Firmware sources]()
- [Firmware binary]()

## TERMS OF USAGE / LICENCE

The material provided in this Github repository is subject to the following conditions. 

Firmware files: All firmwares are free (but not open source). Besides unlimited private use you are also granted the permission to use them for commercial purposes under the condition that (1) you don�t modify the firmware, e.g. remove or change copyright statements, (2) provide it for free, i.e. don�t charge any explicit or implicit fees to your customers, and (3) correctly and clearly cite the origin of the firmware and the project web page in any product documentation or web page. 

Hardware files: All hardware, for which material is provided, is open source hardware, under the terms of the TAPR Open Hardware License as published by the Free Hardware Foundation, see http://www.tapr.org/ohl.html. The TAPR license explicitly permits essentially unlimited commercial use, with only few conditions such as that copyright logos are not removed.

