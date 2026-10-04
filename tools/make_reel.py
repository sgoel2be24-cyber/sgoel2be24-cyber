"""Generate assets/upstream.svg, the rolling one-line header of shipped work.

Run:  python3 tools/make_reel.py
"""
from pathlib import Path

LINES = [  # (what shipped, short reference shown in grey)
    ("ranked #1 on the OSCI&apos;26 leaderboard with 240+ merged PRs", "osci&apos;26"),
    ("won a special award at the HackBlox 2026 open-source hackathon", "hackblox"),
    ("reached the DataForge 2026 finals at IIT Kharagpur", "dataforge"),
    ("finished in the top 1% at three HackerRank Orchestrate editions", "orchestrate"),
    ("shipped a 48-operation Pinecone integration into Corsair", "f7820d6"),
    ("merged a file-descriptor leak fix into NumPy", "444afc2"),
    ("patched Windows path parsing in Google&apos;s Agent Development Kit", "6f6106f"),
    ("landed two bug fixes in Apache Airflow", "c5d7f60"),
    ("fixed the license-compliance audit in Apache Magpie", "99c983b"),
    ("closed a CLI dry-run hole in Cognee", "2de7ab0"),
    ("built a Go job queue that survives kill -9 with zero job loss", "conveyor"),
    ("wrote a ReDoS analyzer that proves each finding with an attack string", "redoscope"),
    ("built an incremental build engine with a content-addressed cache", "forgegraph"),
    ("built an offline screen assistant for blind users on the Snapdragon NPU", "netra"),
    ("built an Android assistant you teach by doing a task once", "teachable-voice"),
]
SLOT = 3.45          # seconds each line is on screen, including the roll
HOLD = 12.0083 / 14.2857
H = 44

n = len(LINES)
dur = round(SLOT * n, 2)
kf = []
for i in range(n):
    kf.append(f"    {100 * i / n:.4f}% {{ transform: translateY({-H * i}px); }}")
    kf.append(f"    {100 * (i + HOLD) / n:.4f}% {{ transform: translateY({-H * i}px); }}")
kf.append(f"    100.0000% {{ transform: translateY({-H * n}px); }}")
texts = "\n".join(
    f'  <text x="450" y="{22.0 + H * i:.1f}" class="ln" dominant-baseline="middle" text-anchor="middle">'
    f'<tspan class="pl">+ </tspan>{t}  <tspan class="sha">{ref}</tspan></text>'
    for i, (t, ref) in enumerate(LINES + LINES[:1])
)
svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="44" viewBox="0 0 900 44" role="img" aria-label="Recent shipped work">
  <title>Recent shipped work</title>
  <style>
    .ln {{
      font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
      font-size: 16px; font-weight: 500; fill: #1f2328;
    }}
    .pl  {{ fill: #1a7f37; font-weight: 700; }}
    .sha {{ fill: #818b98; }}
    @media (prefers-color-scheme: dark) {{
      .ln  {{ fill: #e6edf3; }}
      .pl  {{ fill: #3fb950; }}
      .sha {{ fill: #7d8590; }}
    }}
    #reel {{ animation: roll {dur}s steps(1, end) infinite; }}
    @media (prefers-reduced-motion: no-preference) {{
      #reel {{ animation: roll {dur}s cubic-bezier(.2,.8,.2,1) infinite; }}
    }}
    @keyframes roll {{
{chr(10).join(kf)}
    }}
  </style>
  <g id="reel">
{texts}
  </g>
</svg>
"""
out = Path(__file__).resolve().parent.parent / "assets" / "upstream.svg"
out.write_text(svg)
print(f"{out.name}: {n} lines, {dur}s loop")
