#! /bin/bash
while true; do
clear
echo "Pi 4 ARM CPU status"
vcgencmd measure_temp
vcgencmd measure_clock arm
vcgencmd measure_volts core
sleep 1
done
