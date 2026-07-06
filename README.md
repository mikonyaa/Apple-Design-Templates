<div align="center">
  <h1>Apple Design Templates</h1>
  <p><strong>High-quality SwiftUI templates for iOS, iPadOS, and macOS.</strong></p>
  <p>Focused, documented, and ready to adapt for real products.</p>
  <p>Created by <a href="https://github.com/mikonyaa"><strong>miko.os</strong></a></p>
  <p>
    <a href="https://www.swift.org"><img alt="Swift 6" src="https://img.shields.io/badge/Swift-6.0-F05138?logo=swift&logoColor=white"></a>
    <a href="https://developer.apple.com/xcode/swiftui/"><img alt="SwiftUI" src="https://img.shields.io/badge/SwiftUI-Native-0A7AFF?logo=swift&logoColor=white"></a>
    <img alt="iOS" src="https://img.shields.io/badge/iOS-17%2B-111111?logo=apple">
    <img alt="iPadOS" src="https://img.shields.io/badge/iPadOS-Adaptive-111111?logo=apple">
    <img alt="macOS" src="https://img.shields.io/badge/macOS-Planned-6E6E73?logo=apple">
    <a href="#templates"><img alt="Templates" src="https://img.shields.io/badge/Templates-2-0A7AFF"></a>
    <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/License-MIT-2EA44F"></a>
  </p>
  <p><a href="README.ru.md">Русская версия</a></p>
</div>

---

Apple Design Templates is a curated collection of production-oriented SwiftUI starting points. Every template is a focused, independent repository with reusable source code, a runnable Xcode demo, accessibility support, tests, documentation, screenshots, and a reproducible preview.

## Table of contents

- [Templates](#templates)
- [Choose the right starting point](#choose-the-right-starting-point)
- [Quality baseline](#quality-baseline)
- [How to use a template](#how-to-use-a-template)
- [Who this is for](#who-this-is-for)
- [Repository model](#repository-model)
- [Planned template areas](#planned-template-areas)
- [Contributing and support](#contributing-and-support)
- [Author](#author)
- [License](#license)

## Templates

| Template | Platforms | Stable release | Repository |
| --- | --- | --- | --- |
| Liquid Glass Tab Bars | iOS, iPadOS | `1.0.0` | [Open repository](https://github.com/mikonyaa/LiquidGlassTabBars) |
| Adaptive App Shell | iOS, iPadOS | `1.0.0` | [Open repository](https://github.com/mikonyaa/AdaptiveAppShell) |

### 01 · Liquid Glass Tab Bars

[![Liquid Glass Tab Bars preview](Assets/liquid-glass-tab-bars.gif)](https://github.com/mikonyaa/LiquidGlassTabBars)

Native, floating, and morphing SwiftUI tab bars with iOS 26 Liquid Glass and readable iOS 17–25 fallbacks.

- Native `TabView` and two reusable custom interactions
- Zero-dependency `LiquidUI` Swift Package
- Dynamic Type, Reduce Motion, and Reduce Transparency support
- Four component themes and restrained demo backgrounds

**[Repository](https://github.com/mikonyaa/LiquidGlassTabBars)** · **[Documentation](https://github.com/mikonyaa/LiquidGlassTabBars/tree/main/Docs)** · **[Latest release](https://github.com/mikonyaa/LiquidGlassTabBars/releases/latest)**

### 02 · Adaptive App Shell

[![Adaptive App Shell preview](Assets/adaptive-app-shell.gif)](https://github.com/mikonyaa/AdaptiveAppShell)

One navigation architecture that presents bottom tabs on iPhone and a sidebar with an optional inspector on iPad.

- Independent navigation history for every destination
- Compact tabs, regular-width sidebar, and sidebar-only collections
- Optional contextual inspector and enum-based deep links
- Three semantic, gradient-free themes

**[Repository](https://github.com/mikonyaa/AdaptiveAppShell)** · **[Documentation](https://github.com/mikonyaa/AdaptiveAppShell/tree/main/Docs)** · **[Latest release](https://github.com/mikonyaa/AdaptiveAppShell/releases/latest)**

## Choose the right starting point

| Need | Start with |
| --- | --- |
| Add a polished tab bar to an existing app | [Liquid Glass Tab Bars](https://github.com/mikonyaa/LiquidGlassTabBars) |
| Establish the navigation structure of a new iPhone and iPad app | [Adaptive App Shell](https://github.com/mikonyaa/AdaptiveAppShell) |
| Learn how modern SwiftUI navigation and glass controls are built | Open either demo and use its beginner learning prompt |

## Quality baseline

Every published template is expected to include:

- A reusable Swift Package without third-party runtime dependencies
- A runnable Xcode demo with deterministic local data
- iPhone and iPad review where the component supports both
- Practical fallbacks for supported pre-iOS 26 systems
- Dynamic Type, VoiceOver, contrast, motion, and transparency considerations
- Unit tests, GitHub Actions, versioned releases, and an MIT license
- Architecture, integration, customization, and beginner documentation
- Simulator screenshots and a preview GIF generated from the real demo

## How to use a template

1. Open the template repository and review its requirements.
2. Download the latest release or clone the repository.
3. Run the included demo before copying or customizing code.
4. Add the Swift Package to your project using the repository URL.
5. Read `Docs/Architecture.md` before changing state ownership or navigation behavior.

Each template also contains `Docs/LearningPrompt.md`. Give that prompt to an AI assistant when you want a file-by-file explanation written for a beginner and grounded in the actual source code.

## Who this is for

- iOS developers who want a reliable starting point instead of an isolated snippet
- SwiftUI beginners who learn best from complete, runnable examples
- Indie developers building polished applications with a small team
- Designers learning how Apple-style interfaces map to native SwiftUI
- Experienced engineers who want focused packages they can quickly adapt

## Repository model

This repository is the collection catalog. Template source code stays in separate repositories so each project has focused Issues, Releases, documentation, semantic versions, and a clean Swift Package URL. New templates will be added here only after their own repository is ready to use.

```text
Apple-Design-Templates/
├── .github/ISSUE_TEMPLATE/    Collection-level proposals
├── Assets/                    Optimized showcase previews
├── CONTRIBUTING.md            Contribution scope and quality bar
├── README.md                  English catalog
├── README.ru.md               Russian catalog summary
├── SECURITY.md                Private reporting routes
└── LICENSE                    Catalog license
```

## Planned template areas

- Onboarding and first-run experiences
- Settings and account surfaces
- Search, filtering, and command interfaces
- Empty, loading, error, and offline states
- Paywalls and StoreKit presentation patterns
- macOS menu bar and multi-window templates
- Widgets, Live Activities, watchOS, and visionOS experiments

The roadmap is directional. Small finished templates take priority over a large unfinished component library.

## Contributing and support

Open bugs and implementation questions in the repository for the affected template. Use this catalog for collection-level proposals only. See [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a new template.

If this collection helps you build a better Apple-platform app, consider starring the catalog or the template you used. Stars help other developers find the projects without changing the technical direction of the collection.

## Author

Created and maintained by [miko.os](https://github.com/mikonyaa). Product questions and bug reports belong in the relevant repository so solutions remain searchable for everyone.

## License

The catalog is available under the [MIT License](LICENSE). Each template repository includes its own license. Apple, Swift, SwiftUI, iPhone, iPad, and macOS are trademarks of Apple Inc. This project is not affiliated with or endorsed by Apple.
