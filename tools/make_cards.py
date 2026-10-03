"""Generate the animated project cards in assets/cards/.

Each card is a trace of the project's real mechanism: a playhead sweeps left to
right and reveals events as it passes them. Everything is plain SVG + CSS so it
renders inside GitHub's <img> sandbox, follows the viewer's light/dark scheme,
and falls back to the complete, static trace under prefers-reduced-motion.

Run:  python3 tools/make_cards.py
"""
from pathlib import Path

W, H = 440, 252
CYCLE = 12.0          # seconds per loop
SWEEP_END = 46.0      # % of the cycle at which the playhead reaches the right edge
FADE_FROM, FADE_TO = 94.0, 97.5

OUT = Path(__file__).resolve().parent.parent / "assets" / "cards"

SANS = '-apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif'
MONO = 'ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace'


def pct_at(x, x0, x1):
    """Cycle percentage at which the playhead passes x."""
    return SWEEP_END * (x - x0) / (x1 - x0)


def style(delay, x0, x1, extra=""):
    span = x1 - x0 + 8   # playhead travel; matches the clip edge below
    return f"""
  <style>
    svg {{
      --bg:#f6f8fa; --bd:#d0d7de; --fg:#1f2328; --mu:#59636e; --gd:#d8dee4;
      --bl:#0969da; --gr:#1a7f37; --rd:#cf222e; --am:#bf8700; --amt:#9a6700;
    }}
    @media (prefers-color-scheme: dark) {{
      svg {{
        --bg:#161b22; --bd:#30363d; --fg:#e6edf3; --mu:#8b949e; --gd:#262c36;
        --bl:#4493f8; --gr:#3fb950; --rd:#f85149; --am:#d29922; --amt:#d29922;
      }}
    }}
    .bg {{ fill:var(--bg); stroke:var(--bd); }}
    .t  {{ font-family:{SANS}; font-size:19px; font-weight:600; fill:var(--fg); }}
    .st {{ font-family:{SANS}; font-size:13px; fill:var(--mu); }}
    .m  {{ font-family:{MONO}; font-size:11px; fill:var(--mu); }}
    .mf {{ font-family:{MONO}; font-size:11px; fill:var(--fg); }}
    .ft {{ font-family:{MONO}; font-size:11.5px; fill:var(--fg); }}
    .lg {{ font-family:{MONO}; font-size:11px; fill:var(--mu); text-anchor:end; }}
    .ax {{ stroke:var(--gd); stroke-width:1; }}
    .fbl {{ fill:var(--bl); }} .fgr {{ fill:var(--gr); }} .frd {{ fill:var(--rd); }} .fam {{ fill:var(--am); }}
    .tbl {{ fill:var(--bl); }} .tgr {{ fill:var(--gr); }} .trd {{ fill:var(--rd); }} .tam {{ fill:var(--amt); }}
    .sbl {{ stroke:var(--bl); }} .sgr {{ stroke:var(--gr); }} .srd {{ stroke:var(--rd); }} .sam {{ stroke:var(--am); }}
    .smu {{ stroke:var(--mu); }}
    .anim {{ animation-duration:{CYCLE}s; animation-iteration-count:infinite; animation-delay:{delay}s; }}
    .sweep {{ transform-box:fill-box; transform-origin:0 50%; animation-name:sweep; animation-timing-function:linear; }}
    .ph    {{ opacity:0; animation-name:ph; animation-timing-function:linear; }}
    .trace {{ animation-name:fade; }}
    .late  {{ animation-name:late; }}
    @keyframes sweep {{ 0% {{ transform:scaleX(0); }} {SWEEP_END}% {{ transform:scaleX(1); }} 100% {{ transform:scaleX(1); }} }}
    @keyframes ph {{
      0% {{ transform:translateX(0); opacity:1; }}
      {SWEEP_END}% {{ transform:translateX({span}px); opacity:1; }}
      {SWEEP_END + 3}% {{ transform:translateX({span}px); opacity:0; }}
      100% {{ transform:translateX({span}px); opacity:0; }}
    }}
    @keyframes fade {{ 0% {{ opacity:1; }} {FADE_FROM}% {{ opacity:1; }} {FADE_TO}% {{ opacity:0; }} 100% {{ opacity:0; }} }}
    @keyframes late {{ 0% {{ opacity:0; }} {SWEEP_END}% {{ opacity:0; }} {SWEEP_END + 2}% {{ opacity:1; }} 100% {{ opacity:1; }} }}
    {extra}
    @media (prefers-reduced-motion: reduce) {{ .anim {{ animation:none; }} }}
  </style>"""


def frame(name, lang, subtitle, footer, body, delay, x0, x1, label, extra="", trace_top=70, trace_bot=214):
    cid = "reveal-" + name.replace(" ", "-")
    body = body.replace("url(#reveal)", f"url(#{cid})")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">
  <title>{label}</title>{style(delay, x0, x1, extra)}
  <defs>
    <clipPath id="{cid}"><rect class="sweep anim" x="{x0 - 2}" y="{trace_top}" width="{x1 - x0 + 10}" height="{trace_bot - trace_top}"/></clipPath>
  </defs>
  <rect class="bg" x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="10"/>
  <text class="t" x="24" y="34">{name}</text>
  <text class="m" x="{W - 24}" y="33" text-anchor="end">{lang}</text>
  <text class="st" x="24" y="55">{subtitle}</text>
{body}
  <line class="ph anim" x1="{x0}" y1="{trace_top + 8}" x2="{x0}" y2="{trace_bot - 10}" stroke="var(--fg)" stroke-width="1.25" stroke-opacity="0.55"/>
  <text class="ft" x="24" y="{H - 18}">{footer}</text>
</svg>
"""


# ---------------------------------------------------------------- conveyor
def conveyor(delay):
    x0, x1 = 104, 416
    lanes = {"submit": 100, "WAL": 136, "broker": 172}
    kill_x, replay_a, replay_b = 214, 242, 272
    pre = [112, 132, 152, 172, 192]
    post = [298, 318, 338, 358, 378, 398]
    static, trace = [], []
    for lbl, y in lanes.items():
        static.append(f'  <text class="lg" x="92" y="{y + 4}">{lbl}</text>')
        static.append(f'  <line class="ax" x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke-dasharray="2 4"/>')
    for x in pre + post:
        trace.append(f'<rect class="fbl" x="{x}" y="{lanes["submit"] - 5}" width="10" height="10" rx="2"/>')
        trace.append(f'<rect class="fgr" x="{x + 4}" y="{lanes["WAL"] - 7}" width="12" height="14" rx="1.5" fill-opacity="0.85"/>')
    # kill -9
    trace.append(f'<line class="srd" x1="{kill_x}" y1="84" x2="{kill_x}" y2="186" stroke-width="1.25" stroke-dasharray="3 3"/>')
    trace.append(f'<text class="mf trd" x="{kill_x + 6}" y="86" font-weight="700">kill -9</text>')
    # broker state: up -> killed -> replay -> up
    by = lanes["broker"]
    trace.append(f'<rect class="fgr" x="{x0}" y="{by - 4}" width="{kill_x - x0}" height="8" rx="2"/>')
    trace.append(f'<path class="srd" d="M{kill_x - 5} {by - 5} l10 10 m0 -10 l-10 10" stroke-width="2" stroke-linecap="round"/>')
    trace.append(f'<rect class="fam" x="{replay_a}" y="{by - 4}" width="{replay_b - replay_a}" height="8" rx="2"/>')
    trace.append(f'<text class="m tam" x="{replay_a - 4}" y="{by + 22}">replay 7.7 ms</text>')
    trace.append(f'<rect class="fgr" x="{replay_b + 2}" y="{by - 4}" width="{x1 - replay_b - 2}" height="8" rx="2"/>')
    # replay highlight on the pre-kill log entries, timed to the replay moment
    t = pct_at(replay_a, x0, x1)
    extra = f"""
    .rp {{ animation-name:rp; }}
    @keyframes rp {{ 0% {{ opacity:0; }} {t:.2f}% {{ opacity:0; }} {t + 1.5:.2f}% {{ opacity:1; }} {SWEEP_END + 6:.2f}% {{ opacity:1; }} {SWEEP_END + 10:.2f}% {{ opacity:.35; }} 100% {{ opacity:.35; }} }}"""
    hl = "".join(f'<rect class="sam" x="{x + 2.5}" y="{lanes["WAL"] - 8.5}" width="15" height="17" rx="2.5" fill="none" stroke-width="1.6"/>' for x in pre)
    body = "\n".join(static) + f"""
  <g class="trace anim">
    <g clip-path="url(#reveal)">
      {''.join(trace)}
    </g>
    <g class="rp anim">{hl}</g>
  </g>"""
    return frame("conveyor", "Go", "A job queue that loses nothing to kill -9",
                 "0 jobs lost in 50 kill -9 trials", body, delay, x0, x1,
                 "conveyor: jobs are appended to a write-ahead log, the broker is killed with kill -9, the log is replayed in 7.7 ms and no job is lost",
                 extra)


# ---------------------------------------------------------------- redoscope
def redoscope(delay):
    x0, x1 = 64, 410
    base_y, top_y = 186, 96
    n = 14
    xs = [x0 + 12 + i * (x1 - x0 - 24) / (n - 1) for i in range(n)]
    g = 1.47
    hs = [(top_y - base_y) * -1 * (g ** i - 1) / (g ** (n - 1) - 1) for i in range(n)]
    ys = [base_y - 3 - h for h in hs]
    static = [
        f'  <text class="mf" x="{x0 + 12}" y="{top_y + 12}" font-size="12.5px">/^(a+)+$/</text>',
        f'  <line class="ax" x1="{x0}" y1="{base_y}" x2="{x1 + 6}" y2="{base_y}"/>',
        f'  <line class="ax" x1="{x0}" y1="{base_y}" x2="{x0}" y2="{top_y - 6}"/>',
        f'  <text class="m" x="{x0 - 6}" y="{top_y + 2}" text-anchor="end">time</text>',
        f'  <text class="m" x="{x0 - 6}" y="{base_y + 19}" text-anchor="end">input</text>',
    ]
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in zip(xs, ys))
    trace = [f'<polyline points="{pts}" fill="none" class="sbl" stroke-width="1.5" stroke-opacity="0.55"/>']
    for x, y in zip(xs, ys):
        trace.append(f'<circle class="fbl" cx="{x:.1f}" cy="{y:.1f}" r="2.8"/>')
    for x in xs:
        trace.append(f'<text class="mf" x="{x:.1f}" y="{base_y + 19}" text-anchor="middle">a</text>')
    trace.append(f'<text class="mf trd" x="{xs[-1] + 13:.1f}" y="{base_y + 19}" text-anchor="middle" font-weight="700">!</text>')
    late = f"""
    <g class="late anim">
      <path class="sgr" d="M{xs[-1] - 150:.1f} {top_y - 3} l4 4 l8 -9" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      <text class="mf tgr" x="{xs[-1] - 134:.1f}" y="{top_y + 1}">blow-up verified</text>
    </g>"""
    body = "\n".join(static) + f"""
  <g class="trace anim">
    <g clip-path="url(#reveal)">
      {''.join(trace)}
    </g>{late}
  </g>"""
    return frame("redoscope", "TypeScript", "Finds ReDoS and proves each hit with a real attack",
                 "0 false positives, 0 misses on 627 real regexes", body, delay, x0, x1,
                 "redoscope: a witness attack string grows one character at a time while the regex match time grows exponentially, and the blow-up is verified",
                 trace_top=66)


# ---------------------------------------------------------------- forgegraph
TASKS = {  # name: (duration ms, deps) -- from examples/demo-project/forge.json
    "generate-types": (220, []), "compile-api": (280, ["generate-types"]),
    "compile-sdk": (260, ["generate-types"]), "unit-api": (180, ["compile-api"]),
    "unit-sdk": (170, ["compile-sdk"]), "lint-web": (120, []),
    "compile-web": (300, ["lint-web"]), "unit-web": (150, ["compile-web"]),
    "integration": (240, ["unit-api", "compile-web"]), "docs": (90, []),
    "package": (200, ["integration", "unit-sdk", "unit-web", "docs"]),
}
AFFECTED = ["compile-api", "unit-api", "integration", "package"]


def schedule():
    """Earliest-start schedule (the demo's observed max parallelism is 3)."""
    start, end = {}, {}
    while len(end) < len(TASKS):
        for t, (d, deps) in TASKS.items():
            if t not in end and all(p in end for p in deps):
                start[t] = max([end[p] for p in deps], default=0)
                end[t] = start[t] + d
    rows, row_free = {}, [0, 0, 0]
    for t in sorted(TASKS, key=lambda k: (start[k], k)):
        r = next(i for i, f in enumerate(row_free) if f <= start[t])
        rows[t], row_free[r] = r, end[t]
    return start, end, rows


def forgegraph(delay):
    x0, x1 = 104, 416
    s, e, rows = schedule()
    k = 0.13  # px per ms, shared by both runs so bar lengths are comparable
    row_y = [92, 110, 128]
    cache_y = 160
    edit_x, run2 = 278, 290
    static = [
        f'  <text class="lg" x="92" y="{row_y[1] + 4}">workers</text>',
        f'  <text class="lg" x="92" y="{cache_y + 4}">cache</text>',
        f'  <line class="ax" x1="{x0}" y1="{cache_y + 22}" x2="{x1}" y2="{cache_y + 22}"/>',
    ]
    trace = []
    for t in TASKS:
        x = x0 + s[t] * k
        w = TASKS[t][0] * k - 1.5
        trace.append(f'<rect class="fbl" x="{x:.1f}" y="{row_y[rows[t]] - 6}" width="{w:.1f}" height="12" rx="2" fill-opacity="0.9"/>')
    trace.append(f'<text class="m" x="{x0}" y="{cache_y + 4}">cold</text>')
    trace.append(f'<text class="m" x="{x0}" y="{cache_y + 38}">first build</text>')
    # the edit
    trace.append(f'<line class="sam" x1="{edit_x}" y1="80" x2="{edit_x}" y2="{cache_y + 12}" stroke-width="1.25" stroke-dasharray="3 3"/>')
    trace.append(f'<text class="m tam" x="{edit_x + 6}" y="82">edit src/api.txt</text>')
    # second run: only the affected chain reruns, sequentially
    x = run2
    for t in AFFECTED:
        w = TASKS[t][0] * k
        trace.append(f'<rect class="fam" x="{x:.1f}" y="{row_y[0] - 6}" width="{w - 1.5:.1f}" height="12" rx="2"/>')
        x += w
    for i in range(7):
        trace.append(f'<circle class="fgr" cx="{run2 + 4 + i * 8}" cy="{cache_y}" r="2.8"/>')
    trace.append(f'<text class="m tgr" x="{run2 + 62}" y="{cache_y + 4}">7 hits</text>')
    trace.append(f'<text class="m" x="{run2}" y="{cache_y + 38}">after one edit</text>')
    body = "\n".join(static) + f"""
  <g class="trace anim">
    <g clip-path="url(#reveal)">
      {''.join(trace)}
    </g>
  </g>"""
    return frame("forgegraph", "Go", "A build engine that reruns only what an edit touched",
                 "warm rebuild 1 ms; one edit reruns 4 of 11 tasks", body, delay, x0, x1,
                 "forgegraph: a cold build runs all 11 tasks across three workers; after editing src/api.txt only the 4 affected tasks rerun and 7 come from cache",
                 trace_bot=204)


# ---------------------------------------------------------------- teachable voice
def bubble(x, y, text, cls):
    w = len(text) * 6.62 + 16
    return (f'<rect x="{x}" y="{y - 10}" width="{w:.0f}" height="20" rx="10" class="{cls}" fill-opacity="0.14"/>'
            f'<text class="mf" x="{x + 8}" y="{y + 4}">{text}</text>')


def teachable(delay):
    x0, x1 = 104, 416
    lanes = {"voice": 96, "taps": 134, "guard": 168}
    static = []
    for lbl, y in lanes.items():
        static.append(f'  <text class="lg" x="92" y="{y + 4}">{lbl}</text>')
    static.append(f'  <line class="ax" x1="{x0}" y1="{lanes["taps"]}" x2="{x1}" y2="{lanes["taps"]}" stroke-dasharray="2 4"/>')
    trace = [bubble(x0, lanes["voice"], "order a Margherita", "fbl"),
             bubble(272, lanes["voice"], "a Farmhouse instead", "fgr")]
    for x in [150, 170, 190, 210, 230]:  # you demonstrate once
        trace.append(f'<circle class="fbl" cx="{x}" cy="{lanes["taps"]}" r="4.5"/>'
                     f'<circle class="sbl" cx="{x}" cy="{lanes["taps"]}" r="8" fill="none" stroke-opacity="0.45"/>')
    for x in [300, 316, 332, 348, 364]:  # it replays with the new value
        trace.append(f'<circle class="fgr" cx="{x}" cy="{lanes["taps"]}" r="4.5"/>')
    gy = lanes["guard"]
    trace.append(f'<line class="sgr" x1="{x0}" y1="{gy}" x2="380" y2="{gy}" stroke-width="2" stroke-dasharray="1 5" stroke-linecap="round"/>')
    # padlock at the payment screen
    trace.append(f'<rect class="fam" x="383" y="{gy - 3}" width="14" height="11" rx="2"/>'
                 f'<path class="sam" d="M386 {gy - 3} v-3 a4 4 0 0 1 8 0 v3" fill="none" stroke-width="1.8"/>')
    trace.append(f'<text class="m tam" x="377" y="{gy - 8}" text-anchor="end">stops at payment</text>')
    trace.append(f'<text class="m" x="{x0}" y="200">taught once</text>')
    trace.append(f'<text class="m" x="282" y="200">replayed by voice</text>')
    body = "\n".join(static) + f"""
  <g class="trace anim">
    <g clip-path="url(#reveal)">
      {''.join(trace)}
    </g>
  </g>"""
    return frame("teachable voice", "Kotlin", "An Android assistant that learns a task from one demo",
                 "18/18 commands understood, 7/7 cross-app runs", body, delay, x0, x1,
                 "teachable voice: you say a command and demonstrate it once; later a new spoken value is replayed automatically through the same taps, stopping at the payment screen")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    cards = {"conveyor": conveyor(0), "redoscope": redoscope(-9), "forgegraph": forgegraph(-6), "teachable-voice": teachable(-3)}
    for name, svg in cards.items():
        (OUT / f"{name}.svg").write_text(svg)
        print(f"{name}.svg  {len(svg.encode())} bytes")
