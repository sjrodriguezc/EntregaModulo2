# Proyecto de Microservicios para Sistema de Reservación de Habitaciones

Este proyecto implementa un sistema de reservación de habitaciones utilizando una arquitectura de microservicios. Cada servicio está diseñado para manejar una funcionalidad específica del sistema, permitiendo escalabilidad y mantenimiento eficiente.

## Estructura del Proyecto

El proyecto está organizado en varios servicios, cada uno con su propia lógica y base de datos. A continuación se describen los servicios incluidos en el proyecto:

- **auth_service**: Maneja la autenticación de usuarios, incluyendo el registro, inicio de sesión y gestión de sesiones.
- **booking_service**: Gestiona las reservas de habitaciones, permitiendo crear, modificar y cancelar reservas.
- **inventory_service**: Administra el inventario de habitaciones, incluyendo la disponibilidad y detalles de las habitaciones.
- **payment_service**: Procesa los pagos de las reservas, gestionando transacciones y métodos de pago.
- **notification_service**: Envía notificaciones a los usuarios, incluyendo correos electrónicos y mensajes SMS.
- **user_profile_service**: Maneja la información de los perfiles de usuario, permitiendo la creación y actualización de perfiles.

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instalado Python y las siguientes dependencias en cada servicio:

- FastAPI
- Uvicorn
- Pydantic
- Otros paquetes necesarios según el servicio

Cada servicio tiene un archivo `requirements.txt` donde se listan las dependencias específicas.

## Ejecución

Para ejecutar cada servicio, navega al directorio del servicio correspondiente y utiliza el siguiente comando:

```bash
uvicorn app:app --reload
```

Esto iniciará el servidor de desarrollo de FastAPI, permitiendo acceder a la API en `http://localhost:8000`.

## Documentación

La documentación del sistema se encuentra en la carpeta `docs`, donde se incluyen detalles sobre la arquitectura, diagramas y otros aspectos relevantes del proyecto.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar, por favor abre un issue o un pull request en el repositorio.