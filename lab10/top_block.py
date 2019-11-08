#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Nov  1 15:21:49 2019
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from math import pi
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
        self.timing_bw = timing_bw = 2*pi/100
        self.samp_rate = samp_rate = 80000
        self.rx_taps_0 = rx_taps_0 = filter.firdes.root_raised_cosine(32, 96, 1.0,0.4, 1056)
        self.rx_taps = rx_taps = filter.firdes.root_raised_cosine(32,128,1.0,0.4,1408)
        self.freq_bw = freq_bw = 2*pi/100
        self.fll_ntaps = fll_ntaps = 55

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=5,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_fff(
        	  4,
                  taps=(firdes.root_raised_cosine(32,32,1.0,0.4,1408)),
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)

        self.low_pass_filter_0 = filter.interp_fir_filter_fff(1, firdes.low_pass(
        	1, 400e3, 100e3, 5e3, firdes.WIN_HAMMING, 6.76))
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_fff(4, timing_bw, (rx_taps), 32, 16, 1.5, 1)
        self.digital_diff_encoder_bb_1 = digital.diff_encoder_bb(2)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc(((1,1j,-1,-1j)), 1)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, 400000,True)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, 34)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/safwankdb/Desktop/ee340_lab/lab10/Original_Text.txt', False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/safwankdb/Desktop/ee340_lab/lab10/output3.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.analog_sig_source_x_0 = analog.sig_source_f(400000, analog.GR_COS_WAVE, 100000, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.digital_diff_encoder_bb_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.digital_diff_encoder_bb_1, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_timing_bw(self):
        return self.timing_bw

    def set_timing_bw(self, timing_bw):
        self.timing_bw = timing_bw
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.timing_bw)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_rx_taps_0(self):
        return self.rx_taps_0

    def set_rx_taps_0(self, rx_taps_0):
        self.rx_taps_0 = rx_taps_0

    def get_rx_taps(self):
        return self.rx_taps

    def set_rx_taps(self, rx_taps):
        self.rx_taps = rx_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rx_taps))

    def get_freq_bw(self):
        return self.freq_bw

    def set_freq_bw(self, freq_bw):
        self.freq_bw = freq_bw

    def get_fll_ntaps(self):
        return self.fll_ntaps

    def set_fll_ntaps(self, fll_ntaps):
        self.fll_ntaps = fll_ntaps


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
