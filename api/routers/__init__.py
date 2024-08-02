"""
All Routers are imported here and are exposed to the main app file
"""

from .logs import router as logs_router
from .neko import router as neko_router


__version__ = "v1.0.0-phoenix-release"


__annotations__ = {
    "version": __version__,
    "logs_router": "Logs of API",
    "neko_router": "Neko of API"
}


__all__ = [
    "logs_router",
    "neko_router"
]
