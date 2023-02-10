#!/usr/bin/env python3
"""
Basic Authentication
"""
from api.v1.auth.auth import Auth


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
            return decoded_value
        except Exception as e:
            return None
