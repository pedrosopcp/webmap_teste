#!/usr/bin/env python3
"""
Servidor HTTP simples para executar o WebGIS localmente.
Execute: python server.py
Depois acesse: http://localhost:8000
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Adicionar headers CORS para permitir carregamento de arquivos locais
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

def main():
    # Mudar para o diretório do script
    os.chdir(Path(__file__).parent)
    
    Handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Servidor iniciado em http://localhost:{PORT}")
        print("Pressione Ctrl+C para parar o servidor")
        print("\nAbrindo navegador...")
        
        # Tentar abrir o navegador automaticamente
        try:
            webbrowser.open(f'http://localhost:{PORT}')
        except:
            pass
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServidor encerrado.")

if __name__ == "__main__":
    main()
