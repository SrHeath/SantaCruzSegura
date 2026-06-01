(function() {
    function initMap() {
        const urlParams = new URLSearchParams(window.location.search);
        const targetLat = urlParams.get('lat');
        const targetLng = urlParams.get('lng');
        const targetId = urlParams.get('id');

        const map = L.map('map');

        if (targetLat && targetLng) {
            map.setView([parseFloat(targetLat), parseFloat(targetLng)], 17);
        } else {
            map.setView([-17.7833, -63.1821], 12);
        }

        const googleRoads = L.tileLayer('https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
            attribution: '© Google Maps', maxZoom: 20
        });
        const googleSatellite = L.tileLayer('https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
            attribution: '© Google Maps', maxZoom: 20
        });
        const googleHybrid = L.tileLayer('https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', {
            attribution: '© Google Maps', maxZoom: 20
        });

        googleRoads.addTo(map);

        const incidentes = window.__INCIDENTES__ || [];

        if (incidentes.length > 0) {
            const heatArray = incidentes.map(i => [i.lat, i.lng, 1]);
            L.heatLayer(heatArray, {
                radius: 25, blur: 15, maxZoom: 1,
                gradient: {0.4: 'blue', 0.65: 'lime', 0.8: 'yellow', 1.0: 'red'}
            }).addTo(map);
        }

        function getRadiusForZoom(zoom) {
            if (zoom >= 16) return 10;
            if (zoom >= 14) return 8;
            if (zoom >= 12) return 6;
            if (zoom >= 10) return 4;
            return 2;
        }

        const markers = [];

        incidentes.forEach(function(i) {
            const tipoLower = (i.tipo || '').toLowerCase();
            const color = tipoLower.includes('robo') ? 'red' :
                          tipoLower.includes('asalto') ? 'orange' : 'blue';

            let popupContent = '<div style="max-width: 250px;">' +
                '<h6 class="mb-1 text-primary"><strong>' + escapeHtml(i.titulo) + '</strong></h6>' +
                '<p class="mb-1 small"><strong>Tipo:</strong> ' + escapeHtml(i.tipo) + '</p>' +
                '<p class="mb-1 small"><strong>Sector:</strong> ' + escapeHtml(i.sector) + '</p>' +
                '<p class="mb-2 small text-dark" style="white-space: pre-line;">' + escapeHtml(i.descripcion) + '</p>';

            if (i.imagenUrl) {
                popupContent += '<div class="mt-2 text-center"><img src="' + escapeHtml(i.imagenUrl) + '" class="img-fluid rounded border" style="max-height: 120px; object-fit: cover; width: 100%;" alt="Evidencia" loading="lazy"></div>';
            }

            popupContent += '</div>';

            const marker = L.circleMarker([i.lat, i.lng], {
                radius: getRadiusForZoom(map.getZoom()),
                fillColor: color, color: '#000', weight: 1,
                opacity: 0.7, fillOpacity: 0.7
            }).addTo(map).bindPopup(popupContent, {maxWidth: 300});

            if (targetId && i.id == targetId) {
                setTimeout(function() { marker.openPopup(); }, 500);
            }

            markers.push(marker);
        });

        map.on('zoomend', function() {
            const currentZoom = map.getZoom();
            const newRadius = getRadiusForZoom(currentZoom);
            markers.forEach(function(m) { m.setRadius(newRadius); });
        });

        L.control.layers({
            "Google Maps (Callejero)": googleRoads,
            "Google Maps (Satélite)": googleSatellite,
            "Google Maps (Híbrido)": googleHybrid
        }).addTo(map);

        L.control({position: 'bottomright'}).onAdd = function() {
            const div = L.DomUtil.create('div', 'info legend');
            div.innerHTML = '<div class="card p-3 border-0 shadow-sm" style="background: rgba(255,255,255,0.9); backdrop-filter: blur(4px);">' +
                '<h6 class="fw-bold mb-2 text-dark"><i class="bi bi-info-circle"></i> Leyenda</h6>' +
                '<div class="d-flex flex-column gap-1 small">' +
                '<div><span class="text-danger">●</span> Robo</div>' +
                '<div><span class="text-warning">●</span> Asalto</div>' +
                '<div><span class="text-primary">●</span> Otro</div></div></div>';
            return div;
        }.addTo(map);
    }

    function escapeHtml(str) {
        if (!str) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initMap);
    } else {
        initMap();
    }
})();