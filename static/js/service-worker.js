const CACHE_NAME = "static-cache";
const FILES_TO_CACHE = [
  "/static/offline.html",
  "/static/css/styles.css",
  "/static/images/background.webp",
  "/static/js/materialize.min.js",
  "/static/css/materialize.min.css",
  "static/images/logo-navbar.png",
  "static/images/icon.png",
  "static/images/apple_launch.webp",
  "static/images/apple_icon.png",
];

const offlineUrl = "static/offline.html";

self.addEventListener("install", (evt) => {
  console.log("[ServiceWorker] Install");
  evt.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log("[ServiceWorker] Pre-caching offline page");
      return cache.addAll(FILES_TO_CACHE);
    })
  );
});

self.addEventListener("activate", (evt) => {
  console.log("[ServiceWorker] Activate");
  evt.waitUntil(
    caches.keys().then((keyList) => {
      return Promise.all(
        keyList.map((key) => {
          if (key !== CACHE_NAME) {
            console.log("[ServiceWorker] Removing old cache", key);
            return caches.delete(key);
          }
        })
      );
    })
  );
  self.clients.claim();
});
/*
this.addEventListener("fetch", (event) => {
  // request.mode = navigate isn't supported in all browsers
  // so include a check for Accept: text/html header.
  if (
    event.request.mode === "navigate" ||
    (event.request.method === "GET" &&
      event.request.headers.get("accept").includes("text/html"))
  ) {
    event.respondWith(
      fetch(event.request.url).catch((error) => {
        // Return the offline page
        return caches.match(offlineUrl);
      })
    );
  } else {
    // Respond with everything else if we can
    event.respondWith(
      caches.match(event.request).then(function (response) {
        return response || fetch(event.request);
      })
    );
  }
});
*/
self.addEventListener("fetch", (event) => {
  console.log("Fetch event for ", event.request.url);
  if (
    event.request.mode === "navigate" ||
    (event.request.method === "GET" &&
      event.request.headers.get("accept").includes("text/html"))
  ) {
    event.respondWith(
      caches
        .match(event.request)
        .then((response) => {
          if (response) {
            console.log("Found ", event.request.url, " in cache");
            return response;
          }
          console.log("Network request for ", event.request.url);
          return fetch(event.request);

          // TODO 4 - Add fetched files to the cache
        })
        .catch((error) => {
          return caches.match(offlineUrl);
        })
    );
  } else {
    // Respond with everything else if we can
    event.respondWith(
      caches.match(event.request).then(function (response) {
        return response || fetch(event.request);
      })
    );
  }
});
