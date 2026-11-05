# Ejercicio 2: consulta concurrente de carteleras

## Caso práctico

Una aplicación de cine consulta las carteleras de tres sucursales. Centro responde después de 1 segundo, Norte después de 2 y Sur después de 3. Los datos están definidos en el programa y las esperas simulan respuestas de servicios externos.

`main.py` usa `async def` para definir la consulta, `await asyncio.sleep()` para ceder el control durante la espera y `asyncio.gather()` para ejecutar concurrentemente las tres consultas y reunir sus resultados. No realiza conexiones de red reales.

## Ejecutar con Docker Compose

Con Docker iniciado, abre una terminal en la raíz del repositorio:

```powershell
cd "ejercicio 2"
docker compose run --rm app
```

Para reducir la espera base a medio segundo (las consultas tardarán 0.5, 1 y 1.5 segundos):

```powershell
docker compose run --rm app python main.py --demora 0.5
```

Alternativa local con Python 3.11 o superior:

```powershell
python main.py
```

## Resultado esperado

```text
[ 0.00s] Consultando Cine Centro (espera: 1s)
[ 0.00s] Consultando Cine Norte (espera: 2s)
[ 0.00s] Consultando Cine Sur (espera: 3s)
[ 1.00s] Responde Cine Centro: Órbita 19:00, El último tren 21:00
[ 2.00s] Responde Cine Norte: Órbita 18:00, Mar abierto 20:00
[ 3.00s] Responde Cine Sur: Mar abierto 17:00, El último tren 19:00
Sucursales consultadas: 3
Tiempo total: 3.00 segundos
Espera secuencial teórica: 6.00 segundos
Espera concurrente teórica: 3.00 segundos
```

Los tiempos son aproximados. Secuencialmente las mismas consultas esperarían 1 + 2 + 3 = **6 segundos**; concurrentemente sus esperas se solapan y el total se acerca a la mayor: **3 segundos**. La referencia secuencial se calcula, no se ejecuta una segunda prueba.

Esto demuestra concurrencia durante esperas, no ejecución paralela de cálculos en varios núcleos. Usar `time.sleep()` dentro de estas corrutinas bloquearía el hilo del bucle de eventos y evitaría este solapamiento.
