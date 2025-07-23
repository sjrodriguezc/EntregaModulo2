# Diagrama de Arquitectura de Microservicios

Este documento contiene los diagramas que ilustran la arquitectura y el flujo del sistema de microservicios para el sistema de reservación de habitaciones.

## Diagrama de Arquitectura de Software

```mermaid
graph TD
  subgraph Frontend
    A1[Web App]
    A2[Mobile App]
  end

  subgraph API Gateway
    B1[API Gateway]
  end

  subgraph Services
    B2[Auth Service]
    B3[Booking Service]
    B4[Inventory Service]
    B5[Payment Service]
    B6[Notification Service]
    B7[User Profile Service]
  end

  subgraph External Systems
    C1[Payment Gateway]
    C2[SMS/Email Provider]
    C3[Third-party OTA APIs]
  end

  A1 --> B1
  A2 --> B1
  B1 --> B2
  B1 --> B3
  B1 --> B4
  B1 --> B5
  B1 --> B6
  B1 --> B7

  B5 --> C1
  B6 --> C2
  B4 --> C3
```

## Diagrama de Componentes

```mermaid
graph TD
  subgraph Sistema_de_Reservación
    WebApp[Web App]
    MobileApp[Mobile App]
    APIGateway[API Gateway]
    AuthService[Servicio de Autenticación]
    BookingService[Servicio de Reservas]
    InventoryService[Servicio de Inventario]
    PaymentService[Servicio de Pagos]
    NotificationService[Servicio de Notificaciones]
    UserProfileService[Gestor de Perfiles de Usuario]
  end

  PaymentService --> PaymentGateway[Pasarela de Pago Externa]
  NotificationService --> NotificationProvider[Proveedor de Email/SMS]
  InventoryService --> OTA[Servicios OTA externos]
```

## Diagrama de Secuencias

```mermaid
sequenceDiagram
  participant Usuario
  participant Frontend
  participant API
  participant Inventario
  participant Reservas
  participant Pagos
  participant Notificaciones

  Usuario->>Frontend: Buscar habitación
  Frontend->>API: Solicita disponibilidad
  API->>Inventario: Obtener disponibilidad
  Inventario-->>API: Lista de habitaciones
  API-->>Frontend: Muestra resultados

  Usuario->>Frontend: Selecciona habitación y reserva
  Frontend->>API: Crear reserva
  API->>Reservas: Registrar reserva (estado: pendiente)
  API->>Pagos: Procesar pago
  Pagos-->>API: Confirmación de pago
  API->>Reservas: Actualiza reserva (estado: pagada)
  API->>Notificaciones: Enviar confirmación
  Notificaciones-->>Usuario: Email/SMS de confirmación
```

## Diagrama de Transición de Estados

```mermaid
stateDiagram-v2
  [*] --> Pendiente
  Pendiente --> Confirmada : Disponibilidad verificada
  Confirmada --> Pagada : Pago realizado
  Pagada --> Modificada : Cambio solicitado por usuario
  Pagada --> Cancelada : Cancelación por usuario/admin
  Modificada --> Pagada : Confirmación de cambios
  Cancelada --> [*]
  Pagada --> [*]
```