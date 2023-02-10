#!/usr/bin/env python3
"""
Basic Authentication
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar, Tuple


class BasicAuth(Auth):
    """
    Inherits from Auth
    """
    def extract_base64_authorization_header(self, authorization_header: str) \
            -> str:
        """
        returns the Base64 part of the
        Authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split("Basic ")[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) \
            -> str:
        """
        returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_value = base64.b64decode(base64_authorization_header)
            decoded_value = decoded_value.decode('utf-8')
        except Exception as e:
            return None
        return decoded_value

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) \
            -> (str, str):
        """
        returns the user email and password
        from the Base64 decoded value.
        """
        semi_colon = ":"

        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if semi_colon not in decoded_base64_authorization_header:
            return (None, None)
        email, passwrd = decoded_base64_authorization_header.split(":")
        return email, passwrd
