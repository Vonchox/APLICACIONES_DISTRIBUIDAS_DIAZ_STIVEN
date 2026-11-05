"""Emisión secuencial de entradas: cada reserva termina antes de la siguiente."""

import argparse
import time


def procesar_reserva(cliente, asiento, demora, inicio):
    def informar(mensaje):
        print(f"[{time.perf_counter() - inicio:5.2f}s] [{cliente}] {mensaje}", flush=True)

    informar(f"Inicia reserva del asiento {asiento}")
    for etapa in ("Validando función y asiento", "Procesando pago simulado", "Emitiendo entrada"):
        informar(etapa)
        time.sleep(demora)
    informar(f"Entrada emitida: película Órbita, función 19:00, asiento {asiento}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demora", type=float, default=1, help="Segundos por etapa (predeterminado: 1)")
    args = parser.parse_args()
    if args.demora < 0:
        parser.error("--demora debe ser mayor o igual a cero")

    reservas = [("Ana", "F8"), ("Luis", "F9"), ("Sofía", "F10")]
    print("CINE | EMISIÓN SECUENCIAL DE ENTRADAS", flush=True)
    inicio = time.perf_counter()
    for cliente, asiento in reservas:
        procesar_reserva(cliente, asiento, args.demora, inicio)
    print(f"Entradas emitidas: {len(reservas)}")
    print(f"Tiempo total: {time.perf_counter() - inicio:.2f} segundos")


if __name__ == "__main__":
    main()
