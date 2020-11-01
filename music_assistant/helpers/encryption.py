"""Various helpers for data encryption/decryption."""

import asyncio

from cryptography.fernet import Fernet, InvalidToken
from music_assistant.helpers.app_vars import get_app_var  # noqa # pylint: disable=all


async def async_encrypt_string(str_value: str) -> str:
    """Encrypt a string with Fernet."""
    return await asyncio.get_running_loop().run_in_executor(
        None, encrypt_string, str_value
    )


def encrypt_string(str_value: str) -> str:
    """Encrypt a string with Fernet."""
    return Fernet(get_app_var(3)).encrypt(str_value.encode()).decode()


async def async_encrypt_bytes(bytes_value: bytes) -> bytes:
    """Encrypt bytes with Fernet."""
    return await asyncio.get_running_loop().run_in_executor(
        None, encrypt_bytes, bytes_value
    )


def encrypt_bytes(bytes_value: bytes) -> bytes:
    """Encrypt bytes with Fernet."""
    return Fernet(get_app_var(3)).encrypt(bytes_value)


async def async_decrypt_string(encrypted_str: str) -> str:
    """Decrypt a string with Fernet."""
    return await asyncio.get_running_loop().run_in_executor(
        None, decrypt_string, encrypted_str
    )


def decrypt_string(encrypted_str: str) -> str:
    """Decrypt a string with Fernet."""
    try:
        return Fernet(get_app_var(3)).decrypt(encrypted_str.encode()).decode()
    except (InvalidToken, AttributeError):
        return None


async def async_decrypt_bytes(bytes_value: bytes) -> bytes:
    """Decrypt bytes with Fernet."""
    return await asyncio.get_running_loop().run_in_executor(
        None, decrypt_bytes, bytes_value
    )


def decrypt_bytes(bytes_value):
    """Decrypt bytes with Fernet."""
    try:
        return Fernet(get_app_var(3)).decrypt(bytes_value)
    except (InvalidToken, AttributeError):
        return None