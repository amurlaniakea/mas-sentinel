SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
SPDX-License-Identifier: AGPL-3.0-or-later

from enum import Enum
from pydantic import BaseModel


class InterceptStatus(str, Enum):
    ALLOW = "ALLOW"
    BLOCK = "BLOCK"
    QUARANTINE = "QUARANTINE"


class MessageLog(BaseModel):
    timestamp: float
    status: InterceptStatus
    reason: str
    raw_message: str
