/**
 * 🌐 JS 06: MUSTERLÖSUNG – ASYNC / AWAIT & REST-APIS 🌐
 * ====================================================
 */

async function holeWetterDaten(stadtName, mockApiFetcher) {
  const response = await mockApiFetcher(stadtName);
  if (!response || !response.ok) {
    const status = response ? response.status : 500;
    throw new Error(`Stadt ${stadtName} nicht gefunden (Status: ${status})`);
  }
  const data = await response.json();
  return {
    stadt: data.stadt,
    temperatur: data.temperatur,
    wetterlage: data.wetterlage
  };
}

async function aggregiereBenutzerPosts(userId, mockPostApiFetcher) {
  const response = await mockPostApiFetcher(userId);
  let posts;
  if (response && typeof response.json === "function") {
    if (!response.ok) {
      throw new Error(`Fehler beim Laden der Posts für User ${userId}`);
    }
    posts = await response.json();
  } else if (Array.isArray(response)) {
    posts = response;
  } else {
    posts = [];
  }

  return {
    userId: userId,
    anzahlPosts: posts.length,
    postTitel: posts.map((p) => p.titel)
  };
}

async function sichererApiAufruf(apiPromiseOderFn, standardFallback) {
  try {
    if (typeof apiPromiseOderFn === "function") {
      return await apiPromiseOderFn();
    }
    return await apiPromiseOderFn;
  } catch (err) {
    return standardFallback;
  }
}
