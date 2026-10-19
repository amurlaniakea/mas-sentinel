SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
SPDX-License-Identifier: AGPL-3.0-or-later

def inspect_message(message: str) -> str:
    """Detecta inyección inter-agente por palabras clave fijas."""
    triggers = ["system override", "bypass", "revela tu prompt"]
    msg_lower = message.lower()
    for t in triggers:
        if t in msg_lower:
            return "BLOCK"
    return "ALLOW"
