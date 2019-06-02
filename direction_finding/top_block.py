#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Jun  2 07:02:22 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate_rtlsdr = samp_rate_rtlsdr = 1.8e6
        self.samp_rate_hackrf = samp_rate_hackrf = 10e6
        self.samp_rate_all = samp_rate_all = 1.5e6

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_fftsink2_1 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=102e6,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate_rtlsdr,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_1.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=102e6,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate_hackrf,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.osmosdr_source_1 = osmosdr.source( args="numchan=" + str(1) + " " + "hackrf=0" )
        self.osmosdr_source_1.set_sample_rate(samp_rate_hackrf)
        self.osmosdr_source_1.set_center_freq(102e6, 0)
        self.osmosdr_source_1.set_freq_corr(0, 0)
        self.osmosdr_source_1.set_dc_offset_mode(0, 0)
        self.osmosdr_source_1.set_iq_balance_mode(0, 0)
        self.osmosdr_source_1.set_gain_mode(False, 0)
        self.osmosdr_source_1.set_gain(10, 0)
        self.osmosdr_source_1.set_if_gain(20, 0)
        self.osmosdr_source_1.set_bb_gain(20, 0)
        self.osmosdr_source_1.set_antenna("", 0)
        self.osmosdr_source_1.set_bandwidth(0, 0)
          
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "rtl=0" )
        self.osmosdr_source_0.set_sample_rate(samp_rate_rtlsdr)
        self.osmosdr_source_0.set_center_freq(102e6, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          

        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.wxgui_fftsink2_1, 0))    
        self.connect((self.osmosdr_source_1, 0), (self.wxgui_fftsink2_0, 0))    

    def get_samp_rate_rtlsdr(self):
        return self.samp_rate_rtlsdr

    def set_samp_rate_rtlsdr(self, samp_rate_rtlsdr):
        self.samp_rate_rtlsdr = samp_rate_rtlsdr
        self.osmosdr_source_0.set_sample_rate(self.samp_rate_rtlsdr)
        self.wxgui_fftsink2_1.set_sample_rate(self.samp_rate_rtlsdr)

    def get_samp_rate_hackrf(self):
        return self.samp_rate_hackrf

    def set_samp_rate_hackrf(self, samp_rate_hackrf):
        self.samp_rate_hackrf = samp_rate_hackrf
        self.osmosdr_source_1.set_sample_rate(self.samp_rate_hackrf)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate_hackrf)

    def get_samp_rate_all(self):
        return self.samp_rate_all

    def set_samp_rate_all(self, samp_rate_all):
        self.samp_rate_all = samp_rate_all


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
