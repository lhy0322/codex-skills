# Codex Skills

This repository stores reusable Codex skills. Each skill is a self-contained folder with its own `SKILL.md`, optional UI metadata, and optional bundled resources.

## Layout

```text
skills/
+-- README.md
+-- top-journal-3d-genome-writing/
|   +-- SKILL.md
|   +-- agents/
|   |   +-- openai.yaml
|   +-- references/
|   +-- scripts/
+-- another-skill/
    +-- SKILL.md
    +-- agents/
    +-- references/
    +-- scripts/
    +-- assets/
```

## Skills

| Skill | Purpose |
| --- | --- |
| `top-journal-3d-genome-writing` | Draft, polish, review, and plan figures for top-tier 3D genome and computational genomics papers. |

## Skill Folder Rules

Each skill should be independent and easy for Codex to load:

- `SKILL.md` is required and must contain YAML frontmatter with `name` and `description`.
- `agents/openai.yaml` is recommended for display name, short description, and default prompt.
- `references/` stores detailed guidance that Codex should load only when needed.
- `scripts/` stores reusable utilities that can be executed directly.
- `assets/` stores templates, images, fonts, or other files used in outputs.

Avoid adding extra documentation inside individual skill folders unless it is directly used by the skill. Keep general notes in this root `README.md`.

## Naming

Use short lowercase names with hyphens:

```text
top-journal-3d-genome-writing
scientific-figure-planner
bioinformatics-paper-reviewer
```

## Installation

Codex auto-discovers skills placed under:

```text
C:\Users\HP\.codex\skills
```

To install a skill from this repository, copy the skill folder into that directory. For example:

```powershell
Copy-Item -Recurse -Force .\top-journal-3d-genome-writing C:\Users\HP\.codex\skills\
```

Then invoke it in a prompt:

```text
Use $top-journal-3d-genome-writing to plan a Nature Methods-style 3D genome manuscript and main figures.
```

## Validation

Validate a skill before publishing:

```powershell
python C:\Users\HP\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\HP\.codex\skills\top-journal-3d-genome-writing
```

If `quick_validate.py` reports a missing Python dependency such as `yaml`, install the dependency in the Python environment used for validation or run the check in an environment where `PyYAML` is available.

## Maintenance

When updating a skill:

1. Keep the `description` accurate because it controls when Codex uses the skill.
2. Keep `SKILL.md` concise and move detailed guidance into `references/`.
3. Test any script in `scripts/` after editing it.
4. Update `agents/openai.yaml` if the display name, short description, or default prompt becomes stale.
5. Prefer one repository for many related skills; split a skill into its own repository only when it needs independent versioning, permissions, or heavy assets.
