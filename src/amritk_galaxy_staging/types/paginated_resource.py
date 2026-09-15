# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PaginatedResource", "Meta"]


class Meta(BaseModel):
    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None

    next: Optional[str] = None


class PaginatedResource(BaseModel):
    """A paginated resource"""

    meta: Optional[Meta] = None
