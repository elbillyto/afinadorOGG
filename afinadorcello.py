# encoding: utf-8
__author__ = 'elbillyto'

from gi.repository import Gtk, Gst, GObject
import sys, os
# import os

#Comment the first line and uncomment the second before installing
#or making the tarball (alternatively, use project variables)
UI_FILE = "window_afinadorcelo.glade"
#UI_FILE ="/usr/local/share/afinadorcello/ui/window_afinadorcelo.glade"


class GUI:
    LENGTH = 500
    # Frequencies of the strings
    frequencies = {
        'DO2': 130.813,
        'SOL2': 195.998,
        'RE3': 293.665,
        'LA3': 440
    }

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(UI_FILE)
        self.builder.connect_signals(self)
        window = self.builder.get_object('window')
        window.show_all()

    def on_button_clicked(self, button):
        label = button.get_child()
        text = label.get_label()
        #self.play_sound(self.frequencies[text])
        self.play_sound(text)

    def destroy(window, self):
        Gtk.main_quit()

    def play_sound(self, frequency):
        pipeline = Gst.Pipeline(name='note')
        pipeline = Gst.ElementFactory.make("playbin", "player")
        pipeline.set_property('uri', 'file://' + os.path.abspath(frequency + '.ogg'))
        pipeline.set_state(Gst.State.PLAYING)

    def pipeline_stop(self, pipeline):
        pipeline.set_state(Gst.State.NULL)
        return False


def main():
    Gst.init_check(sys.argv)  #inicializar GStreamer
    app = GUI()
    Gtk.main()


if __name__ == "__main__":
    sys.exit(main())