"""VigilTech editor settings, seeded once into the Engine config directory."""
from pathlib import Path
import hashlib
import re

MARK = '; amerika-engine theme v3'
LEGACY_SETTINGS_SHA256 = 'd22ce6f23bfff6ecf464395ce12eb8983b65901f5f8fe50eb936f7303e6eb5ac'
FONT = (Path(__file__).with_name('vigiltech') / 'fonts/VigilSans-Regular.ttf').as_posix()
BOLD_FONT = (Path(__file__).with_name('vigiltech') / 'fonts/VigilSans-Bold.ttf').as_posix()

# VigilTech tokens (vigiltech/tokens.json). Night #120a14 is the editor base, Pink 400 #ff4d86 the accent.
# Every syntax colour below is >= 6:1 on Night (checked by tests/test_studio_engine.py).
NIGHT = '#120a14'
ACCENT = '#ff4d86'
SYNTAX = {
    'symbol_color': '#ffc66e',
    'keyword_color': '#ff7aa6',
    'control_flow_keyword_color': '#ff8fb4',
    'base_type_color': '#8fd8cc',
    'string_color': '#ffe08a',
    'number_color': '#c8b4ff',
    'comment_color': '#a893a3',
}


def _c(hexcolor):
    h = hexcolor.lstrip('#')
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return f'Color({r:.3f}, {g:.3f}, {b:.3f}, 1)'


SETTINGS = f"""{MARK}
[gd_resource type="EditorSettings" format=3]

[resource]
interface/theme/preset = "Custom"
interface/theme/base_color = {_c(NIGHT)}
interface/theme/accent_color = {_c(ACCENT)}
interface/theme/contrast = 0.4
interface/theme/draw_extra_borders = true
interface/theme/corner_radius = 8
interface/editor/main_font = "{FONT}"
interface/editor/main_font_bold = "{BOLD_FONT}"
interface/editor/show_update_spinner = 1
interface/editor/update_continuously = false
network/connection/check_for_updates = 2
""" + ''.join(f'text_editor/theme/highlighting/{k} = {_c(v)}\n' for k, v in SYNTAX.items()) + f"""text_editor/theme/highlighting/background_color = {_c(NIGHT)}
"""

# The previous generated default (Cohnsoft green, "theme v2"), reproduced so it can be recognised byte for byte and upgraded.
_V2 = """; amerika-engine theme v2
[gd_resource type="EditorSettings" format=3]

[resource]
interface/theme/preset = "Custom"
interface/theme/base_color = Color(0.110, 0.110, 0.118, 1)
interface/theme/accent_color = Color(0.247, 0.831, 0.467, 1)
interface/theme/contrast = 0.4
interface/theme/draw_extra_borders = true
interface/theme/corner_radius = 6
interface/editor/main_font = "{font}"
interface/editor/main_font_bold = "{bold}"
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


def _is_generated_v2(text):
    m = re.search(r'main_font = "([^"]*)CohnSans-Regular\.ttf"', text)
    if not m:
        return False
    base = m.group(1)
    return text == _V2.format(font=base + 'CohnSans-Regular.ttf', bold=base + 'CohnSans-Bold.ttf')


def seed(config_home):
    """config_home is the XDG_CONFIG_HOME used for Godot (Godot reads <it>/godot/). Never overwrites a user-modified file."""
    d = Path(config_home) / 'godot'
    d.mkdir(parents=True, exist_ok=True)
    f = d / 'editor_settings-4.tres'
    if f.exists():
        # Upgrade only the exact generated v1/v2 defaults; never overwrite custom settings.
        raw = f.read_bytes()
        if hashlib.sha256(raw).hexdigest() == LEGACY_SETTINGS_SHA256 or _is_generated_v2(raw.decode('utf-8', 'replace')):
            f.write_text(SETTINGS)
        return f
    f.write_text(SETTINGS)
    return f
