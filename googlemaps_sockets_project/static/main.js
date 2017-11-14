// Mexico 23.293178, -102.296618
function initMap() {

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: {lat: 23.293178, lng: -102.296618}
  });
  var markerCluster = new MarkerClusterer(map,null,
    {imagePath: '../static/images/m'});

    //Sockets
    // Correctly decide between ws:// and wss://
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var ws_path = ws_scheme + '://' + window.location.host + "/webhook/map/";
    console.log("Connecting to " + ws_path);
    var socket = new ReconnectingWebSocket(ws_path);

    // Helpful debugging
    socket.onopen = function () {
      console.log("Connected to chat socket");
    };
    socket.onclose = function () {
      console.log("Disconnected from chat socket");
    };

    socket.onmessage = function (message) {
      // Decode the JSON
      var data = JSON.parse(message.data);
      // Handle errors
      if (data.error) {
        console.log(data.error);
        return;
      }
      console.log(data);
      var location = {lat: parseFloat(data.lat), lng: parseFloat(data.lng)};
      var marker = new google.maps.Marker({
        position: location,
        label: "CP:" + data.zipcode
      });
      markerCluster.addMarker(marker);
    };
  }
