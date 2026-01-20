// Arquivo de exemplo de configuração
// Copie este arquivo para config.js e configure sua chave de API

const CONFIG = {
    // Cole sua chave de API do Google Maps aqui
    // Obtenha uma chave em: https://console.cloud.google.com/
    GOOGLE_MAPS_API_KEY: 'SUA_CHAVE_API_AQUI',
    
    // Configurações do mapa
    MAP_CENTER: [-22.9, -43.0], // Coordenadas [latitude, longitude]
    MAP_ZOOM: 10,
    
    // Estilos das camadas
    LAYER_STYLES: {
        ANM: {
            color: '#ff6b6b',
            weight: 2,
            opacity: 0.8,
            fillColor: '#ff6b6b',
            fillOpacity: 0.3
        },
        UCS: {
            color: '#4ecdc4',
            weight: 2,
            opacity: 0.8,
            fillColor: '#4ecdc4',
            fillOpacity: 0.3
        }
    }
};
