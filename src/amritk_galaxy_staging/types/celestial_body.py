# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo

from .planet import Planet
from .satellite import Satellite

__all__ = ["CelestialBody"]

CelestialBody: TypeAlias = Annotated[Union[Planet, Satellite], PropertyInfo(discriminator="type")]
