chrome.extension.onMessage.addListener(
  function(request, sender, sendResponse) {
    chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
        var url = tabs[0].url;
        console.log("Got message")
        console.log(url)
        chrome.runtime.sendNativeMessage('run_omx',
      { text: url })
      })
    })

chrome.browserAction.onClicked.addListener(function (tab) {
    chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
        var url = tabs[0].url;
        console.log("Got click")
        console.log(url)
        chrome.runtime.sendNativeMessage('run_omx',
      { text: url })
      })
});
