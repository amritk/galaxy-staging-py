# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Token"]


class Token(BaseModel):
    """A token to authenticate a user"""

    token: Optional[str] = None
