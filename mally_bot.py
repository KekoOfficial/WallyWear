import telebot
import requests

TOKEN = "8795507175:AAEf9ujkj_jUMJZeChq6L1bFeS8IMRNFwt4" # Tu token de BotFather
bot = telebot.TeleBot(TOKEN)
API_URL = "http://127.0.0.1:5000/api/admin/add"

@bot.message_handler(func=lambda message: True)
def procesar_pedido(message):
    texto = message.text
    lineas = [l.strip() for l in texto.split('\n') if l.strip()]
    
    # Validamos que el mensaje empiece con "subir"
    if not lineas[0].lower().startswith("subir"):
        return # Si no empieza con subir, ignoramos

    try:
        # Extraemos tipo de producto de la primera línea
        tipo = lineas[0].split(" ", 1)[1] if len(lineas[0].split(" ")) > 1 else "General"
        
        # Asignamos variables según el orden que pediste
        nombre = lineas[1]
        tallas = lineas[2]
        colores = lineas[3]
        
        # Precio: Si hay una 5ta línea, es precio, si no, lo dejamos en 0
        precio = int(lineas[4]) if len(lineas) > 4 else 0
        
        # Imagen: Buscamos un link en el mensaje
        foto = "https://via.placeholder.com/400"
        for l in lineas:
            if l.startswith("http"):
                foto = l

        payload = {
            "type": tipo,
            "name": nombre,
            "price": precio,
            "sizes": tallas,
            "img": foto,
            "user": message.from_user.first_name
        }

        # Conectar al servidor Flask
        response = requests.post(API_URL, json=payload)
        
        if response.status_code == 200:
            bot.reply_to(message, f"✅ **{tipo.upper()} AGREGADA**\n📦 {nombre}\n💰 {precio} Gs\n🎨 {colores}")
        else:
            bot.reply_to(message, "❌ Servidor no responde. ¿Está prendido el `app.py` en Termux?")

    except Exception as e:
        bot.reply_to(message, "⚠️ Error de formato. Usa este esquema:\n\nSubir [Tipo]\nNombre\nTamaño\nColores\nPrecio\nLinkImagen")

print("🤖 BOT ACTIVO: Esperando órdenes...")
bot.polling()
