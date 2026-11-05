# Ejercicio 3: reserva de un asiento con hilos y Lock

## Caso práctico

Ana y Luis intentan reservar el único asiento disponible, **F8**, para la misma función. Cada versión inicia con exactamente el mismo estado: un asiento libre y dos clientes. La regla del negocio es que solo una persona puede recibir una reserva confirmada.

## Ejecutar con Docker Compose

Con Docker iniciado, abre una terminal en la raíz del repositorio:

```powershell
cd "ejercicio 3"
docker compose run --rm sin-lock
docker compose run --rm con-lock
```

Ejecuta los comandos uno después de otro para comparar sus resultados. Cada comando inicia un proceso nuevo y restablece el asiento a disponible.

Alternativa local con Python 3.11 o superior:

```powershell
python sin_lock.py
python con_lock.py
```

## Sin Lock: condición de carrera

`sin_lock.py` crea dos hilos con `threading.Thread`, los inicia con `start()` y espera su finalización con `join()`.

Cada hilo lee la disponibilidad y conserva una copia local. Una `threading.Barrier(2)` hace que ambos terminen esa lectura antes de actualizar el asiento. Así se reproduce de forma controlada la intercalación que causa el fallo, sin depender de una pausa o del azar. La barrera coordina la demostración, pero no da exclusión mutua a la operación de reserva.

Salida posible:

```text
[Ana] Consulta F8: DISPONIBLE
[Luis] Consulta F8: DISPONIBLE
[Luis] Reserva confirmada: F8
[Ana] Reserva confirmada: F8
Total de reservas confirmadas: 2
Clientes con entrada para F8: Ana, Luis
ERROR DEMOSTRADO: se vendió el mismo asiento a dos clientes.
```

La variable del asiento termina ocupada, pero se han emitido dos confirmaciones: mirar únicamente su valor final ocultaría la sobreventa. Cada hilo escribe su confirmación en una posición distinta de una lista para registrar el problema sin introducir otro contador compartido inseguro.

## Con Lock: una sola reserva

`con_lock.py` coloca la lectura, comprobación, confirmación y actualización dentro de `with lock:`. Solo un hilo puede ejecutar esa sección crítica a la vez. Cuando el segundo entra, vuelve a consultar el estado y encuentra el asiento ocupado.

La barrera de esta versión está antes del Lock: reúne los intentos iniciales sin bloquear al hilo que ya posee el recurso. La pausa de un segundo simula el procesamiento de la confirmación dentro de la sección protegida.

Salida posible:

```text
[Ana] Consulta F8: DISPONIBLE
[Ana] Reserva confirmada: F8
[Luis] Consulta F8: OCUPADO
[Luis] Reserva rechazada: F8 ya está ocupado
Total de reservas confirmadas: 1
Cliente con entrada para F8: Ana
Resultado correcto: una reserva confirmada y una rechazada.
```

El ganador puede ser Ana o Luis; el Lock no garantiza qué hilo entra primero. Lo garantizado es una confirmación y un rechazo. El orden de los mensajes entre hilos también puede variar.

Para reducir el tiempo de confirmación:

```powershell
docker compose run --rm con-lock python con_lock.py --demora 0.1
```

## Alcance

Esta simulación protege memoria compartida por hilos dentro de un único proceso. Un Lock local no coordina contenedores ni servidores diferentes. Un cine real con varias instancias debe garantizar la reserva exclusiva mediante mecanismos compartidos, como transacciones y restricciones únicas en una base de datos.
