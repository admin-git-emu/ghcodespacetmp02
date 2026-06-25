# Python + Azure — Codespaces Template

A custom GitHub Codespaces template that gives every developer an identical,
ready-to-code environment: **Python 3.12**, **Azure CLI**, **Bicep**, **azd**,
the **GitHub CLI**, and a curated set of VS Code extensions.

Launch a codespace from this repo and you can run Azure scripts, build
FastAPI apps, and deploy infrastructure within seconds — no local setup.

---

## What's inside

| Path | Purpose |
|------|---------|
| `.devcontainer/devcontainer.json` | Defines the environment: base image, features (Azure CLI, Bicep, azd, GitHub CLI), VS Code extensions, settings, forwarded ports. |
| `.devcontainer/post-create.sh` | Runs once after the container is built — installs Python dependencies and verifies tooling. |
| `requirements.txt` | Python + Azure SDK dependencies. |
| `src/main.py` | A FastAPI starter that lists Azure resource groups. |
| `.gitignore` | Keeps secrets (`.env`, `.azure/`) and build artifacts out of Git. |

---

## How to turn this into a reusable template

1. **Create a new GitHub repository** and add these files (keep the folder structure).
2. On GitHub, go to the repo's **Settings** → check **Template repository**.
   - This lets anyone click **Use this template** to start a fresh project,
     or create a codespace directly from it.
3. (Optional, recommended for teams) Enable **prebuilds**:
   **Settings → Codespaces → Set up prebuild** so new codespaces start in seconds.
4. Share the repo. Anyone clicks **Code → Codespaces → Create codespace on main**
   and lands in the fully configured environment.

> Multiple environments? Add more configs under
> `.devcontainer/<name>/devcontainer.json` (e.g. `.devcontainer/data/devcontainer.json`)
> and users pick one when creating a codespace. Settings are **not** inherited
> between configs, so co-locate any scripts each one needs.

---

## Using the codespace

```bash
# 1. Sign in to Azure (device-code flow works in the browser editor)
az login --use-device-code

# 2. Point the app at your subscription
export AZURE_SUBSCRIPTION_ID="<your-subscription-id>"

# 3. Run the starter API
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Open the forwarded **port 8000** (Ports tab) and hit `/` and `/resource-groups`.

---

## Customizing the environment

- **Add a tool/runtime** → add a Feature to the `features` block in
  `devcontainer.json` (browse https://containers.dev/features).
- **Add a VS Code extension** → add its ID to `customizations.vscode.extensions`.
- **Change Python version** → edit the `image` tag (e.g. `3.11-bookworm`).
- **Run extra setup** → add commands to `.devcontainer/post-create.sh`.

After editing, run **Codespaces: Rebuild Container** (Command Palette / `F1`)
to apply changes.

---

## Cost reminder

Codespaces bills for **compute while active** and **storage while it exists**.
Stop or delete codespaces when you're done (manage them at
`github.com/codespaces`) and set a short auto-stop timeout to stay within your
included monthly quota.

---

### Source references
- Introduction to dev containers — https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers
- Dev Container spec & Features — https://containers.dev
- Microsoft-maintained dev container images — https://mcr.microsoft.com/en-us/product/devcontainers/python/about
