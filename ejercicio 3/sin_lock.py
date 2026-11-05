"""Demostración controlada de una doble reserva por condición de carrera."""

import threading


def main():
    asiento = {"codigo": "F8", "disponible": True}
    confirmaciones = [None, None]
    # Fuerza que ambos hayan leído el asiento antes de permitir actualizarlo.
    # Es una ayuda didáctica, no una solución para proteger la reserva.
    consultas_completas = threading.Barrier(2)

    def reservar(cliente, indice):
        disponible = asiento["disponible"]
        print(f"[{cliente}] Consulta {asiento['codigo']}: {'DISPONIBLE' if disponible else 'OCUPADO'}\n", end="", flush=True)
        consultas_completas.wait()
        if disponible:
            asiento["disponible"] = False
            confirmaciones[indice] = cliente
            print(f"[{cliente}] Reserva confirmada: {asiento['codigo']}\n", end="", flush=True)

    print("CINE | RESERVA SIN LOCK", flush=True)
    hilos = [threading.Thread(target=reservar, args=(cliente, indice))
             for indice, cliente in enumerate(("Ana", "Luis"))]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()

    clientes = [cliente for cliente in confirmaciones if cliente is not None]
    print(f"Total de reservas confirmadas: {len(clientes)}")
    print(f"Clientes con entrada para F8: {', '.join(clientes)}")
    print("ERROR DEMOSTRADO: se vendió el mismo asiento a dos clientes.")
    print("El resultado correcto sería una sola reserva confirmada.")


if __name__ == "__main__":
    main()
