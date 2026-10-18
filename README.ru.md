# Apple Design Templates

Четыре независимых SwiftUI-шаблона и один инструмент разработчика для Apple-платформ. У каждого проекта свои исходники, документация, issues, тесты и история релизов.

Выберите проект, изучите demo и ограничения, затем адаптируйте только нужную часть.

[English](README.md) · [MIT](LICENSE) · Автор: [miko](https://github.com/mikonyaa)

<!-- catalog:begin -->

## Как выбрать

- **Улучшить tab bar в существующем iOS-приложении** → [Liquid Glass Tab Bars](#liquid-glass-tab-bars) · 1.0.3
- **Создать навигационную основу нового iPhone/iPad-продукта** → [Adaptive App Shell](#adaptive-app-shell) · 1.0.3
- **Показывать краткий статус на Lock Screen и Dynamic Island** → [Live Activity & Dynamic Island Kit](#live-activity-dynamic-island-kit) · 0.1.0
- **Создать сфокусированную Mac menu bar утилиту** → [Mac Menu Bar Command Kit](#mac-menu-bar-command-kit) · 0.2.0
- **Находить неадаптивные Swift/UIKit-предположения до runtime QA** → [ResizeLint](#resizelint) · 1.0.0

Выбирайте минимальный package, который решает вашу задачу. Четыре UI-шаблона независимы; ResizeLint можно использовать отдельно.

**Released** означает опубликованный release с указанным tag. **Preview** — ещё не опубликованный или prerelease-проект. **Verified scope** указывает только реально проведённую проверку; source review и CI не подтверждают device или production behavior.

## Шаблоны

<a name="liquid-glass-tab-bars"></a>

### Liquid Glass Tab Bars

> **Released 1.0.3** · iOS 17+; macOS 14+ (package) · Swift 6.0; Xcode 26+ for native Liquid Glass

Три варианта tab bar с общей моделью выбора: системный, floating и morphing.

<p align="center">
  <a href="Assets/liquid-glass-tab-bars.gif">
    <img src="Assets/liquid-glass-tab-bars-poster.png" width="320" alt="Кадр реального demo: Home и системная навигация по вкладкам">
  </a>
</p>

[Посмотреть исходную анимацию](Assets/liquid-glass-tab-bars.gif)

**Когда достаточно более простого решения:** Если системного TabView достаточно, дополнительный package не требуется.

- В исходниках есть custom-варианты для 2–5 разделов, настройки accessibility и условное оформление iOS 26.

**Ограничения:**

- Для более пяти разделов используйте системную навигацию. На старых ОС действуют fallbacks; accessibility на устройстве здесь независимо не проверялась.

**Verified scope · source-review · 2026-10-14:** Release metadata и versioned source; ссылка на CI относится к upstream. Независимого device или production test нет.

[Репозиторий](https://github.com/mikonyaa/LiquidGlassTabBars) · [Release 1.0.3](https://github.com/mikonyaa/LiquidGlassTabBars/releases/tag/1.0.3) · [Документация версии](https://github.com/mikonyaa/LiquidGlassTabBars/tree/828ded25395e66fa7640d496ecc18cc83e6b1777/Docs) · [Доказательства и область проверки](Docs/Catalog-evidence.md#liquid-glass-tab-bars)

---

<a name="adaptive-app-shell"></a>

### Adaptive App Shell

> **Released 1.0.3** · iOS 17+; macOS 14+ (package) · Swift 6.0; Xcode 26+

Общая модель состояния для компактных tabs, sidebar на широком экране и опционального inspector.

<p align="center">
  <a href="Assets/adaptive-app-shell.gif">
    <img src="Assets/adaptive-app-shell-poster.png" width="320" alt="Кадр реального demo: iPhone overview и список проектов">
  </a>
</p>

[Посмотреть исходную анимацию](Assets/adaptive-app-shell.gif)

**Когда достаточно более простого решения:** Если существующему приложению нужен только tab bar, полноценный shell избыточен.

- В исходниках есть независимые navigation paths, deep links через enum и три семантические темы.

**Ограничения:**

- Create в demo только закрывает sheet: проект не добавляется и не сохраняется. Бизнес-модель и persistence нужно реализовать в приложении.

**Verified scope · source-review · 2026-10-14:** Release metadata и versioned source; ссылка на CI относится к upstream. Независимого device или production test нет.

[Репозиторий](https://github.com/mikonyaa/AdaptiveAppShell) · [Release 1.0.3](https://github.com/mikonyaa/AdaptiveAppShell/releases/tag/1.0.3) · [Документация версии](https://github.com/mikonyaa/AdaptiveAppShell/tree/ed5cc9573a7258cc2549125d538102c9029e753a/Docs) · [Доказательства и область проверки](Docs/Catalog-evidence.md#adaptive-app-shell)

---

<a name="live-activity-dynamic-island-kit"></a>

### Live Activity & Dynamic Island Kit

> **Released 0.1.0** · iOS 17+; macOS 14+ (package) · Swift 6.0; Xcode 16.4+

Независимый от домена rendering core с примерами Activity Lab и lifecycle ActivityKit на стороне приложения.

<p align="center">
  <a href="https://github.com/mikonyaa/LiveActivityDynamicIslandKit">
    <img src="Assets/live-activity-dynamic-island-kit.png" width="360" alt="Существующий скриншот реального Activity Lab">
  </a>
</p>

**Когда достаточно более простого решения:** Если статус нужен только внутри приложения, ActivityKit не требуется.

- В исходниках есть Lock Screen, compact, minimal и expanded Dynamic Island, а также примеры start, update, recovery и end.

**Ограничения:**

- При выборе другого scenario content может обновиться, а attributes активной activity останутся прежними. Завершайте и запускайте activity при смене scenario; lifecycle на устройстве здесь не проверен.

**Verified scope · source-review · 2026-10-14:** Release metadata и versioned source; ссылка на CI относится к upstream. Независимого device или production test нет.

[Репозиторий](https://github.com/mikonyaa/LiveActivityDynamicIslandKit) · [Release 0.1.0](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/releases/tag/0.1.0) · [Документация версии](https://github.com/mikonyaa/LiveActivityDynamicIslandKit/tree/f577568f466136e28da427e55aa639170fafbac6/Docs) · [Доказательства и область проверки](Docs/Catalog-evidence.md#live-activity-dynamic-island-kit)

---

<a name="mac-menu-bar-command-kit"></a>

### Mac Menu Bar Command Kit

> **Released 0.2.0** · macOS 14+ · Swift 6.0; Xcode 26+

Command shell с управлением с клавиатуры для сфокусированных macOS-утилит.

<p align="center">
  <a href="https://github.com/mikonyaa/MacMenuBarCommandKit">
    <img src="Assets/mac-menu-bar-command-kit.png" width="760" alt="Скриншот dashboard реального Mac command demo">
  </a>
</p>

**Когда достаточно более простого решения:** Для одного стандартного меню MenuBarExtra полноценный command shell избыточен.

- В исходниках есть MenuBarExtra, главное окно, command palette, Settings, интеграция Launch at Login и clipboard handlers.

**Ограничения:**

- Start Timer увеличивает focus minutes и выставляет флаг, но не измеряет elapsed time. Настоящий таймер нужно реализовать в приложении.

**Verified scope · source-review · 2026-10-14:** Release metadata и versioned source; ссылка на CI относится к upstream. Независимого device или production test нет.

[Репозиторий](https://github.com/mikonyaa/MacMenuBarCommandKit) · [Release 0.2.0](https://github.com/mikonyaa/MacMenuBarCommandKit/releases/tag/0.2.0) · [Документация версии](https://github.com/mikonyaa/MacMenuBarCommandKit/tree/ab43ae5d750f1005ee3e704b3756f4af8c2b3a37/Docs) · [Доказательства и область проверки](Docs/Catalog-evidence.md#mac-menu-bar-command-kit)

---

## Инструмент разработчика

<a name="resizelint"></a>

### ResizeLint

> **Released 1.0.0** · macOS 14+; Ubuntu 22.04+ x86_64 with Swift runtime · Swift 6.3.3 (source build)

Локальный CLI для поиска предположений о глобальном экране, scene, idiom, orientation и layout.

<p align="center">
  <a href="https://github.com/mikonyaa/ResizeLint">
    <img src="Assets/resizelint-terminal.svg" width="760" alt="Иллюстрация терминала ResizeLint с RL001; это не снимок результата теста">
  </a>
</p>

**Когда достаточно более простого решения:** Статические diagnostics дополняют resizing и device QA, но не доказывают корректность layout во время выполнения.

- В исходниках определены девять правил, human/Xcode/JSON/SARIF output и Action с проверкой checksum. Анализ выполняется локально.

**Ограничения:**

- Опубликованный Linux-архив 1.0.0 требует Swift shared libraries, включая libswiftCore.so: одной чистой Ubuntu недостаточно. Подпись/notarization macOS подтверждается release CI, а не независимой проверкой Gatekeeper в этом каталоге.

**Verified scope · source-review · 2026-10-14:** Release metadata и versioned source; ссылка на CI относится к upstream. Независимого device или production test нет.

[Репозиторий](https://github.com/mikonyaa/ResizeLint) · [Release 1.0.0](https://github.com/mikonyaa/ResizeLint/releases/tag/1.0.0) · [Документация версии](https://github.com/mikonyaa/ResizeLint/tree/cde1a7b5165cd6dc225166e6e0a7614a32ebce28/Docs) · [Доказательства и область проверки](Docs/Catalog-evidence.md#resizelint)

---

<!-- catalog:end -->

## Критерии качества по роли

Это критерии сопровождения, а не общая гарантия завершённости всех demo-сценариев:

- **UI-шаблоны:** сфокусированный package, явные требования Apple-платформ, demo с локальными данными, документация accessibility и fallbacks, тесты, versioned docs и реальные превью. Манифесты reusable packages не объявляют сторонних Swift-зависимостей; инструменты сборки demo рассматриваются отдельно.
- **CLI:** воспроизводимые fixtures, детерминированные отчёты, документированные source dependencies и runtime requirements, checksums и distribution evidence. ResizeLint использует SwiftSyntax, ArgumentParser и Yams; Linux-бинарнику могут требоваться Swift shared libraries.
- **Каталог:** согласованные EN/RU-факты, доказательства claims, корректные маршруты поддержки, целые локальные ссылки и лимит media bytes. Catalog CI проверяет эти свойства; upstream CI и приёмка на устройстве имеют отдельную область проверки.

## Три шага использования

1. Выберите минимальный репозиторий, который решает задачу продукта.
2. Прочитайте документацию версии, запустите demo в требуемом окружении и проверьте ограничения.
3. При адаптации package оставьте бизнес-модели, persistence и платформенные side effects в своём приложении.

## Сопровождение каталога

Локальная проверка на Python 3.10+:

```sh
python3 Scripts/verify-catalog.py
python3 Scripts/test-verify-catalog.py
```

Команда `python3 Scripts/verify-catalog.py --online` явно перепроверяет releases и immutable commits. Недоступная сеть и rate limits дают **UNVERIFIED** с ненулевым exit; команда не переписывает факты каталога.

[Сопровождение и media bytes](Docs/Catalog-maintenance.md) · [Доказательства и область проверки](Docs/Catalog-evidence.md) · [Протокол независимого теста выбора](Docs/Selection-test.md)

Структура каталога, сломанные ссылки и предложения коллекции — в [catalog Issues](https://github.com/mikonyaa/Apple-Design-Templates/issues). Реализация и интеграция — в соответствующем проекте: [Contributing](CONTRIBUTING.md). Для сообщения об уязвимости следуйте [security policy](SECURITY.md) нужного проекта.

**[Основная визуальная витрина](README.md)**
