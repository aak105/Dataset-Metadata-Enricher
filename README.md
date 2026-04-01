# 📚 Dataset Metadata Augmenter

> AI-powered metadata enrichment for research datasets from government and open data platforms

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

## Overview

Dataset Metadata Augmenter is a client-side web application that helps researchers and data professionals catalog and enrich secondary datasets with AI-powered metadata extraction. It's particularly useful for government datasets from platforms like data.gov.in, Census India, RBI, and similar open data portals.

### Key Features

- **🤖 LLM-Agnostic**: Works with Anthropic Claude, OpenAI GPT-4, Google Gemini, and Mistral AI
- **📊 Multi-Format Upload**: Supports CSV, Excel (.xlsx, .xls), JSON, TSV, and text files
- **🔧 Dynamic Schema Builder**: Customize metadata fields with types, validation, and AI inference toggles
- **📈 In-Data Statistics**: Automatic computation of fill rates, unique values, and data types
- **💾 Local Persistence**: Your data stays in your browser — nothing sent to external servers except LLM calls
- **🎨 Dark Mode Support**: Automatic theme switching based on system preferences

## Screenshots

*Coming soon*

## Quick Start

### Option 1: Just Use It

1. Download `index.html`
2. Open it in any modern browser
3. Configure your LLM API key in Settings
4. Start uploading datasets!

### Option 2: GitHub Pages

1. Fork this repository
2. Enable GitHub Pages in repository settings
3. Access at `https://[your-username].github.io/Dataset-Metadata-Augmenter`

### Option 3: Local Development

```bash
# Clone the repository
git clone https://github.com/[username]/Dataset-Metadata-Augmenter.git
cd Dataset-Metadata-Augmenter

# For the standalone HTML version, just open index.html
open index.html

# For the React version (future)
cd react-app
npm install
npm run dev
```

## Usage Guide

### 1. Configure LLM Provider

Go to **Settings** and:
- Select your preferred LLM provider
- Choose a model
- Enter your API key

> 🔒 **Security Note**: Your API key is stored only in browser memory for the current session. It's never persisted to disk or sent anywhere except directly to your chosen LLM provider.

### 2. Customize Schema (Optional)

Go to **Schema** to:
- Add/remove metadata fields
- Set field types (text, enum, tags, date, etc.)
- Mark fields as required
- Toggle AI inference per field
- Load presets for common use cases

**Available Presets:**
- 📋 Government Dataset
- 📝 Survey Data
- 📈 Time Series

### 3. Upload Datasets

Go to **Datasets** and:
- Click "Upload Dataset" or drag-and-drop files
- Preview data before importing
- Review automatic statistics

**Supported Formats:**
- CSV, TSV
- Excel (.xlsx, .xls)
- JSON (array of objects)
- Plain text

### 4. Augment with AI

Open a dataset and:
1. Fill in the Source URL (important for context)
2. Click "🤖 Augment with AI"
3. Watch the augmentation log
4. Review and edit inferred metadata

### 5. Export

- **Export Metadata**: JSON with just the metadata and schema
- **Export Full**: JSON with metadata, schema, data, and statistics

## Schema Field Types

| Type | Description | Example |
|------|-------------|---------|
| `text` | Single-line text | "Ministry of Agriculture" |
| `longtext` | Multi-line text | Methodology notes |
| `url` | Web URL | "https://data.gov.in/..." |
| `date` | Date picker | "2024-01-15" |
| `enum` | Dropdown options | "Annual", "Quarterly" |
| `tags` | Comma-separated | "agriculture, crops, yield" |
| `number` | Numeric value | 35000 |
| `boolean` | Yes/No | true |

## Architecture

```
Dataset-Metadata-Augmenter/
├── index.html          # Standalone single-file application
├── README.md           # This file
├── LICENSE             # MIT License
├── CONTRIBUTING.md     # Contribution guidelines
├── .gitignore          # Git ignore rules
│
└── react-app/          # Future React migration scaffold
    ├── package.json
    ├── vite.config.js
    ├── index.html
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── components/
        ├── hooks/
        ├── utils/
        └── styles/
```

## Roadmap

### v1.0 (Current)
- [x] Multi-provider LLM support
- [x] Dynamic schema builder
- [x] CSV/Excel/JSON upload
- [x] In-data statistics
- [x] Local persistence
- [x] Dark mode

### v1.1 (Planned)
- [ ] Batch augmentation for multiple datasets
- [ ] Source URL web fetching (with CORS proxy)
- [ ] DCAT-AP export format
- [ ] Schema.org/Dataset export

### v1.2 (Planned)
- [ ] Comparison view for multiple datasets
- [ ] Metadata quality scoring
- [ ] Duplicate detection
- [ ] Data lineage tracking

### v2.0 (Future)
- [ ] React migration for better maintainability
- [ ] Backend service for web fetching
- [ ] User authentication
- [ ] Cloud sync (optional)
- [ ] Team collaboration

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

For the standalone HTML version:
1. Edit `index.html` directly
2. Open in browser to test
3. No build step required

For future React version:
```bash
cd react-app
npm install
npm run dev
```

## API Costs

This tool uses your own LLM API keys. Typical costs per dataset augmentation:

| Provider | Model | ~Cost |
|----------|-------|-------|
| Anthropic | Claude Sonnet | $0.01-0.03 |
| Anthropic | Claude Haiku | $0.001-0.005 |
| OpenAI | GPT-4o | $0.01-0.03 |
| OpenAI | GPT-4o-mini | $0.001-0.005 |
| Google | Gemini 1.5 Pro | $0.01-0.02 |
| Mistral | Large | $0.01-0.02 |

*Estimates based on ~2000 tokens per augmentation request*

## Privacy & Security

- **No server**: Everything runs in your browser
- **No tracking**: No analytics or telemetry
- **API keys**: Stored only in memory, never persisted
- **Data storage**: Uses localStorage, stays on your device
- **LLM calls**: Go directly to your chosen provider

## License

MIT License — see [LICENSE](LICENSE) for details.

## Acknowledgments

- Built for the research data community
- Inspired by challenges in cataloging Indian government datasets
- Uses [PapaParse](https://www.papaparse.com/) for CSV parsing
- Uses [SheetJS](https://sheetjs.com/) for Excel support
- Uses [Chart.js](https://www.chartjs.org/) for visualizations

---

**Made with ❤️ for researchers working with secondary data**
