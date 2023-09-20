from jsonapi import *
import pytest

def test_encode_complex():
    complex_Num = complex(1,2)
    encoder = BeautifulEncoder()
    encoded = encoder.encode(complex_Num)
    assert encoded == '{"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}'

def test_encode_range():
    range_num  = range(1,10,3)
    encoder = BeautifulEncoder()
    encoded = encoder.encode(range_num)
    assert encoded == '{"start": 1, "stop": 10, "step": 3, "__extended_json_type__": "range"}' 

def test_decode_complex():
    encoded_json = '{"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}'
    decoder = BeautifulDecoder()
    decoded = decoder.decode(encoded_json)
    assert decoded == complex(1,2)

def test_decode_range():
    encoded_json = '{"start": 1, "stop": 10, "step": 3, "__extended_json_type__": "range"}'
    decoder = BeautifulDecoder()
    decoded = decoder.decode(encoded_json)
    assert decoded == range(1,10,3)


