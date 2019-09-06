"""
Administrative parser init

Overview
===============================================================================

+----------+------------------------------------------------------------------+
| Path     | PyPoE/cli/exporter/wiki/admin/__init__.py                        |
+----------+------------------------------------------------------------------+
| Version  | 1.0.0a0                                                          |
+----------+------------------------------------------------------------------+
| Revision | $Id$                  |
+----------+------------------------------------------------------------------+
| Author   | Omega_K2                                                         |
+----------+------------------------------------------------------------------+

Description
===============================================================================

Agreement
===============================================================================

See PyPoE/LICENSE
"""

# =============================================================================
# Imports
# =============================================================================

from PyPoE.cli.exporter.wiki.admin.unique import UniqueCommandHandler

# =============================================================================
# Globals
# =============================================================================


ADMIN_HANDLERS = [UniqueCommandHandler]

__all__ = ['ADMIN_HANDLERS']