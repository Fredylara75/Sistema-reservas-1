from servicio import Servicio
from excepciones import *
import logging


# ======================================================
# RESERVA DE SALAS
# ======================================================

class ReservaSala(Servicio):

    def __init__(self, nombre, costo_base, capacidad,
                 disponible=True,
                 aire_acondicionado=False,
                 internet=False,
                 videobeam=False):

        super().__init__(nombre, costo_base)

        self.capacidad = capacidad
        self.disponible = disponible

        self.aire_acondicionado = aire_acondicionado
        self.internet = internet
        self.videobeam = videobeam

    def validar_disponibilidad(self):

        if not self.disponible:
            raise ServicioNoDisponibleError(
                "La sala no se encuentra disponible"
            )

    def calcular_costo(self, horas=1):

        costo = self._costo_base * horas

        if self.aire_acondicionado:
            costo += 50000

        if self.internet:
            costo += 30000

        if self.videobeam:
            costo += 40000

        return costo

    def descripcion(self):

        return (
            f"Sala: {self._nombre} | "
            f"Capacidad: {self.capacidad} personas"
        )


# ======================================================
# ALQUILER DE EQUIPOS
# ======================================================

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, costo_base,
                 tipo_equipo,
                 cantidad_disponible):

        super().__init__(nombre, costo_base)

        self.tipo_equipo = tipo_equipo
        self.cantidad_disponible = cantidad_disponible

    def validar_disponibilidad(self, cantidad):

        if cantidad > self.cantidad_disponible:
            raise EquipoNoDisponibleError(
                "No hay suficientes equipos disponibles"
            )

    def calcular_costo(self, dias=1, cantidad=1):

        return self._costo_base * dias * cantidad

    def descripcion(self):

        return (
            f"Equipo: {self.tipo_equipo} | "
            f"Disponibles: {self.cantidad_disponible}"
        )


# ======================================================
# ASESORIAS
# ======================================================

class Asesoria(Servicio):

    def __init__(self, nombre, costo_base,
                 especialidad,
                 experto_certificado=True):

        super().__init__(nombre, costo_base)

        self.especialidad = especialidad
        self.experto_certificado = experto_certificado

    def validar_disponibilidad(self):

        if not self.experto_certificado:
            raise ServicioNoDisponibleError(
                "No existe asesor certificado disponible"
            )

    def calcular_costo(self, horas=1):

        costo = self._costo_base * horas

        if horas > 5:
            costo *= 0.9

        return costo

    def descripcion(self):

        return (
            f"Asesoría especializada en "
            f"{self.especialidad}"
        )
