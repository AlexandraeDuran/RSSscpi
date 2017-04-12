# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import pytest
from common import *
from RSSscpi.gen.Instrument import SCPICmdFormatter
from RSSscpi.gen.Instrument import LimitedCapacityDict


def test_SCPICmdFormatter():
    f = SCPICmdFormatter
    arg = (1, 2, 3)
    assert f().vformat("{:q*}", (arg, ), {}) == "'1', '2', '3'"
    assert f().format("{:d*}", arg) == "1, 2, 3"
    assert f().format("{:s}", arg) == "(1, 2, 3)"
    assert f().format("{:q}", arg) == "'(1, 2, 3)'"
    assert f().format("{:q}", "'Q'") == "'Q'"
    assert f().format("{:s}", "'Q'") == "'Q'"
    assert f().format("{:q}", "Q") == "'Q'"
    assert f().format("{:s}", "Q") == "Q"
    arg_str_list = ("'Q'", "Q", "S", "'S'")
    assert f().format("{:q}, {:q}, {:s}, {:s}", *arg_str_list) == "'Q', 'Q', S, 'S'"
    assert f().format("{:q*}", arg_str_list) == "'Q', 'Q', 'S', 'S'"
    assert f().format("{:s*}", arg_str_list) == "'Q', Q, S, 'S'"


def test_cmd_formatting(znb):
    znb.TRACe.COPY.MATH().w("MDATA8")  # This shouldn't be quoted
    znb.TRACe.COPY.MATH().w("sq")  # Quote
    znb.SENSe.SWEep.POINts().w(1e9)
    znb.SENSe.SWEep.POINts().w("1000000000")
    znb.SENSe.SWEep.POINts().w(1000000000)
    znb.TRIGger.SEQuence.LINK().w("POINt")  # This should be quoted
    znb.TRIGger.SEQuence.LINK().w("'POINT'")  # This should only have one pair of quotes
    with pytest.warns(UserWarning) as record:
        znb.CALCulate.MARKer.Y().q("")
        znb.CALCulate.MARKer.Y().q("asd", fmt="{:s}")
        znb.CALCulate.MARKer.Y().q("asd", fmt="")
    assert len(record) == 1
    assert ["TRACe:COPY:MATH MDATA8",
            "TRACe:COPY:MATH 'sq'",
            "SENSe:SWEep:POINts 1000000000.0",
            "SENSe:SWEep:POINts 1000000000",
            "SENSe:SWEep:POINts 1000000000",
            "TRIGger:SEQuence:LINK 'POINt'",
            "TRIGger:SEQuence:LINK 'POINT'",
            "CALCulate:MARKer:Y?",
            "CALCulate:MARKer:Y? asd",
            "CALCulate:MARKer:Y?",
            ] == visa.cmd


def test_LimitedCapacityDict():
    d = LimitedCapacityDict()
    assert d.max_len is None
    for n in range(100):
        d[n] = str(n)
    assert len(d) == 100
    assert list(d.keys()) == list(range(100))
    d.max_len = 50
    assert len(d) == 50
    assert list(d.keys()) == list(range(50, 100))
    for n in range(20):
        d[n] = str(n)
    assert len(d) == 50
    assert list(d.keys()) == list(range(70, 100)) + list(range(20))