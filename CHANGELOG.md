# Changelog

All notable changes to the Dataset Metadata Augmenter project.

## [2.1.0] - 2026-04-15

### Added
- **Quality Scoring System** — Two-agent architecture for metadata quality assurance
  - Proponent Agent generates metadata values
  - Judge Agent scores each field (0-10) using World Bank rubric
  - Per-field quality indicators (🟢 🟡 🔴)
  - Quality Summary Card with overall score and progress bar
- **Editable Feedback** — Modify judge's suggestions before regenerating
- **Accept/Decline/Dismiss Actions** — Three options for each low-scoring field
- **Regeneration with Feedback** — Up to 3 attempts per field
- **Re-Judge All** — Button to re-assess quality after manual edits
- **Quality Scoring Matrix** — Documentation added to Guide page
- **Ashoka Datalake Schema Preset** — 18 fields for social sector datasets in India
- **Professional Landing Page** — Hero section, feature cards, comparison table
- **Getting Started Guide** — Step-by-step documentation
- **Site Navigation** — Home, Guide, Tool, GitHub links
- **Light/Dark Theme Toggle** — With localStorage persistence
- **Modern Design System** — DM Sans typography, gradient accents, glassmorphism nav

### Fixed
- Export dropdowns now collapse properly when clicking outside
- Schema import handles multiple JSON formats (native, Field/Description, string array)
- Removed auto-enum detection — all fields default to text with AI inference enabled

### Changed
- Feedback only shows for fields scoring < 7 (cleaner UI)
- Theme toggle persists across sessions


## [2.0.0] - 2026-04-13

### Added
- **OpenMetadata Integration** — Push datasets directly to OpenMetadata catalog
  - Automatic DatabaseService → Database → Schema → Table creation
  - JWT authentication support
  - CORS proxy (server.py) for browser-based integration
- **Web Search Integration** — DuckDuckGo search for enhanced context
- **Source URL Fetching** — Extract metadata from data portal pages
- **Full Data Statistics** — Compute stats from entire dataset, not just samples
- **Custom Schema Management** — Save, load, and manage custom schemas
- **Multiple Export Formats** — CSV, Excel, JSON, Full Dataset

### Changed
- Complete UI redesign with card-based layout
- Improved prompt engineering for better metadata quality
- Enhanced statistics display with column-level details


## [1.0.0] - 2026-04-10

### Added
- Initial release
- **LLM Integration** — Support for Anthropic, OpenAI, Google, Mistral, Perplexity
- **Local Model Support** — Ollama and LM Studio via custom endpoint
- **Schema Presets** — 5 World Bank metadata standards:
  - Microdata (DDI 2.5) — 31 fields
  - Document — 33 fields
  - Timeseries — 33 fields
  - Table — 30 fields
  - Geospatial (ISO 19115) — 40 fields
- **CSV/Excel Upload** — Papa Parse and SheetJS integration
- **Per-field Inference** — Generate individual metadata fields
- **Metadata Export** — CSV, Excel, JSON formats


---

## Version History

| Version | Date | Highlights |
|---------|------|------------|
| 2.1.0 | 2026-04-15 | Quality scoring, UI redesign, Ashoka preset |
| 2.0.0 | 2026-04-13 | OpenMetadata integration, web search |
| 1.0.0 | 2026-04-10 | Initial release |
