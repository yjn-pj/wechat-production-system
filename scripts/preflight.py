#!/usr/bin/env python3
import argparse
import re
import unicodedata
from pathlib import Path
from urllib.parse import urlparse


REQUIRED = {
    "standard": ("article.md", "title-options.md", "publish-check.md", "research/source-ledger.md"),
    "deep": ("article.md", "title-options.md", "publish-check.md", "research/source-ledger.md"),
}


def has_source_section(text: str) -> bool:
    return bool(re.search(r"^#{1,3}\s*(参考|来源|References?)", text, flags=re.I | re.M))


def cjk_count(text: str) -> int:
    return sum(1 for char in text if "CJK" in unicodedata.name(char, ""))


def main() -> None:
    parser = argparse.ArgumentParser(description="Mechanical preflight for a WeChat article package.")
    parser.add_argument("package", type=Path)
    parser.add_argument("--mode", choices=("quick", "standard", "deep"), default="standard")
    parser.add_argument("--min-chars", type=int)
    parser.add_argument("--no-min-length", action="store_true")
    args = parser.parse_args()

    package = args.package.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    article_character_count = 0

    if not package.is_dir():
        raise SystemExit(f"Package not found: {package}")

    for name in REQUIRED.get(args.mode, ("article.md",)):
        if not (package / name).is_file():
            errors.append(f"missing {name}")

    article = package / "article.md"
    if article.is_file():
        text = article.read_text(encoding="utf-8")
        if not text.lstrip().startswith("# "):
            errors.append("article has no level-1 title")
        if args.mode != "quick" and not has_source_section(text):
            errors.append("article has no references section")
        if not re.search(r"!\[", text):
            errors.append("article has no images")
        for image in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
            path = image if urlparse(image).scheme else package / image
            if not path.exists():
                errors.append(f"missing image: {image}")
        image_count = len(re.findall(r"!\[", text))
        heading_count = len(re.findall(r"\n#{2,}\s", text))
        char_count = cjk_count(text)
        article_character_count = char_count
        minimum_chars = 0 if args.no_min_length else (
            args.min_chars
            if args.min_chars is not None
            else {"quick": 0, "standard": 2000, "deep": 3500}[args.mode]
        )
        minimum_headings = {"quick": 1, "standard": 5, "deep": 7}[args.mode]
        minimum_images = {"quick": 0, "standard": 3, "deep": 4}[args.mode]
        if char_count < minimum_chars:
            errors.append(f"article too short: {char_count}/{minimum_chars} Chinese characters")
        if heading_count < minimum_headings:
            errors.append(f"too few sections: {heading_count}/{minimum_headings}")
        if image_count < minimum_images:
            errors.append(f"too few images: {image_count}/{minimum_images}")

    ledger = package / "research/source-ledger.md"
    if ledger.is_file() and args.mode in {"standard", "deep"}:
        rows = [
            line
            for line in ledger.read_text(encoding="utf-8").splitlines()
            if line.startswith("|") and not re.match(r"^\|\s*(Claim|---)", line, flags=re.I)
        ]
        if not rows:
            errors.append("source ledger has no fact rows")

    title_file = package / "title-options.md"
    if title_file.is_file():
        titles = [line for line in title_file.read_text(encoding="utf-8").splitlines() if re.match(r"^\d+\.\s+\S", line)]
        if len(titles) < 10:
            warnings.append(f"title options: {len(titles)}/10")

    print(f"Package: {package}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        raise SystemExit(1)
    print(f"Chinese characters: {article_character_count}")
    print("Mechanical checks passed. Still require human fact, tone, title, and visual review.")


if __name__ == "__main__":
    main()
