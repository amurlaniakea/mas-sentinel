# SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later

import time

from mas_sentinel.interceptor.inspector import inspect_message
from mas_sentinel.interceptor.models import InterceptStatus, MessageLog


class MessageInterceptor:
    def process(self, message: str) -> MessageLog:
        status_str = inspect_message(message)
        status = InterceptStatus(status_str)
        reason = "Inyección inter-agente detectada." if status == InterceptStatus.BLOCK else "Mensaje limpio."
        return MessageLog(
            timestamp=time.time(),
            status=status,
            reason=reason,
            raw_message=message,
        )
