// Background script (service worker) that handles API communication
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'extractText') {
    console.log('Received text content from content script:', request.data);
    sendToExternalAPI(request.data)
    sendResponse({ success: true, message: 'Data received and being processed' });

  }
  
  
  
  if (request.action === 'testAPIConnection') {
    // Test API connection with a simple request
    testAPIConnection()
      .then(response => {
        sendResponse({ success: true, message: 'Connection successful' });
      })
      .catch(error => {
        sendResponse({ success: false, message: error.message });
      });
    return true; // Keep message channel open for async response
  }
  
  if (request.action === 'updateSettings') {
    // Update stored settings
    chrome.storage.local.set(request.settings, function() {
      console.log('Settings updated:', request.settings);
      sendResponse({ success: true, message: 'Settings updated' });
    });
    return true; // Keep message channel open for async response
  }
});

// Function to send data to external API
async function sendToExternalAPI(data) {
  // Get API configuration from storage
  console.log(data);
  const config = await chrome.storage.local.get(['apiEndpoint', 'apiKey']);
  const API_ENDPOINT = config.apiEndpoint || 'https://127.0.0.1/api/extract';
  
  try {
    const headers = {
      'Content-Type': 'application/json'
    };
    
    // Add API key if provided
    if (config.apiKey) {
      headers['Authorization'] = `Bearer ${config.apiKey}`;
      headers['X-API-Key'] = config.apiKey;
    }
    
    const response = await fetch(API_ENDPOINT, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify({
        url: data.url,
        title: data.title,
        content: data.content,
        timestamp: data.timestamp,
        contentLength: data.contentLength,
        userAgent: navigator.userAgent,
        extensionVersion: '1.0',
        source: 'chrome-extension'
      })
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const result = await response.json();
    return result;
  } catch (error) {
    console.error('Fetch error:', error);
    throw error;
  }
}

// Function to test API connection
async function testAPIConnection() {
  const config = await chrome.storage.local.get(['apiEndpoint', 'apiKey']);
  const API_ENDPOINT = config.apiEndpoint || 'https://127.0.0.1/api/extract';
  
  try {
    const headers = {
      'Content-Type': 'application/json'
    };
    
    if (config.apiKey) {
      headers['Authorization'] = `Bearer ${config.apiKey}`;
      headers['X-API-Key'] = config.apiKey;
    }
    
    // Send a test request (usually a GET request to check if endpoint is reachable)
    const response = await fetch(API_ENDPOINT, {
      method: 'GET',
      headers: headers
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return { success: true, message: 'Connection successful' };
  } catch (error) {
    console.error('Connection test error:', error);
    throw error;
  }
}

// Handle extension installation
chrome.runtime.onInstalled.addListener((details) => {
  if (details.reason === 'install') {
    console.log('Text Content Extractor extension installed');
    
    // Set default configuration
    chrome.storage.local.set({
      apiEndpoint: 'https://127.0.0.1/api/extract',
      apiKey: '',
      autoExtract: true,
      extractDelay: 1000
    });
  }
});

// Handle extension startup
chrome.runtime.onStartup.addListener(() => {
  console.log('Text Content Extractor extension started');
});






