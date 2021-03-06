# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import absolute_import, division, print_function

import pytest
from .conftest import VISA  # noqa: F401

from RSSscpi import znb  # noqa: F401
from RSSscpi.znb import ZNB  # noqa: F401
from RSSscpi.SCPI_property import SCPIPropertyMinMax


class PropertyTester(object):
    @staticmethod
    def prop_parametrize(props):
        return pytest.mark.parametrize('prop_name, scpi_cmd, scpi_write, scpi_query', props, ids=[x[0] for x in props])

    @staticmethod
    def test_float_properties(prop_name, scpi_cmd, scpi_write, scpi_query, scpi_float, instance, visa):
        PropertyTester.test_properties(prop_name, scpi_cmd, scpi_write, scpi_query, scpi_float, instance, visa, float)

    @staticmethod
    def test_properties(prop_name, scpi_cmd, scpi_write, scpi_query, scpi_values, instance, visa, type_):
        visa.ret = scpi_values[1]  # the string representation of the value
        x = getattr(instance, prop_name)
        assert isinstance(x, type_) and x == scpi_values[0]
        setattr(instance, prop_name, scpi_values[0])
        assert [scpi_query.format(scpi_cmd), scpi_write.format(scpi_cmd, scpi_values[1])] == visa.cmd
        minmax = prop_name + "_minmax"
        if hasattr(instance, minmax):
            assert isinstance(getattr(instance, minmax), SCPIPropertyMinMax)
            setattr(instance, minmax, scpi_values[0])
            assert [scpi_write.format(scpi_cmd, scpi_values[1])] == visa.cmd


class TestZNB(object):
    def test_init(self, dummy_znb, visa):
        # type: (ZNB, VISA) -> None
        dummy_znb.init()
        assert ["*CLS;*ESE 127;*SRE 36",
                "SYSTem:COMMunicate:CODec UTF8",
                "SYSTem:LANGuage?",
                "SYSTem:LANGuage 'SCPI'",
                ] == visa.cmd

    def test_reset_remote_emulation(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        visa.ret = "SCPI"
        assert dummy_vna.reset_remote_emulation() == "SCPI"
        assert ["SYSTem:LANGuage?"] == visa.cmd
        visa.ret = "ZVR"
        assert dummy_vna.reset_remote_emulation() == "ZVR"
        assert ["SYSTem:LANGuage?",
                "SYSTem:LANGuage 'SCPI'",
                ] == visa.cmd

    def test_active_channel(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        vna = dummy_vna
        x = vna.active_channel
        assert x.n == 1
        vna.active_channel = 3
        vna.active_channel = "2"
        vna.active_channel = x
        assert ["INSTrument:NSELect?",
                "INSTrument:NSELect 3",
                "INSTrument:NSELect 2",
                "INSTrument:NSELect 1",
                ] == visa.cmd

    def test_query_port_count(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        vna = dummy_vna
        visa.ret = "4"
        x = vna.query_number_of_ports()
        assert x == 4
        assert ["INSTrument:PORT:COUNt?",
                ] == visa.cmd
        visa.ret = "1"
        x = vna.query_number_of_ports()  # The number of ports on the instrument should be cached
        assert x == 4
        assert [] == visa.cmd

    def test_znb_screenshot(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        vna = dummy_vna
        scr = vna.save_screenshot("scr.png")
        assert scr.filename == "scr.png"
        assert ["MMEMory:NAME 'scr.png'",
                "HCOPy:DESTination 'MMEM'",
                "HCOPy:DEVice:LANGuage PNG",
                "HCOPy:PAGE:WINDow HARDcopy",
                "HCOPy:IMMediate",
                "MMEMory:CDIRectory?",
                ] == visa.cmd
        pytest.raises(ValueError, 'vna.save_screenshot("scr.docx")')
        assert visa.cmd == []


class TestChannel(object):
    @pytest.fixture
    def ch(self, dummy_vna):
        return dummy_vna.get_channel(2)

    def test_channel(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        ch = dummy_vna.get_channel(3)
        assert ch.name == "1"
        ch.name = "Ch2"
        assert ["CONFigure:CHANnel3:NAME?",
                "CONFigure:CHANnel3:NAME 'Ch2'",
                ] == visa.cmd

        tr = ch.create_trace("Tr1", "S11")
        assert tr.name == "Tr1"
        tr = ch.create_trace("Tr2", "S22", dummy_vna.get_diagram(1))
        assert tr.name == "Tr2"
        assert ["CALCulate3:PARameter:SDEFine 'Tr1', 'S11'",
                "CALCulate3:PARameter:SDEFine 'Tr2', 'S22'",
                "DISPlay:WINDow1:TRACe:EFEed 'Tr2'",
                ] == visa.cmd

        visa.ret = "Tr1"
        tr = ch.active_trace
        visa.ret = "1"
        assert tr.name == "Tr1"
        ch.active_trace = "Tr3"
        ch.active_trace = ch.get_trace("Tr2")
        assert ["CALCulate3:PARameter:SELect?",
                "CALCulate3:PARameter:SELect 'Tr3'",
                "CALCulate3:PARameter:SELect 'Tr2'",
                ] == visa.cmd

        ch.power_level = -10.33
        assert ch.power_level == 1.
        assert ["SOURce3:POWer:LEVel:IMMediate:AMPLitude -10.33",
                "SOURce3:POWer:LEVel:IMMediate:AMPLitude?",
                ] == visa.cmd

    def test_channel_sweep(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        ch = dummy_vna.get_channel(3)
        assert isinstance(ch.sweep.points_minmax.query_default(), int)
        ch.sweep.points = 301
        assert isinstance(ch.sweep.points, int)
        ch.sweep.points_minmax = 301
        ch.sweep.TYPE.w("LIN")
        assert ["SENSe3:SWEep:POINts? DEF",
                "SENSe3:SWEep:POINts 301",
                "SENSe3:SWEep:POINts?",
                "SENSe3:SWEep:POINts 301",
                "SENSe3:SWEep:TYPE LIN",
                ] == visa.cmd

        visa.ret = "LIN"
        assert ch.sweep.type == "LIN"
        ch.sweep.type = "POW"
        assert ["SENSe3:SWEep:TYPE?",
                "SENSe3:SWEep:TYPE POW",
                ] == visa.cmd

        ch.configure_freq_sweep(10e6, 9e9)
        assert ["SENSe3:SWEep:TYPE LIN",
                "SENSe3:FREQuency:STARt 10000000.0",
                "SENSe3:FREQuency:STOP 9000000000.0",
                ] == visa.cmd

        ch.configure_freq_sweep(10, 10e6, points=101, ifbw=1e3, power=-10, log_sweep=True)
        ch.init_sweep()
        assert ["SENSe3:SWEep:TYPE LOG",
                "SENSe3:FREQuency:STARt 10",
                "SENSe3:FREQuency:STOP 10000000.0",
                "SENSe3:SWEep:POINts 101",
                "SENSe3:BANDwidth 1000.0",
                "SOURce3:POWer:LEVel:IMMediate:AMPLitude -10",
                "INITiate3:IMMediate",
                ] == visa.cmd

        ch.configure_power_sweep(freq=40e9, start_power=-40, stop_power=10, points=41, ifbw=1e3)
        assert ["SENSe3:SWEep:TYPE POW",
                "SENSe3:FREQuency:CW 40000000000.0",
                "SOURce3:POWer1:STARt -40",
                "SOURce3:POWer1:STOP 10",
                "SENSe3:SWEep:POINts 41",
                "SENSe3:BANDwidth 1000.0",
                ] == visa.cmd

    float_properties = [
        ("freq_cw", "SENSe2:FREQuency:CW", "{:s} {:s}", "{:s}?"),
        ("freq_start", "SENSe2:FREQuency:STARt", "{:s} {:s}", "{:s}?"),
        ("freq_stop", "SENSe2:FREQuency:STOP", "{:s} {:s}", "{:s}?"),
        ("freq_center", "SENSe2:FREQuency:CENTer", "{:s} {:s}", "{:s}?"),
        ("freq_span", "SENSe2:FREQuency:SPAN", "{:s} {:s}", "{:s}?"),
        ("power_level", "SOURce2:POWer:LEVel:IMMediate:AMPLitude", "{:s} {:s}", "{:s}?"),
    ]

    @PropertyTester.prop_parametrize(float_properties)
    def test_float_properties(self, prop_name, scpi_cmd, scpi_write, scpi_query, scpi_float, ch, visa):
        PropertyTester.test_float_properties(prop_name, scpi_cmd, scpi_write, scpi_query, scpi_float, ch, visa)

    int_properties = [
        ("ifbw", "SENSe2:BANDwidth", "{:s} {:s}", "{:s}?"),
    ]

    @PropertyTester.prop_parametrize(int_properties)
    def test_int_properties(self, prop_name, scpi_cmd, scpi_write, scpi_query, scpi_int, ch, visa):
        PropertyTester.test_properties(prop_name, scpi_cmd, scpi_write, scpi_query, scpi_int, ch, visa, int)

    def test_channel_properties(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        ch = dummy_vna.get_channel(1)
        visa.ret = "'Ch1'"
        assert ch.name == "Ch1"
        ch.name = "Ch2"
        assert ["CONFigure:CHANnel1:NAME?",
                "CONFigure:CHANnel1:NAME 'Ch2'",
                ] == visa.cmd

    def test_channel_cal(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        ch = dummy_vna.get_channel(2)
        ch.cal_auto((1, 2, 3, 4))
        assert ["SENSe2:CORRection:COLLect:AUTO:TYPE FNPort, '', 1, 2, 3, 4",
                ] == visa.cmd
        ch.cal_auto((1, 2, 3, 4), (3, 4, 1, 2), cal_type="FOPort")
        assert ["SENSe2:CORRection:COLLect:AUTO:PORTs:TYPE FOPort, '', 1, 3, 2, 4, 3, 1, 4, 2",
                ] == visa.cmd
        ch.cal_auto((1, 2, 3, 4), cal_unit_characterization="user2.calkit")
        assert ["SENSe2:CORRection:COLLect:AUTO:TYPE FNPort, 'user2.calkit', 1, 2, 3, 4",
                ] == visa.cmd

    def test_channel_save_touchstone(self, dummy_vna, visa):
        # type: (ZNB, VISA) -> None
        ch = dummy_vna.get_channel(2)
        f = ch.save_touchstone("file.s3p", (1, 2, 3))
        assert f.filename == "file.s3p"
        assert ["MMEMory:STORe:TRACe:PORTs 2, 'file.s3p', LOGPhase, CIMPedance, 1, 2, 3",
                "MMEMory:CDIRectory?",
                ] == visa.cmd


class TestSweep(object):
    @pytest.fixture
    def sw(self, dummy_vna):
        return dummy_vna.get_channel(2).sweep

    @pytest.fixture
    def seg(self, sw):
        return sw.segments[5]

    def test_sweep_dwell(self, dummy_znb, visa):
        # type: (ZNB, VISA) -> None
        """
        This setting is not available on the ZVA
        """
        sw = dummy_znb.get_channel(2).sweep
        sw.dwell_on_each_partial_measurement = True
        sw.dwell_on_each_partial_measurement = False
        visa.ret = "FIRSt"
        assert sw.dwell_on_each_partial_measurement is False
        visa.ret = "ALL"
        assert sw.dwell_on_each_partial_measurement is True
        assert ["SENSe2:SWEep:DWELl:IPOint ALL",
                "SENSe2:SWEep:DWELl:IPOint FIRSt",
                "SENSe2:SWEep:DWELl:IPOint?",
                "SENSe2:SWEep:DWELl:IPOint?",
                ] == visa.cmd

    float_properties = [
        ("dwell_time", "SENSe2:SWEep:DWELl", "{:s} {:s}", "{:s}?"),
        ("time",       "SENSe2:SWEep:TIME",  "{:s} {:s}", "{:s}?"),
        ("step_size",  "SENSe2:SWEep:STEP",  "{:s} {:s}", "{:s}?"),
    ]

    @PropertyTester.prop_parametrize(float_properties)
    def test_float_properties(self, prop_name, scpi_cmd, scpi_write, scpi_query, scpi_float, sw, visa):
        PropertyTester.test_properties(prop_name, scpi_cmd, scpi_write, scpi_query, scpi_float, sw, visa, float)

    int_properties = [
        ("points", "SENSe2:SWEep:POINts", "{:s} {:s}", "{:s}?"),
        ("count", "SENSe2:SWEep:COUNt",   "{:s} {:s}", "{:s}?"),
    ]

    @PropertyTester.prop_parametrize(int_properties)
    def test_int_properties(self, prop_name, scpi_cmd, scpi_write, scpi_query, scpi_int, sw, visa):
        PropertyTester.test_properties(prop_name, scpi_cmd, scpi_write, scpi_query, scpi_int, sw, visa, int)


class TestSweepSegments(object):
    @pytest.fixture
    def sw(self, dummy_vna):
        return dummy_vna.get_channel(2).sweep

    @pytest.fixture
    def seg(self, sw):
        return sw.segments[5]

    def test_segments_properties(self, sw, visa):
        # type: (znb.Sweep, VISA) -> None
        sw.TYPE.w(sw.SEGMENT)

        sw.analog_sweep_is_enabled = True
        sw.analog_sweep_is_enabled = False
        sw.use_auto_time = True
        assert ["SENSe2:SWEep:TYPE SEGM",
                "SENSe2:SWEep:GENeration ANALog",
                "SENSe2:SWEep:GENeration STEPped",
                "SENSe2:SWEep:TIME:AUTO ON",
                ] == visa.cmd

    def test_segmented_sweep(self, sw, visa):
        # type: (znb.Sweep, VISA) -> None
        visa.ret = "5"
        assert len(sw.segments) == 5
        assert sw.segments[0].n == 1
        assert len(sw.segments[1:5]) == 4
        assert ["SENSe2:SEGMent:COUNt?",
                "SENSe2:SEGMent:COUNt?",
                ] == visa.cmd

        sw.segments.query_total_sweep_time()
        assert ["SENSe2:SEGMent:SWEep:TIME:SUM?"] == visa.cmd

        for (seg, n) in zip(iter(sw.segments), range(5)):
            assert seg.n == n + 1
        visa.clear_cmd()

    def test_delete(self, sw, visa):
        # type: (znb.Sweep, VISA) -> None
        visa.ret = "5"
        del sw.segments[2]
        del sw.segments[0:5:2]
        assert ["SENSe2:SEGMent3:DELete",
                "SENSe2:SEGMent:COUNt?",
                "SENSe2:SEGMent5:DELete",
                "SENSe2:SEGMent3:DELete",
                "SENSe2:SEGMent1:DELete",
                ] == visa.cmd

        sw.segments.delete_all_segments()
        sw.segments.delete_segment(3)
        assert ["SENSe2:SEGMent:DELete:ALL",
                "SENSe2:SEGMent3:DELete",
                ] == visa.cmd

        seg = sw.segments[5]
        seg.delete()
        assert ["SENSe2:SEGMent6:DELete"] == visa.cmd

    def test_disable_methods(self, sw, visa):
        sw.segments.disable_per_segment_dwell_time()
        sw.segments.disable_per_segment_if_selectivity()
        sw.segments.disable_per_segment_power()
        sw.segments.disable_per_segment_sweep_time()
        assert ["SENSe2:SEGMent:SWEep:DWELl:CONTrol OFF",
                "SENSe2:SEGMent:BWIDth:RESolution:SELect:CONTrol OFF",
                "SENSe2:SEGMent:POWer:LEVel:CONTrol OFF",
                "SENSe2:SEGMent:SWEep:TIME:CONTrol OFF",
                ] == visa.cmd

    def test_insert_segment(self, dummy_znb, visa):
        # type: (ZNB, VISA) -> None
        """ANALog sweeps are only supported on the ZNB"""
        sw = dummy_znb.get_channel(2).sweep
        x = sw.segments.insert_segment(1e6, 1e9, 11, 1e3, -10, position=3)
        assert x.n == 3
        sw.segments.insert_segment(1e6, 1e9, 11, 1e3, -10, position=3, analog_sweep=True)
        assert ["SENSe2:SEGMent3:INSert 1000000.0, 1000000000.0, 11, -10, AUTO, 0, 1000.0, AUTO, NORMal, STEPped",
                "SENSe2:SEGMent3:INSert 1000000.0, 1000000000.0, 11, -10, AUTO, 0, 1000.0, AUTO, NORMal, ANALog",
                ] == visa.cmd


class TestSweepSegment(object):
    @pytest.fixture
    def sw(self, dummy_vna):
        return dummy_vna.get_channel(2).sweep

    @pytest.fixture
    def seg(self, sw):
        return sw.segments[5]

    def test_segment_analog_sweep(self, dummy_znb, visa):
        # type: (ZNB, VISA) -> None
        """ANALog sweeps are only supported on the ZNB"""
        seg = dummy_znb.get_channel(2).sweep.segments[5]
        seg.analog_sweep_is_enabled = True
        seg.analog_sweep_is_enabled = False
        assert ["SENSe2:SEGMent6:SWEep:GENeration ANALog",
                "SENSe2:SEGMent6:SWEep:GENeration STEPped",
                ] == visa.cmd

    segment_float_properties = [
        ("dwell_time",  "SENSe2:SEGMent6:SWEep:DWELl",     "{:s} {:s}", "{:s}?"),
        ("freq_start",  "SENSe2:SEGMent6:FREQuency:STARt", "{:s} {:s}", "{:s}?"),
        ("freq_stop",   "SENSe2:SEGMent6:FREQuency:STOP",  "{:s} {:s}", "{:s}?"),
        ("power_level", "SENSe2:SEGMent6:POWer",           "{:s} {:s}", "{:s}?"),
        ("sweep_time",  "SENSe2:SEGMent6:SWEep:TIME",      "{:s} {:s}", "{:s}?"),
    ]

    @PropertyTester.prop_parametrize(segment_float_properties)
    def test_segment_float_properties(self, prop_name, scpi_cmd, scpi_write, scpi_query, scpi_float, seg, visa):
        PropertyTester.test_properties(prop_name, scpi_cmd, scpi_write, scpi_query, scpi_float, seg, visa, float)

    segment_int_properties = [
        ("if_bandwidth",     "SENSe2:SEGMent6:BWIDth:RESolution", "{:s} {:s}", "{:s}?"),
        ("number_of_points", "SENSe2:SEGMent6:SWEep:POINts",      "{:s} {:s}", "{:s}?"),
    ]

    @PropertyTester.prop_parametrize(segment_int_properties)
    def test_segment_int_properties(self, prop_name, scpi_cmd, scpi_write, scpi_query, scpi_int, seg, visa):
        PropertyTester.test_properties(prop_name, scpi_cmd, scpi_write, scpi_query, scpi_int, seg, visa, int)

    def test_properties(self, seg, visa):
        visa.ret = "0"
        assert seg.is_enabled is False
        assert seg.if_selectivity == "0"
        assert ["SENSe2:SEGMent6:STATe?",
                "SENSe2:SEGMent6:BWIDth:RESolution:SELect?",
                ] == visa.cmd


def test_vna_port(dummy_vna, visa):
    # type: (ZNB, VISA) -> None
    ch = dummy_vna.get_channel(1)
    p2 = ch.get_vna_port(2)

    p2.cal_power_offset = -3.4
    x = p2.cal_power_offset
    assert isinstance(x, float) and x == 1
    assert ["SOURce1:POWer2:CORRection:LEVel:OFFSet -3.4",
            "SOURce1:POWer2:CORRection:LEVel:OFFSet?",
            ] == visa.cmd

    p2.power_enabled = False
    assert p2.power_enabled is True
    assert ["SOURce1:POWer2:STATe OFF",
            "SOURce1:POWer2:STATe?",
            ] == visa.cmd

    p2.power_gen = False
    assert p2.power_gen is True
    assert ["SOURce1:POWer2:PERManent:STATe OFF",
            "SOURce1:POWer2:PERManent:STATe?",
            ] == visa.cmd

    p2.power_slope = 13.3
    x = p2.power_slope
    assert isinstance(x, float) and x == 1
    assert ["SOURce1:POWer2:LEVel:IMMediate:SLOPe 13.3",
            "SOURce1:POWer2:LEVel:IMMediate:SLOPe?",
            ] == visa.cmd

    visa.ret = "-2,CPAD"
    (power, rel) = p2.get_source_power_offset()
    assert power == -2 and rel is True
    p2.set_source_power_offset(0)
    p2.set_source_power_offset(12.3, False)
    p2.set_source_power_offset(3.45, True)
    assert ["SOURce1:POWer2:LEVel:IMMediate:OFFSet?",
            "SOURce1:POWer2:LEVel:IMMediate:OFFSet 0, CPAD",
            "SOURce1:POWer2:LEVel:IMMediate:OFFSet 12.3, ONLY",
            "SOURce1:POWer2:LEVel:IMMediate:OFFSet 3.45, CPAD",
            ] == visa.cmd


def test_diagram(dummy_vna, visa):
    """
    :param ZNB dummy_vna:
    :param VISA visa:
    """
    dia = dummy_vna.get_diagram(1)
    f = dia.save_screenshot("hej.png")
    assert str(f) == "1\hej.png"
    assert ["MMEMory:NAME 'hej.png'",
            "HCOPy:DESTination 'MMEM'",
            "HCOPy:DEVice:LANGuage PNG",
            "DISPlay:WINDow1:MAXimize?",
            "DISPlay:WINDow1:MAXimize ON",
            "HCOPy:PAGE:WINDow ACTive",
            "HCOPy:IMMediate",
            "MMEMory:CDIRectory?",
            ] == visa.cmd
    assert dia.is_maximized
    dia.is_maximized = False
    dia.select_diagram()
    assert dia.n == 1
    dia.delete()
    assert dia.name == "1"
    dia.name = "Name2"
    assert dia.title == "1"
    dia.title = "Title2"
    assert dia.title_is_visible is True
    assert ["DISPlay:WINDow1:MAXimize?",
            "DISPlay:WINDow1:MAXimize OFF",
            "DISPlay:WINDow1:MAXimize?",
            "DISPlay:WINDow1:MAXimize ON",
            "DISPlay:WINDow1:STATe OFF",
            "DISPlay:WINDow1:NAME?",
            "DISPlay:WINDow1:NAME 'Name2'",
            "DISPlay:WINDow1:TITLe:DATA?",
            "DISPlay:WINDow1:TITLe:DATA 'Title2'",
            "DISPlay:WINDow1:TITLe:STATe?",
            ] == visa.cmd


def test_diagram_assigned_traces(dummy_vna, visa):
    """
    :param ZNB dummy_vna:
    :param VISA visa:
    """
    dia = dummy_vna.get_diagram(2)
    traces = []
    for a in range(1, 3):
        for b in range(1, 3):
            n = (a - 1) * 2 + b
            traces.append((n, "S%i%i" % (b, a)))

    visa.ret_dict["DISPlay:WINDow2:TRACe:CATalog?"] = "'1,S11,2,S21,3,S12,4,S22'"
    cnt = 0
    for (tr, (n, name)) in zip(dia.query_assigned_traces(), traces):
        assert tr.name == name
        cnt += 1
    assert cnt == 4
    assert ["DISPlay:WINDow2:TRACe:CATalog?",
            "CONFigure:TRACe:CHANnel:NAME:ID? 'S11'",
            "CONFigure:TRACe:CHANnel:NAME:ID? 'S21'",
            "CONFigure:TRACe:CHANnel:NAME:ID? 'S12'",
            "CONFigure:TRACe:CHANnel:NAME:ID? 'S22'",
            ] == visa.cmd


def test_marker(dummy_vna, visa):
    """
    Test that the Marker class works as expected.

    :param ZNB dummy_vna: This can be either a ZVA or ZNB instance with visa_res = visa dummy.
    :param VISA visa:
    """
    ch = dummy_vna.get_channel(2)
    tr = ch.get_trace("Tr1")
    m1 = tr.get_marker(3)
    assert [] == visa.cmd

    x = m1.tracking
    m1.tracking = False
    assert ["CALCulate2:PARameter:SELect 'Tr1'",
            "CALCulate2:MARKer3:SEARch:TRACking?",
            "CALCulate2:MARKer3:SEARch:TRACking OFF"] == visa.cmd
    assert isinstance(x, bool)

    tr.name = "Tr2"  # Change the trace name to force an "active trace" select
    visa.clear_cmd()
    m1.is_enabled = True
    x = m1.is_enabled
    m1.is_enabled = "OFF"
    assert ["CALCulate2:PARameter:SELect 'Tr2'",
            "CALCulate2:MARKer3:STATe ON",
            "CALCulate2:MARKer3:STATe?",
            "CALCulate2:MARKer3:STATe OFF"] == visa.cmd
    assert isinstance(x, bool)

    m1.x = 3.3
    x = m1.x
    assert ["CALCulate2:MARKer3:X 3.3",
            "CALCulate2:MARKer3:X?"] == visa.cmd
    assert isinstance(x, float)

    x = m1.y
    assert ["CALCulate2:MARKer3:Y?"] == visa.cmd
    assert isinstance(x, float)


def test_marker_y_set(dummy_znb, visa):
    # type: (ZNB, VISA) -> None
    m1 = dummy_znb.get_channel(2).get_trace("Tr2").get_marker(3)
    m1.TYPE.w("ARB")
    m1.y = 2
    assert m1.y == 1
    assert ["CALCulate2:MARKer3:TYPE ARB",
            "CALCulate2:PARameter:SELect 'Tr2'",
            "CALCulate2:MARKer3:Y 2",
            "CALCulate2:MARKer3:Y?",
            ] == visa.cmd


class TestTrace(object):
    @pytest.fixture
    def tr(self, dummy_vna):
        return dummy_vna.get_channel(2).get_trace("Tr3")

    float_properties = [
        ("scale_per_div",   "DISPlay:WINDow:TRACe:Y:SCALe:PDIVision",   "{:s} {!s}, 'Tr3'", "{:s}? 'Tr3'"),
        ("scale_top",       "DISPlay:WINDow:TRACe:Y:SCALe:TOP",         "{:s} {!s}, 'Tr3'", "{:s}? 'Tr3'"),
        ("scale_bottom",    "DISPlay:WINDow:TRACe:Y:SCALe:BOTTom",      "{:s} {!s}, 'Tr3'", "{:s}? 'Tr3'"),
        ("ref_level",       "DISPlay:WINDow:TRACe:Y:SCALe:RLEVel",      "{:s} {!s}, 'Tr3'", "{:s}? 'Tr3'"),
        ("ref_pos",         "DISPlay:WINDow:TRACe:Y:SCALe:RPOSition",   "{:s} {!s}, 'Tr3'", "{:s}? 'Tr3'"),
    ]

    @PropertyTester.prop_parametrize(float_properties)
    def test_float_properties(self, prop_name, scpi_cmd, scpi_write, scpi_query, scpi_float, tr, visa):
        PropertyTester.test_float_properties(prop_name, scpi_cmd, scpi_write, scpi_query, scpi_float, tr, visa)

    def test_trace_format(self, tr, visa):
        # type: (ZNB, VISA) -> None
        visa.ret = "REAL"
        assert tr.trace_format == "REAL"
        tr.trace_format = 2
        assert ["CALCulate2:PARameter:SELect 'Tr3'",
                "CALCulate2:FORMat?",
                "CALCulate2:FORMat 2",
                ] == visa.cmd

    def test_trace_copy(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        tr.copy_data_to_mem("Mem1")
        tr.copy_math_to_mem("MathMem1")
        assert ["TRACe:COPY 'Mem1', 'Tr3'",
                "TRACe:COPY:MATH 'MathMem1', 'Tr3'",
                ] == visa.cmd

        visa.ret = "S11"
        tr_new = tr.copy("NEW_TRACE")
        assert isinstance(tr_new, type(tr))
        assert ["CALCulate2:PARameter:MEASure? 'Tr3'",
                "CALCulate2:PARameter:SDEFine 'NEW_TRACE', 'S11'",
                ] == visa.cmd

    def test_trace_id(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        """Test that the trace id is cached, and can't be assigned"""
        visa.ret = "1"
        assert tr.n == 1
        assert tr.n == 1
        with pytest.raises(AttributeError):
            tr.n = 2
        assert ["CONFigure:TRACe:NAME:ID? 'Tr3'"] == visa.cmd

    def test_cal_state_label(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        """"Test fetching the cal state label"""
        visa.ret = "Cal"
        x = tr.query_cal_state_label()
        assert isinstance(x, str) and x == "Cal"
        assert ["CALCulate2:PARameter:SELect 'Tr3'",
                "SENSe2:CORRection:SSTate?",
                ] == visa.cmd

    def test_is_active(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        visa.ret = "Tr3\r\n"
        assert tr.is_active() is True
        visa.ret = "Tr6\r\n"
        assert not tr.is_active()
        assert ["CALCulate2:PARameter:SELect?",
                "CALCulate2:PARameter:SELect?",
                ] == visa.cmd

    def test_trace_removal(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        tr.delete()
        assert ["CALCulate2:PARameter:DELete 'Tr3'"] == visa.cmd

    def test_trace_name(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        """Test that the trace name attribute works and is cached"""
        assert tr.name == "Tr3"
        tr.name = "Abc[12]"
        tr.name = "[MEM]a"
        assert ["CONFigure:TRACe:REName 'Tr3', 'Abc[12]'",
                "CONFigure:TRACe:REName 'Abc[12]', '[MEM]a'",
                ] == visa.cmd

    @pytest.mark.parametrize("name", [
        "0"  # Leading integer
        "ASD.a",  # "." in name
        "...",  # "." in name
        "09a",  # Leading integer
    ])
    def test_trace_name_validation(self, name, tr, visa):
            assert pytest.raises(ValueError, "tr.channel.get_trace(name)")
            assert pytest.raises(ValueError, "tr.name = name")
            assert pytest.raises(ValueError, "tr.copy(name)")
            assert pytest.raises(ValueError, "tr.copy_data_to_mem(name)")
            assert pytest.raises(ValueError, "tr.copy_math_to_mem(name)")
            assert [] == visa.cmd

    def test_trace_scaling(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        tr.autoscale()
        assert ["DISPlay:WINDow:TRACe:Y:SCALe:AUTO ONCE, 'Tr3'"] == visa.cmd

    def test_trace_measurement(self, tr, visa):
        # type: (znb.Trace, VISA) -> None
        meas = tr.measurement
        assert isinstance(meas, str)
        tr.measurement = "S21AVG"
        assert ["CALCulate2:PARameter:MEASure? 'Tr3'",
                "CALCulate2:PARameter:MEASure 'Tr3', 'S21AVG'",
                ] == visa.cmd
        tr.measurement = tr.MeasParam.Wave("b", 1, src_port=1, detector="sam")
        assert ["CALCulate2:PARameter:MEASure 'Tr3', 'B01D01SAM'"] == visa.cmd
