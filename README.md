# Cohnsoft Engine

<img src="src/amerika_engine/cohnsoft/logos/mark/cohnsoft-mark.svg" alt="Cohnsoft" width="96">

**A product of Cohnsoft.** Founded by **Demetria Althea Cohn**.

Canonical company identity and Cohn Sans are pinned to cohnsoftassets `752e894f90f1e58e62ae466352cb03c8bfd7d703`.



**Engine**: Godot 4 with an AI game assembler (editor plugin, game recipe, assembler, templates). Powered by the Godot Engine (MIT); Godot is a trademark of the Godot Foundation; not affiliated or endorsed.

Developed by **Cohnsoft** for **Cohnsoft OS** (Ubuntu 26.10 ARM64): describe what you want, and the built-in assistant (Anthropic Claude, through your own API key) builds it. The key is stored in your login keyring by Studio and never reaches the app; see `docs/STUDIO-ARCHITECTURE.md` and `docs/README.md`. Local automation uses the existing Studio bridge; installing OpenClaw is not required.



Source layout: `src/` (installed under `/usr/share`), `tools/builders/engine.py` (Debian package builder used by the Amerika OS build), `tests/`, `docs/engine.md`.
Licence: GPL-3.0-only for Amerika code (see `LICENSE`); third-party licences are listed in `src/NOTICE`.

Package names, plugin paths, game recipes, project data and Studio APIs remain compatible. Cohnsoft defaults upgrade only a byte-for-byte original generated theme; custom editor settings are retained. Godot and all upstream licence notices remain intact. Original product icon SVG and Sprite sources are included.
