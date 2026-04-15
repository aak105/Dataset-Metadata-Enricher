# Dataset Metadata Augmenter

An AI-powered tool for enriching dataset metadata using LLMs. Upload a CSV or Excel file, and the tool will automatically generate comprehensive metadata based on the data structure, column names, sample values, and optionally the source URL.

🔗 **Live Demo:** [aak105.github.io/Dataset-Metadata-Enricher](https://aak105.github.io/Dataset-Metadata-Enricher/)

![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-2.1.0-green.svg)

## Features

### 🤖 AI-Powered Metadata Generation
- Supports multiple LLM providers: Anthropic Claude, OpenAI GPT, Google Gemini, Mistral, and Perplexity
- Local model support via Ollama or LM Studio
- Web search integration for enhanced context (DuckDuckGo)
- Automatic source URL fetching for additional context

### ⚖️ Quality Scoring System (NEW in v2.1)
- **Two-agent architecture**: Proponent generates metadata, Judge scores quality (0-10)
- **Per-field scoring** with visual indicators (🟢 🟡 🔴)
- **Editable feedback** — modify judge suggestions before regenerating
- **Accept/Decline/Dismiss** actions for each field
- **Up to 3 regeneration attempts** per field with feedback loop

### 📋 Schema Presets
Based on [World Bank Metadata Standards](https://github.com/worldbank/metadata-schemas):
- **Microdata (DDI 2.5)** — Surveys, censuses, unit-level data (31 fields)
- **Document** — Reports, publications, PDFs (33 fields)
- **Timeseries** — Economic indicators, time-indexed statistics (33 fields)
- **Table** — Statistical tables, cross-tabulations (30 fields)
- **Geospatial (ISO 19115)** — GIS data, maps, satellite imagery (40 fields)
- **Ashoka Datalake** — Social sector datasets for India (18 fields)

### 🔗 OpenMetadata Integration
- Push enriched datasets directly to your OpenMetadata catalog
- Automatic creation of DatabaseService → Database → Schema → Table hierarchy
- CORS proxy included for browser-based integration

### 📤 Export Options
- CSV, Excel, JSON formats
- Full dataset export with data + metadata
- Direct push to OpenMetadata

## Quick Start

### Option 1: Use Online (No Installation)
Visit [aak105.github.io/Dataset-Metadata-Enricher](https://aak105.github.io/Dataset-Metadata-Enricher/)

### Option 2: Run Locally

```bash
# Clone the repository
git clone https://github.com/aak105/Dataset-Metadata-Enricher.git
cd Dataset-Metadata-Enricher

# Open in browser
open index.html
# or
python -m http.server 8000  # then visit http://localhost:8000
```

### Option 3: With OpenMetadata Integration

```bash
# Start the CORS proxy
python server.py

# The proxy runs at http://localhost:3000
# Configure OpenMetadata URL in Settings tab
```

## Usage

1. **Configure LLM** — Go to Settings and enter your API key (Anthropic, OpenAI, Google, etc.)
2. **Select Schema** — Choose a preset or customize fields in the Schema tab
3. **Upload Dataset** — Drag and drop a CSV or Excel file
4. **Add Source URL** (optional) — Paste the data portal URL for better context
5. **Generate Metadata** — Click "Augment with AI"
6. **Review Quality** — Check scores, edit feedback, regenerate low-scoring fields
7. **Export** — Download as CSV/Excel/JSON or push to OpenMetadata

## Quality Scoring Rubric

| Score | Rating | Description |
|-------|--------|-------------|
| 9-10 | 🟢 Excellent | Clear, precise, contextually relevant, aligned with standards |
| 7-8 | 🟢 Good | Mostly clear and accurate, minor issues |
| 5-6 | 🟡 Satisfactory | Understandable but lacks precision or specificity |
| 3-4 | 🔴 Needs Improvement | Lacks clarity, broad, or technically inaccurate |
| 0-2 | 🔴 Poor | Unclear, irrelevant, or unusable |

## Local LLM Setup

### Using Ollama
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull a model
ollama pull llama3

# Ollama runs at http://localhost:11434 by default
```

In the tool, select "Custom / Local Model" and use:
- Endpoint: `http://localhost:11434/v1/chat/completions`
- Model: `llama3`

### Using LM Studio
1. Download and install LM Studio
2. Load a model (e.g., Mistral, Llama)
3. Start the local server (default port 1234)
4. Configure endpoint: `http://localhost:1234/v1/chat/completions`

## OpenMetadata Setup

1. Install OpenMetadata via Docker (v1.3.8+ recommended)
2. Get JWT token: Settings → Bots → ingestion-bot → Copy Token
3. Run the CORS proxy: `python server.py`
4. Configure in Settings tab:
   - OpenMetadata URL: `http://localhost:8585`
   - JWT Token: (paste your token)
   - Proxy URL: `http://localhost:3000`

## Tech Stack

- **Frontend**: Vanilla JavaScript + React-inspired state management
- **Styling**: Custom CSS with dark/light theme support
- **LLM Integration**: REST APIs (Anthropic, OpenAI, Google, Mistral, Perplexity)
- **Data Processing**: Papa Parse (CSV), SheetJS (Excel)
- **Proxy**: Python Flask (for OpenMetadata CORS)

## Project Structure

```
Dataset-Metadata-Enricher/
├── index.html      # Main application (single-file)
├── server.py       # CORS proxy for OpenMetadata
├── README.md       # This file
├── CHANGELOG.md    # Version history
└── LICENSE         # MIT License
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

**Aakash Sharma**  
Dataset Lead, Centre for Data Science and Analytics, Ashoka University

- LinkedIn: [linkedin.com/in/aakashsharma8a6888131](https://www.linkedin.com/in/aakashsharma8a6888131/)
- GitHub: [github.com/aak105](https://github.com/aak105)

## License

MIT License — see [LICENSE](LICENSE) for details.

## Acknowledgments

- [World Bank Metadata Schemas](https://github.com/worldbank/metadata-schemas) for schema standards
- [OpenMetadata](https://open-metadata.org/) for the data catalog platform
- [Anthropic](https://anthropic.com/), [OpenAI](https://openai.com/), [Google](https://ai.google.dev/), [Mistral](https://mistral.ai/), [Perplexity](https://perplexity.ai/) for LLM APIs
