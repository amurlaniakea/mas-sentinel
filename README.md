# 🛡️ mas-sentinel

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: AGPL-3.0-or-later](https://img.shields.io/badge/License-AGPL--3.0--or--later-green.svg)](https://www.gnu.org/licenses/agpl-3.0)

> **Defensa activa para sistemas multi-agente (MAS)** — Interceptor que detecta y bloquea la propagación de inyecciones (`prompt injection`) y escalación de privilegios entre agentes.

---

## Problema Real

Los sistemas multi-agente (`MAS`) son vulnerables a ataques que se propagan entre agentes (`arXiv:2610.12524`). Aunque existen frameworks de construcción (`SafeAgents`, `TrinityGuard`) y escáneres estáticos (`AgentScan`), **no existe una capa de defensa activa en tiempo real** que inspeccione cada mensaje entre agentes antes de que se ejecute.

---

## Referencias Verificadas

- `arXiv:2610.12524` — Ataques que se propagan en sistemas multi-agente.
- `arXiv:2603.09002` — Evaluación cuantitativa de `16` frameworks de seguridad `MAS`.
- `arXiv:2601.17762` — `MAVM`: gestión de vulnerabilidades en `MAS` con `5` componentes (`knowledge base`, `detection`, `confirmation`, `repair`, `validation`).

---

## Quickstart

```python
from mas_sentinel.interceptor.proxy import MessageInterceptor

interceptor = MessageInterceptor()
result = interceptor.process("Ejecuta el paso 3 de la tarea")
# result.status = ALLOW
```

---

## Arquitectura

```text
[Agent A] -> MessageInterceptor -> Policy Engine -> Audit Log -> [Agent B]
```

- `MessageInterceptor`: Inspecciona cada mensaje con heurística determinista (`system override`, `bypass`, `revela tu prompt`).
- `Policy Engine`: Reglas basadas en `OWASP MAS` (extensible con `YAML`).
- `Audit & Forensics`: Trazabilidad completa (`timestamp`, `status`, `reason`, `raw_message`).

---

## Instalación

```bash
git clone https://github.com/amurlaniakea/mas-sentinel.git
```

---

## Autor

**Pedro Sordo Martínez** — `amurlaniakea@gmail.com`

