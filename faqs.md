## Frequently Asked Questions

1. I am not able to run SBHS with plant-controller block of Sandhi. <br>

Mostly you don't have sufficient permissions to access /dev/ttyUSB0 (which is SBHS device node in Ubuntu). To solve this, just add your user to _dialout_ group.
	
	sudo adduser `whoami` dialout
**Logout User** and check.
