"""Consulta concurrente de carteleras mediante asyncio y esperas simuladas."""

import argparse
import asyncio
import time


async def consultar_cartelera(sucursal, espera, peliculas, inicio):
    print(f"[{time.perf_counter() - inicio:5.2f}s] Consultando {sucursal} (espera: {espera:g}s)", flush=True)
    # Simula la espera de una respuesta; no bloquea las demás consultas.
    await asyncio.sleep(espera)
    print(f"[{time.perf_counter() - inicio:5.2f}s] Responde {sucursal}: {', '.join(peliculas)}", flush=True)
    return sucursal, peliculas


async def main(demora):
    sucursales = [
        ("Cine Centro", demora, ["Órbita 19:00", "El último tren 21:00"]),
        ("Cine Norte", demora * 2, ["Órbita 18:00", "Mar abierto 20:00"]),
        ("Cine Sur", demora * 3, ["Mar abierto 17:00", "El último tren 19:00"]),
    ]
    print("CINE | CONSULTA CONCURRENTE DE CARTELERAS", flush=True)
    inicio = time.perf_counter()
    resultados = await asyncio.gather(*(
        consultar_cartelera(sucursal, espera, peliculas, inicio)
        for sucursal, espera, peliculas in sucursales
    ))
    print(f"Sucursales consultadas: {len(resultados)}")
    print(f"Tiempo total: {time.perf_counter() - inicio:.2f} segundos")
    print(f"Espera secuencial teórica: {demora * 6:.2f} segundos")
    print(f"Espera concurrente teórica: {demora * 3:.2f} segundos")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demora", type=float, default=1, help="Espera base en segundos (predeterminado: 1)")
    args = parser.parse_args()
    if args.demora < 0:
        parser.error("--demora debe ser mayor o igual a cero")
    asyncio.run(main(args.demora))
