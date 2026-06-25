# MarkItDown Codespace Template

A ready-to-use [GitHub Codespaces](https://github.com/features/codespaces) dev
container with **[Microsoft MarkItDown](https://github.com/microsoft/markitdown)**
the **[Azure CLI](https://learn.microsoft.com/cli/azure/)** (plus Bicep),
the **[AWS CLI](https://aws.amazon.com/cli/)**, and **[Terraform](https://developer.hashicorp.com/terraform)**
(with the HashiCorp VS Code extension) pre-installed. Anyone who opens a
codespace from this repository gets every tool automatically — no local setup
required.

> **MarkItDown** converts PDF, Word, PowerPoint, Excel, images (OCR), audio,
> HTML, CSV/JSON/XML, ZIP, and more into clean Markdown. Requires Python 3.10+.
>
> **Azure CLI (`az`)** manages Azure resources from the terminal; this template
> also installs **Bicep** for infrastructure-as-code.
>
> **AWS CLI (`aws`)** manages AWS resources from the terminal.
>
> **Terraform** provisions multi-cloud infrastructure-as-code; the
> `hashicorp.terraform` extension adds syntax, validation, and plan support, and
> **tfsec** is included for security scanning.

---

## What's in this template

```
.devcontainer/
├── Dockerfile                                  # Builds the image with MarkItDown baked in (recommended)
├── devcontainer.json                           # Active config — Dockerfile + Azure/AWS CLI + Terraform features
└── devcontainer.alternative-no-dockerfile.json # Optional config — installs via onCreateCommand instead
README.md
```

Both configs install **MarkItDown** plus a full cloud-IaC toolchain — **Azure
CLI + Bicep**, **AWS CLI**, and **Terraform + tfsec** — all via official dev
container Features, so they're baked into the prebuild.

Two install approaches are provided. Pick **one**:

| Approach | File to use | Best when |
|---|---|---|
| **Image build (recommended)** | `devcontainer.json` + `Dockerfile` | You want the install cached in prebuilds and full converter support (audio/OCR via ffmpeg & poppler). |
| **Lifecycle command** | rename `devcontainer.alternative-no-dockerfile.json` → `devcontainer.json` | You want a simpler, Dockerfile-free setup. |

The **Azure CLI** and **Bicep** are installed the same way in both configs — via
the official `azure-cli` dev container Feature, so they're included in the
prebuild regardless of which approach you pick.

Both use **`onCreateCommand`** (not `postCreateCommand`) so the install is part
of the **prebuild snapshot** and codespaces start in seconds.

---

## How to use this template

1. **Copy the `.devcontainer/` folder** into your repository (or use this repo
   as a [template repository](https://docs.github.com/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)).
2. **Commit and push** to your default branch. That's it — the config is now
   *Configuration-as-Code* and applies to everyone.
3. **(Recommended) Enable a prebuild:** repo **Settings → Codespaces → Prebuilds → Set up prebuild**.
   - Select the branch (usually `main`)
   - Trigger: *on push* (or on configuration change)
   - Restrict to the region(s) where your team works (controls storage cost)
4. **Open a codespace:** green **Code** button → **Codespaces** tab → **Create codespace**.
   When a prebuild is available you'll see a **"Prebuild ready"** label.

---

## Verify it works (inside the codespace)

```bash
markitdown --version

# Convert a file to Markdown
markitdown sample.pdf -o sample.md

# Print Markdown to stdout
markitdown report.docx

# Azure CLI + Bicep
az version
bicep --version

# AWS CLI
aws --version

# Terraform + tfsec
terraform version
tfsec --version

# Sign in to Azure (device-code flow works well in a browser-based codespace)
az login --use-device-code
```

> **Azure auth tip:** in a cloud codespace, use `az login --use-device-code`
> rather than the default browser redirect. For automation, prefer a
> service principal or Azure managed identity over storing credentials in the
> codespace.
>
> **AWS auth tip:** avoid hard-coding access keys in the codespace. Prefer
> `aws configure sso` (IAM Identity Center) or short-lived credentials, and
> store any secrets as [Codespaces secrets](https://docs.github.com/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces)
> (Settings → Codespaces → Secrets) rather than committing them.
>
> **Terraform tip:** keep state in a remote backend (Azure Storage / Amazon S3),
> not inside the codespace — codespaces are disposable.

---

## Customizing the install

**Lighter image (smaller storage footprint):** `markitdown[all]` pulls in OCR
and audio dependencies. If you only need Office + PDF, edit the `Dockerfile`
(or the `onCreateCommand`) to install only what you need:

```bash
pip install 'markitdown[pdf,docx,pptx,xlsx]'
```

**Expose MarkItDown to AI tools (optional):** MarkItDown ships an MCP server.
Add to the `Dockerfile`:

```dockerfile
RUN pip install --no-cache-dir markitdown-mcp
```

---

## Cost notes (for budget-conscious teams)

- **Storage** for the image/prebuild is billed at **$0.07/GB-month**. The
  `[all]` extras and system packages increase image size — trim them if you
  don't need audio/OCR.
- **Prebuilds** consume **GitHub Actions minutes** to generate/update. Limit
  prebuilds to the branches that need them and to fewer regions.
- **Stop idle codespaces** (set an idle timeout) so compute isn't billed while
  unused. Storage continues until the codespace is deleted.

---

## References

- MarkItDown — https://github.com/microsoft/markitdown
- Dev container `devcontainer.json` reference — https://containers.dev/implementors/json_reference/
- Codespaces prebuilds — https://docs.github.com/codespaces/prebuilding-your-codespaces
