import telebot
import requests
from config import TOKEN, FOUNDER_ID, GERENTES, API_URL

bot = telebot.TeleBot(TOKEN)

def obtener_rango(user_id):
    if user_id == FOUNDER_ID:
        return "FOUNDER 👑"
    elif user_id in GERENTES:
        return "GERENTE 🛡️"
    return None

@bot.message_handler(content_types=['text', 'photo'])
def manejar_entrada(message):
    user_id = message.from_user.id
    rango = obtener_rango(user_id)

    # 1. Seguridad Imperial
    if not rango:
        bot.reply_to(message, "🚫 ACCESO DENEGADO.\nTu ID no tiene rango en el Imperio IMP.")
        return

    # 2. Extraer texto (de la descripción de la foto o mensaje solo)
    texto = message.caption if message.content_type == 'photo' else message.text
    
    if not texto or not texto.lower().startswith("subir"):
        return

    try:
        # Limpiamos y dividimos por líneas
        lineas = [l.strip() for l in texto.split('\n') if l.strip()]
        
        # Estructura requerida:
        # [0] Subir Tipo / [1] Nombre / [2] Tamaño / [3] Colores / [4] Precio
        tipo = lineas[0].split(" ", 1)[1] if len(lineas[0].split(" ")) > 1 else "Producto"
        nombre = lineas[1]
        tallas = lineas[2]
        colores = lineas[3]
        precio = int(lineas[4]) if len(lineas) > 4 else 0
        
        # 3. Procesar Imagen de Telegram
        foto_url = ""
        if message.content_type == 'photo':
            file_info = bot.get_file(message.photo[-1].file_id)
            foto_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}"
        else:
            # Si es solo texto, busca un link HTTP
            for l in lineas:
                if l.startswith("http"): foto_url = l

        # 4. Enviar datos al servidor Flask de Mally Wear
        payload = {
            "type": tipo,
            "name": nombre,
            "price": precio,
            "sizes": f"{tallas} | {colores}",
            "img": foto_url,
            "user": f"{rango} {message.from_user.first_name}"
        }

        response = requests.post(API_URL, json=payload, timeout=10)
        
        if response.status_code == 200:
            bot.reply_to(message, f"✅ **{tipo.upper()} PUBLICADA**\n\n👤 **Autor:** {message.from_user.first_name}\n🎖️ **Rango:** {rango}\n📦 **Modelo:** {nombre}\n💰 **Precio:** {precio:,} Gs.")
        else:
            bot.reply_to(message, "❌ Error: El servidor Flask en Termux no responde.")

    except Exception as e:
        bot.reply_to(message, "⚠️ **ERROR DE FORMATO**\n\nEnviá así:\nSubir [Tipo]\nNombre\nTamaño\nColores\nPrecio\n(Adjuntar foto)")

print(f"🚀 Mally Bot Online.\nFundador: {FOUNDER_ID}\nGerentes: {len(GERENTES)}")
bot.polling()
