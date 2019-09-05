"""
Tests and examples for the barcode decoding challenge.

Note: Please modify those tests as you wish! Your choice of
implementation may be different from mine, don't hesitate to play
around with he code here.
"""
import pytest

from .barcode import decode_digit, decode_barcode


class TestDecodeDigit:

    def test_decode_left(self):
        assert decode_digit("0001101") == 0
        assert decode_digit("0111011") == 7
        assert decode_digit("0011001") == 1

        with pytest.raises(Exception):
            decode_digit("0000000")

    @pytest.mark.skip("Remove me for exercise 2")
    def test_decode_right(self):
        assert decode_digit("1110010") == 0
        assert decode_digit("1000100") == 7
        assert decode_digit("1100110") == 1

    @pytest.mark.skip("Remove me for exercise 5.1")
    def test_decode_even(self):
        assert decode_digit("0100111") == 0
        assert decode_digit("0010001") == 7
        assert decode_digit("0110011") == 1


# The dataset below is a list of tuples made of an UPC-A code and
# its corresponding barcode. Those will be automatically tested by
# test_decode_upc_a below. So add your examples here to test them.
TEST_UPC_A = [
    (
        "075755331853",
        "10100011010111011011000101110110110001011000101010100001010000101100110100100010011101000010101"
    ),
    (
        "760712090019",
        "10101110110101111000110101110110011001001001101010111001011101001110010111001011001101110100101"
    ),
    (
        "037431882400",
        "10100011010111101011101101000110111101001100101010100100010010001101100101110011100101110010101"
    ),
    (
        "296480306484",
        "10100100110001011010111101000110110111000110101010100001011100101010000101110010010001011100101"
    ),
    (
        "193872293318",
        "10100110010001011011110101101110111011001001101010110110011101001000010100001011001101001000101"
    ),
]

# This dataset is a list of barcodes that should fail because their
# checksum is invalid. Those are automatically tested by test_checksum_fail.
TEST_CHECKSUM_FAIL = [
    "10100011010111011011000101110110110001011000101010100001010000101100110100100010011101000100101",
    "10100100110001011010111101000110110111000110101010100001011100101110100101110010010001011100101",
]

# The dataset below is a list of tuples made of an EAN-13 code and
# its corresponding barcode. Those will be automatically tested by
# test_decode_ean_13 below. So add your examples here to test them.
TEST_EAN_13 = [
    (
        "9781593276669",
        "10101110110001001011001101100010010111011110101010110110010001001010000101000010100001110100101"
    ),
    (
        "3037920112008",
        "10100011010111101001000100101110011011000110101010110011011001101101100111001011100101001000101"
    ),
    (
        "9001890194818",
        "10100011010100111011001101101110010111000110101010110011011101001011100100100011001101001000101"
    ),
    (
        "4607087287544",
        "10101011110100111011101100011010001001001000101010110110010010001000100100111010111001011100101"
    ),
    (
        "9781593275990",
        "10101110110001001011001101100010010111011110101010110110010001001001110111010011101001110010101"
    ),
    (
        "9780201616224",
        "10101110110001001010011100100110100111001100101010101000011001101010000110110011011001011100101"
    ),
    (
        "9780008323448",
        "10101110110001001010011100011010100111011011101010100001011011001000010101110010111001001000101"
    ),
]


class TestDecodeBarcode:

    @pytest.mark.skip("Remove me for exercise 3")
    @pytest.mark.parametrize("expected_code,barcode", TEST_UPC_A)
    def test_decode_upc_a(self, expected_code, barcode):
        assert decode_barcode(barcode) == expected_code

    @pytest.mark.skip("Remove me for exercise 4")
    @pytest.mark.parametrize("invalid_barcode", TEST_CHECKSUM_FAIL)
    def test_checksum_fail(self, invalid_barcode):
        with pytest.raises(Exception):
            decode_barcode(invalid_barcode)

    @pytest.mark.skip("Remove me for exercise 5.2")
    @pytest.mark.parametrize("expected_code,barcode", TEST_EAN_13)
    def test_decode_ean_13(self, expected_code, barcode):
        assert decode_barcode(barcode) == expected_code