import os

WIDTH, HEIGHT = 840, 880
PAD = 20
TITLEBAR_H = 30
TILE_W = 392
TILE_H = 218
GAP = 16

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <style>
    .tile {{ opacity: 0; animation: fadeIn 0.45s ease-out both; }}
    .label {{ fill: #7d8590; font-size: 22px; }}
    .value {{ fill: #e6edf3; font-size: 17px; font-weight: 700; }}
    .muted {{ fill: #7d8590; font-size: 18px; }}
    @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(14px); }} to {{ opacity: 1; transform: translateY(0); }} }}
  </style>
  <defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#111722"/><stop offset="1" stop-color="#0d1117"/></linearGradient></defs>
  <rect width="{WIDTH}" height="{HEIGHT}" rx="12" fill="url(#bg)"/>
  <rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{HEIGHT - 1}" rx="12" fill="none" stroke="#30363d"/>
  <line x1="0" y1="{TITLEBAR_H}" x2="{WIDTH}" y2="{TITLEBAR_H}" stroke="#30363d"/>
  <circle cx="{PAD}" cy="15" r="5" fill="#ff5f56"/>
  <circle cx="{PAD + 16}" cy="15" r="5" fill="#ffbd2e"/>
  <circle cx="{PAD + 32}" cy="15" r="5" fill="#27c93f"/>
  <text x="{WIDTH / 2}" y="19" fill="#7d8590" font-size="12" text-anchor="middle">aziel@github: ~$ ./neofetch</text>

  <g class="tile" style="animation-delay:0.00s">
    <rect x="{PAD}" y="54" width="{TILE_W}" height="{TILE_H}" rx="10" fill="#161b22" stroke="#30363d"/>
    <text x="44" y="94" class="label">$ whoami</text>
    <text x="44" y="144" class="value">Aziel Zhero</text>
    <text x="44" y="180" class="muted">Fullstack Developer &amp; CyberSec</text>
  </g>

  <g class="tile" style="animation-delay:0.15s">
    <rect x="{PAD + TILE_W + GAP}" y="54" width="{TILE_W}" height="{TILE_H}" rx="10" fill="#161b22" stroke="#30363d"/>
    <text x="452" y="94" class="label">$ location</text>
    <text x="452" y="144" class="value">Pindamonhangaba</text>
    <text x="452" y="180" class="muted">São Paulo, Brazil</text>
  </g>

  <g class="tile" style="animation-delay:0.30s">
    <rect x="{PAD}" y="288" width="{TILE_W}" height="{TILE_H}" rx="10" fill="#161b22" stroke="#30363d"/>
    <text x="44" y="328" class="label">$ certifications</text>
    <text x="44" y="378" class="value">CEH Master</text>
    <text x="44" y="414" class="muted">OSINT &amp; Cybersecurity</text>
  </g>

  <g class="tile" style="animation-delay:0.45s">
    <rect x="{PAD + TILE_W + GAP}" y="288" width="{TILE_W}" height="{TILE_H}" rx="10" fill="#161b22" stroke="#30363d"/>
    <text x="452" y="328" class="label">$ stack</text>
    <text x="452" y="378" class="value">Node.js • React • Python</text>
    <text x="452" y="414" class="muted">PHP • PostgreSQL • Redis</text>
  </g>

  <g class="tile" style="animation-delay:0.60s">
    <rect x="{PAD}" y="522" width="{TILE_W}" height="{TILE_H}" rx="10" fill="#161b22" stroke="#30363d"/>
    <text x="44" y="562" class="label">$ workflow</text>
    <text x="44" y="612" class="value">N8N • Make</text>
    <text x="44" y="648" class="muted">Smart Contracts &amp; Automation</text>
  </g>

  <g class="tile" style="animation-delay:0.75s">
    <rect x="{PAD + TILE_W + GAP}" y="522" width="{TILE_W}" height="{TILE_H}" rx="10" fill="#161b22" stroke="#30363d"/>
    <text x="452" y="562" class="label">$ design</text>
    <text x="452" y="612" class="value">Flat Design</text>
    <text x="452" y="648" class="muted">Vector Graphics &amp; SVG</text>
  </g>
</svg>"""

with open("info-card.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
print("✅ info-card.svg gerado com sucesso!")
