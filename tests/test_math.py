from models import Link

def test_decode_logic():
    short_id='1C'
    expected_id=100

    original_id=Link.decode_id(short_link=short_id)

    assert original_id== expected_id

def test_decode_zero():
    
    assert Link.decode_id('0')==0

def test_decode_invalid():
    assert Link.decode_id("Invalid!") is None