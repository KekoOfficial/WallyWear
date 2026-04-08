import telebot
import requests
from config import TOKEN, FOUNDER_ID, GERENTES, API_URL

bot = telebot.TeleBot(TOKEN)

def obtener_rango(user_id):
    if user_id == FOUNDER_ID:
        return "FOUNDER"
    elif user_id in GERENTES:
        return "GERENTE"
    return None

@bot.message_handler(content_types=['text', 'photo'])
def manejar_entrada(message):
    user_id = message.from_user.id
    rango = obtener_rango(user_id)

    # 1. Seguridad: Solo Fundador y Gerentes
    if not rango:
        bot.reply_to(message, "🚫 Acceso Denegado. No perteneces al staff de Imperio IMP.")
        return

    # 2. Extraer texto (ya sea de una foto o mensaje solo)
    texto = message.caption if message.content_type == 'photo' else message.text
    
    if not texto or not texto.lower().startswith("subir"):
        return

    try:
        # Separar por líneas y limpiar espacios
        lineas = [l.strip() for l in texto.split('\n') if l.strip()]
        
        # Estructura según tu pedido:
        # [0] Subir Tipo / [1] Nombre / [2] Tamaño / [3] Colores / [4] Precio
        tipo = lineas[0].split(" ", 1)[1] if len(lineas[0].split(" ")) > 1 else "Prenda"
        nombre = lineas[1]
        tallas = lineas[2]
        colores = lineas[3]
        precio = int(lineas[4]) if len(lineas) > 4 else 0
        
        # 3. Procesar Imagen
        foto_url = ""
        if message.content_type == 'photo':
            # Obtenemos la URL de la foto directamente de Telegram
            file_info = bot.get_file(message.photo[-1].file_id)
            foto_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}"
        else:
            # Si es solo texto, buscamos si hay un link http
            for l in lineas:
                if l.startswith("http"): foto_url = l

        # 4. Enviar datos al servidor Flask
        payload = {
            "type": tipo,
            "name": nombre,
            "price": precio,
            "sizes": f"{tallas} | {colores}",
            "img": foto_url,
            "user": f"[{rango}] {message.from_user.first_name}"
        }

        response = requests.post(API_URL, json=payload, timeout=10)
        
        if response.status_code == 200:
            bot.reply_to(message, f"✅ **{tipo.upper()} PUBLICADA**\n👤 Por: {message.from_user.first_name}\n🛡️ Rango: {rango}\n💰 {precio:,} Gs.")
        else:
            bot.reply_to(message, "❌ Error: Flask está apagado o la DB no conectó.")

    except Exception as e:
        bot.reply_to(message, "⚠️ Error de formato. Enviá así:\n\nSubir [Tipo]\nNombre\nTalles\nColores\nPrecio\n(Adjuntar foto)")

print(f"🚀 Bot Mally Wear activo. Fundador: {FOUNDER_ID}")
bot.polling()
