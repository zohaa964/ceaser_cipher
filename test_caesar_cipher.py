"""Unit tests for the Caesar Cipher project."""

import unittest

from main import (
    brute_force,
    calculate_statistics,
    decrypt_text,
    encrypt_text,
)


class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_uppercase(self) -> None:
        self.assertEqual(encrypt_text("HELLO", 3), "KHOOR")

    def test_encrypt_lowercase(self) -> None:
        self.assertEqual(encrypt_text("hello", 3), "khoor")

    def test_preserves_case(self) -> None:
        self.assertEqual(encrypt_text("Hello", 3), "Khoor")

    def test_preserves_non_letters(self) -> None:
        self.assertEqual(
            encrypt_text("Hello, World! 123", 3),
            "Khoor, Zruog! 123",
        )

    def test_wrap_around(self) -> None:
        self.assertEqual(encrypt_text("XYZ xyz", 3), "ABC abc")

    def test_decryption(self) -> None:
        self.assertEqual(decrypt_text("KHOOR", 3), "HELLO")

    def test_reversibility(self) -> None:
        message = "DecodeLabs Project 2!"
        shift = 7
        encrypted = encrypt_text(message, shift)
        self.assertEqual(decrypt_text(encrypted, shift), message)

    def test_large_shift(self) -> None:
        self.assertEqual(encrypt_text("ABC", 29), "DEF")

    def test_zero_shift(self) -> None:
        self.assertEqual(encrypt_text("No Change!", 0), "No Change!")

    def test_statistics(self) -> None:
        stats = calculate_statistics("Hello Ahmed! 123")
        self.assertEqual(stats["total_characters"], 16)
        self.assertEqual(stats["letters"], 10)
        self.assertEqual(stats["uppercase"], 2)
        self.assertEqual(stats["lowercase"], 8)
        self.assertEqual(stats["spaces"], 2)
        self.assertEqual(stats["digits"], 3)
        self.assertEqual(stats["symbols"], 1)

    def test_brute_force_contains_plaintext(self) -> None:
        candidates = dict(brute_force("Khoor"))
        self.assertEqual(candidates[3], "Hello")


if __name__ == "__main__":
    unittest.main(verbosity=2)
