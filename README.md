This device allows you to flash the programm to stm32 MCUs using SWD and get data from UAVCAN.

## Special thanks for

https://github.com/GolinskiyKonstantin/ST-Link-V2-1

https://habr.com/ru/post/442290/

## UAVCAN 

GUI Tool 

https://legacy.uavcan.org/GUI_Tool/Overview/

repo

https://github.com/UAVCAN/gui_tool

## To flash the programmer

Install exactly this version of STM32 ST-LINK Utility v4.3.0

Take another programmer

Flash the Protected-2-1-Bootloader.bin

Now connect new programmer to USB and press update in STM32 ST-LINK Utility v4.3.0

Choose STM32 + MSD + VCP

Profit

## To flash the CAN-SNIFFER

Connect programmer output to  programming port  of CAN-SNIFFER MCU

Flash the can-uart.bin

Profit



