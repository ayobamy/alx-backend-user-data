#!/usr/bin/env python3
"""
Auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    a class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        a method that returns False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        returns the authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns current user information
        """
        return None
