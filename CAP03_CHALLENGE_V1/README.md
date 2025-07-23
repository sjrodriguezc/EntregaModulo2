# Proyecto de Microservicios para Sistema de Reservación de Habitaciones

Este proyecto implementa un sistema de reservación de habitaciones utilizando una arquitectura de microservicios. Cada servicio está diseñado para manejar una funcionalidad específica del sistema, permitiendo escalabilidad y mantenimiento eficiente.

## Estructura del Proyecto

El proyecto está organizado en varios servicios, cada uno con su propia lógica y base de datos. A continuación se describen los servicios incluidos:

### Servicios

- **auth_service**: Maneja la autenticación de usuarios, incluyendo el registro, inicio de sesión y gestión de sesiones.
- **booking_service**: Gestiona las reservas de habitaciones, permitiendo crear, modificar y cancelar reservas.
- **inventory_service**: Administra el inventario de habitaciones, incluyendo la disponibilidad y detalles de las habitaciones.
- **payment_service**: Procesa los pagos de las reservas, gestionando transacciones y métodos de pago.
- **notification_service**: Envía notificaciones a los usuarios, incluyendo correos electrónicos y mensajes SMS.
- **user_profile_service**: Maneja la información de los perfiles de usuario, permitiendo la creación y actualización de perfiles.

### API Gateway

El **api_gateway** actúa como un punto de entrada para todas las solicitudes, redirigiendo las peticiones a los servicios correspondientes.

## Requisitos

Cada servicio tiene su propio archivo `requirements.txt` que lista las dependencias necesarias. Asegúrate de instalar las dependencias antes de ejecutar los servicios.

## Ejecución

Para ejecutar los servicios, navega a la carpeta de cada servicio y ejecuta el archivo `app.py`. Por ejemplo:

```bash
cd services/auth_service
uvicorn app:app --reload
```

Repite este proceso para cada servicio según sea necesario.

## Documentación

La documentación del proyecto se encuentra en la carpeta `docs`, donde se incluyen detalles sobre la arquitectura y diagramas que ilustran el flujo del sistema.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o un pull request en el repositorio.

## Licencia

Este proyecto está bajo la Licencia MIT.