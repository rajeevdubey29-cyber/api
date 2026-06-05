# AGENTS.md

## Cursor Cloud specific instructions

### What this repo is

A flat collection of **standalone FastAPI learning APIs** (not a monorepo). Each `*.py` file defines its own `app = FastAPI()`. Only **one app per Uvicorn process** unless you use different ports.

| Module file | Port (example) | Main endpoints |
|-------------|----------------|----------------|
| `Calculator.py` | 8000 | `POST /calculator` |
| `UserRegistrationApi.py` | 8001 | `POST /register`, `GET /users` |
| `API_Basic.py`, `Multiplication_API_with_Validation.py` | 8002+ | math routes (see file) |
| `testing.py` | 8003+ | in-memory user PUT/DELETE |

Notebooks under `VictorDB/` call an external Euron API and need extra packages (`requests`, `numpy`) and credentials; they are optional for API work.

### Dependencies

- Python 3.12+ with `pip3 install -r requirements.txt` (user site-packages is fine).
- `python3 -m venv` may fail on this image without `python3.12-venv`; use `pip3 install --user` and `python3 -m uvicorn` instead of relying on a venv.
- Ensure `~/.local/bin` is on `PATH`, or invoke Uvicorn as `python3 -m uvicorn`.

### Run a dev server

From `/workspace`, pick **one** module (module name = filename without `.py`):

```bash
export PATH="$HOME/.local/bin:$PATH"
cd /workspace
python3 -m uvicorn Calculator:app --host 127.0.0.1 --port 8000 --reload
```

Interactive docs: `http://127.0.0.1:<port>/docs`

Use **tmux** for long-running servers in Cloud Agent VMs (see environment setup notes).

### Lint / test / build

There are **no** configured linters, pytest suites, or build steps in this repo.

- **Sanity check:** `python3 -m py_compile *.py`
- **Smoke test (Calculator):**  
  `curl -s -X POST http://127.0.0.1:8000/calculator -H 'Content-Type: application/json' -d '{"a":10,"b":5,"operation":"multiply"}'`
- **Smoke test (registration):** start `UserRegistrationApi:app` on another port, then `POST /register` and `GET /users`.
