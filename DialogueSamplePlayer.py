#    The Dialogue Sample Player is desinged to play samples for a dialog of 
#    three persons and sends related OSC-messages.
#
#    Copyright (C) 2018 Johannes Redlich <johannes.redlich@tu-ilmenau.de>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys
from os import path,system
import argparse
#import numpy as np
import sounddevice as sd                # MIT
import soundfile as sf                  # BSD 3-Clause
from PyQt5 import QtWidgets, QtCore     # GPLv3 <http://www.gnu.org/licenses/>
from PyQt5.uic import loadUi            
from pythonosc import udp_client        # The Unlicense <http://unlicense.org/>
import images.vista                     # import of picture sources

"""
This is a player desinged to play samples for a dialog of three persons.
Therfore the buttons are ordered in an table with three columns.
Each of the columns represents one person. For each person the player chooses 
one output channel. 
Further the player sends OSC commands when a player starts playing and when the 
user clicked the stop, ring, hangup or reset button.
OSC commands out: 
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

The Dialogue Sample Player markes the played samples with bluish green color.
To reset the color of all buttons press 'Reset' or if you just want to reset one
button hold the right mouse key and left click the button you want.

TODO: 
    - Playing parallel
"""

class Sampler(QtWidgets.QMainWindow):
    
    def __init__(self):
        """
        Initalizes the sampler graphical user interface (GUI)
        """
        super(Sampler, self).__init__()
        loadUi(path.abspath('DialogueSampler.ui'),self)
        self.setWindowTitle('Dialogue Sample Player')
        self.colorRST()
        #self.frame.setStyleSheet("background-color: white")
        self.ButtonActions()

    def ButtonActions(self):
        """
        Specifies the action that are performed when a button is clicked.
        Button numbers and other GUI variables can be find by opening the 
        'DialogueSampler.ui' in Qt-Designer.
        """
        self.pushButton_77.clicked.connect(lambda: client.send_message("Ring",0)) # Ringing
        self.pushButton_73.clicked.connect(lambda: (sd.stop(),sys.exit())) # Quit-Button
        self.pushButton_74.clicked.connect(lambda: (self.colorRST(), \
            client.send_message("Reset",0))) # Reset Color
        self.pushButton_75.clicked.connect(lambda: (sd.stop(), \
            client.send_message("Stop",0))) # Stop #
        self.pushButton_76.clicked.connect(lambda: (sd.stop(), \
            client.send_message("Hangup",0))) # Hangup #
        
        # Person1
        path_1 = 'Person1_200-7000Hz_3rd-order\\'
        suffix_1 = '_200-7000Hz.wav'
        self.pushButton_1.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Guten Tag'+suffix_1)))
        self.pushButton_2.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Sie haben uns wegen eines Praktikums'+suffix_1)))
        self.pushButton_3.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Auf der Zweiten Leitung'+suffix_1)))
        self.pushButton_13.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Und dann ist noch unser Projektleiter zugeschaltet'+suffix_1)))
        self.pushButton_30.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Mehr erfahren'+suffix_1)))
        self.pushButton_19.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Oh warum denn nicht'+suffix_1)))
        self.pushButton_20.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Joar(gemütlich)'+suffix_1)))
        self.pushButton_21.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Joa(Kurz)'+suffix_1)))
        self.pushButton_18.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Ja'+suffix_1)))
        self.pushButton_24.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Ja genau'+suffix_1)))
        self.pushButton_31.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Inst_thermodyn'+suffix_1)))
        self.pushButton_33.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Das stimmt'+suffix_1)))
        self.pushButton_80.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'hmhm(zustimmend)'+suffix_1)))
        self.pushButton_40.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'hmm(zustimmend)'+suffix_1)))
        self.pushButton_28.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'imhm'+suffix_1)))
        self.pushButton_83.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Aha(gelangweilt)'+suffix_1)))
        self.pushButton_86.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Okay'+suffix_1)))
        self.pushButton_56.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Okay das reicht'+suffix_1)))
        self.pushButton_48.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Danke schön'+suffix_1)))
        self.pushButton_55.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Unterschied gut aussergewoehnlich'+suffix_1)))
        self.pushButton_32.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Angst'+suffix_1)))
        self.pushButton_38.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Umziehen'+suffix_1)))
        self.pushButton_35.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Freizeit'+suffix_1)))
        self.pushButton_42.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Danke soweit'+suffix_1)))
        self.pushButton_63.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Danke gespraech'+suffix_1)))
        self.pushButton_69.clicked.connect(lambda: self.player \
            (1, path.abspath(path_1+'Aufwiederhoeren'+suffix_1)))
        
        # Person2
        path_2 = 'Person2_200-7000Hz_3rd-order\\'
        suffix_2 = '_200-7000Hz.wav'
        self.pushButton_11.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Hallo'+suffix_2)))
        self.pushButton_27.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Anfang'+suffix_2)))
        self.pushButton_23.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Geht'+suffix_2)))
        self.pushButton_16.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Studieren'+suffix_2)))
        self.pushButton_34.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Machen'+suffix_2)))
        self.pushButton_45.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Job'+suffix_2)))
        self.pushButton_46.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Charakter'+suffix_2)))
        self.pushButton_52.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Mehr'+suffix_2)))
        self.pushButton_49.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Spaß'+suffix_2)))
        self.pushButton_59.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Reicht'+suffix_2)))
        self.pushButton_54.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Sehrgut'+suffix_2)))
        self.pushButton_64.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Zurück'+suffix_2)))
        self.pushButton_78.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Frage wiederholen'+suffix_2)))
        self.pushButton_79.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Sind Sie noch da'+suffix_2)))
        self.pushButton_81.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'mhm'+suffix_2)))
        self.pushButton_58.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'mhm(zustimmend)'+suffix_2)))
        self.pushButton_85.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Oh wirklich'+suffix_2)))
        self.pushButton_90.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Okay(zustimmend)'+suffix_2)))
        self.pushButton_87.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'mmmh(nachfragend)'+suffix_2)))
        self.pushButton_36.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Damn'+suffix_2)))
        self.pushButton_84.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Damn(kurz)'+suffix_2)))
        self.pushButton_39.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Kack'+suffix_2)))
        self.pushButton_43.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'ou fuck'+suffix_2)))
        self.pushButton_65.clicked.connect(lambda: self.player \
            (2, path.abspath(path_2+'Uhm'+suffix_2)))
		
        #Person3
        path_3 = 'Person3_200-7000Hz_3rd-order\\'
        suffix_3 = '_200-7000Hz.wav'
        self.pushButton_22.clicked.connect(lambda: self.player \
            (3, path.abspath(path_3+'Hallo'+suffix_3)))
        self.pushButton_50.clicked.connect(lambda: self.player \
            (3, path.abspath(path_3+'Interessant'+suffix_3)))
        self.pushButton_37.clicked.connect(lambda: self.player \
            (3, path.abspath(path_3+'Motivieren'+suffix_3)))
        self.pushButton_41.clicked.connect(lambda: self.player \
            (3, path.abspath(path_3+'Stärken'+suffix_3)))
        self.pushButton_57.clicked.connect(lambda: self.player \
            (3, path.abspath(path_3+'Spannend'+suffix_3)))
    
    def player(self,pl,file):
        """
        Plays the sound for the clicked button and sends the OSC-message. It 
        also can reset the color of the clicked button by hold the right mouse
        button and click the button.
        pl:     - chooses the player(1-3)
        file:   - the absolute file path
        """
        if QtWidgets.QApplication.mouseButtons() & QtCore.Qt.RightButton:
            P1 = [1,2,3,13,30,19,20,21,18,24,31,33,80,40,28,83,86,56,48,55,32,\
                    38,35,42,63,69] #28,40
            P2 = [11,27,23,16,34,45,46,52,49,59,54,64,78,79,81,58,85,90,87,36,\
                    84,39,43,65] #44,51
            P3 = [22,50,37,41,57]
            # reset the color
            bgc = ['rgb(210,190,255)','rgb(170,255,255)','rgb(255,255,150)','rgb(220,220,220)']
            button_pressed = int(self.sender().objectName()[11:])
            if button_pressed in P1:
                self.sender().setStyleSheet("background-color: "+bgc[0])
            elif button_pressed in P2:
                self.sender().setStyleSheet("background-color: "+bgc[1])
            elif button_pressed in P3:
                self.sender().setStyleSheet("background-color: "+bgc[2])
            else:
                self.sender().setStyleSheet("background-color: "+bgc[3])
        else:
            # set the color
            self.sender().setStyleSheet("background-color: rgb(0,200,180)")
            # read the .wav file
            data, samplerate = sf.read(file)
            # send OSC message: 'Player<Nr.>', length in milliseconds
            playABC = ['A','B','C'] 
            client.send_message(playABC[pl-1],len(data)/samplerate*1000)
            # play the sound
            sd.play(data, samplerate, mapping=[ch[pl-1]])
#            if pl == 1:
#                sd1.start()
#                sd1.write(np.float32(data))
            #sd.get_stream().active
    
    
    def colorRST(self):
        """
        To reset the colors of the buttons
        """
        P1 = [1,2,3,13,30,19,20,21,18,24,31,33,80,40,28,83,86,56,48,55,32,\
                    38,35,42,63,69] #28,40
        P2 = [11,27,23,16,34,45,46,52,49,59,54,64,78,79,81,58,85,90,87,36,\
                    84,39,43,65] #44,51
        P3 = [22,50,37,41,57]
#        for i in range(92,1,-1):
#            getattr(self, 'pushButton_%d' %i).setStyleSheet\
#                                     ("background-color: rgb(220,220,220)")
        for i in P1:
            getattr(self, 'pushButton_%d' %i).setStyleSheet\
                                     ("background-color: rgb(210,190,255)")
        for i in P2:
            getattr(self, 'pushButton_%d' %i).setStyleSheet\
                                     ("background-color: rgb(170,255,255)")
        for i in P3:
            getattr(self, 'pushButton_%d' %i).setStyleSheet\
                                     ("background-color: rgb(255,255,150)")


class SoundDev(QtWidgets.QDialog):
    """
    This is the dialogue to choose the sound device and the channels you want to
    use.
    """
    def __init__(self):
        """
        Initalizes the dialogue graphical user interface (GUI)
        """
        super(SoundDev, self).__init__()
        loadUi(path.abspath('ChooseSoundDev.ui'),self)
        self.setWindowTitle("Choose ASIO Sounddevice / OSC Settings")
        self.frame.setStyleSheet("background-color: white")
        self.set_devicelist()
        
    def set_devicelist(self):
        devlist = sd.query_devices()                # ask for devices
        i = -1
        for item in devlist:
            if item['max_output_channels']>0:       # min number of players
                self.comboBox.addItem(item['name']) # list devices in dropdown box
                i = i+1
                if ('ASIO' or 'asio' or 'Asio') in item['name']:
                    asioDevInd = i
        if 'asioDevInd' in locals():
            self.comboBox.setCurrentIndex(asioDevInd) # set ASIO device as default
        self.set_lable_text(devlist)  # initalize label text and channel selectors

        # if a new device is selceted than change label text and refresh channel list
        self.comboBox.currentTextChanged.connect(lambda: self.set_lable_text(devlist))
        # set OSC network
        self.lineEdit.setText('192.168.1.107')
        self.lineEdit_2.setText('5005')
        self.check_network()
        self.pushButton.clicked.connect(lambda: self.check_network())
    
    def check_network(self):
        rep = system('ping -n 1 -w 10 ' + self.lineEdit.text())
        if rep == 0:
            self.label_10.setStyleSheet('color: green')
            self.label_10.setText('IP address OK')
        if rep == 1:
            self.label_10.setStyleSheet('color: red')
            self.label_10.setText('IP address not reachable')

    def set_lable_text(self,devlist):
        if not ('ASIO' or 'asio' or 'Asio') in self.comboBox.currentText():
            self.label.setStyleSheet('color: red')
            self.label.setText(self.comboBox.currentText()+"\n "\
                "You need an ASIO-driver.\n Are you shure that this is an ASIO-driver?")
        else:
            # show which device is selceted
            self.label.setStyleSheet('color: default')
            self.label.setText(self.comboBox.currentText())
        # fill dropdown boxes for channel selction
        for item in devlist:
            if item['name']==self.comboBox.currentText():   # find current device
                self.comboBox_2.clear()     # clear channel list for refreshing
                self.comboBox_3.clear()     # the channel selctor
                self.comboBox_4.clear()
                for i in range(item['max_output_channels']): # fill with all channels
                    self.comboBox_2.addItem(str(i+1))
                    self.comboBox_3.addItem(str(i+1))
                    self.comboBox_4.addItem(str(i+1))
                if item['max_output_channels']==2:
                    self.comboBox_2.setCurrentIndex(0)  # give a preselection with [1,2,1]
                    self.comboBox_3.setCurrentIndex(1)
                elif item['max_output_channels']==1:
                    self.comboBox_2.setCurrentIndex(0)  # give a preselection with [1,1,1]
                    self.comboBox_3.setCurrentIndex(0)
                else:
                    self.comboBox_2.setCurrentIndex(2)  # give a preselection with [1,2,3]
                    self.comboBox_3.setCurrentIndex(1)


def run():
    
    #start application - choose sounddevice - network settings
    app = QtWidgets.QApplication(sys.argv)
    dialog = SoundDev()
    dialog.buttonBox.rejected.connect(lambda: sys.exit(app.exec_()))    # close application if close is pressed
    dialog.exec_()
    
    # set OSC-UDP client
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default=dialog.lineEdit.text(), help="The ip of the OSC server") # 192.168.1.107 , 127.0.0.1
    parser.add_argument("--port", type=int, default=dialog.lineEdit_2.text(), \
        help="The port the OSC server is listening on")
    args = parser.parse_args()
    global client 
    client = udp_client.SimpleUDPClient(args.ip, args.port)
    
    # set sounddevice
    sd.default.device = dialog.comboBox.currentText() #'ASIO Hammerfall DSP'
#    asio_out = sd.AsioSettings(channel_selectors=[0,1,2])
#    sd.default.extra_settings = asio_out
    global ch
    ch = [int(dialog.comboBox_4.currentText()),int(dialog.comboBox_3.currentText()), \
        int(dialog.comboBox_2.currentText())]
    
    # initalize sounddevice streams
#    global sd1,sd2,sd3
#    data, samplerate = sf.read(path.abspath('stille.wav'))
#    asio_out = sd.AsioSettings(channel_selectors=[0,1,2])
#    sd.play(data, samplerate, extra_settings=asio_out)
#    sd.OutputStream(device = sd.default.device,extra_settings=asio_out, channels=1).start()
#    sd1 = sd.get_stream()
#    outdata[:,1] = np.float32(data)
#    sd.OutputStream(extra_settings=asio_out, channels=1).write(outdata)
#    
#    asio_out = sd.AsioSettings(channel_selectors=[1])
#    sd.play(data, samplerate, extra_settings=asio_out)
#    sd2 = sd.get_stream()
#    asio_out = sd.AsioSettings(channel_selectors=[2])
#    sd.play(data, samplerate, extra_settings=asio_out)
#    sd3 = sd.get_stream()
    
    # start sampler UI
    widget = Sampler()
    widget.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    run()
