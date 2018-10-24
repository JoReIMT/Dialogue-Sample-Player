# Dialogue-Sample-Player

What is DialogueSamplePlayer:
-----------------------------
This is a player desinged to play samples for a dialogue of three persons.
Therfore the buttons are ordered in an table with three columns. Each of the 
columns represents one person. For each person the player chooses one output 
channel.

The Dialogue Sample Player markes the played samples with bluish green color.
To reset the color of all buttons press 'Reset' or if you just want to reset one
button hold the right mouse key and left click the button you want.

Further the player sends OSC commands when a player starts playing and when the 
user clicked the stop, ring, hangup or reset button.

Prerequisites:
------------
1. Install Python (version 3.6 or later): https://www.python.org/downloads/
2. Run setup.bat (installs sounddevice, soundfile, PyQT5, python-osc)

Quick start (for Windows):
------------
1. Start 'DialogueRun.bat'
2. Choose an ASIO soundcard
3. Choose output channels (Player1-3)
* OSC if needed:
4. Set 'Network address' 
	* ('Test IP' button sends a ping and shows if IP address is OK)
5. Set 'OSC port'
* If all is okay:
6. Click 'OK'
* The main window shows up:
7. Click the buttons with the messages you want and build a dialogue
8. Click 'Quit' to close the DialogueSamplePlayer.

Usage without ASIO soundcard:
------------
* Download and install ASIO4ALL http://www.asio4all.org/ and restart PC.
* Choose ASIO4ALL as sounddevice and set the channels.
* If you just own a stereo-soundcard you can select only channel 1 or 2.

Usage without OSC
------------
* There is no need to change or enter a network address.
* The OSC data will be sent to Nirvana.

Usage with OSC
------------
* For local usage:
	* Enter 127.0.0.1 as network address.
	* Enter OSC port.
* For network usage:
	* Enter the network address of the receiver.
	* Enter OSC port.
* You can test whether the IP address is reachable by clicking the 'Test IP' 
  button 
	* that will send a ping and show if the IP address is OK

Special buttons:
----------------
'Stop'		- Stops the current playback and sends OSC message 'Stop'

'Ring'		- Send an OSC message to trigger en external ringing sound

'Hangup'	- Stops the current playback and sends OSC message 'Hangup'

'Reset'		- Reset the color of all buttons and sends OSC message 'Reset'

If you want to reset only one button hold the right mouse key and left click 
the button you want.

OSC commands out: 
-----------------
    Player start: 
        Adress: 'A','B','C'
        Data:   <length of sample in milliseconds>
    Stop clicked:
        Adress: 'Stop'
        Data:   0
    Ring clicked:
        Adress: 'Ring'
        Data:   0
    Hangup clicked:
        Adress: 'Hangup'
        Data:   0
    Reset clicked:
        Adress: 'Reset'
        Data:   0

TODO:
----- 
	* Playing parallel



