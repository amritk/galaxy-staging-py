# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["SatelliteParam", "Orbit"]


class SatelliteParam(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]

    diameter: float
    """Diameter in kilometers"""

    type: Required[Literal["satellite", "moon", "asteroid", "comet"]]

    orbit: Orbit


class Orbit(TypedDict, total=False):
    planet_id: Annotated[int, PropertyInfo(alias="planetId")]
    """The ID of the planet this satellite orbits"""

    orbital_period: Annotated[float, PropertyInfo(alias="orbitalPeriod")]
    """Orbital period in Earth days"""

    distance: float
    """Average distance from the planet in kilometers"""
