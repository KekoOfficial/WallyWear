import telebot
import requests

# === CONFIGURACIÓN DE PODER (JERARQUÍA) ===
TOKEN = "8795507175:AAEf9ujkj_jUMJZeChq6L1bFeS8IMRNFwt4"
bot = telebot.TeleBot(TOKEN)

# IDs de Telegram (Sustituir por los números reales)
ID_FUNDADOR = 8729717891  # Eder Villalba
ID_CREADOR = 8630490789  # Oliver Favero

# Diccionario de Gerentes (ID: Nombre)
GERENTES = {
    111222333: "Gerente 1",
    444555666: "Gerente 2",
    777888999: "Gerente 3",
    000111222: "Gerente 4",
    333444555: "Gerente 5"
}

# URL de la futura Web (donde se enviarán los datos)
URL_WEB_API = "https://tu-pagina-web.com/api/productos"

# === FUNCIONES DE VERIFICACIÓN ===
def es_admin(user_id):
    return user_id == ID_FUNDADOR or user_id == ID_CREADOR or user_id in GERENTES

# === COMANDOS ===

@bot.message_handler(commands=['start'])
def bienvenido(message):
    bot.reply_to(message, "🔌 Sistema Mally Wear Conectado.\nEsperando órdenes de la administración.")

@bot.message_handler(commands=['subir'])
def subir_contenido(message):
    user_id = message.from_user.id
    
    if not es_admin(user_id):
        bot.reply_to(message, "❌ No tienes permisos para subir contenido.")
        return

    try:
        # Formato: /subir [tipo] [nombre] [precio] [talles] [link_imagen]
        # Ejemplo: /subir zapatilla "Jordan Retro" 1200000 38,39,40,41 link.jpg
        datos = message.text.split(' ', 5)
        tipo = datos[1]      # zapatilla / remera / gorra
        nombre = datos[2]    # Entre comillas si tiene espacios
        precio = datos[3]    # En Gs.
        talles = datos[4]    # Ej: 38,39,40 o M,L,XL
        imagen = datos[5]    # Link directo

        # Determinar quién es el autor
        if user_id == ID_FUNDADOR: autor = f"Fundador ({ID_FUNDADOR})"
        elif user_id == ID_CREADOR: autor = "Oliver Favero (Creador)"
        else: autor = GERENTES[user_id]

        # --- AQUÍ SE ENVÍA A LA WEB ---
        # Por ahora simulamos la respuesta de la web
        # En el futuro, esto enviará un POST a tu base de datos
        id_falso_producto = "MW-" + str(requests.utils.quote(nombre[:3])) + "01" 

        bot.reply_to(message, f"✅ Contenido enviado a la Web.\n🆔 ID: {id_falso_producto}\n👤 Autor: {autor}")

        # --- NOTIFICACIÓN AUTOMÁTICA AL FUNDADOR (EDER VILLALBA) ---
        reporte = (
            f"🔔 *INFORME DE NUEVO CONTENIDO*\n\n"
            f"👤 *Subido por:* {autor}\n"
            f"📦 *Categoría:* {tipo.upper()}\n"
            f"👕 *Producto:* {nombre}\n"
            f"📏 *Talles:* {talles}\n"
            f"💰 *Precio:* Gs. {int(precio):,}\n"
            f"🖼️ [Ver Imagen]({imagen})\n\n"
            f"🆔 *ID para eliminar:* `{id_falso_producto}`"
        ).replace(",", ".") # Formato de miles para Paraguay

        bot.send_message(ID_FUNDADOR, reporte, parse_mode="Markdown")

    except Exception as e:
        bot.reply_to(message, "⚠️ Error de formato. Usa:\n/subir [tipo] [nombre] [precio] [talles] [link_imagen]")

@bot.message_handler(commands=['eliminar'])
def eliminar_contenido(message):
    user_id = message.from_user.id
    
    # Solo el Fundador (Eder) puede eliminar
    if user_id != ID_FUNDADOR:
        bot.reply_to(message, "⛔ Acceso denegado. Solo el Fundador puede eliminar publicaciones.")
        return

    try:
        id_producto = message.text.split(' ')[1]
        # Aquí se enviaría la orden de borrado a la base de datos SQL
        bot.reply_to(message, f"🗑️ El producto con ID `{id_producto}` ha sido eliminado de la página web.")
    except:
        bot.reply_to(message, "⚠️ Usa: /eliminar [ID_DEL_PRODUCTO]")

# Iniciar el Bot
print("Bot de Mally Wear en marcha...")
bot.polling()
