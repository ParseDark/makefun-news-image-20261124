# One image: 24 November 2026 world news

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/c/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/ParseDark/makefun-news-image-20261124/rank.svg)](https://make.fun/c/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/ParseDark/makefun-news-image-20261124/reward.svg)](https://make.fun/c/news-image-20261124)

An entry for the [make.fun](https://make.fun/c/news-image-20261124) bounty
**news-image-20261124**: sum up Tuesday 24 November 2026's world news in a
single image.

The image is a pixel-art newspaper front page, *The Pixel Globe Gazette*:
four complete headlines, each with its date chip, plus a pixel Earth with
five numbered markers tying each story to the place it happened, and one
caption line. It was drawn programmatically from the four verified
headlines above (no headline is truncated, and every figure was checked
against the cited article) and rendered at 1024×1024. `main.py` (Python
3.13, standard library only) copies the bundled `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output` when the variable is
unset). The output is a 1024×1024 RGB PNG, well under the 1 MiB limit,
and byte-identical on every run.

## The four headlines

1. **NVIDIA-led chip selloff** — NVDA −5.86% to $155.38, SOX −7.88%,
   Nasdaq −1.48%, giving back part of Monday's historic Jensen Huang
   rally.
2. **Dow closes above 50,000** — 50,018.70, up 0.85%, while tech fell.
3. **USTR tariff probe** — the US is expected to unveil findings of an
   industrial-subsidy investigation covering China, the EU and 14 other
   nations.
4. **US consumer confidence** — 103.3, far above the 92.5 expected, the
   highest since January 2025.

## Sources

- [Motley Fool] — Stock Market Today, Nov. 24: Nvidia Gives Back $240 Billion in Market Value Despite Wall Street Upgrade Signaling 29% Upside (Nov 24, 2026)
- [MarketWatch] — Dow logs back-to-back gains, but Nasdaq and S&P 500 end lower as tech selloff resumes (Nov 24, 2026)
- [Wall Street Journal] — U.S. Prepares to Raise Tariffs on China and Other Countries (Nov 24, 2026)
- [Reuters] — US consumer confidence surges to highest level in nearly two years (Nov 24, 2026)

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024, byte-identical every run)
```

## License

MIT — see [LICENSE](LICENSE).
