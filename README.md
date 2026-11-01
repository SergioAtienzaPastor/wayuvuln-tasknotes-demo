# tasknotes · Wayuvuln Live Security Showcase

Micro-aplicación Flask de notas y soporte interno utilizada como **banco de pruebas E2E en vivo** de **Wayuvuln (`wayuvuln[bot]`)**.

> [!WARNING]
> **Repositorio de demostración de seguridad:** contiene vulnerabilidades intencionales para exhibir el ciclo autónomo de detección verificada (`E2`), auto-remediación con pruebas ROJO→VERDE y gobierno en GitHub. No desplegar en producción.

## 🗺️ Qué puedes inspeccionar en este repositorio

| Capacidad demostrada | Dónde verlo en vivo | Qué observar |
|---|---|---|
| **1. Issues DevUX ("10 segundos")** | [Issues abiertas](../../issues?q=is%3Aissue+is%3Aopen) | Bloque `[!CAUTION]`, **snippet interactivo del código vulnerable incrustado**, tabla de exploit real y enlace de 1 clic al PR de solución. |
| **2. PRs Auto-Fix ROJO → VERDE** | [Pull Requests abiertos](../../pulls?q=is%3Apr+is%3Aopen) | Firmados por `wayuvuln[bot]`, diff quirúrgico + test de regresión, **GitHub Checks API (`wayuvuln/verify`)** y resumen en vivo de GitHub Actions. |
| **3. Bloqueo de un fix insuficiente** | [PRs cerrados (`trap`)](../../pulls?q=is%3Apr+is%3Aclosed+trap) | `wayuvuln/verify` en **ROJO** con **anotación inline en la línea exacta del diff** impidiendo el merge por Branch Protection. |
| **4. Fix manual del dev + auto-limpieza + regresión** | [Issues cerradas (`FIXED`)](../../issues?q=is%3Aissue+is%3Aclosed) | El dev sube su propio fix → `wayuvuln[bot]` cierra su PR huérfano (`👏`), detecta una regresión posterior (`♻️ REOPENED`) y verifica el cierre final. |
| **5. Respeto a *"Close as not planned"*** | [Issues cerradas (`not planned`)](../../issues?q=is%3Aissue+reason%3A%22not+planned%22) | Marcada como `DISMISSED`: cero comentarios y cero reaperturas en re-escaneos posteriores. |
| **6. Shift-Left en PRs humanos (1 clic y silencio)** | [PRs `#1`–`#4`](../../pulls?q=is%3Apr+is%3Aclosed) | Bloques ```` ```suggestion ```` aplicables a 1 clic en PRs con riesgo (`#1`–`#3`) y **cero ruido** en PR limpio (`#4`). |
| **7. Code Scanning (SARIF)** | [Security → Code scanning](../../security/code-scanning) | Alertas nativas sincronizadas con los hallazgos verificados en `main`. |

## Ejecución local

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```
