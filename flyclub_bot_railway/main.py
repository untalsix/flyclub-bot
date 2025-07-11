
import asyncio
import json
import random
from datetime import datetime
import pytz
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, AIORateLimiter
import nest_asyncio

TOKEN = "7869557741:AAHMJ_XIoIHC8QOwCqFuRt3CdIJQwxPF9_E"

def cargar_usuarios():
    try:
        with open("usuarios.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def generar_rutina(nombre):
    frases = [
        "🔥 La disciplina supera al talento.",
        "🚀 Hoy es un buen día para darlo todo.",
        "💪 Tú no paras, tú mejoras.",
        "🎯 El cambio viene del compromiso.",
        "🏁 Paso a paso, día a día. ¡Vamos!"
    ]
    rutina = random.choice([
        "Trote suave 3 km + estiramientos",
        "4x10 ejercicios de fuerza + 2 km de trote",
        "HIIT + core + caminata 30 min"
    ])
    frase = random.choice(frases)
    return f"{frase}\n\n🏋️‍♂️ *Tu rutina personalizada de hoy* 🏃‍♀️\n\n{rutina}\n\n¡A darle, {nombre}! 💥"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    nombre = update.effective_user.first_name
    usuarios = cargar_usuarios()
    if not any(u["chat_id"] == chat_id for u in usuarios):
        usuarios.append({"chat_id": chat_id, "nombre": nombre})
        with open("usuarios.json", "w") as f:
            json.dump(usuarios, f)
    await update.message.reply_text(f"Hola {nombre}, ¡estás registrado!")

async def enviar_rutinas(context: ContextTypes.DEFAULT_TYPE):
    print("⏰ Enviando rutina diaria")
    usuarios = cargar_usuarios()
    for u in usuarios:
        msg = generar_rutina(u["nombre"])
        try:
            await context.bot.send_message(chat_id=u["chat_id"], text=msg, parse_mode="Markdown")
        except Exception as e:
            print(f"Error al enviar a {u['nombre']}: {e}")

async def main():
    app = Application.builder().token(TOKEN).rate_limiter(AIORateLimiter()).build()
    app.add_handler(CommandHandler("start", start))

    zona_mexico = pytz.timezone("America/Mexico_City")
    hora = datetime.strptime("06:00", "%H:%M").time()
    app.job_queue.run_daily(enviar_rutinas, time=hora, timezone=zona_mexico)

    print("✅ Bot corriendo...")
    await app.run_polling()

nest_asyncio.apply()
asyncio.get_event_loop().run_until_complete(main())
