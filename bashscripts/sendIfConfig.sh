#!/bin/bash
ifconfig > ifconfig.log
cat ifconfig.log | sendEmail -f simon-pierre.gingras.2@ulaval.ca -t robotpicasso@gmail.com -s smtp.ulaval.ca -u “Ifconfig output”
