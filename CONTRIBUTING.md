# Contributing to Dataset Metadata Augmenter

First off, thank you for considering contributing to Dataset Metadata Augmenter! It's people like you that make this tool better for researchers everywhere.

## Code of Conduct

By participating in this project, you are expected to uphold our values of respect, inclusivity, and constructive collaboration.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (sample data if applicable)
- **Describe the behavior you observed and what you expected**
- **Include browser and OS information**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description of the proposed functionality**
- **Explain why this enhancement would be useful**
- **List any alternatives you've considered**

### Pull Requests

1. Fork the repo and create your branch from `main`
2. Make your changes
3. Test thoroughly in multiple browsers
4. Update documentation if needed
5. Submit the PR with a clear description

## Development Guidelines

### For the Standalone HTML Version

The `index.html` file is a self-contained application. When making changes:

1. **Keep it single-file**: All CSS, HTML, and JS should remain in one file for easy distribution
2. **Test in multiple browsers**: Chrome, Firefox, Safari, Edge
3. **Test both light and dark modes**
4. **Maintain backward compatibility** with saved localStorage data

### Code Style

- Use meaningful variable and function names
- Add JSDoc comments for public functions
- Keep functions focused and small
- Use ES6+ features (const/let, arrow functions, template literals)

### CSS Guidelines

- Use CSS custom properties (variables) for colors
- Support both light and dark modes
- Use semantic class names
- Mobile-responsive where applicable

### JavaScript Guidelines

```javascript
// Good: Descriptive function name with JSDoc
/**
 * Parse CSV text into headers and rows
 * @param {string} text - Raw CSV content
 * @returns {{headers: string[], rows: string[][]}} Parsed data
 */
const parseCSV = (text) => {
  // ...
};

// Good: Clear state updates
const updateField = (id, key, value) => {
  const field = state.schema.find(f => f.id === id);
  if (field) {
    field[key] = value;
    saveState();
    render();
  }
};
```

## Testing

Since this is a client-side application:

1. **Manual Testing Checklist**:
   - [ ] Upload CSV file
   - [ ] Upload Excel file
   - [ ] Upload JSON file
   - [ ] Add/remove schema fields
   - [ ] Load schema presets
   - [ ] Export schema
   - [ ] Configure each LLM provider
   - [ ] Test API connection
   - [ ] Augment dataset (if you have API key)
   - [ ] Export metadata
   - [ ] Verify localStorage persistence
   - [ ] Test dark mode
   - [ ] Test on mobile viewport

2. **Browser Testing**:
   - [ ] Chrome (latest)
   - [ ] Firefox (latest)
   - [ ] Safari (latest)
   - [ ] Edge (latest)

## Project Structure

```
Dataset-Metadata-Augmenter/
├── index.html          # Main application (standalone)
├── README.md           # Project documentation
├── LICENSE             # MIT License
├── CONTRIBUTING.md     # This file
├── .gitignore          # Git ignore rules
│
└── react-app/          # Future React version
    ├── package.json    # Dependencies
    ├── vite.config.js  # Build config
    └── src/            # Source code
```

## Adding New Features

### Adding a New LLM Provider

1. Add provider config to `state.settings.providers`:
```javascript
newprovider: {
  name: 'New Provider',
  models: ['model-a', 'model-b'],
  endpoint: 'https://api.newprovider.com/v1/chat'
}
```

2. Add handling in `callLLM()` function
3. Test the connection
4. Update documentation

### Adding a New Schema Field Type

1. Add type to the select options in `renderSchema()`
2. Handle rendering in `renderMetadataInput()`
3. Handle value parsing in `updateMetadata()` if needed
4. Test with sample data

### Adding a New Schema Preset

1. Add preset to `schemaPresets` object
2. Add button in `renderSchema()`
3. Document the use case in README

## Questions?

Feel free to open an issue for any questions about contributing!

---

Thank you for contributing! 🙏
