(function() {
    function initMap() {
        var urlParams = new URLSearchParams(window.location.search);
        var targetLat = urlParams.get('lat');
        var targetLng = urlParams.get('lng');
        var targetId = urlParams.get('id');

        var mapDiv = document.getElementById('map');
        if (!mapDiv || typeof L === 'undefined') return;

        var map = L.map('map');

        if (targetLat && targetLng) {
            map.setView([parseFloat(targetLat), parseFloat(targetLng)], 17);
        } else {
            map.setView([-17.7833, -63.1821], 12);
        }

        var googleRoads = L.tileLayer('https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
            attribution: '© Google', maxZoom: 20
        });
        var googleSatellite = L.tileLayer('https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
            attribution: '© Google', maxZoom: 20
        });
        var googleHybrid = L.tileLayer('https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', {
            attribution: '© Google', maxZoom: 20
        });

        googleRoads.addTo(map);

        var incidentes = window.__INCIDENTES__ || [];

        try {
            if (incidentes.length > 0 && typeof L.heatLayer === 'function') {
                var heatArray = incidentes.map(function(i) { return [i.lat, i.lng, 1]; });
                L.heatLayer(heatArray, {
                    radius: 25, blur: 15, maxZoom: 10,
                    gradient: {0.4: 'blue', 0.65: 'lime', 0.8: 'yellow', 1.0: 'red'}
                }).addTo(map);
            }
        } catch(e) {}

        var markers = [];

        incidentes.forEach(function(i) {
            var tipoLower = (i.tipo || '').toLowerCase();
            var color = tipoLower.indexOf('robo') !== -1 ? 'red' :
                        tipoLower.indexOf('asalto') !== -1 ? 'orange' : 'blue';

            var popupContent = '<div style="max-width:250px;">' +
                '<h6 class="mb-1 text-primary"><strong>' + escapeHtml(i.titulo) + '</strong></h6>' +
                '<p class="mb-1 small"><strong>Tipo:</strong> ' + escapeHtml(i.tipo) + '</p>' +
                '<p class="mb-1 small"><strong>Sector:</strong> ' + escapeHtml(i.sector) + '</p>' +
                '<p class="mb-2 small text-dark">' + escapeHtml(i.descripcion) + '</p>';

            if (i.imagenUrl) {
                popupContent += '<div class="mt-2 text-center"><img src="' + escapeHtml(i.imagenUrl) + '" class="img-fluid rounded border" style="max-height:120px;object-fit:cover;width:100%;" alt="Evidencia" loading="lazy"></div>';
            }

            popupContent += '</div>';

            function getRadiusForZoom(z) {
                if (z >= 16) return 10;
                if (z >= 14) return 8;
                if (z >= 12) return 6;
                if (z >= 10) return 4;
                return 2;
            }

            var marker = L.circleMarker([i.lat, i.lng], {
                radius: getRadiusForZoom(map.getZoom()),
                fillColor: color, color: '#000', weight: 1,
                opacity: 0.7, fillOpacity: 0.7
            }).addTo(map).bindPopup(popupContent, {maxWidth: 300});

            if (targetId && String(i.id) === targetId) {
                setTimeout(function() { marker.openPopup(); }, 500);
            }

            markers.push(marker);
        });

        map.on('zoomend', function() {
            var z = map.getZoom();
            var newRadius = z >= 16 ? 10 : z >= 14 ? 8 : z >= 12 ? 6 : z >= 10 ? 4 : 2;
            markers.forEach(function(m) { m.setRadius(newRadius); });
        });

        L.control.layers({
            "Google Maps (Callejero)": googleRoads,
            "Google Maps (Satélite)": googleSatellite,
            "Google Maps (Híbrido)": googleHybrid
        }).addTo(map);

        L.control({position: 'bottomright'}).onAdd = function() {
            var div = L.DomUtil.create('div', 'info legend');
            div.innerHTML = '<div class="card p-3 border-0 shadow-sm" style="background:rgba(255,255,255,0.9);backdrop-filter:blur(4px);">' +
                '<h6 class="fw-bold mb-2 text-dark"><i class="bi bi-info-circle"></i> Leyenda</h6>' +
                '<div class="d-flex flex-column gap-1 small">' +
                '<div><span class="text-danger">●</span> Robo</div>' +
                '<div><span class="text-warning">●</span> Asalto</div>' +
                '<div><span class="text-primary">●</span> Otro</div></div></div>';
            return div;
        }.addTo(map);

        setTimeout(function() { map.invalidateSize(); }, 300);
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