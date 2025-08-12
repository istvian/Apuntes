# Sistemas operativos

Se realiza instalación y configuración de distintos sistemas operativos de escritorio, en relación a sus requerimientos de hardware

**_Máquina VirtualBox Win10_**

## Crear usuarios

usuario: usuario20
password: 123456

### GUI

1. Abrir panel de control
2. Cuentas
3. Familia y otros usuarios

### CMD

### Ver lista de usuarios

```console
net user
```

### Crear usuario

```console
net user usuario20 123456 /add
```

### Eliminar usuario

```console
net user usuario20 /delete
```

> [!NOTE]
> Si un usuario tiene espacio el comando debe incluir el nombre entre ""

## Directiva de seguridad local

Permite modificar:

- El largo de las contraseñas
- La complejidad
- Bloqueo despues de x intentos

## Administrador de tareas

Si es que es un usuario administrador permite cerrar la sesión de otros usuarios
