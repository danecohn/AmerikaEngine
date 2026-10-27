"""Boot splash for new projects: VigilTech Engine icon on a plum-black night, drawn with PIL (or Qt/pure-python fallback)."""
import struct
import zlib
from pathlib import Path


def _png_fallback(path, w, h):
    rows = []
    for y in range(h):
        t = y / h
        r, g, b = int(18 + 14 * t), int(10 + 5 * t), int(20 + 16 * t)
        rows.append(b'\x00' + bytes([r, g, b]) * w)
    raw = b''.join(rows)
    def chunk(tag, data):
        c = struct.pack('>I', len(data)) + tag + data
        return c + struct.pack('>I', zlib.crc32(tag + data) & 0xffffffff)
    Path(path).write_bytes(b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0)) + chunk(b'IDAT', zlib.compress(raw)) + chunk(b'IEND', b''))


def make_splash(path, title='Vigil Engine', w=640, h=360):
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        _png_fallback(path, w, h)
        return path
    img = Image.new('RGB', (w, h), (18, 10, 20))
    d = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(1, h - 1)
        d.line([(0, y), (w, y)], fill=(int(18 + 14*t), int(10 + 5*t), int(20 + 16*t)))
    emblem = Path(__file__).with_name('artemis.png')
    if emblem.exists():
        logo = Image.open(emblem).convert('RGBA')
        side = int(h * 0.60)
        logo = logo.resize((side, side), Image.Resampling.LANCZOS)
        img.paste(logo, ((w-side)//2, (h-side)//2-8), logo)
    font = ImageFont.truetype(str(Path(__file__).with_name('vigiltech') / 'fonts/VigilSans-Regular.ttf'), 13)
    d.text((w // 2 - len(title) * 3, int(h * 0.10)), title.upper(), fill=(246, 241, 244), font=font)
    d.text((20, h-33), 'A product of VigilTech, vigiltech.org', fill=(246, 241, 244), font=font)
    d.text((20, h-18), 'Powered by the Godot Engine (MIT)', fill=(185, 168, 180), font=font)
    img.save(path)
    return path
