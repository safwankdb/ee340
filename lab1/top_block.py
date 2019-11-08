#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Aug  8 15:44:02 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt, QtCore
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.var_5 = var_5 = 100
        self.var_4 = var_4 = 100
        self.var_3 = var_3 = 100
        self.var_2 = var_2 = 100
        self.var_1 = var_1 = 100
        self.samp_rate = samp_rate = 48000

        ##################################################
        # Blocks
        ##################################################
        self._var_5_range = Range(0, 250, 1, 100, 200)
        self._var_5_win = RangeWidget(self._var_5_range, self.set_var_5, "var_5", "counter_slider", float)
        self.top_layout.addWidget(self._var_5_win)
        self._var_4_range = Range(0, 250, 1, 100, 200)
        self._var_4_win = RangeWidget(self._var_4_range, self.set_var_4, "var_4", "counter_slider", float)
        self.top_layout.addWidget(self._var_4_win)
        self._var_3_range = Range(0, 250, 1, 100, 200)
        self._var_3_win = RangeWidget(self._var_3_range, self.set_var_3, "var_3", "counter_slider", float)
        self.top_layout.addWidget(self._var_3_win)
        self._var_2_range = Range(0, 250, 1, 100, 200)
        self._var_2_win = RangeWidget(self._var_2_range, self.set_var_2, "var_2", "counter_slider", float)
        self.top_layout.addWidget(self._var_2_win)
        self._var_1_range = Range(0, 250, 1, 100, 200)
        self._var_1_win = RangeWidget(self._var_1_range, self.set_var_1, "var_1", "counter_slider", float)
        self.top_layout.addWidget(self._var_1_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/safwankdb/Desktop/ee340_lab/lab1/Bach.wav', True)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0_3_1 = filter.interp_fir_filter_fff(1, firdes.band_pass(
        	var_5/100, samp_rate, 9000, 15000, 5, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_3_0 = filter.interp_fir_filter_fff(1, firdes.band_pass(
        	var_4/100, samp_rate, 6000, 9000, 5, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_3 = filter.interp_fir_filter_fff(1, firdes.band_pass(
        	var_3/100, samp_rate, 3000, 6000, 5, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0 = filter.interp_fir_filter_fff(1, firdes.band_pass(
        	var_2/100, samp_rate, 500, 3000, 5, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0 = filter.interp_fir_filter_fff(1, firdes.band_pass(
        	var_1/100, samp_rate, 20, 500, 5, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(samp_rate, '', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.band_pass_filter_0_3, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.band_pass_filter_0_3_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.band_pass_filter_0_3_1, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_3, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_3_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_3_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_var_5(self):
        return self.var_5

    def set_var_5(self, var_5):
        self.var_5 = var_5
        self.band_pass_filter_0_3_1.set_taps(firdes.band_pass(self.var_5/100, self.samp_rate, 9000, 15000, 5, firdes.WIN_HAMMING, 6.76))

    def get_var_4(self):
        return self.var_4

    def set_var_4(self, var_4):
        self.var_4 = var_4
        self.band_pass_filter_0_3_0.set_taps(firdes.band_pass(self.var_4/100, self.samp_rate, 6000, 9000, 5, firdes.WIN_HAMMING, 6.76))

    def get_var_3(self):
        return self.var_3

    def set_var_3(self, var_3):
        self.var_3 = var_3
        self.band_pass_filter_0_3.set_taps(firdes.band_pass(self.var_3/100, self.samp_rate, 3000, 6000, 5, firdes.WIN_HAMMING, 6.76))

    def get_var_2(self):
        return self.var_2

    def set_var_2(self, var_2):
        self.var_2 = var_2
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(self.var_2/100, self.samp_rate, 500, 3000, 5, firdes.WIN_HAMMING, 6.76))

    def get_var_1(self):
        return self.var_1

    def set_var_1(self, var_1):
        self.var_1 = var_1
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.var_1/100, self.samp_rate, 20, 500, 5, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0_3_1.set_taps(firdes.band_pass(self.var_5/100, self.samp_rate, 9000, 15000, 5, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_3_0.set_taps(firdes.band_pass(self.var_4/100, self.samp_rate, 6000, 9000, 5, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_3.set_taps(firdes.band_pass(self.var_3/100, self.samp_rate, 3000, 6000, 5, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(self.var_2/100, self.samp_rate, 500, 3000, 5, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.var_1/100, self.samp_rate, 20, 500, 5, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
