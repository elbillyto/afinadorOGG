__author__ = 'elbillyto'
import gst
import gobject
import os

mainloop = gobject.MainLoop()
pl = gst.element_factory_make("playbin", "player")
pl.set_property('uri','file://'+os.path.abspath('Do2.ogg'))
pl.set_state(gst.STATE_PLAYING)
mainloop.run()
