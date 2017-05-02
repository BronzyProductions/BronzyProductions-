sudo apt-get update
sudo apt-get upgrade

sudo apt-get install python pip
sudo pip install pibrella 

sudo python -i 

import pibrella 
pibrella.buzzer.fail()
pibrella.light.pulse(0.2)

quit()