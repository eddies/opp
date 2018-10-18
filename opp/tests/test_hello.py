import pytest
import opp as opp

def test_hello():
    assert opp.hello() == "Treach down with O.P.P. (Yeah, you know me!)"
    assert opp.hello("Kay Gee") == "Kay Gee down with O.P.P. (Yeah, you know me!)"