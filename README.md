# Text Content Extractor Chrome Extension

A Chrome extension that automatically extracts text content from web pages and sends it to an external API via a background script.

## Features

- **Automatic Text Extraction**: Automatically extracts text content when pages load
- **Manual Extraction**: Trigger text extraction manually via the popup interface
- **Smart Content Detection**: Prioritizes main content areas over navigation and ads
- **Background Processing**: Uses a service worker background script for API communication
- **Configurable API Endpoint**: Set your own API endpoint in the extension settings
- **Activity History**: Track extraction history and API responses
- **Modern UI**: Clean, responsive popup interface

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

### Expected API Response

Your API should return a JSON response. The extension will store this response for reference.

## Usage

### Text Extraction

- The extension automatically extracts text when you visit a new page
- Extraction happens after the page fully loads (with configurable delay)
- **Manual Control**: Use the popup buttons to control when data is sent to your API

### Manual Extraction

1. Click the extension icon in your browser toolbar
2. Click "Extract Text" to manually trigger extraction
3. Use "Manual Extract" for additional control
4. Use "Send Data" to manually send extracted data to your API

### Settings

- **API Endpoint**: Your external API URL
- **API Key**: Optional authentication key for your API
- **Auto-extract**: Enable/disable automatic extraction
- **Extract Delay**: Milliseconds to wait after page load before extraction


## File Structure

```
├── manifest.json          # Extension configuration
├── content.js            # Content script (runs on web pages)
├── background.js         # Background script (service worker)
├── popup.html           # Popup interface HTML
├── popup.css            # Popup styling
├── popup.js             # Popup functionality
├── icon16.png           # Extension icon (16x16)
├── icon48.png           # Extension icon (48x48)
├── icon128.png          # Extension icon (128x128)
└── README.md            # This file
```

## Permissions

- `activeTab`: Access to the currently active tab
- `storage`: Store settings and history locally
- `scripting`: Execute scripts in tabs
- `host_permissions`: Access to all websites for content extraction

## Customization

### Modifying Text Extraction Logic

Edit `content.js` to change how text is extracted:

```javascript
// Modify the mainSelectors array to prioritize different content areas
const mainSelectors = [
  'main',
  'article',
  '[role="main"]',
  '.main-content',
  '.content',
  '#content',
  '#main'
];
```

### Changing API Communication

Edit `background.js` to modify how data is sent to your API:

```javascript
// Add custom headers
headers: {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer YOUR_API_KEY',
  'X-Custom-Header': 'value'
}
```

### Styling the Popup

Edit `popup.css` to customize the appearance of the extension popup.

## Troubleshooting

### Extension Not Working

1. Check the browser console for errors
2. Verify the extension is enabled in `chrome://extensions/`
3. Ensure the content script is running on the target page
4. Check if the page has any Content Security Policy restrictions

### API Communication Issues

1. Verify your API endpoint is correct and accessible
2. Check browser console for network errors
3. Ensure your API accepts POST requests with JSON content
4. Verify CORS settings if testing locally

### Content Not Extracting

1. Some pages may block content scripts
2. Dynamic content might not be available immediately
3. Check if the page uses iframes or shadow DOM

## Development

### Testing Changes

1. Make your changes to the source files
2. Go to `chrome://extensions/`
3. Click the refresh icon on your extension
4. Test on a new page

### Debugging

- Use `console.log()` statements in your scripts
- Check the browser console for errors
- Use Chrome DevTools to inspect the extension

## Security Considerations

- The extension requests access to all websites
- Extracted content is sent to your external API
- Consider implementing rate limiting and authentication
- Be mindful of sensitive content extraction

## License

This project is open source. Feel free to modify and distribute as needed.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review browser console logs
3. Verify extension permissions and settings
4. Test with different websites to isolate issues
