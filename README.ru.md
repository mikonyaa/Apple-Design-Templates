# Apple Design Templates

Профессиональная витрина независимых SwiftUI-шаблонов для Apple-платформ. Это каталог, а не monorepo: у каждого проекта есть отдельный package, запускаемый Xcode demo, документация, тесты, issues, CI и собственная история релизов.

## Коллекция

### Liquid Glass Tab Bars

**Stable 1.0.2 · iOS 17+ · Swift 6**

Нативный, floating и morphing tab bar для существующего приложения. Custom-варианты рассчитаны на 2–5 основных разделов; для большего количества используется системный `TabView`.

[Репозиторий](https://github.com/mikonyaa/LiquidGlassTabBars) · [Release](https://github.com/mikonyaa/LiquidGlassTabBars/releases/latest) · [Документация](https://github.com/mikonyaa/LiquidGlassTabBars/tree/main/Docs)

### Adaptive App Shell

**Stable 1.0.2 · iOS 17+ · Swift 6**

Общая навигационная модель: bottom tabs на iPhone, sidebar и опциональный inspector на iPad, независимые route paths и enum-based deep links.

[Репозиторий](https://github.com/mikonyaa/AdaptiveAppShell) · [Release](https://github.com/mikonyaa/AdaptiveAppShell/releases/latest) · [Документация](https://github.com/mikonyaa/AdaptiveAppShell/tree/main/Docs)

### Live Activity & Dynamic Island Kit

**Preview · Unreleased · iOS 17+ · Swift 6**

Domain-neutral rendering core для Lock Screen и Dynamic Island с полноценным app-specific ActivityKit/WidgetKit demo. Первый release остаётся заблокирован до проверки start/update/end на физическом устройстве.

[Репозиторий](https://github.com/mikonyaa/LiveActivityDynamicIslandKit) · [Документация](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/tree/main/Docs)

### Mac Menu Bar Command Kit

**Published 0.1.0 · macOS 14+ · Swift 6**

Keyboard-first shell для menu bar утилит: `MenuBarExtra`, обычное окно, command palette, Settings, Launch at Login и реальные clipboard workflows.

[Репозиторий](https://github.com/mikonyaa/MacMenuBarCommandKit) · [Release](https://github.com/mikonyaa/MacMenuBarCommandKit/releases/latest) · [Документация](https://github.com/mikonyaa/MacMenuBarCommandKit/tree/main/Docs)

## Как выбрать

- Нужен tab bar в существующем приложении — **Liquid Glass Tab Bars**.
- Нужна навигационная основа нового iPhone/iPad продукта — **Adaptive App Shell**.
- Нужен glanceable status вне приложения — **Live Activity & Dynamic Island Kit**.
- Нужна сфокусированная Mac menu bar утилита — **Mac Menu Bar Command Kit**.

## Стандарт коллекции

- Swift Package без сторонних runtime-зависимостей.
- Запускаемый Xcode demo-проект с deterministic local data.
- Accessibility-поведение и практичные fallbacks.
- Tests, CI, changelog и честная release-история.
- Архитектурная, integration и customization документация.
- Превью из реального demo, без fictional mockups.

Новые проекты появляются в каталоге только после полной проверки. Реализация и подробные инструкции остаются в соответствующих репозиториях.

**[Открыть основную визуальную витрину](README.md)**
