# Aplicaciones Distribuidas — Díaz Stiven

Repositorio de prácticas de clase. Estas tres actividades usan un cine como caso cotidiano para estudiar ejecución secuencial, concurrencia y sincronización con hilos.

| Carpeta | Caso práctico | Conceptos |
| --- | --- | --- |
| [ejercicio 1](ejercicio%201/README.md) | Emitir entradas de tres clientes, uno después de otro | Funciones, `time.sleep`, `time.perf_counter` |
| [ejercicio 2](ejercicio%202/README.md) | Consultar carteleras de tres sucursales | `asyncio`, `await`, `gather` |
| [ejercicio 3](ejercicio%203/README.md) | Evitar vender el asiento F8 a dos clientes | `threading`, condición de carrera, `Lock` |

## Requisitos

- Docker Engine y Docker Compose; en Windows puedes usar Docker Desktop iniciado con contenedores Linux.
- Git para clonar el repositorio, o descargarlo y descomprimirlo desde GitHub.
- No necesitas instalar Python en tu equipo para ejecutar con Docker.

Desde una terminal en la raíz del repositorio, comprueba Docker:

```powershell
docker --version
docker compose version
docker info
```

## Ejecutar desde la raíz

Ejecuta los comandos individualmente para observar cada demostración:

```powershell
docker compose -f "ejercicio 1/docker-compose.yml" run --rm app
docker compose -f "ejercicio 2/docker-compose.yml" run --rm app
docker compose -f "ejercicio 3/docker-compose.yml" run --rm sin-lock
docker compose -f "ejercicio 3/docker-compose.yml" run --rm con-lock
```

La primera ejecución necesita conexión para descargar `python:3.11-slim`. Las siguientes reutilizan la imagen local. Cada comando crea un contenedor temporal y `--rm` lo elimina al terminar. Los archivos Compose montan la carpeta de su propio ejercicio en modo de solo lectura. No hay dependencias externas, puertos ni servicios que deban quedar encendidos.

Los tres ejercicios comparten la imagen de Python, pero se ejecutan de manera independiente. Los servicios del ejercicio 3 son alternativas para comparar: cada proceso inicia su propio asiento disponible.

## Qué se demuestra

- **Secuencial:** un pedido de entradas termina antes de comenzar el siguiente; las esperas se suman.
- **Concurrente:** las consultas a sucursales se solapan durante sus esperas; `asyncio` no requiere un hilo por consulta ni implica paralelismo de CPU.
- **Hilos y Lock:** dos hilos comparten el estado de un asiento. El Lock protege la operación completa de consultar, comprobar y actualizar.

Son simulaciones educativas en consola: los títulos, funciones, pagos y consultas son ficticios. Las pausas representan esperas de procesamiento o comunicación, no mediciones de un sistema de cine real. Los tiempos medidos pueden variar ligeramente por la planificación del sistema.

`threading.Lock` protege hilos del mismo proceso. Un sistema real con varias instancias necesitaría garantizar la exclusividad en un almacenamiento compartido, por ejemplo mediante una transacción y una restricción única sobre función y asiento.

Los README de cada carpeta incluyen explicación, comandos y resultados esperados. Para la entrega, publica el repositorio en GitHub con visibilidad pública y utiliza el enlace de la actividad correspondiente.
