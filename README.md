# Wally Wear - E-commerce Local

Wally Wear es una plataforma de e-commerce diseñada para funcionar localmente (optimizada para Termux en Android o cualquier navegador moderno), utilizando el `localStorage` para la persistencia de datos.

## 📁 Estructura del Proyecto

- `index.py`: Servidor principal en Python que redirige a la tienda.
- `public/`: Contenido para clientes (catálogo, carrito, políticas, nosotros).
- `admin/`: Zona de administración protegida por contraseña para gestionar productos, pedidos y redes sociales.
- `img/`: Carpeta exclusiva para fotos de productos.

## 🔐 Seguridad

El panel de administración está protegido por un sistema de **doble contraseña**:
1. **Contraseña Maestra:** `WallyMaster2026`
2. **Contraseña de Verificación:** `WallyShop_777`

Todas las páginas de administración verifican la autenticación mediante `sessionStorage`. Si se intenta acceder directamente sin autenticación, se redirigirá a la pantalla de login.

## ⚙️ Funcionalidades

### Tienda Pública
- Catálogo dinámico por categorías.
- Carrito de compras con cálculo de total.
- Generación de pedidos con ID único (`PED-timestamp`).
- Información sobre políticas de privacidad y sobre nosotros.

### Panel Admin
- **Gestión de Productos:** Crear categorías y productos con carga de imagen nativa (selector de archivos).
- **Gestión de Pedidos:** Visualización de pedidos ordenados por fecha y cambio de estado a "Pago confirmado".
- **Redes Sociales:** Configuración dinámica de enlaces a redes sociales que aparecen en el footer de la tienda.

## 🚀 Cómo ejecutar
1. Instala Python si no lo tienes.
2. Ejecuta el servidor: `python index.py`.
3. Accede a `http://localhost:8080`.
