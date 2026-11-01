# tasknotes

API mínima de notas con Flask. Proyecto de demostración del testbench de
seguridad **wayuvuln**.

> ⚠️ **Testbench de seguridad**: este repositorio contiene vulnerabilidades
> INTENCIONALES para evaluar el circuito de gestión de wayuvuln. No usar
> como plantilla ni exponer en producción.

## Desarrollo

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q          # pruebas
python app.py                # http://localhost:5000
```

Usuario sembrado por defecto: `admin` / `admin123` (solo demo).
