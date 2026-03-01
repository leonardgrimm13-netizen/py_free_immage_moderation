# py_free_immage_moderation
A flexible Python project for **image and GIF moderation** with multiple engines (local + API), pHash lists, and clear CLI output.

**Languages:** **English** | [Deutsch](README.de.md)

## Contents
- [Features](#-features)
- [Project structure](#-project-structure)
- [Installation](#-installation)
- [Quickstart](#-quickstart)
- [Verification](#-verification)
- [Important configuration (.env)](#-important-configuration-env)
- [Result logic (OK / REVIEW / BLOCK)](#-result-logic-ok--review--block)
- [Tips for running](#-tips-for-running)

---

## ✨ Features
- **Multi-stage moderation** for single images, GIFs, directories, and URLs
- **pHash allowlist/blocklist** for very fast short-circuit decisions
- **OCR text check** (e.g., against text blocklists)
- Combinable engines:
  - `OpenNSFW2`
  - `NudeNet`
  - `YOLO` (weapon detection)
  - `OpenAI Moderation` (optional via API key)
  - `Sightengine` (optional via API credentials)
- **GIF handling** with configurable frame sampling
- **JSON export** for further processing in pipelines
- **Conservative verdict logic** with clear, traceable reasons

---

## 📁 Project structure
```text
py_free_immage_moderation/
├── moderate_image.py         # Entry point (CLI wrapper)
├── requirements.txt
├── requirements_api.txt
├── data/
│   ├── phash_allowlist.txt
│   ├── phash_blocklist.txt
│   └── ocr_text_blocklist.txt
└── modimg/
    ├── cli.py               # Args, output, JSON export
    ├── pipeline.py          # Flow & engine orchestration
    ├── verdict.py           # Final decision logic
    ├── frames.py            # Image/GIF frame loading
    ├── phash.py             # pHash utilities
    ├── config.py            # .env loading
    └── engines/             # Individual moderation engines
