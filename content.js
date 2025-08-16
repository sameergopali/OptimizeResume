// Content script that runs on every webpage
(function() {
  'use strict';

  // Store extracted data in memory (not storage)

  // Function to extract text content from the page
  function extractTextContent() {
    // Remove script and style elements to get clean text


    // Get the main content - try different selectors for better text extraction
    let content = '';
    
    // Try to get main content first
    const mainSelectors = [
      'main',
      'article',
      '[role="main"]',
      '.main-content',
      '.content',
      '#content',
      '#main'
    ];

    let mainElement = null;
    for (const selector of mainSelectors) {
      mainElement = document.querySelector(selector);
      if (mainElement) break;
    }

    if (mainElement) {
      content = mainElement.textContent || mainElement.innerText;
    } else {
      // Fallback to body content
      content = document.body.textContent || document.body.innerText;
    }

    // Clean up the extracted text
    content = content
      .replace(/\s+/g, ' ')  // Replace multiple whitespace with single space
      .replace(/\n+/g, '\n') // Replace multiple newlines with single newline
      .trim();

    const data = {
      url: window.location.href,
      title: document.title,
      content: content,
      timestamp: new Date().toISOString(),
      contentLength: content.length
    };

    // Store in memory
    console.log(data);
    return data;
  }

  // Listen for messages from popup or background script
  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'extractText') {
      const data = extractTextContent();
      if (data) {
        sendResponse({ success: true, data: data });
      } else {
        sendResponse({ success: false, message: 'No data available. Please extract text first.' });
      }
    }
  });

 

  console.log('Text Content Extractor content script loaded');
})();
