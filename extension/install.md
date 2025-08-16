# Quick Installation Guide

## Step 1: Generate Icons
1. Open `create_icons.html` in your browser
2. Download all three icon files (icon16.png, icon48.png, icon128.png)
3. Place them in the same folder as your extension files

## Step 2: Install Extension
1. Open Chrome and go to `chrome://extensions/`
2. Enable "Developer mode" (toggle in top right)
3. Click "Load unpacked"
4. Select the folder containing your extension files
5. The extension should now appear in your extensions list

## Step 3: Configure API Endpoint
1. Click the extension icon in your browser toolbar
2. Go to Settings section
3. Enter your API endpoint URL
4. Click "Save Settings"

## Step 4: Test
1. Visit any webpage
2. The extension should automatically extract text content
3. Check the popup to see extraction status and history

## Troubleshooting
- If icons don't appear, make sure you downloaded them from `create_icons.html`
- If the extension doesn't work, check the browser console for errors
- Make sure your API endpoint is accessible and accepts POST requests

## File Checklist
Make sure you have all these files in your extension folder:
- [ ] manifest.json
- [ ] content.js
- [ ] background.js
- [ ] popup.html
- [ ] popup.css
- [ ] popup.js
- [ ] icon16.png
- [ ] icon48.png
- [ ] icon128.png
- [ ] README.md
- [ ] install.md
