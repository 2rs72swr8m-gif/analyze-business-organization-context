"""Generate a PDF from a complete HTML industry-research report.

Usage:
    python generate_pdf.py HTML_PATH [OUTPUT_PDF_PATH] [HEADER_TEXT]
"""

from __future__ import annotations

import argparse
import asyncio
from html import escape
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html_path", type=Path)
    parser.add_argument("output_pdf_path", nargs="?", type=Path)
    parser.add_argument("header_text", nargs="?", default="企业战略、组织与人力研究报告")
    return parser.parse_args()


async def generate_pdf(html_path: Path, pdf_path: Path, header_text: str) -> None:
    try:
        from playwright.async_api import async_playwright
    except ImportError as exc:
        raise SystemExit(
            "缺少 Playwright。请安装 playwright，并运行 `playwright install chromium`。"
        ) from exc

    header = (
        '<div style="font-size:8pt;color:#777;text-align:center;width:100%;'
        'font-family:Arial,\'Microsoft YaHei\',sans-serif;line-height:1;'
        f'padding-top:2mm">{escape(header_text)}</div>'
    )
    footer = (
        '<div style="font-size:8pt;color:#777;text-align:center;width:100%;'
        'font-family:Arial,\'Microsoft YaHei\',sans-serif;line-height:1">'
        '<span class="pageNumber"></span></div>'
    )

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page()
        await page.goto(html_path.as_uri(), wait_until="networkidle")
        await page.emulate_media(media="print")

        await page.evaluate(
            """() => {
                const cover = document.querySelector('.header, .cover');
                if (!cover) return;
                cover.style.minHeight = '241mm';
                cover.style.display = 'flex';
                cover.style.flexDirection = 'column';
                cover.style.justifyContent = 'center';
                cover.style.alignItems = 'center';
            }"""
        )

        await page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template=header,
            footer_template=footer,
            margin={"top": "28mm", "bottom": "28mm", "left": "22mm", "right": "22mm"},
        )
        await browser.close()


def main() -> None:
    args = parse_args()
    html_path = args.html_path.expanduser().resolve()
    if not html_path.is_file():
        raise SystemExit(f"HTML 文件不存在：{html_path}")
    if html_path.suffix.lower() not in {".html", ".htm"}:
        raise SystemExit(f"输入文件不是 HTML：{html_path}")

    pdf_path = (
        args.output_pdf_path.expanduser().resolve()
        if args.output_pdf_path
        else html_path.with_suffix(".pdf")
    )
    if pdf_path.suffix.lower() != ".pdf":
        raise SystemExit(f"输出文件必须使用 .pdf 扩展名：{pdf_path}")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    asyncio.run(generate_pdf(html_path, pdf_path, args.header_text))
    print(f"PDF saved: {pdf_path} ({pdf_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
