"""Reserva de un asiento con lectura y actualización protegidas por Lock."""

import argparse
import threading
import time


def main(demora):
    asiento = {"codigo": "F8", "disponible": True}
    confirmaciones = []
    lock = threading.Lock()
    inicio_reservas = threading.Barrier(2)

    def reservar(cliente):
        # Ambos clientes llegan al intento de reserva antes de competir por el Lock.
        inicio_reservas.wait()
        with lock:
            print(f"[{cliente}] Consulta {asiento['codigo']}: {'DISPONIBLE' if asiento['disponible'] else 'OCUPADO'}", flush=True)
            if asiento["disponible"]:
                # Simula la confirmación dentro de la operación protegida.
                time.sleep(demora)
                asiento["disponible"] = False
                confirmaciones.append(cliente)
                print(f"[{cliente}] Reserva confirmada: {asiento['codigo']}", flush=True)
            else:
                print(f"[{cliente}] Reserva rechazada: {asiento['codigo']} ya está ocupado", flush=True)

    print("CINE | RESERVA CON LOCK", flush=True)
    hilos = [threading.Thread(target=reservar, args=(cliente,)) for cliente in ("Ana", "Luis")]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()
    print(f"Total de reservas confirmadas: {len(confirmaciones)}")
    print(f"Cliente con entrada para F8: {', '.join(confirmaciones)}")
    print("Resultado correcto: una reserva confirmada y una rechazada.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demora", type=float, default=1, help="Segundos para confirmar la reserva (predeterminado: 1)")
    args = parser.parse_args()
    if args.demora < 0:
        parser.error("--demora debe ser mayor o igual a cero")
    main(args.demora)
