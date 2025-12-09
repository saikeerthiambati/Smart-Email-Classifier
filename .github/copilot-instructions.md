# Copilot instructions — small Python email/NLP utility

These instructions help an AI coding agent be effective immediately in this repository.

**Repository snapshot**
- Single Python source file: `email.py` (root). Current imports: `re`, `string`, `nltk.corpus.stopwords`.
- No tests, packaging files, or CI config were found in the workspace root.

**Big picture / intent**
- This repo appears to be a small email / text-processing utility that uses NLTK stopwords. Work should assume a single-file, script-first workflow rather than a full package.

**Environment & setup (Windows PowerShell)**
- Recommended Python: 3.8+ (3.10+ preferred).
- Install NLTK and ensure stopwords dataset is available:

```powershell
python -m pip install --upgrade pip
pip install nltk
python -c "import nltk; nltk.download('stopwords')"
```

- Run the script:

```powershell
python .\email.py
```

**What to look for when editing `email.py`**
- Imports: the presence of `nltk.corpus.stopwords` implies runtime data dependency. If you add code that uses stopwords, ensure the downloader step is present or handled gracefully (try/except with user-friendly message).
- Keep the surface API simple: prefer small, testable functions (e.g., `normalize_text(text)`, `extract_addresses(text)`), since the repo currently has a script-level layout.
- Use `re` and `string` for lightweight parsing; avoid heavy new dependencies unless justified.

**Patterns and examples specific to this repo**
- Example: If implementing tokenization/cleanup, follow this compact approach:

```python
import re
import string
from nltk.corpus import stopwords

STOP = set(stopwords.words('english'))

def normalize_text(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[" + re.escape(string.punctuation) + r"]+", " ", s)
    return " ".join(w for w in s.split() if w and w not in STOP)
```

**Agent-specific rules (what to do / what not to do)**
- Do: Add minimal, focused functions when expanding `email.py`; include docstrings and small examples in the module-level docstring.
- Do: Add an explicit data-availability check for NLTK resources when introducing code that requires them.
- Don't: Introduce a large framework (Django/Flask) or heavy dependencies without creating a project layout and a `requirements.txt` / `pyproject.toml`.
- Don't: Assume tests exist — if you add code, add a small test file (e.g., `tests/test_email.py`) and suggest how to run it.

**Developer workflows to document in PRs**
- When adding NLTK usage, include the one-liner to download datasets in the PR description.
- For any new dependency, add a `requirements.txt` with pinned versions and update README.md with setup steps.

**Files to reference while editing**
- `email.py` — primary source of truth. Any changes must keep the script runnable by the commands above.

If anything here is unclear or you want the instructions to assume a different project direction (packaging, tests, CI), tell me which direction and I will update this file.
