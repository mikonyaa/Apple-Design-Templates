# Catalog evidence

Release metadata and source reviewed on **2026-10-14**. Dates use Asia/Almaty.

The public release, the versioned source, the linked upstream CI, and independent runtime acceptance are separate facts. A source review establishes what the source declares; a CI success establishes only the workflow scope. No device, pilot, production, or independent Gatekeeper check is claimed by this catalog.

| Product | Release | Immutable source | Review type |
| --- | --- | --- | --- |
| [Liquid Glass Tab Bars](#liquid-glass-tab-bars) | [1.0.3](https://github.com/mikonyaa/LiquidGlassTabBars/releases/tag/1.0.3) | [828ded25395e](https://github.com/mikonyaa/LiquidGlassTabBars/tree/828ded25395e66fa7640d496ecc18cc83e6b1777) | source-review |
| [Adaptive App Shell](#adaptive-app-shell) | [1.0.3](https://github.com/mikonyaa/AdaptiveAppShell/releases/tag/1.0.3) | [ed5cc9573a72](https://github.com/mikonyaa/AdaptiveAppShell/tree/ed5cc9573a7258cc2549125d538102c9029e753a) | source-review |
| [Live Activity & Dynamic Island Kit](#live-activity-dynamic-island-kit) | [0.1.0](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/releases/tag/0.1.0) | [f577568f4661](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/tree/f577568f466136e28da427e55aa639170fafbac6) | source-review |
| [Mac Menu Bar Command Kit](#mac-menu-bar-command-kit) | [0.2.0](https://github.com/mikonyaa/MacMenuBarCommandKit/releases/tag/0.2.0) | [ab43ae5d750f](https://github.com/mikonyaa/MacMenuBarCommandKit/tree/ab43ae5d750f1005ee3e704b3756f4af8c2b3a37) | source-review |
| [ResizeLint](#resizelint) | [1.0.0](https://github.com/mikonyaa/ResizeLint/releases/tag/1.0.0) | [cde1a7b5165c](https://github.com/mikonyaa/ResizeLint/tree/cde1a7b5165cd6dc225166e6e0a7614a32ebce28) | source-review |

<a name="liquid-glass-tab-bars"></a>

## Liquid Glass Tab Bars

- **Tag / SHA:** `1.0.3` / `828ded25395e66fa7640d496ecc18cc83e6b1777`.
- **Minimum OS:** iOS 17+; macOS 14+ (package).
- **Toolchain:** Swift 6.0; Xcode 26+ for native Liquid Glass.
- **Declared third-party Swift dependencies:** none in the reusable package manifest.

| Claim or limitation | Evidence | Verification type / date |
| --- | --- | --- |
| The source provides custom variants for 2–5 destinations, accessibility settings, and guarded iOS 26 styling. | [source](https://github.com/mikonyaa/LiquidGlassTabBars/blob/828ded25395e66fa7640d496ecc18cc83e6b1777/Package.swift) | source-review / 2026-10-14 |
| Use system navigation for more than five destinations. Earlier OS versions use fallbacks; device accessibility has not been independently checked here. | [demo-limit](https://github.com/mikonyaa/LiquidGlassTabBars/blob/828ded25395e66fa7640d496ecc18cc83e6b1777/README.md) | source-review / 2026-10-14 |

### Sources

- **release** · release-metadata · 2026-10-14: [source 1](https://github.com/mikonyaa/LiquidGlassTabBars/releases/tag/1.0.3) · [source 2](https://github.com/mikonyaa/LiquidGlassTabBars/tree/828ded25395e66fa7640d496ecc18cc83e6b1777)
- **source** · source-review · 2026-10-14: [source 1](https://github.com/mikonyaa/LiquidGlassTabBars/blob/828ded25395e66fa7640d496ecc18cc83e6b1777/Package.swift) · [source 2](https://github.com/mikonyaa/LiquidGlassTabBars/blob/828ded25395e66fa7640d496ecc18cc83e6b1777/README.md)
- **demo-limit** · source-review · 2026-10-14: [source 1](https://github.com/mikonyaa/LiquidGlassTabBars/blob/828ded25395e66fa7640d496ecc18cc83e6b1777/README.md)
- **ci** · published-ci · 2026-10-14: [source 1](https://github.com/mikonyaa/LiquidGlassTabBars/actions/runs/29193187211) · [source 2](https://github.com/mikonyaa/LiquidGlassTabBars/tree/828ded25395e66fa7640d496ecc18cc83e6b1777)

- **Preview provenance:** [existing catalog asset](https://github.com/mikonyaa/Apple-Design-Templates/blob/4828708e88c8410f1d870d6aef942058b1a56e42/Assets/liquid-glass-tab-bars.gif). Lossless frame `48`; original animation remains linked.
- **Preview scope:** an existing demo capture; appearance alone does not prove a complete workflow.

<a name="adaptive-app-shell"></a>

## Adaptive App Shell

- **Tag / SHA:** `1.0.3` / `ed5cc9573a7258cc2549125d538102c9029e753a`.
- **Minimum OS:** iOS 17+; macOS 14+ (package).
- **Toolchain:** Swift 6.0; Xcode 26+.
- **Declared third-party Swift dependencies:** none in the reusable package manifest.

| Claim or limitation | Evidence | Verification type / date |
| --- | --- | --- |
| The source includes per-destination navigation paths, enum-based deep links, and three semantic themes. | [source](https://github.com/mikonyaa/AdaptiveAppShell/blob/ed5cc9573a7258cc2549125d538102c9029e753a/Package.swift) | source-review / 2026-10-14 |
| The demo Create action only dismisses its sheet; it does not add or persist a project. Supply your own business model and persistence. | [demo-limit](https://github.com/mikonyaa/AdaptiveAppShell/blob/ed5cc9573a7258cc2549125d538102c9029e753a/Examples/AdaptiveShellDemo/AdaptiveShellDemo/StudioSheets.swift) | source-review / 2026-10-14 |

### Sources

- **release** · release-metadata · 2026-10-14: [source 1](https://github.com/mikonyaa/AdaptiveAppShell/releases/tag/1.0.3) · [source 2](https://github.com/mikonyaa/AdaptiveAppShell/tree/ed5cc9573a7258cc2549125d538102c9029e753a)
- **source** · source-review · 2026-10-14: [source 1](https://github.com/mikonyaa/AdaptiveAppShell/blob/ed5cc9573a7258cc2549125d538102c9029e753a/Package.swift) · [source 2](https://github.com/mikonyaa/AdaptiveAppShell/blob/ed5cc9573a7258cc2549125d538102c9029e753a/README.md)
- **demo-limit** · source-review · 2026-10-14: [source 1](https://github.com/mikonyaa/AdaptiveAppShell/blob/ed5cc9573a7258cc2549125d538102c9029e753a/Examples/AdaptiveShellDemo/AdaptiveShellDemo/StudioSheets.swift)
- **ci** · published-ci · 2026-10-14: [source 1](https://github.com/mikonyaa/AdaptiveAppShell/actions/runs/29193186473) · [source 2](https://github.com/mikonyaa/AdaptiveAppShell/tree/ed5cc9573a7258cc2549125d538102c9029e753a)

- **Preview provenance:** [existing catalog asset](https://github.com/mikonyaa/Apple-Design-Templates/blob/4828708e88c8410f1d870d6aef942058b1a56e42/Assets/adaptive-app-shell.gif). Lossless frame `60`; original animation remains linked.
- **Preview scope:** an existing demo capture; appearance alone does not prove a complete workflow.

<a name="live-activity-dynamic-island-kit"></a>

## Live Activity & Dynamic Island Kit

- **Tag / SHA:** `0.1.0` / `f577568f466136e28da427e55aa639170fafbac6`.
- **Minimum OS:** iOS 17+; macOS 14+ (package).
- **Toolchain:** Swift 6.0; Xcode 16.4+.
- **Declared third-party Swift dependencies:** none in the reusable package manifest.

| Claim or limitation | Evidence | Verification type / date |
| --- | --- | --- |
| The source contains Lock Screen and compact, minimal, expanded Dynamic Island views plus start, update, recovery, and end examples. | [source](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/blob/f577568f466136e28da427e55aa639170fafbac6/Package.swift) | source-review / 2026-10-14 |
| Selecting another scenario can update content while the active activity keeps its original attributes. End and restart the activity when changing scenario; device lifecycle is unverified here. | [demo-limit](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/blob/f577568f466136e28da427e55aa639170fafbac6/Examples/LiveActivityDemo/LiveActivityDemo/LiveActivityDemoController.swift) | source-review / 2026-10-14 |

### Sources

- **release** · release-metadata · 2026-10-14: [source 1](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/releases/tag/0.1.0) · [source 2](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/tree/f577568f466136e28da427e55aa639170fafbac6)
- **source** · source-review · 2026-10-14: [source 1](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/blob/f577568f466136e28da427e55aa639170fafbac6/Package.swift) · [source 2](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/blob/f577568f466136e28da427e55aa639170fafbac6/README.md)
- **demo-limit** · source-review · 2026-10-14: [source 1](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/blob/f577568f466136e28da427e55aa639170fafbac6/Examples/LiveActivityDemo/LiveActivityDemo/LiveActivityDemoController.swift)
- **ci** · published-ci · 2026-10-14: [source 1](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/actions/runs/29208578871) · [source 2](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/tree/f577568f466136e28da427e55aa639170fafbac6)

- **Preview provenance:** [existing catalog asset](https://github.com/mikonyaa/Apple-Design-Templates/blob/4828708e88c8410f1d870d6aef942058b1a56e42/Assets/live-activity-dynamic-island-kit.png).
- **Preview scope:** an existing demo capture; appearance alone does not prove a complete workflow.

<a name="mac-menu-bar-command-kit"></a>

## Mac Menu Bar Command Kit

- **Tag / SHA:** `0.2.0` / `ab43ae5d750f1005ee3e704b3756f4af8c2b3a37`.
- **Minimum OS:** macOS 14+.
- **Toolchain:** Swift 6.0; Xcode 26+.
- **Declared third-party Swift dependencies:** none in the reusable package manifest.

| Claim or limitation | Evidence | Verification type / date |
| --- | --- | --- |
| The source includes MenuBarExtra, a main window, command palette, Settings, Launch at Login integration, and clipboard handlers. | [source](https://github.com/mikonyaa/MacMenuBarCommandKit/blob/ab43ae5d750f1005ee3e704b3756f4af8c2b3a37/Package.swift) | source-review / 2026-10-14 |
| Start Timer increments focus minutes and sets a flag; it does not measure elapsed time. Implement a real timer in the app. | [demo-limit](https://github.com/mikonyaa/MacMenuBarCommandKit/blob/ab43ae5d750f1005ee3e704b3756f4af8c2b3a37/Examples/CommandKitDemo/CommandKitDemo/App/DemoCommandCatalog.swift) | source-review / 2026-10-14 |

### Sources

- **release** · release-metadata · 2026-10-14: [source 1](https://github.com/mikonyaa/MacMenuBarCommandKit/releases/tag/0.2.0) · [source 2](https://github.com/mikonyaa/MacMenuBarCommandKit/tree/ab43ae5d750f1005ee3e704b3756f4af8c2b3a37)
- **source** · source-review · 2026-10-14: [source 1](https://github.com/mikonyaa/MacMenuBarCommandKit/blob/ab43ae5d750f1005ee3e704b3756f4af8c2b3a37/Package.swift) · [source 2](https://github.com/mikonyaa/MacMenuBarCommandKit/blob/ab43ae5d750f1005ee3e704b3756f4af8c2b3a37/README.md)
- **demo-limit** · source-review · 2026-10-14: [source 1](https://github.com/mikonyaa/MacMenuBarCommandKit/blob/ab43ae5d750f1005ee3e704b3756f4af8c2b3a37/Examples/CommandKitDemo/CommandKitDemo/App/DemoCommandCatalog.swift)
- **ci** · published-ci · 2026-10-14: [source 1](https://github.com/mikonyaa/MacMenuBarCommandKit/actions/runs/29193185600) · [source 2](https://github.com/mikonyaa/MacMenuBarCommandKit/tree/ab43ae5d750f1005ee3e704b3756f4af8c2b3a37)

- **Preview provenance:** [existing catalog asset](https://github.com/mikonyaa/Apple-Design-Templates/blob/4828708e88c8410f1d870d6aef942058b1a56e42/Assets/mac-menu-bar-command-kit.png).
- **Preview scope:** an existing demo capture; appearance alone does not prove a complete workflow.

<a name="resizelint"></a>

## ResizeLint

- **Tag / SHA:** `1.0.0` / `cde1a7b5165cd6dc225166e6e0a7614a32ebce28`.
- **Minimum OS:** macOS 14+; Ubuntu 22.04+ x86_64 with Swift runtime.
- **Toolchain:** Swift 6.3.3 (source build).
- **Declared third-party Swift dependencies:** SwiftSyntax, ArgumentParser, Yams.

| Claim or limitation | Evidence | Verification type / date |
| --- | --- | --- |
| The source defines nine rules, human/Xcode/JSON/SARIF output, and a checksum-verifying Action. Source stays local during analysis. | [source](https://github.com/mikonyaa/ResizeLint/blob/cde1a7b5165cd6dc225166e6e0a7614a32ebce28/Package.swift) | source-review / 2026-10-14 |
| The published Linux 1.0.0 archive needs Swift shared libraries including libswiftCore.so; a clean Ubuntu install alone is insufficient. macOS signing/notarization is evidenced by release CI, not an independent Gatekeeper check in this catalog. | [demo-limit](https://github.com/mikonyaa/ResizeLint/blob/cde1a7b5165cd6dc225166e6e0a7614a32ebce28/Package.swift); [linux-artifact](https://github.com/mikonyaa/ResizeLint/releases/download/1.0.0/ResizeLint-1.0.0-linux-x86_64.tar.gz); [ci](https://github.com/mikonyaa/ResizeLint/actions/runs/29513460101) | artifact-inspection, published-ci, source-review / 2026-10-14 |

### Sources

- **release** · release-metadata · 2026-10-14: [source 1](https://github.com/mikonyaa/ResizeLint/releases/tag/1.0.0) · [source 2](https://github.com/mikonyaa/ResizeLint/tree/cde1a7b5165cd6dc225166e6e0a7614a32ebce28)
- **source** · source-review · 2026-10-14: [source 1](https://github.com/mikonyaa/ResizeLint/blob/cde1a7b5165cd6dc225166e6e0a7614a32ebce28/Package.swift) · [source 2](https://github.com/mikonyaa/ResizeLint/blob/cde1a7b5165cd6dc225166e6e0a7614a32ebce28/README.md)
- **demo-limit** · source-review · 2026-10-14: [source 1](https://github.com/mikonyaa/ResizeLint/blob/cde1a7b5165cd6dc225166e6e0a7614a32ebce28/Package.swift)
- **ci** · published-ci · 2026-10-14: [source 1](https://github.com/mikonyaa/ResizeLint/actions/runs/29513460101) · [source 2](https://github.com/mikonyaa/ResizeLint/tree/cde1a7b5165cd6dc225166e6e0a7614a32ebce28)
- **linux-artifact** · artifact-inspection · 2026-10-14: [source 1](https://github.com/mikonyaa/ResizeLint/releases/download/1.0.0/ResizeLint-1.0.0-linux-x86_64.tar.gz) · [source 2](https://github.com/mikonyaa/ResizeLint/tree/cde1a7b5165cd6dc225166e6e0a7614a32ebce28)
  Archive SHA-256: `4d1a116520e901076920262f7059a737d4af538738cdae4f8e1ff29df4a24225`.

- **Preview provenance:** [existing catalog asset](https://github.com/mikonyaa/Apple-Design-Templates/blob/4828708e88c8410f1d870d6aef942058b1a56e42/Assets/resizelint-terminal.svg).
- **Preview scope:** appearance only. The ResizeLint SVG is a terminal illustration, not execution evidence.

## ResizeLint distribution boundary

The published 1.0.0 Linux archive was re-downloaded and matched SHA-256 `4d1a116520e901076920262f7059a737d4af538738cdae4f8e1ff29df4a24225`. ELF inspection identifies Swift shared-library dependencies including `libswiftCore.so`. A bare Ubuntu version is therefore insufficient. This catalog update does not execute the ELF on Linux; the earlier runtime audit reported exit 127 without Swift libraries.

The macOS release workflow includes signing, notarization, stapling, signature checks, and Gatekeeper assessment. The linked successful release run is **upstream CI evidence**. Downloaded macOS artifacts have not received an independent Gatekeeper assessment in this catalog update.

Unreleased upstream branches and local release candidates are not substitutes for published versions. Re-check these limitations when selecting a later release.
