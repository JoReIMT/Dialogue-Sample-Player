# Dialogue-Sample-Player

What is DialogueSamplePlayer:
-----------------------------

This is a player desinged to play samples for a dialogue of three persons.
Therfore the buttons are ordered in an table with three columns.
Each of the columns represents one person. For each person the player chooses 
one output channel.
The Dialogue Sample Player markes the played samples with bluish green color.
To reset the color of all buttons press 'Reset' or if you just want to reset one
button hold the right mouse key and left click the button you want.

Further the player sends OSC commands when a player starts playing and when the 
user clicked the stop, ring, hangup or reset button.


Quick start:
------------
1. Start 'DialogueRun.bat'
2. Choose an ASIO soundcard
3. Choose output channels (Player1-3)
OSC if needed:
4. Set 'Network address' 
	('Test IP' button sends a ping and shows if IP address is OK)
5. Set 'OSC port'
If all is okay:
6. Click 'OK'
The main window shows up:
7. Click the buttons with the messages you want and build a dialogue
8. Click 'Quit' to close the DialogueSamplePlayer.


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
	- Playing parallel



