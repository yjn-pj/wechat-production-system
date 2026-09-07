#!/usr/bin/env python3
import argparse
from pathlib import Path


TEMPLATES = {
    "research/source-ledger.md": """# Source ledger\n\n| Claim | Source | URL | Accessed | Evidence | Confidence | Article location |\n|---|---|---:|---|---|---|---|\n""",
    "title-options.md": "# Title options\n\n1. \n2. \n3. \n4. \n5. \n6. \n7. \n8. \n9. \n10. \n\nRecommended: \n",
    "publish-check.md": "# Publish check\n\n- [ ] Facts verified\n- [ ] Evidence screenshots\n- [ ] Diagram added\n- [ ] AI tone edited\n- [ ] Visuals inspected\n- [ ] Risks disclosed\n",
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a WeChat article production package.")
    parser.add_argument("slug")
    parser.add_argument("--root", default="outputs")
    parser.add_argument("--mode", choices=("quick", "standard", "deep"), default="standard")
    args = parser.parse_args()

    package = Path(args.root) / args.slug
    if package.exists():
        raise SystemExit(f"Package already exists: {package}")

    (package / "images").mkdir(parents=True)
    (package / "prompts").mkdir()
    (package / "research").mkdir()
    (package / "article.md").write_text(f"# {args.slug}\n\n")
    for relative_path, template in TEMPLATES.items():
        if args.mode == "quick" and relative_path == "research/source-ledger.md":
            continue
        target = package / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(template)

    print(package.resolve())


if __name__ == "__main__":
    main()
