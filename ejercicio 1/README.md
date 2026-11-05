# Ejercicio 1: ejecución secuencial en un cine

## Caso práctico

Tres clientes compran entradas para la película ficticia **Órbita**, función **19:00**. Ana reserva F8, Luis F9 y Sofía F10. Cada reserva valida la función y el asiento, simula el pago y emite la entrada. La reserva siguiente comienza solamente cuando termina la anterior.

`main.py` usa llamadas normales a funciones y `time.sleep()` para representar cada etapa. `time.perf_counter()` mide el tiempo y permite ver el orden de los eventos.

## Ejecutar con Docker Compose

Con Docker iniciado, abre una terminal en la raíz del repositorio:

```powershell
cd "ejercicio 1"
docker compose run --rm app
```

No requiere construir una imagen propia ni instalar bibliotecas. Docker descarga la imagen de Python si todavía no existe localmente.

Para una demostración más rápida, usa medio segundo por etapa:

```powershell
docker compose run --rm app python main.py --demora 0.5
```

También puedes ejecutarlo sin Docker si tienes Python 3.11 o superior:

```powershell
python main.py
```

## Resultado esperado

```text
[ 0.00s] [Ana] Inicia reserva del asiento F8
...
[ 3.00s] [Ana] Entrada emitida: película Órbita, función 19:00, asiento F8
[ 3.00s] [Luis] Inicia reserva del asiento F9
...
[ 6.00s] [Sofía] Inicia reserva del asiento F10
...
Entradas emitidas: 3
Tiempo total: 9.00 segundos
```

La salida abreviada muestra tiempos aproximados. Con el valor predeterminado hay tres clientes × tres etapas × un segundo = **9 segundos de espera**. No se solapan reservas. El tiempo mostrado por el programa excluye el arranque del contenedor.
