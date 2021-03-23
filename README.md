# home-HTTPserver

Unefficient home automation with HTTP
## How to install it

- clone this repository: `git clone https://github.com/edoardesd/home-HTTPserver`
- update: `sudo apt-get update`
- install pip3: `sudo apt install -y python3-pip`
- move into the direcotry: `cd home-HTTPserver`
- install pip requirements `python3.8 -m pip install -r requirements.txt --user`


## How to run it
- `sudo python3 server.py`

Request: `curl http://0.0.0.0:<port>/living_room/temperature`
Verbose request: `curl -v http://0.0.0.0:<port>/living_room/temperature`
