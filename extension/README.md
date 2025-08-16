# Text Content Extractor Chrome Extension

A Chrome extension that automatically extracts text content from web pages and sends it to an external API via a background script.

## Features

- **Background Processing**: Uses a service worker background script for API communication
- **Configurable API Endpoint**: Set your own API endpoint in the extension settings

## How It Works

1. **Content Script** (`content.js`): Runs on every webpage, extracts text content using intelligent selectors
2. **Background Script** (`background.js`): Service worker that receives extracted data and sends it to your external API
3. **Popup Interface**: User interface for manual extraction, settings, and viewing status

## Installation

### Method 1: Load Unpacked Extension (Development)

1. Clone or download this repository
2. Open Chrome and navigate to `chrome://extensions/`
3. Enable "Developer mode" in the top right
4. Click "Load unpacked" and select the extension folder
5. The extension should now appear in your extensions list

### Method 2: Package and Install

1. Zip all the extension files
2. Rename the zip file to `.crx`
3. Drag and drop the `.crx` file into Chrome's extensions page

## Configuration

### API Endpoint Setup

1. Open the extension popup
2. Go to the Settings section
3. Enter your API endpoint URL (e.g., `https://127.0.0.1/api/extract`)
4. Optionally add your API key for authentication
5. Click "Save Settings"
6. Use "Test Connection" to verify your API is accessible

### API Request Format

The extension sends POST requests to your API with the following JSON structure:

```json
{
  "url": "https://example.com/page",
  "title": "Page Title",
  "content": "Extracted text content...",
  "timestamp": "2024-01-01T12:00:00.000Z",
  "contentLength": 1234,
  "userAgent": "Mozilla/5.0...",
  "extensionVersion": "1.0",
  "source": "chrome-extension"
}
```













