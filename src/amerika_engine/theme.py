"""Cohnsoft editor settings, seeded once into the Engine config directory."""
from pathlib import Path
import hashlib

MARK = '; amerika-engine theme v2'
LEGACY_SETTINGS_SHA256 = 'd22ce6f23bfff6ecf464395ce12eb8983b65901f5f8fe50eb936f7303e6eb5ac'
FONT = (Path(__file__).with_name('cohnsoft') / 'fonts/CohnSans-Regular.ttf').as_posix()
BOLD_FONT = (Path(__file__).with_name('cohnsoft') / 'fonts/CohnSans-Bold.ttf').as_posix()

SETTINGS = f"""{MARK}
[gd_resource type="EditorSettings" format=3]

[resource]
interface/theme/preset = "Custom"
interface/theme/base_color = Color(0.110, 0.110, 0.118, 1)
interface/theme/accent_color = Color(0.247, 0.831, 0.467, 1)
interface/theme/contrast = 0.4
interface/theme/draw_extra_borders = true
interface/theme/corner_radius = 6
interface/editor/main_font = "{FONT}"
interface/editor/main_font_bold = "{BOLD_FONT}"
interface/editor/show_update_spinner = 1
interface/editor/update_continuously = false
network/connection/check_for_updates = 2
text_editor/theme/highlighting/symbol_color = Color(1, 0.69, 0.18, 1)
text_editor/theme/highlighting/keyword_color = Color(0.72, 0.58, 0.39, 1)
text_editor/theme/highlighting/control_flow_keyword_color = Color(0.72, 0.58, 0.39, 1)
text_editor/theme/highlighting/base_type_color = Color(0.65, 0.79, 0.73, 1)
text_editor/theme/highlighting/string_color = Color(1, 0.88, 0.3, 1)
text_editor/theme/highlighting/background_color = Color(0.110, 0.110, 0.118, 1)
"""


def seed(config_home):
    """config_home is the XDG_CONFIG_HOME used for Godot (Godot reads <it>/godot/). Never overwrites a user-modified file."""
    d = Path(config_home) / 'godot'
    d.mkdir(parents=True, exist_ok=True)
    f = d / 'editor_settings-4.tres'
    if f.exists():
        # Upgrade only the exact generated v1 defaults; never overwrite custom settings.
        if hashlib.sha256(f.read_bytes()).hexdigest() == LEGACY_SETTINGS_SHA256:
            f.write_text(SETTINGS)
        return f
    f.write_text(SETTINGS)
    return f
