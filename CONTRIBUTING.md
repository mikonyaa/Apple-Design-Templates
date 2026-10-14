# Contributing

Thank you for helping improve Apple Design Templates.

## Where to open an issue

- Report implementation bugs and integration questions in the affected project repository:
  [Liquid Glass Tab Bars](https://github.com/mikonyaa/LiquidGlassTabBars/issues/new/choose),
  [Adaptive App Shell](https://github.com/mikonyaa/AdaptiveAppShell/issues/new/choose),
  [Live Activity & Dynamic Island Kit](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/issues/new/choose), or
  [Mac Menu Bar Command Kit](https://github.com/mikonyaa/MacMenuBarCommandKit/issues/new/choose), or
  [ResizeLint](https://github.com/mikonyaa/ResizeLint/issues/new/choose).
- Use this catalog for collection structure, broken catalog links, EN/RU consistency, and proposals for a standalone template or tool.
- Report security concerns using the affected project's policy listed in [SECURITY.md](SECURITY.md). ResizeLint's policy describes a fallback when private reporting is unavailable.

## Proposing a template

A useful proposal explains:

1. The recurring product or engineering problem.
2. Why a reusable template is better than a short code snippet.
3. Supported Apple platforms and minimum OS versions.
4. Expected compact and regular-width behavior.
5. Accessibility and fallback requirements.
6. What belongs in the reusable package and what belongs only in the demo.

New templates should remain focused. A small, complete repository is preferred over a broad unfinished component library.

## Pull requests

Keep catalog changes narrow and use clear commit messages. Update `catalog.json`, run `python3 Scripts/render-catalog.py`, then run `python3 Scripts/verify-catalog.py` and `python3 Scripts/test-verify-catalog.py`. Use the explicit `--online` mode to check release tags and immutable commits before changing a version. See [catalog maintenance](Docs/Catalog-maintenance.md) for the evidence and media checks.

Do not add generated build data, credentials, personal data, or application-specific source code.
