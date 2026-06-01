document.addEventListener("DOMContentLoaded", function() {
    const gpsStatus = document.getElementById("gps-status");
    const submitBtn = document.getElementById("submit-btn");
    const latInput = document.getElementById("id_latitud");
    const lngInput = document.getElementById("id_longitud");

    const defaultLat = -17.7833;
    const defaultLng = -63.1821;

    function updateCoordinates(lat, lng, source) {
        if (latInput) latInput.value = lat.toFixed(7);
        if (lngInput) lngInput.value = lng.toFixed(7);
        if (submitBtn) submitBtn.disabled = false;
        
        gpsStatus.className = "alert alert-success d-flex align-items-center gap-2 mb-3";
        gpsStatus.innerHTML = `<span><i class="bi bi-check-circle-fill"></i> Ubicación fijada por <strong>${source}</strong>: <strong>${lat.toFixed(5)}, ${lng.toFixed(5)}</strong></span>`;
    }

    updateCoordinates(defaultLat, defaultLng, "defecto (Santa Cruz)");

    let map, marker;
    try {
        if (typeof L === 'undefined') throw new Error("Leaflet no está cargado");

        map = L.map('map-picker').setView([defaultLat, defaultLng], 13);
        L.tileLayer('https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
            attribution: '© Google Maps',
            maxZoom: 20
        }).addTo(map);

        marker = L.marker([defaultLat, defaultLng], { draggable: true }).addTo(map);

        marker.on('dragend', function(e) {
            const position = marker.getLatLng();
            updateCoordinates(position.lat, position.lng, "marcador manual");
        });

        map.on('click', function(e) {
            marker.setLatLng(e.latlng);
            updateCoordinates(e.latlng.lat, e.latlng.lng, "clic en mapa");
        });
    } catch (error) {
        console.error("Error cargando Leaflet:", error);
        if (latInput) {
            latInput.setAttribute('type', 'text');
            latInput.className = "form-control mb-2";
        }
        if (lngInput) {
            lngInput.setAttribute('type', 'text');
            lngInput.className = "form-control mb-2";
        }
        if (gpsStatus) {
            gpsStatus.className = "alert alert-danger d-flex align-items-center gap-2 mb-3";
            gpsStatus.innerHTML = "<span><i class='bi bi-exclamation-triangle-fill'></i> No se pudo cargar el mapa. Puedes introducir las coordenadas manualmente.</span>";
        }
    }

    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(
            function(position) {
                const lat = position.coords.latitude;
                const lng = position.coords.longitude;
                if (map && marker) {
                    marker.setLatLng([lat, lng]);
                    map.setView([lat, lng], 16);
                }
                updateCoordinates(lat, lng, "GPS del dispositivo");
            },
            function() {
                if (gpsStatus) {
                    gpsStatus.className = "alert alert-info d-flex align-items-center gap-2 mb-3";
                    gpsStatus.innerHTML = "<span><i class='bi bi-info-circle-fill'></i> Dispositivo sin señal GPS. Por favor, <strong>mueve el marcador</strong>.</span>";
                }
            },
            { enableHighAccuracy: true, timeout: 5000, maximumAge: 0 }
        );
    }
});