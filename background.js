chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.sync.set({ "myKey": "Hello, World!" }, function() {
      console.log("Value is set to 'Hello, World!'");
    });
  });
  