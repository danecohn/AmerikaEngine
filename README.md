# Engine

<!-- artemis-publisher:start -->
<img src="brand/artemis/artemis-wordmark.svg" alt="Artemis Softworks LLC" width="340">

**A product of Artemis Softworks LLC.** Founded by **Demetria Althea Cohn**.

Companion software for macOS, thoughtfully available for Windows and Linux. See the [Artemis identity and design system](brand/artemis/BRAND.md). Platform availability varies by product and release.
<!-- artemis-publisher:end -->


**Engine**: Godot 4 with an AI game assembler (editor plugin, game recipe, assembler, templates). Powered by the Godot Engine (MIT); Godot is a trademark of the Godot Foundation; not affiliated or endorsed.

Developed by **Artemis Softworks LLC** for **Makk OS** (Ubuntu 26.10 ARM64): describe what you want, and the built-in assistant (Anthropic Claude, through your own API key) builds it. The key is stored in your login keyring by Studio and never reaches the app; see `docs/STUDIO-ARCHITECTURE.md` and `docs/README.md`. Local automation uses the existing Studio bridge; installing OpenClaw is not required.



Source layout: `src/` (installed under `/usr/share`), `tools/builders/engine.py` (Debian package builder used by the Amerika OS build), `tests/`, `docs/engine.md`.
Licence: GPL-3.0-only for Amerika code (see `LICENSE`); third-party licences are listed in `src/NOTICE`.
