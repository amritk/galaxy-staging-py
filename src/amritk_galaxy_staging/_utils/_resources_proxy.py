from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `amritk_galaxy_staging.resources` module.

    This is used so that we can lazily import `amritk_galaxy_staging.resources` only when
    needed *and* so that users can just import `amritk_galaxy_staging` and reference `amritk_galaxy_staging.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("amritk_galaxy_staging.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
