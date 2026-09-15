# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Satellite", "Orbit"]


class Orbit(BaseModel):
    planet_id: Optional[int] = FieldInfo(alias="planetId", default=None)
    """The ID of the planet this satellite orbits"""

    orbital_period: Optional[float] = FieldInfo(alias="orbitalPeriod", default=None)
    """Orbital period in Earth days"""

    distance: Optional[float] = None
    """Average distance from the planet in kilometers"""


class Satellite(BaseModel):
    """Every satellite in the Scalar Galaxy"""

    id: Optional[int] = None

    name: str

    description: Optional[str] = None

    diameter: Optional[float] = None
    """Diameter in kilometers"""

    type: Literal["satellite", "moon", "asteroid", "comet"]

    orbit: Optional[Orbit] = None
