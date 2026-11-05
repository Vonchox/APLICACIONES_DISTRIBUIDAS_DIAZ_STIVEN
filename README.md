# Aplicaciones Distribuidas — Díaz Stiven

Tres ejercicios de Python que simulan operaciones de un cine.

| Carpeta | Caso práctico | Conceptos |
| --- | --- | --- |
| [Ejercicio 1](ejercicio%201/README.md) | Emitir entradas de tres clientes, uno después de otro | Ejecución secuencial |
| [Ejercicio 2](ejercicio%202/README.md) | Consultar las carteleras de tres sucursales concurrentemente | Concurrencia con `asyncio` |
| [Ejercicio 3](ejercicio%203/README.md) | Comparar la reserva del asiento F8 sin Lock y con Lock | Hilos y condiciones de carrera |

## Requisitos

- Docker con Docker Compose, en Windows, iniciar Docker Desktop con contenedores Linux.
- Tener el repositorio descargado o clonado, NO es necesario instalar Python.

## Ejecución

Abre una terminal en la raíz del repositorio y ejecuta cada comando por separado:

```powershell
docker compose -f "ejercicio 1/docker-compose.yml" run --rm app
docker compose -f "ejercicio 2/docker-compose.yml" run --rm app
docker compose -f "ejercicio 3/docker-compose.yml" run --rm sin-lock
docker compose -f "ejercicio 3/docker-compose.yml" run --rm con-lock
```

La primera ejecución descarga la imagen `python:3.11-slim` y requiere internet. `--rm` elimina el contenedor al terminar.

Cada carpeta incluye un README con la explicación y los resultados esperados.
