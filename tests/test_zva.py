# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import absolute_import, division, print_function

import pytest
from .conftest import VISA  # noqa: F401

from RSSscpi.zva import ZVA  # noqa: F401


def test_vna_port(zva, visa):
    # type: (ZVA, VISA) -> None
    ch = zva.get_channel(1)
    p2 = ch.get_vna_port(2)

    p2.src_attenuator = 20
    x = p2.src_attenuator
    assert isinstance(x, int) and x == 1
    assert ["SOURce1:POWer2:ATTenuation 20",
            "SOURce1:POWer2:ATTenuation:AUTO:VALue?",
            ] == visa.cmd

    visa.ret = "MAN"
    p2.src_attenuator_mode = "AUTO"
    assert p2.src_attenuator_mode == "MAN"
    assert ["SOURce1:POWer2:ATTenuation:MODE AUTO",
            "SOURce1:POWer2:ATTenuation:MODE?",
            ] == visa.cmd


def test_marker_y_set(zva, visa):
    # type: (ZVA, VISA) -> None
    m4 = zva.get_channel(2).get_trace("Tr2").get_marker(4)
    assert [] == visa.cmd
    with pytest.raises(AttributeError, message="Assignment to marker y value is not possible."):
        m4.y = 2


def test_sweep_dwell(zva, visa):
    # type: (ZVA, VISA) -> None
    """
    This setting is not available on the ZVA
    """
    sw = zva.get_channel(2).sweep
    with pytest.raises(AttributeError):
        sw.dwell_on_each_partial_measurement = True
    assert sw.dwell_on_each_partial_measurement is True
    assert [] == visa.cmd