#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import geopy.distance
import random
import time

# Diccionario de ciudades con sus coordenadas (latitud, longitud)
ciudades = {
    'chile': {
        santiago: (-33.4489, -70.6693),
        valparaíso: (-33.0472, -71.6127),
        concepción: (-36.8267, -73.0617),
        antofagasta: (-23.6533, -70.3942)
    },
    'argentina': {
        buenos aires: (-34.6037, -58.3816),
        córdoba: (-31.4201, -64.1888),
        mendoza: (-32.8895, -68.8458),
        bariloche: (-41.1335, -71.3103)
    }
}

# Velocidades promedio por tipo de transporte (km/h)
transportes = {
    '1': {'nombre': 'Automóvil', 'velocidad': 90},
    '2': {'nombre': 'Autobús', 'velocidad': 70},
    '3': {'nombre': 'Avión', 'velocidad': 800},
    '4': {'nombre': 'Tren', 'velocidad': 100}
}

def calcular_distancia(ciudad_origen, ciudad_destino):
    """Calcula la distancia entre dos ciudades en km y millas"""
    coords_origen = None
    coords_destino = None
    
    # Buscar coordenadas en ambos países
    for pais, ciudades_pais in ciudades.items():
        if ciudad_origen in ciudades_pais:
            coords_origen = ciudades_pais[ciudad_origen]
        if ciudad_destino in ciudades_pais:
            coords_destino = ciudades_pais[ciudad_destino]
    
    if not coords_origen or not coords_destino:
        return None
    
    distancia_km = geopy.distance.distance(coords_origen, coords_destino).km
    distancia_millas = distancia_km * 0.621371
    return distancia_km, distancia_millas

def calcular_tiempo_viaje(distancia_km, transporte):
    """Calcula el tiempo de viaje en horas"""
    velocidad = transportes[transporte]['velocidad']
    tiempo_h = distancia_km / velocidad
    return tiempo_h

def generar_narrativa(ciudad_origen, ciudad_destino, transporte, tiempo_h):
    """Genera una descripción narrativa del viaje"""
    medio = transportes[transporte]['nombre']
    
    narrativas = [
        f"Emprenderás un emocionante viaje desde {ciudad_origen} hasta {ciudad_destino} en {medio}.",
        f"La aventura comienza en {ciudad_origen}, cruzando paisajes increíbles hacia {ciudad_destino}.",
        f"Prepara tu {medio.lower()} para un recorrido inolvidable entre {ciudad_origen} y {ciudad_destino}."
    ]
    
    tiempo_estimado = f"{int(tiempo_h)} horas y {int((tiempo_h % 1) * 60)} minutos" if tiempo_h > 1 else f"{int(tiempo_h * 60)} minutos"
    
    return f"{random.choice(narrativas)}\nEl viaje tomará aproximadamente {tiempo_estimado}."

def mostrar_menu_transportes():
    """Muestra el menú de medios de transporte"""
    print("\nSeleccione medio de transporte:")
    for codigo, info in transportes.items():
        print(f"{codigo}. {info['nombre']}")

def main():
    print("=== CALCULADOR DE VIAJES CHILE-ARGENTINA ===")
    print("Ingrese 's' para salir en cualquier momento\n")
    
    while True:
        # Solicitar ciudades
        ciudad_origen = input("Ciudad de Origen (Chile/Argentina): ").strip()
        if ciudad_origen.lower() == 's':
            break
            
        ciudad_destino = input("Ciudad de Destino (Chile/Argentina): ").strip()
        if ciudad_destino.lower() == 's':
            break
        
        # Calcular distancia
        resultado = calcular_distancia(ciudad_origen, ciudad_destino)
        if not resultado:
            print("Error: Una o ambas ciudades no están en la base de datos.")
            continue
            
        distancia_km, distancia_millas = resultado
        
        # Seleccionar transporte
        while True:
            mostrar_menu_transportes()
            transporte = input("Opción: ").strip()
            if transporte.lower() == 's':
                break
            if transporte not in transportes:
                print("Opción inválida. Intente nuevamente.")
                continue
                
            tiempo_h = calcular_tiempo_viaje(distancia_km, transporte)
            
            # Mostrar resultados
            print("\n=== RESULTADOS ===")
            print(f"Distancia: {distancia_km:.2f} km ({distancia_millas:.2f} millas)")
            print(f"Transporte: {transportes[transporte]['nombre']}")
            print(f"Duración estimada: {tiempo_h:.1f} horas")
            print("\n--- NARRATIVA ---")
            print(generar_narrativa(ciudad_origen, ciudad_destino, transporte, tiempo_h))
            print("\n")
            break
            
    print("\n¡Gracias por usar el calculador de viajes!")

if __name__ == "__main__":
    main()