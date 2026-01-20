# WebGIS - Visualização de Dados Geoespaciais

Este projeto é um WebGIS simples para visualização de dados geoespaciais usando Leaflet e basemaps do Google Maps.

## Características

- Visualização de dois conjuntos de dados GeoJSON:
  - `base_ANM_pol_X_UCs.geojson` - Dados da ANM (Agência Nacional de Mineração) sobrepostos com Unidades de Conservação
  - `lim_UCs_pol.geojson` - Limites de Unidades de Conservação
- Alternância entre basemaps do Google:
  - Satélite
  - Mapa base (roadmap)
- Controle de visibilidade das camadas
- Popups informativos ao clicar nos polígonos

## Requisitos

- Um servidor web local (para evitar problemas de CORS ao carregar arquivos GeoJSON)
- Chave de API do Google Maps (opcional, mas recomendado para usar os basemaps do Google)

## Como usar

### 1. Configurar chave de API do Google Maps (Opcional)

1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto ou selecione um existente
3. Ative a API "Maps JavaScript API"
4. Crie uma chave de API
5. Abra o arquivo `index.html` e substitua `SUA_CHAVE_API_AQUI` pela sua chave de API na linha:
   ```javascript
   const GOOGLE_MAPS_API_KEY = 'SUA_CHAVE_API_AQUI';
   ```

**Nota:** Se você não configurar a chave do Google Maps, o sistema usará OpenStreetMap como fallback.

### 2. Executar o projeto

#### Opção 1: Usando o servidor Python incluído (recomendado)

```bash
python server.py
```

O servidor iniciará automaticamente e abrirá o navegador. Se não abrir automaticamente, acesse: `http://localhost:8000`

#### Opção 2: Usando Python simples

```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

Depois acesse: `http://localhost:8000`

#### Opção 3: Usando Node.js

```bash
npx http-server -p 8000
```

Depois acesse: `http://localhost:8000`

#### Opção 4: Usando PHP

```bash
php -S localhost:8000
```

Depois acesse: `http://localhost:8000`

### 3. Usar o WebGIS

- Use os controles no painel superior direito para:
  - Alternar entre basemaps (Satélite ou Mapa Base)
  - Ativar/desativar camadas individuais
- Clique nos polígonos para ver informações detalhadas
- Use o mouse para navegar pelo mapa (zoom, pan)

## Estrutura de arquivos

```
.
├── index.html              # Arquivo principal HTML
├── server.py               # Servidor HTTP simples (Python)
├── config.example.js       # Arquivo de exemplo de configuração
├── .gitignore             # Arquivos ignorados pelo Git
├── data/
│   ├── base_ANM_pol_X_UCs.geojson
│   └── lim_UCs_pol.geojson
└── README.md              # Este arquivo
```

## Tecnologias utilizadas

- [Leaflet](https://leafletjs.com/) - Biblioteca JavaScript para mapas interativos
- [Leaflet Google Mutant](https://github.com/robbiet480/leaflet-google) - Plugin para integração com Google Maps
- Google Maps API - Para basemaps de satélite e roadmap

## Notas importantes

- Os arquivos GeoJSON devem estar na pasta `data/`
- É necessário usar um servidor web local devido às políticas de CORS dos navegadores
- A chave de API do Google Maps tem limites de uso gratuitos. Consulte a documentação do Google para mais informações

## Solução de problemas

### Os basemaps do Google não aparecem
- Verifique se a chave de API está configurada corretamente
- Certifique-se de que a API "Maps JavaScript API" está ativada no Google Cloud Console
- Verifique o console do navegador para erros

### Os arquivos GeoJSON não carregam
- Certifique-se de estar usando um servidor web local
- Verifique se os arquivos estão na pasta `data/`
- Verifique o console do navegador para erros de CORS

### O mapa não aparece
- Verifique sua conexão com a internet
- Verifique o console do navegador para erros JavaScript
- Certifique-se de que todas as bibliotecas estão carregando corretamente
