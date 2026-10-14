# Maintaining the catalog

`catalog.json` owns the five product records: role, URL, release tag, immutable commit, OS and toolchain, selection scenario, limits, claim evidence, preview provenance, and support routes. Text fields contain English and Russian together. Python 3.10+ and the standard library are sufficient.

## One local gate

```sh
python3 Scripts/verify-catalog.py
python3 Scripts/test-verify-catalog.py
```

The first command checks the manifest schema, five unique slugs and roles, safe existing local paths, generated EN/RU sections, evidence references, support/security routes, responsive README structure, tracked-file hygiene, and the union of local images embedded in either README. The second uses disposable copies to prove broken tags, missing previews, language drift, absent routes, excess media bytes, and unsupported claims fail the gate.

**Offline PASS is an integrity check**, not a new GitHub release check, native build, device test, signing check, or proof that the demo works end to end. A valid-looking nonexistent release must be checked online.

```sh
python3 Scripts/verify-catalog.py --online
```

This read-only mode queries each exact GitHub release and resolves its tag to the immutable commit. It also reports a newer published release if present. Set `GITHUB_TOKEN` in your environment only when needed for rate limits; the script never prints it. `--network-timeout` controls seconds per request.

| Exit | Meaning |
| --- | --- |
| 0 | The requested checks passed within their stated scope. |
| 1 | Invalid local facts or a verified remote release/tag/SHA mismatch. |
| 2 | Online verification is incomplete: network, service, authentication, or rate limit unavailable. Output says UNVERIFIED. |

Network failures never rewrite facts or become ONLINE PASS. `--api-base` exists for a controlled offline failure fixture; use the default GitHub API for a real verification.

## Updating a version

1. Inspect the published release and resolve its tag to a commit. Do not replace a release with an unreleased branch or a local candidate.
2. Review that commit's package requirements, dependencies, relevant demo handlers, distribution artifacts, CI scope, and current security policy. Re-evaluate old limitations instead of copying them indefinitely.
3. Edit the product in `catalog.json`. Keep evidence URLs at immutable SHAs; a release label alone does not prove behavior. Set the new review date and match each claim or limitation to an evidence ID. Actual device/signing claims require independent evidence of that type.
4. Run `python3 Scripts/render-catalog.py` to update the manifest-owned README sections and evidence reference. Handwritten introduction and maintenance prose remain outside the marked regions.
5. Run both offline commands, the online mode, and `git diff --check`. Review EN/RU meaning, individual previews, and the README at 390/1280 CSS px in light/dark. A compatible local preview is preparation; inspect the exact GitHub render after publication.
6. Publish a narrow reviewable change, preserving concurrent work. Record the exact commit's CI result separately from upstream runtime acceptance.

## Media budget

The baseline is catalog commit `4828708e88c8410f1d870d6aef942058b1a56e42`. Its embedded PNG/GIF set totals **8,835,016 bytes**. The ResizeLint SVG adds **3,055 bytes**, so all original embedded local files total **8,838,071 bytes**.

| Displayed file | Before bytes | After bytes |
| --- | ---: | ---: |
| Banner PNG | 85,061 | 85,061 |
| Liquid Glass GIF → PNG poster, frame 48 | 2,566,851 | 102,662 |
| Adaptive GIF → PNG poster, frame 60 | 4,387,038 | 99,027 |
| Live Activity PNG | 389,496 | 389,496 |
| Mac command PNG | 1,406,570 | 1,406,570 |
| ResizeLint SVG | 3,055 | 3,055 |
| **All embedded local files** | **8,838,071** | **2,085,871** |

The current set is **76.4% smaller by bytes**. The gate measures unique files used by either language, including SVG, against **5,301,009 bytes**, the requested 60% raster-baseline cap rounded down. The Russian page reuses the same preview files, so they are counted once. Remote page chrome, network speed, and GitHub transfer behavior are not measured by this byte comparison.

Posters retain the full 400×870 decoded GIF frame, saved losslessly. The original animations remain intact and are loaded when explicitly opened. They are not embedded in the README. Reproduce the posters with FFmpeg:

```sh
ffmpeg -i Assets/liquid-glass-tab-bars.gif -vf 'select=eq(n\,48)' -frames:v 1 Assets/liquid-glass-tab-bars-poster.png
ffmpeg -i Assets/adaptive-app-shell.gif -vf 'select=eq(n\,60)' -frames:v 1 Assets/adaptive-app-shell-poster.png
```

FFmpeg is only needed to recreate posters; neither local validation nor CI needs it. A different encoder can produce different PNG bytes. Update the measurement table after a deliberate media change and keep the cap enforced.

The catalog's ResizeLint SVG is a terminal illustration. It supports orientation, not a claim that its depicted result was executed.
