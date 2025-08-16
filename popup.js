// Popup script that handles user interactions
document.addEventListener('DOMContentLoaded', function() {
  // Get DOM elements
  const extractBtn = document.getElementById('extractBtn');
  const contentLength = document.getElementById('contentLength');
  const apiEndpoint = document.getElementById('apiEndpoint');
  const apiKey = document.getElementById('apiKey');

  const saveSettings = document.getElementById('saveSettings');

  // Load saved settings
  loadSettings();
  
  // Load history

  // Event listeners
  extractBtn.addEventListener('click', handleExtract);
  saveSettings.addEventListener('click', saveSettingsHandler);

  // Handle extract button click
  function handleExtract() {

    // Get the active tab and send message to content script
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      if (tabs[0]) {
        chrome.tabs.sendMessage(tabs[0].id, { action: 'extractText' }, function(response) {
        if (response && response.success) {
            updateContentLength(response);
            chrome.runtime.sendMessage({action:'extractText', data:response.data} )
          }
        });
      }
    });
  }



  // Update content length from content script
  function updateContentLength(response) {
    contentLength.textContent = response.data.contentLength || 0;
       
  }

  // Load settings from storage
  function loadSettings() {
    chrome.storage.local.get(['apiEndpoint', 'apiKey'], function(result) {
      if (result.apiEndpoint) {
        apiEndpoint.value = result.apiEndpoint;
      }
      if (result.apiKey) {
        apiKey.value = result.apiKey;
      }
    });
  }

  // Save settings to storage
  function saveSettingsHandler() {
    const settings = {
      apiEndpoint: apiEndpoint.value,
      apiKey: apiKey.value,
    };

    chrome.storage.local.set(settings, function() {
      
      // Also update the background script with new settings
      chrome.runtime.sendMessage({
        action: 'updateSettings',
        settings: settings
      });
      
    });
  }




});
