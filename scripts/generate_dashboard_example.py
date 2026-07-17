"""Wrap a real Streamlit dashboard capture in a self-contained README SVG."""

# ruff: noqa: E501

from __future__ import annotations

import argparse
import base64
from pathlib import Path


def build_svg(screenshot: Path) -> str:
    """Embed a PNG dashboard capture and dataset provenance in SVG."""
    payload = base64.b64encode(screenshot.read_bytes()).decode("ascii")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="790" viewBox="0 0 1280 790" role="img" aria-labelledby="title description">
  <title id="title">Medical Imaging Dashboard with LUNG1-001</title>
  <desc id="description">Real Streamlit dashboard capture displaying axial DICOM slice 67 from the NSCLC-Radiomics LUNG1-001 case.</desc>
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#0f172a"/><stop offset="1" stop-color="#071018"/></linearGradient><clipPath id="capture"><rect x="24" y="82" width="1232" height="665" rx="12"/></clipPath></defs>
  <rect width="1280" height="790" rx="20" fill="url(#bg)"/>
  <text x="30" y="38" fill="#e5edf5" font-family="Inter,Segoe UI,sans-serif" font-size="22" font-weight="700">Medical Imaging Dashboard · LUNG1-001</text>
  <text x="30" y="63" fill="#8fa3b8" font-family="Inter,Segoe UI,sans-serif" font-size="11">Real Streamlit viewer · 134 DICOM slices · axial slice 67 · NSCLC-Radiomics</text>
  <g clip-path="url(#capture)"><image href="data:image/png;base64,{payload}" x="24" y="82" width="1232" height="665" preserveAspectRatio="xMidYMid slice"/></g>
  <text x="30" y="773" fill="#71869a" font-family="Inter,Segoe UI,sans-serif" font-size="9">Research demonstration · dataset doi:10.7937/K9/TCIA.2015.PF0M9REI</text>
</svg>
"""


def main() -> None:
    """Read the capture and write the self-contained SVG."""
    parser = argparse.ArgumentParser()
    parser.add_argument("screenshot", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build_svg(args.screenshot), encoding="utf-8")
    print(f"output={args.output}")


if __name__ == "__main__":
    main()
