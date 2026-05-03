from servicios_especificos import *
import logging


# ======================================================
# PRUEBA RESERVA DE SALA
# ======================================================

try:

    sala1 = ReservaSala(
        "Sala Ejecutiva",
        100000,
        20,
        disponible=True,
        aire_acondicionado=True,
        internet=True,
        videobeam=True
    )

    print(sala1.descripcion())

    sala1.validar_disponibilidad()

    print("Costo:",
          sala1.calcular_costo(3))

except Exception as e:

    logging.error(e)

    print("Error:", e)


print("\n========================\n")


# ======================================================
# PRUEBA ALQUILER EQUIPO
# ======================================================

try:

    equipo1 = AlquilerEquipo(
        "Video Beam Epson",
        50000,
        "Proyector",
        2
    )

    equipo1.validar_disponibilidad(5)

except Exception as e:

    logging.error(e)

    print("Error:", e)


print("\n========================\n")


# ======================================================
# PRUEBA ASESORIA
# ======================================================

try:

    asesoria1 = Asesoria(
        "Consultoría TI",
        80000,
        "Ciberseguridad",
        experto_certificado=True
    )

    asesoria1.validar_disponibilidad()

    print(asesoria1.descripcion())

    print(
        "Costo:",
        asesoria1.calcular_costo(6)
    )

except Exception as e:

    logging.error(e)

    print("Error:", e)
