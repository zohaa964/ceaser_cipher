"""
DecodeLabs Cyber Security Internship — Project 2
Basic Encryption & Decryption using the Caesar Cipher

Features:
- Encrypt and decrypt text
- Custom shift key
- Preserves case, spaces, numbers, and symbols
- Input validation
- Encryption/decryption verification
- Message statistics
- Brute-force demonstration
- Session history
- Save results to a text file
- Coloured terminal interface
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import TypedDict


class Color:
    """ANSI terminal colour codes."""

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


class Statistics(TypedDict):
    total_characters: int
    letters: int
    uppercase: int
    lowercase: int
    spaces: int
    digits: int
    symbols: int


class HistoryRecord(TypedDict):
    operation: str
    input_text: str
    output_text: str
    shift_key: int
    timestamp: str


def transform_text(text: str, shift: int) -> str:
    """
    Shift every English alphabetic character by `shift` positions.

    Positive shifts encrypt. Negative shifts decrypt.
    Non-alphabetic characters remain unchanged.
    """
    transformed: list[str] = []

    for character in text:
        if "A" <= character <= "Z":
            position = ord(character) - ord("A")
            new_position = (position + shift) % 26
            transformed.append(chr(new_position + ord("A")))

        elif "a" <= character <= "z":
            position = ord(character) - ord("a")
            new_position = (position + shift) % 26
            transformed.append(chr(new_position + ord("a")))

        else:
            transformed.append(character)

    return "".join(transformed)


def encrypt_text(text: str, shift: int) -> str:
    """Encrypt text using the Caesar Cipher."""
    return transform_text(text, shift)


def decrypt_text(text: str, shift: int) -> str:
    """Decrypt Caesar Cipher text using the same shift key."""
    return transform_text(text, -shift)


def calculate_statistics(text: str) -> Statistics:
    """Count message character categories."""
    statistics: Statistics = {
        "total_characters": len(text),
        "letters": 0,
        "uppercase": 0,
        "lowercase": 0,
        "spaces": 0,
        "digits": 0,
        "symbols": 0,
    }

    for character in text:
        if character.isalpha():
            statistics["letters"] += 1
            if character.isupper():
                statistics["uppercase"] += 1
            else:
                statistics["lowercase"] += 1
        elif character.isspace():
            statistics["spaces"] += 1
        elif character.isdigit():
            statistics["digits"] += 1
        else:
            statistics["symbols"] += 1

    return statistics


def get_non_empty_text(prompt: str) -> str:
    """Request a non-empty message."""
    while True:
        text = input(prompt)
        if text.strip():
            return text

        print(
            Color.RED
            + Color.BOLD
            + "Message cannot be empty. Please try again."
            + Color.RESET
        )


def get_shift_key() -> int:
    """Request and normalise a valid integer shift key."""
    while True:
        raw_value = input(
            Color.MAGENTA + "Enter the shift key: " + Color.RESET
        ).strip()

        try:
            return int(raw_value) % 26
        except ValueError:
            print(
                Color.RED
                + Color.BOLD
                + "Invalid shift key. Enter a whole number."
                + Color.RESET
            )


def ask_yes_no(prompt: str) -> bool:
    """Return True for yes and False for no."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False

        print("Please enter Y or N.")


def display_header() -> None:
    """Display the program banner."""
    print(Color.CYAN + Color.BOLD)
    print("=" * 68)
    print("          DECODELABS CYBER SECURITY INTERNSHIP")
    print("                         PROJECT 2")
    print("             BASIC ENCRYPTION AND DECRYPTION")
    print("                   CAESAR CIPHER SYSTEM")
    print("=" * 68)
    print(Color.RESET)


def display_menu() -> None:
    """Display all available operations."""
    print(Color.BLUE + Color.BOLD + "\nSelect an operation:" + Color.RESET)
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Encrypt and verify")
    print("4. Brute-force a ciphertext")
    print("5. View session history")
    print("6. Exit")


def display_statistics(text: str, shift_key: int) -> None:
    """Display statistics for a supplied message."""
    stats = calculate_statistics(text)

    print(Color.BLUE + Color.BOLD + "\nMESSAGE STATISTICS" + Color.RESET)
    print("-" * 34)
    print(f"Total characters   : {stats['total_characters']}")
    print(f"Letters             : {stats['letters']}")
    print(f"Uppercase letters   : {stats['uppercase']}")
    print(f"Lowercase letters   : {stats['lowercase']}")
    print(f"Spaces              : {stats['spaces']}")
    print(f"Digits              : {stats['digits']}")
    print(f"Symbols             : {stats['symbols']}")
    print(f"Shift key           : {shift_key}")
    print("-" * 34)


def display_result(
    heading: str,
    input_label: str,
    input_text: str,
    output_label: str,
    output_text: str,
    shift_key: int,
) -> None:
    """Display a formatted encryption or decryption result."""
    print(Color.CYAN + "\n" + "-" * 68 + Color.RESET)
    print(Color.BOLD + heading + Color.RESET)
    print(f"{input_label:<19}: {input_text}")
    print(f"{'Shift key':<19}: {shift_key}")
    print(Color.GREEN + f"{output_label:<19}: {output_text}" + Color.RESET)
    print(Color.CYAN + "-" * 68 + Color.RESET)


def save_result(record: HistoryRecord) -> Path:
    """Append one operation result to results.txt."""
    output_path = Path(__file__).resolve().parent / "results.txt"

    content = (
        "\n"
        + "=" * 68
        + "\n"
        + f"Date and time      : {record['timestamp']}\n"
        + f"Operation          : {record['operation']}\n"
        + f"Input text         : {record['input_text']}\n"
        + f"Output text        : {record['output_text']}\n"
        + f"Shift key          : {record['shift_key']}\n"
        + "=" * 68
        + "\n"
    )

    with output_path.open("a", encoding="utf-8") as file:
        file.write(content)

    return output_path


def create_history_record(
    operation: str,
    input_text: str,
    output_text: str,
    shift_key: int,
) -> HistoryRecord:
    """Create a structured history record."""
    return {
        "operation": operation,
        "input_text": input_text,
        "output_text": output_text,
        "shift_key": shift_key,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def handle_save(record: HistoryRecord) -> None:
    """Ask whether the user wants to save a result."""
    if ask_yes_no("\nSave this result to results.txt? (Y/N): "):
        path = save_result(record)
        print(
            Color.GREEN
            + f"Result saved successfully: {path.name}"
            + Color.RESET
        )


def brute_force(ciphertext: str) -> list[tuple[int, str]]:
    """Generate all 25 meaningful Caesar Cipher decryptions."""
    return [
        (shift, decrypt_text(ciphertext, shift))
        for shift in range(1, 26)
    ]


def display_history(history: list[HistoryRecord]) -> None:
    """Display operations completed during the current session."""
    print(Color.BLUE + Color.BOLD + "\nSESSION HISTORY" + Color.RESET)

    if not history:
        print("No encryption or decryption operations have been completed yet.")
        return

    for index, record in enumerate(history, start=1):
        print("\n" + "-" * 68)
        print(f"Record {index}")
        print(f"Time       : {record['timestamp']}")
        print(f"Operation  : {record['operation']}")
        print(f"Input      : {record['input_text']}")
        print(f"Output     : {record['output_text']}")
        print(f"Shift key  : {record['shift_key']}")
    print("-" * 68)


def main() -> None:
    """Run the Caesar Cipher application."""
    history: list[HistoryRecord] = []
    display_header()

    while True:
        display_menu()
        choice = input(
            Color.MAGENTA + "\nEnter your choice (1-6): " + Color.RESET
        ).strip()

        if choice == "1":
            message = get_non_empty_text(
                "\nEnter the message you want to encrypt: "
            )
            shift_key = get_shift_key()
            encrypted_message = encrypt_text(message, shift_key)

            display_result(
                "ENCRYPTION RESULT",
                "Original message",
                message,
                "Encrypted message",
                encrypted_message,
                shift_key,
            )
            display_statistics(message, shift_key)

            record = create_history_record(
                "Encryption", message, encrypted_message, shift_key
            )
            history.append(record)
            handle_save(record)

        elif choice == "2":
            ciphertext = get_non_empty_text(
                "\nEnter the encrypted message: "
            )
            shift_key = get_shift_key()
            decrypted_message = decrypt_text(ciphertext, shift_key)

            display_result(
                "DECRYPTION RESULT",
                "Encrypted message",
                ciphertext,
                "Decrypted message",
                decrypted_message,
                shift_key,
            )
            display_statistics(ciphertext, shift_key)

            record = create_history_record(
                "Decryption", ciphertext, decrypted_message, shift_key
            )
            history.append(record)
            handle_save(record)

        elif choice == "3":
            message = get_non_empty_text(
                "\nEnter the message you want to encrypt: "
            )
            shift_key = get_shift_key()

            encrypted_message = encrypt_text(message, shift_key)
            decrypted_message = decrypt_text(encrypted_message, shift_key)
            successful = decrypted_message == message

            print(Color.CYAN + "\n" + "-" * 68 + Color.RESET)
            print(Color.BOLD + "ENCRYPTION VERIFICATION" + Color.RESET)
            print(f"{'Original message':<19}: {message}")
            print(f"{'Shift key':<19}: {shift_key}")
            print(
                Color.GREEN
                + f"{'Encrypted message':<19}: {encrypted_message}"
                + Color.RESET
            )
            print(
                Color.YELLOW
                + f"{'Decrypted message':<19}: {decrypted_message}"
                + Color.RESET
            )

            if successful:
                print(
                    Color.GREEN
                    + Color.BOLD
                    + f"{'Verification':<19}: Successful"
                    + Color.RESET
                )
            else:
                print(
                    Color.RED
                    + Color.BOLD
                    + f"{'Verification':<19}: Failed"
                    + Color.RESET
                )

            print(Color.CYAN + "-" * 68 + Color.RESET)
            display_statistics(message, shift_key)

            record = create_history_record(
                "Encrypt and verify",
                message,
                encrypted_message,
                shift_key,
            )
            history.append(record)
            handle_save(record)

        elif choice == "4":
            ciphertext = get_non_empty_text(
                "\nEnter the ciphertext to brute-force: "
            )

            print(
                Color.YELLOW
                + Color.BOLD
                + "\nTrying all 25 possible shift keys:"
                + Color.RESET
            )
            print("-" * 68)

            for shift, possible_text in brute_force(ciphertext):
                print(f"Shift {shift:>2}: {possible_text}")

            print("-" * 68)
            print(
                Color.YELLOW
                + "Review the outputs and identify the readable plaintext."
                + Color.RESET
            )

        elif choice == "5":
            display_history(history)

        elif choice == "6":
            print(
                Color.GREEN
                + Color.BOLD
                + "\nProgram closed successfully."
                + Color.RESET
            )
            break

        else:
            print(
                Color.RED
                + Color.BOLD
                + "\nInvalid option. Choose a number from 1 to 6."
                + Color.RESET
            )


if __name__ == "__main__":
    main()
""" if you need any help running this code 
you can use chatgpt bcz gpt has more knowledge 
than uu ,mee  and us"""