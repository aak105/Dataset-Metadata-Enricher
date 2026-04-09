# 📚 Dataset Metadata Augmenter

> AI-powered metadata enrichment for research datasets with OpenMetadata integration

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/aak105/Dataset-Metadata-Enricher/releases)
[![OpenMetadata](https://img.shields.io/badge/OpenMetadata-v1.3+-green.svg)](https://open-metadata.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

## Overview

Dataset Metadata Augmenter is a browser-based tool that helps researchers and data professionals catalog datasets with AI-powered metadata extraction. It supports multiple LLM providers and integrates directly with OpenMetadata for enterprise data catalog management.

**🌐 Live Demo**: [aak105.github.io/Dataset-Metadata-Enricher](https://aak105.github.io/Dataset-Metadata-Enricher/)

### Key Features

| Feature | Description |
|---------|-------------|
| 🤖 **Multi-LLM Support** | Anthropic Claude, OpenAI GPT, Google Gemini, Mistral AI, Perplexity |
| 🏠 **Custom / Local Models** | Ollama, LM Studio, vLLM, or any OpenAI-compatible API |
| 📊 **OpenMetadata Integration** | Push cataloged datasets directly to your data catalog |
| 🌍 **World Bank Standards** | Schema presets based on official IHSN/World Bank metadata schemas |
| 💾 **Custom Schemas** | Save and reuse your own metadata templates |
| 🔍 **DuckDuckGo Web Search** | Free web search for context-aware augmentation (no API key needed) |
| 🌐 **URL Fetching** | Extract metadata from source URLs with CORS proxy fallbacks |
| 📈 **Auto Statistics** | Column-level fill rates, unique counts, data types, samples |
| 🎨 **Dark Mode** | Automatic theme switching based on system preferences |

---

## What's New in v2.0

### 🔗 OpenMetadata Integration
Push your cataloged datasets directly to OpenMetadata with one click:
- Automatic Service → Database → Schema → Table hierarchy creation
- Column metadata with statistics and data types
- Rich descriptions from AI-generated metadata

### 🌍 World Bank Metadata Standards
Five schema presets based on official standards:
- **Microdata (DDI 2.5)** — Surveys, censuses, unit-level data
- **Document** — Reports, publications, research papers
- **Timeseries** — Indicators, time-based statistics
- **Table** — Statistical tables, cross-tabulations
- **Geospatial (ISO 19115)** — GIS data, maps, satellite imagery

### ⭐ Custom Schema Management
- Save current schema as your default
- Create named custom schemas for different workflows
- Schemas persist across browser sessions

### 🔍 DuckDuckGo Web Search
- Free web search integration (no API key required!)
- Searches for dataset context, license info, methodology
- Results enhance LLM prompts for better metadata inference
- Toggle on/off in Settings with test button

### 🌐 URL Fetching with CORS Proxies
- Fetch metadata from dataset source URLs
- 4 automatic CORS proxy fallbacks for reliability
- Extracts title, description, keywords from web pages

### 🏠 Custom / Local Model Support
- Use **any OpenAI-compatible API** (Ollama, LM Studio, vLLM, text-generation-webui)
- Configure endpoint URL, model name, max tokens, temperature
- **No API key required** for local models
- Popular models: llama3, mistral, codellama, phi3, gemma2, qwen2

### 📈 Full Data Statistics
- Time range computed from **entire dataset** (not just samples)
- Complete geographic coverage with all unique locations
- All categorical values for low-cardinality columns
- Accurate numeric ranges from full data scan

---

## Quick Start

### Option 1: Use Online (No Install)
Visit **[aak105.github.io/Dataset-Metadata-Enricher](https://aak105.github.io/Dataset-Metadata-Enricher/)**

### Option 2: Download & Run Locally
```bash
# Download index.html
# Open in any modern browser
# Configure your LLM API key in Settings
```

### Option 3: With OpenMetadata Integration
```bash
# Clone the repository
git clone https://github.com/aak105/Dataset-Metadata-Enricher.git
cd Dataset-Metadata-Enricher

# Start the CORS proxy server
python3 server.py

# Open http://localhost:3000 in your browser
```

---

## Usage Guide

### 1. Configure LLM Provider
Go to **Settings** tab:
- Select your LLM provider (Anthropic, OpenAI, Google, Mistral, Perplexity)
- Choose a model
- Enter your API key

> 🔒 **Security**: API keys are stored only in browser memory, never persisted.

### 2. Enable Web Search (Optional)
In **Settings** → Web Search Enhancement:
- Toggle "Enable Web Search (DuckDuckGo)"
- Click "Test Search" to verify it works
- No API key needed!

### 3. Set Up Schema
Go to **Schema** tab:
- Load a World Bank preset (Microdata, Document, Timeseries, Table, Geospatial)
- Or create custom fields
- Save as your default or a named custom schema

### 4. Upload & Augment
Go to **Datasets** tab:
- Upload CSV, Excel, or JSON files
- Optionally add Source URL for context
- Click **🤖 Augment with AI** to auto-fill metadata
- Review and edit as needed

### 5. Export or Push
- **Export CSV/Excel/JSON**: Download for local use
- **Push to OpenMetadata**: Sync to your data catalog (requires `server.py`)

---

## OpenMetadata Setup

### Prerequisites
- OpenMetadata v1.3+ running locally or in cloud
- JWT token from OpenMetadata (Settings → Bots → ingestion-bot → Copy Token)

### Configuration
1. Start the proxy server: `python3 server.py`
2. Open http://localhost:3000
3. Go to **Settings** → OpenMetadata Integration:
   - **URL**: `http://localhost:8585` (or your OM instance)
   - **JWT Token**: Paste from OpenMetadata
   - **Service Name**: e.g., `dataset_augmenter`
   - **Database Name**: e.g., `research`
4. Click **Test Connection**

### Pushing Datasets
1. Upload and augment a dataset
2. Click the ⋮ menu → **Push to OpenMetadata**
3. View in OpenMetadata under: Service → Database → default → Your Table

---

## Schema Presets

### World Bank Metadata Standards

| Preset | Fields | Use Case |
|--------|--------|----------|
| 📊 Microdata (DDI) | 31 | Surveys (NSSO, PLFS), censuses, unit-level records |
| 📄 Document | 33 | Reports, PDFs, publications, working papers |
| 📈 Timeseries | 33 | WDI-style indicators, RBI statistics, annual data |
| 📋 Table | 30 | Statistical tables, DES crop data, census tables |
| 🗺️ Geospatial | 40 | Shapefiles, GeoJSON, satellite imagery, maps |

All presets include field descriptions for better AI inference.

---

## Supported LLM Providers

| Provider | Models | Web Search |
|----------|--------|------------|
| **Anthropic** | Claude Opus 4.5/4.6, Sonnet 4.5/4.6, Haiku 4.5 | ❌ |
| **OpenAI** | GPT-5.4, GPT-4.1, GPT-4o, o4-mini | ✅ (via Responses API) |
| **Google** | Gemini 3.1 Pro, 2.5 Pro/Flash/Lite | ❌ |
| **Mistral** | Magistral Medium/Small, Codestral | ❌ |
| **Perplexity** | Sonar, Sonar Pro, Sonar Reasoning | ✅ (built-in) |
| **Custom / Local** | Any model (Ollama, LM Studio, vLLM) | ❌ |

**Bonus**: DuckDuckGo web search works with ANY provider!

### Using Local Models (Ollama, LM Studio)

1. Start your local model server:
   ```bash
   # Ollama
   ollama serve
   ollama run llama3
   
   # LM Studio
   # Start server in LM Studio UI → Local Server tab
   ```

2. In Settings, select **"Custom / Local Model"**

3. Configure:
   - **Endpoint**: `http://localhost:11434/v1/chat/completions` (Ollama) or `http://localhost:1234/v1/chat/completions` (LM Studio)
   - **Model Name**: `llama3`, `mistral`, etc.
   - **API Key**: Leave blank for local models

4. Click **Test Connection**

---

## File Structure

```
Dataset-Metadata-Augmenter/
├── index.html          # Main application (standalone)
├── server.py           # CORS proxy for OpenMetadata
├── README.md           # This file
├── CHANGELOG.md        # Version history
├── LICENSE             # MIT License
├── CONTRIBUTING.md     # Contribution guidelines
└── react-app/          # Future React migration scaffold
```

---

## Privacy & Security

- ✅ **No server required**: Runs entirely in your browser
- ✅ **No tracking**: No analytics or telemetry
- ✅ **API keys in memory only**: Never saved to disk
- ✅ **Local data storage**: Uses localStorage, stays on your device
- ✅ **Direct LLM calls**: Data goes only to your chosen provider

---

## Roadmap

### v2.1 (Planned)
- [ ] Fetch tags/classifications from OpenMetadata
- [ ] Constrained LLM outputs to match OM taxonomy
- [ ] Glossary term creation
- [ ] Batch push multiple datasets

### v2.2 (Planned)
- [ ] Two-way sync with OpenMetadata
- [ ] Column-level PII detection
- [ ] Data lineage tracking
- [ ] Quality score computation

### v3.0 (Future)
- [ ] React migration
- [ ] Backend service option
- [ ] Team collaboration features

---

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

```bash
# Development
# Edit index.html directly, open in browser to test
# No build step required for the standalone version
```

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

## Author

**Aakash Sharma**  
[LinkedIn](https://www.linkedin.com/in/aakashsharma8a6888131/)

---

## Acknowledgments

- [World Bank Metadata Schemas](https://github.com/worldbank/metadata-schemas)
- [OpenMetadata](https://open-metadata.org/)
- [PapaParse](https://www.papaparse.com/) for CSV parsing
- [SheetJS](https://sheetjs.com/) for Excel support
- [DuckDuckGo](https://duckduckgo.com/) for free web search

---

**Made with ❤️ for researchers working with secondary data**
