import http.server
import socketserver
import os
import sys

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({".js": "application/javascript"})

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor corriendo en: http://localhost:{PORT}")
    print("Abre esa URL en tu navegador.")
    print("Presiona Ctrl+C para detener.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
