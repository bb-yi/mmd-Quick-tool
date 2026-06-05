# Compatibility shim. The generated implementation is split across feature modules.
from .registration import register, unregister

__all__ = ['register', 'unregister']
