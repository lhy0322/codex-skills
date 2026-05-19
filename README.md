# Codex Skills

Reusable Codex skills for scientific writing, figure planning, and domain-specific research workflows.

## Skills

| Skill | Purpose |
| --- | --- |
| `top-journal-3d-genome-writing` | Draft, polish, review, and plan figures for top-tier 3D genome and computational genomics papers. |

## Repository Layout

```text
codex-skills/
+-- README.md
+-- top-journal-3d-genome-writing/
    +-- SKILL.md
    +-- agents/
    |   +-- openai.yaml
    +-- references/
    +-- scripts/
```

## Installation

Clone this repository:

```powershell
git clone https://github.com/lhy0322/codex-skills.git
cd codex-skills
```

Copy a skill folder into your local Codex skills directory:

```powershell
Copy-Item -Recurse -Force .\top-journal-3d-genome-writing C:\Users\HP\.codex\skills\
```

On macOS or Linux, use:

```bash
cp -R ./top-journal-3d-genome-writing ~/.codex/skills/
```

## Usage

Invoke a skill by name in Codex:

```text
Use $top-journal-3d-genome-writing to plan a Nature Methods-style 3D genome manuscript and main figures.
```

More examples:

```text
Use $top-journal-3d-genome-writing to redesign Figure 1-6 for my 3D genome paper.
```

```text
Use $top-journal-3d-genome-writing to review whether my manuscript has enough top-journal evidence.
```

```text
Use $top-journal-3d-genome-writing to polish this Results section for a Genome Biology-style paper.
```

## Skill Folder Rules

Each skill should be self-contained:

- `SKILL.md` is required and must include `name` and `description` in YAML frontmatter.
- `agents/openai.yaml` is recommended for display metadata.
- `references/` stores detailed guidance loaded only when needed.
- `scripts/` stores reusable utilities.
- `assets/` stores templates, images, or other output resources.

Avoid adding unnecessary files inside individual skill folders. General documentation belongs in this root `README.md`.

## Validation

Validate a skill before publishing:

```powershell
python C:\Users\HP\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\HP\.codex\skills\top-journal-3d-genome-writing
```

If validation fails because `yaml` is missing, install `PyYAML` in the Python environment used for validation.

## Maintenance

When updating a skill:

1. Keep the `description` in `SKILL.md` accurate, because it controls when Codex uses the skill.
2. Keep `SKILL.md` concise and move detailed guidance into `references/`.
3. Test scripts in `scripts/` after editing.
4. Update `agents/openai.yaml` when display metadata changes.
5. Prefer one repository for related skills; split into separate repositories only for independent versioning, permissions, or heavy assets.

## License

Add a license if you plan to share these skills publicly.
