#!/usr/bin/env python3
"""Generate simple deterministic mono PCM16 WAV sound effects."""

from __future__ import annotations

import argparse
import json
import math
import random
import struct
import wave
from pathlib import Path

VERSION = "1.0.0"
PRESETS = ("ui_click", "card_draw", "card_play", "impact", "warning")
DEFAULT_DURATION_MS = {
    "ui_click": 90,
    "card_draw": 260,
    "card_play": 220,
    "impact": 320,
    "warning": 600,
}


def envelope(index: int, frames: int, attack_ratio: float, release_power: float) -> float:
    position = index / max(1, frames - 1)
    attack = min(1.0, position / max(attack_ratio, 1e-6))
    release = max(0.0, 1.0 - position) ** release_power
    return attack * release


def synthesize(preset: str, frames: int, sample_rate: int, seed: int) -> list[float]:
    rng = random.Random(seed)
    variation = rng.uniform(0.96, 1.04)
    phase = rng.uniform(0.0, math.tau)
    samples: list[float] = []

    for i in range(frames):
        t = i / sample_rate
        x = i / max(1, frames - 1)
        noise = rng.uniform(-1.0, 1.0)

        if preset == "ui_click":
            env = envelope(i, frames, 0.03, 4.5)
            value = env * (
                0.72 * math.sin(math.tau * 1280.0 * variation * t + phase)
                + 0.28 * math.sin(math.tau * 710.0 * variation * t)
                + 0.05 * noise
            )
        elif preset == "card_draw":
            env = envelope(i, frames, 0.08, 2.2)
            sweep = (1500.0 - 850.0 * x) * variation
            value = env * (0.58 * noise + 0.42 * math.sin(math.tau * sweep * t + phase))
        elif preset == "card_play":
            env = envelope(i, frames, 0.025, 3.0)
            thump = (170.0 - 65.0 * x) * variation
            value = env * (
                0.63 * math.sin(math.tau * thump * t + phase)
                + 0.24 * math.sin(math.tau * 460.0 * variation * t)
                + 0.13 * noise
            )
        elif preset == "impact":
            env = envelope(i, frames, 0.012, 3.8)
            low = (105.0 - 35.0 * x) * variation
            value = env * (
                0.56 * noise
                + 0.44 * math.sin(math.tau * low * t + phase)
            )
        elif preset == "warning":
            env = envelope(i, frames, 0.04, 1.2)
            pulse = 1.0 if int(t * 8.0) % 2 == 0 else 0.38
            frequency = (690.0 + 70.0 * math.sin(math.tau * 2.0 * t)) * variation
            value = env * pulse * (
                0.78 * math.sin(math.tau * frequency * t + phase)
                + 0.22 * math.sin(math.tau * frequency * 2.0 * t)
            )
        else:
            raise ValueError(f"Unsupported preset: {preset}")

        samples.append(value)

    peak = max((abs(value) for value in samples), default=1.0)
    scale = 0.85 / max(peak, 1e-9)
    return [max(-1.0, min(1.0, value * scale)) for value in samples]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate deterministic basic game SFX as mono PCM16 WAV."
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    parser.add_argument("--preset", choices=PRESETS, required=True)
    parser.add_argument("--duration-ms", type=int)
    parser.add_argument("--sample-rate", type=int, default=48000)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    duration_ms = (
        args.duration_ms
        if args.duration_ms is not None
        else DEFAULT_DURATION_MS[args.preset]
    )
    if not 20 <= duration_ms <= 5000:
        raise SystemExit("--duration-ms must be between 20 and 5000")
    if not 8000 <= args.sample_rate <= 192000:
        raise SystemExit("--sample-rate must be between 8000 and 192000")
    if args.output.suffix.lower() != ".wav":
        raise SystemExit("--output must use the .wav extension")
    if args.output.exists():
        raise SystemExit(f"Refusing to overwrite existing file: {args.output}")

    frames = max(1, round(args.sample_rate * duration_ms / 1000.0))
    samples = synthesize(args.preset, frames, args.sample_rate, args.seed)
    pcm = b"".join(struct.pack("<h", round(value * 32767.0)) for value in samples)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(args.output), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(args.sample_rate)
        wav.writeframes(pcm)

    peak = max(abs(value) for value in samples)
    print(json.dumps({
        "output": str(args.output.resolve()),
        "preset": args.preset,
        "duration_ms": duration_ms,
        "sample_rate": args.sample_rate,
        "channels": 1,
        "sample_width_bits": 16,
        "frames": frames,
        "peak_linear": round(peak, 6),
        "seed": args.seed,
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
