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
        if request is None:
            return None
        if 'Authorization' not in request:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns current user information
        """
        return None
