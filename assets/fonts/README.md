# Nunito Sans

Copyright 2016 The Nunito Sans Project Authors.
Distributed under the [SIL Open Font License 1.1](OFL.txt).

Source: [Google Fonts / Nunito Sans](https://github.com/google/fonts/tree/main/ofl/nunitosans),
downloaded 2026-09-19. Upstream font version: `3.101;gftools[0.9.27]`.

The three bundled TTFs are static instances of
`NunitoSans[YTLC,opsz,wdth,wght].ttf`, generated with FontTools 4.65.0.
Source SHA-256:
`f934d7142fb4784bf828da485b7dcbd90c0c80d514e9d49a5da0ed3a1ae2491d`.

To reproduce them with FontTools installed and the source font in the current
directory, run this Python snippet from this directory:

```python
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

font = TTFont("NunitoSans[YTLC,opsz,wdth,wght].ttf")
for weight, name in [(400, "Regular"), (700, "Bold"), (800, "ExtraBold")]:
    instance = instantiateVariableFont(
        font,
        {"wght": weight, "wdth": 100, "opsz": 12, "YTLC": 500},
        inplace=False,
        updateFontNames=True,
    )
    instance.save(f"NunitoSans-{name}.ttf")
```

FontTools and the variable source font are not required for normal CV builds.
