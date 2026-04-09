# Changelog

All notable changes to Dataset Metadata Augmenter will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-04-08

### 🚀 Major Features

#### OpenMetadata Integration
- **Push to OpenMetadata**: Direct integration with OpenMetadata v1.3+ data catalogs
- Automatically creates Service → Database → Schema → Table hierarchy
- Pushes column metadata with data types and statistics
- Rich descriptions with source information
- CORS proxy server (`server.py`) for local development
- Test connection button with auth validation

#### World Bank Metadata Standards
- Replaced all schema presets with 5 official World Bank metadata standards:
  - 📊 **Microdata (DDI 2.5)**: Surveys, censuses, unit-level data (31 fields)
  - 📄 **Document**: Reports, publications, PDFs (33 fields)
  - 📈 **Timeseries**: Time-based indicators, WDI-style data (33 fields)
  - 📋 **Table**: Statistical tables, cross-tabulations (30 fields)
  - 🗺️ **Geospatial (ISO 19115)**: GIS data, maps, satellite imagery (40 fields)
- Each field includes descriptions for better AI inference

#### Custom Schema Management
- **Save as Default**: Set your preferred schema as the default
- **Save Custom Schemas**: Create named schema presets for different workflows
- **Load/Delete Custom Schemas**: Manage your saved schemas
- Schemas persist across sessions in localStorage

#### DuckDuckGo Web Search Integration
- **Free web search**: No API key required
- Searches for dataset context, license info, methodology
- Results injected into LLM prompt for better metadata inference
- Toggle on/off in Settings
- Test search button to verify functionality

#### URL Fetching with CORS Proxy Fallbacks
- **Fetch Source URL**: Extract metadata from dataset source pages
- **4 CORS proxy fallbacks**: Automatic failover if one proxy fails
  - corsproxy.io
  - allorigins.win
  - corsproxy.org
  - codetabs.com
- Extracts title, description, keywords from web pages

#### Enhanced LLM Support
- **Updated model lists** for all providers (April 2026):
  - Anthropic: Claude Opus 4.5/4.6, Sonnet 4.5/4.6, Haiku 4.5
  - OpenAI: GPT-5.4, GPT-4.1, o4-mini (with web search via Responses API)
  - Google: Gemini 3.1 Pro, Gemini 2.5 Pro/Flash/Lite
  - Mistral: Magistral Medium/Small, Codestral
  - Perplexity: Sonar, Sonar Pro, Sonar Reasoning (with built-in web search)
- **Web search models**: OpenAI and Perplexity models with live web search
- **Per-field inference**: Click to infer individual fields with AI

#### Custom / Local Model Support (NEW)
- **Use any model**: Ollama, LM Studio, vLLM, text-generation-webui, or any OpenAI-compatible API
- **Configurable settings**: Endpoint URL, model name, max tokens, temperature
- **API format options**: OpenAI-compatible (default) or Anthropic-compatible
- **No API key required**: For local models running on your machine
- **Popular local models**: llama3, mistral, codellama, phi3, gemma2, qwen2

#### Full Data Statistics for Accurate Metadata (NEW)
- **Time range computed from ALL data**: Not just sample rows
- **Complete geographic coverage**: All unique states/districts/regions
- **All categorical values**: Full list for columns with ≤100 unique values
- **True numeric ranges**: Min/max from entire dataset
- **Year detection**: Automatically identifies year columns and extracts all years

### ✨ Improvements

#### UI/UX
- Improved Settings page with better organization
- OpenMetadata configuration section with setup instructions
- Web Search section with toggle and test button
- Schema preset buttons with tooltips and descriptions
- Better toast notifications with emoji indicators
- Footer with author attribution
- Dataset action menu with more options

#### Data Processing
- Column statistics now include sample values
- Better data type detection (numeric, date, string)
- Improved fill rate and unique value counting
- Statistics dashboard for uploaded files

#### Export Options
- Export as CSV
- Export as Excel (.xlsx)
- Export as JSON (metadata only or full)
- Push to OpenMetadata

#### Code Quality
- Better error handling throughout
- Console logging for debugging
- Cleaner code organization
- Modular function structure

### 🐛 Bug Fixes
- Fixed schema preset loading issues
- Fixed 409 conflict handling in OpenMetadata integration
- Fixed proxy status code passthrough
- Fixed tag validation errors (tags now optional)
- Fixed CORS issues with multiple proxy fallbacks

### 📁 New Files
- `server.py`: CORS proxy server for OpenMetadata integration
- `CHANGELOG.md`: Version history documentation

---

## [1.0.0] - 2024-12-01

### Initial Release

#### Features
- Multi-provider LLM support (Anthropic, OpenAI, Google, Mistral)
- Dynamic schema builder with field types
- CSV/Excel/JSON file upload with preview
- AI-powered metadata augmentation
- In-data statistics computation
- Local persistence with localStorage
- Dark mode support
- Export to JSON format

#### Schema Presets
- Government Dataset
- Survey Data
- Time Series

---

## Version Naming

- **Major (X.0.0)**: Breaking changes, major new features
- **Minor (0.X.0)**: New features, backwards compatible
- **Patch (0.0.X)**: Bug fixes, minor improvements
