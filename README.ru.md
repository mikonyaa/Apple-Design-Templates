# Apple Design Templates

Профессиональная витрина независимых SwiftUI-шаблонов и сфокусированных инструментов для Apple-платформ. Это каталог, а не monorepo: у каждого проекта есть собственные исходники, воспроизводимое demo или CLI-evidence, документация, тесты, issues, CI и история релизов.

## Коллекция

### Liquid Glass Tab Bars

**Stable 1.0.3 · iOS 17+ · Swift 6**

Нативный, floating и morphing tab bar для существующего приложения. Custom-варианты рассчитаны на 2–5 основных разделов; для большего количества используется системный `TabView`.

[Репозиторий](https://github.com/mikonyaa/LiquidGlassTabBars) · [Release](https://github.com/mikonyaa/LiquidGlassTabBars/releases/latest) · [Документация](https://github.com/mikonyaa/LiquidGlassTabBars/tree/main/Docs)

### Adaptive App Shell

**Stable 1.0.3 · iOS 17+ · Swift 6**

Общая навигационная модель: bottom tabs на iPhone, sidebar и опциональный inspector на iPad, независимые route paths и enum-based deep links.

[Репозиторий](https://github.com/mikonyaa/AdaptiveAppShell) · [Release](https://github.com/mikonyaa/AdaptiveAppShell/releases/latest) · [Документация](https://github.com/mikonyaa/AdaptiveAppShell/tree/main/Docs)

### Live Activity & Dynamic Island Kit

**Released 0.1.0 · iOS 17+ · Swift 6 · Xcode 16.4+**

Domain-neutral rendering core для Lock Screen и Dynamic Island с polished Activity Lab, app-owned lifecycle, recovery после relaunch, exact deep links и light/dark appearance palettes.

[Репозиторий](https://github.com/mikonyaa/LiveActivityDynamicIslandKit) · [Release](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/releases/latest) · [Документация](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/tree/main/Docs)

### Mac Menu Bar Command Kit

**Published 0.2.0 · macOS 14+ · Swift 6**

Keyboard-first shell для menu bar утилит: `MenuBarExtra`, обычное окно, command palette, Settings, Launch at Login и реальные clipboard workflows.

[Репозиторий](https://github.com/mikonyaa/MacMenuBarCommandKit) · [Release](https://github.com/mikonyaa/MacMenuBarCommandKit/releases/latest) · [Документация](https://github.com/mikonyaa/MacMenuBarCommandKit/tree/main/Docs)

## Инструмент разработчика

### ResizeLint

**Stable 1.0.0 · macOS 14+ и Ubuntu 22.04+ · Swift 6 · CLI и GitHub Action**

Локальный детерминированный статический анализатор для UIKit- и Swift-предположений о размере экрана, сцене, idiom и orientation, которые ломаются в изменяемых окнах iPhone-приложений. ResizeLint остаётся отдельным developer tool и не входит в число четырёх дизайн-шаблонов.

- Девять high-confidence правил с human, Xcode, JSON и SARIF output.
- Исходники не покидают машину: нет account, daemon, telemetry или cloud service.
- Доступны checksum-verifying Action `mikonyaa/ResizeLint@v1`, подписанный и notarized universal macOS package и Linux x86_64 binary.

Установка проверенного macOS package из релиза `1.0.0`:

```bash
curl -fLO https://github.com/mikonyaa/ResizeLint/releases/download/1.0.0/ResizeLint-1.0.0-macos-universal.pkg
sudo installer -pkg ResizeLint-1.0.0-macos-universal.pkg -target /
resizelint version
```

[Репозиторий](https://github.com/mikonyaa/ResizeLint) · [Release 1.0.0](https://github.com/mikonyaa/ResizeLint/releases/tag/1.0.0) · [Правила](https://github.com/mikonyaa/ResizeLint/tree/1.0.0/Docs/Rules) · [CLI](https://github.com/mikonyaa/ResizeLint/blob/1.0.0/Docs/CLI.md)

## Как выбрать

- Нужен tab bar в существующем приложении — **Liquid Glass Tab Bars**.
- Нужна навигационная основа нового iPhone/iPad продукта — **Adaptive App Shell**.
- Нужен glanceable status вне приложения — **Live Activity & Dynamic Island Kit**.
- Нужна сфокусированная Mac menu bar утилита — **Mac Menu Bar Command Kit**.
- Нужно находить неадаптивные UIKit-предположения до runtime QA — **ResizeLint**.

## Стандарт коллекции

- Swift Package без сторонних runtime-зависимостей.
- Запускаемый Xcode demo-проект с deterministic local data.
- Accessibility-поведение и практичные fallbacks.
- Tests, CI, changelog и честная release-история.
- Архитектурная, integration и customization документация.
- Превью из реального demo, без fictional mockups.

Developer tools могут заменять Xcode demo воспроизводимыми CLI-fixtures, machine-readable output, checksums и distribution evidence; они не считаются дизайн-шаблонами.

Новые шаблоны и инструменты появляются в каталоге только после полной проверки. Реализация и подробные инструкции остаются в соответствующих репозиториях.

**[Открыть основную визуальную витрину](README.md)**
