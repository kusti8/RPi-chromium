function triggerMouseEvent(element, eventName, userOptions) {
  var options = { // defaults
    clientX: 0, clientY: 0, button: 0,
    ctrlKey: false, altKey: false, shiftKey: false,
    metaKey: false, bubbles: true, cancelable: true
     // create event object:
  }, event = element.ownerDocument.createEvent("MouseEvents");

  if (!/^(?:click|mouse(?:down|up|over|move|out))$/.test(eventName)) {
    throw new Error("Only MouseEvents supported");
  }

  if (typeof userOptions != 'undefined'){ // set the userOptions
    for (var prop in userOptions) {
      if (userOptions.hasOwnProperty(prop))
        options[prop] = userOptions[prop];
    }
  }
  // initialize the event object
  event.initMouseEvent(eventName, options.bubbles, options.cancelable,
                       element.ownerDocument.defaultView,  options.button,
                       options.clientX, options.clientY, options.clientX,
                       options.clientY, options.ctrlKey, options.altKey,
                       options.shiftKey, options.metaKey, options.button,
                       element);
  // dispatch!
  element.dispatchEvent(event);
}

// triggerMouseEvent(document.getElementById('button.ytp-play-button.ytp-button'), 'click')
var player = document.getElementsByTagName('video')[0].pause()
//player.pauseVideo()
