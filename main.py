import asyncio
import json
import random
from datetime import datetime
import pytz
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,

    CommandHandler,

    CallbackQueryHandler,

    ContextTypes,

    AIORateLimiter

)

import nest_asyncio

TOKEN = "7869557741:AAHMJ_XIoIHC8QOwCqFuRt3CdIJQwxPF9_E"

def cargar_usuarios():

    try:

        with open("usuarios.json", "r") as f:

            return json.load(f)

    except FileNotFoundError:

        return []

def guardar_usuarios(usuarios):

    with open("usuarios.json", "w") as f:

        json.dump(usuarios, f, indent=2)

def generar_rutina(usuario):

    nivel = usuario['nivel']

    tipo = usuario['rutina_tipo']

    rutinas = {

        "gym": {

            "principiante": [

                "Circuito full body 3x15: sentadilla, lagartija, abdominales",

                "Entrenamiento con mancuernas: 3x10 (bíceps, tríceps, hombros)"

            ],

            "intermedio": [

                "Día de pecho y espalda: 4x10 press banca + jalón al pecho",

                "Piernas: sentadilla 4x10 + prensa 4x12 + glúteos 3x20"

            ],

            "avanzado": [

                "Hipertrofia avanzada: 5x8 en superseries de empuje y tracción",

                "Fuerza máxima: 5x5 peso muerto + press militar"

            ]

        },

        "running": {

            "principiante": [

                "Trote suave 3 km + estiramientos",

                "Fartlek ligero: 30 seg rápido / 90 seg trote x 5"

            ],

            "intermedio": [

                "6 km ritmo medio + técnica de carrera",

                "4 km tempo run + 1 km suave"

            ],

            "avanzado": [

                "8 km intervalado (2 km suave + 4x1 rápido + 2 km)",

                "10 km progresivo (cada 2 km más rápido)"

            ]

        },

        "mixto": {

            "principiante": [

                "2 km trote + 3 circuitos de fuerza cuerpo completo",

                "Bike 15 min + abdominales y flexiones 3x15"

            ],

            "intermedio": [

                "3 km run + 4x10 ejercicios con peso",

                "Tabata: 4 ejercicios intensos x 20 seg/10 seg"

            ],

            "avanzado": [

                "5 km + tren superior en gimnasio",

                "Entreno cruzado: HIIT + escaleras + core"

            ]

        }

    }



    desayuno = random.choice([

        "Avena con fruta y almendras",

        "Tostadas con huevo y aguacate",

        "Smoothie de proteína y avena"

    ])

    comida = random.choice([

        "Pollo con arroz integral y brócoli",

        "Carne magra con camote y ensalada",

        "Pasta integral con atún y espinacas"

    ])

    cena = random.choice([

        "Ensalada con huevo y semillas",

        "Wrap integral con atún",

        "Yogur con frutas y avena"

    ])

    frases = [

        "🔥 La disciplina supera al talento.",

        "🚀 Hoy es un buen día para darlo todo.",

        "💪 Tú no paras, tú mejoras.",

        "🎯 El cambio viene del compromiso.",

        "🏁 Paso a paso, día a día. ¡Vamos!"

    ]

    agua = round(random.uniform(2.0, 3.5), 1)

    rutina_dia = random.choice(rutinas[tipo][nivel])

    frase = random.choice(frases)



    return f"""{frase}



🏋️‍♂️ *Tu rutina personalizada de hoy* 🏃‍♀️



{rutina_dia}



🍽️ Desayuno: {desayuno}

🍛 Comida: {comida}

🌙 Cena: {cena}

💧 Agua: {agua} litros



¡A darle, {usuario['nombre']}! 💥"""



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    nombre = update.effective_user.first_name

    usuarios = cargar_usuarios()

    if any(u["chat_id"] == chat_id for u in usuarios):

        await update.message.reply_text(f"👋 Hola {nombre}, ya estás registrado.")

        return



    nuevo_usuario = {

        "nombre": nombre,

        "chat_id": chat_id,

        "objetivo": "salud",

        "nivel": "principiante",

        "rutina_tipo": "mixto"

    }

    usuarios.append(nuevo_usuario)

    guardar_usuarios(usuarios)



    await update.message.reply_text(

        f"✅ ¡Bienvenido {nombre}!\nHas sido registrado con rutina *mixta*, nivel *principiante*.\nUsa /menu para configurar tu perfil.",

        parse_mode="Markdown"

    )



async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [InlineKeyboardButton("Nivel", callback_data='menu_nivel')],

        [InlineKeyboardButton("Objetivo", callback_data='menu_objetivo')],

        [InlineKeyboardButton("Tipo Rutina", callback_data='menu_tipo')],

        [InlineKeyboardButton("Ver perfil", callback_data='menu_perfil')]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Selecciona qué quieres modificar o ver:", reply_markup=reply_markup)



async def perfil(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    usuarios = cargar_usuarios()

    usuario = next((u for u in usuarios if u["chat_id"] == chat_id), None)

    if not usuario:

        await update.message.reply_text("❌ No estás registrado. Usa /start primero.")

        return

    texto = (f"📋 *Tu perfil actual:*\n\n"

             f"👤 Nombre: {usuario['nombre']}\n"

             f"🎯 Objetivo: *{usuario['objetivo']}*\n"

             f"📈 Nivel: *{usuario['nivel']}*\n"

             f"🏋️ Tipo de rutina: *{usuario['rutina_tipo']}*")

    await update.message.reply_text(texto, parse_mode="Markdown")





async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    chat_id = query.message.chat.id

    usuarios = cargar_usuarios()

    usuario = next((u for u in usuarios if u["chat_id"] == chat_id), None)

    if not usuario:

        await query.edit_message_text("❌ No estás registrado. Usa /start primero.")

        return



    data = query.data



    if data == "menu_perfil":

        await perfil(update, context)

        return



    if data == "menu_nivel":

        keyboard = [

            [InlineKeyboardButton("Principiante", callback_data='nivel_principiante')],

            [InlineKeyboardButton("Intermedio", callback_data='nivel_intermedio')],

            [InlineKeyboardButton("Avanzado", callback_data='nivel_avanzado')],

            [InlineKeyboardButton("Volver", callback_data='menu')]

        ]

        await query.edit_message_text("Selecciona tu nivel:", reply_markup=InlineKeyboardMarkup(keyboard))

        return



    if data == "menu_objetivo":

        keyboard = [

            [InlineKeyboardButton("Salud", callback_data='objetivo_salud')],

            [InlineKeyboardButton("Volumen", callback_data='objetivo_volumen')],

            [InlineKeyboardButton("Definición", callback_data='objetivo_definicion')],

            [InlineKeyboardButton("Resistencia", callback_data='objetivo_resistencia')],

            [InlineKeyboardButton("Volver", callback_data='menu')]

        ]

        await query.edit_message_text("Selecciona tu objetivo:", reply_markup=InlineKeyboardMarkup(keyboard))

        return



    if data == "menu_tipo":

        keyboard = [

            [InlineKeyboardButton("Gym", callback_data='tipo_gym')],

            [InlineKeyboardButton("Running", callback_data='tipo_running')],

            [InlineKeyboardButton("Mixto", callback_data='tipo_mixto')],

            [InlineKeyboardButton("Volver", callback_data='menu')]

        ]

        await query.edit_message_text("Selecciona tipo de rutina:", reply_markup=InlineKeyboardMarkup(keyboard))

        return



    if data.startswith("nivel_"):

        usuario["nivel"] = data.split("_")[1]

        guardar_usuarios(usuarios)

        await query.edit_message_text(f"✅ Nivel actualizado a *{usuario['nivel']}*.", parse_mode="Markdown")

        return



    if data.startswith("objetivo_"):

        usuario["objetivo"] = data.split("_")[1]

        guardar_usuarios(usuarios)

        await query.edit_message_text(f"✅ Objetivo actualizado a *{usuario['objetivo']}*.", parse_mode="Markdown")

        return



    if data.startswith("tipo_"):

        usuario["rutina_tipo"] = data.split("_")[1]

        guardar_usuarios(usuarios)

        await query.edit_message_text(f"✅ Tipo de rutina actualizado a *{usuario['rutina_tipo']}*.", parse_mode="Markdown")

        return



    if data == "menu":

        await menu(update, context)

        return



async def enviar_rutinas(context: ContextTypes.DEFAULT_TYPE):

    bot = context.bot

    usuarios = cargar_usuarios()

    for usuario in usuarios:

        try:

            mensaje = generar_rutina(usuario)

            await bot.send_message(chat_id=usuario["chat_id"], text=mensaje, parse_mode="Markdown")

        except Exception as e:

            print(f"❌ Error enviando a {usuario['nombre']}: {e}")



async def rutina_manual(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    usuarios = cargar_usuarios()

    usuario = next((u for u in usuarios if u["chat_id"] == chat_id), None)

    if not usuario:

        await update.message.reply_text("❌ No estás registrado. Usa /start primero.")

        return

    mensaje = generar_rutina(usuario)

    await update.message.reply_text(mensaje, parse_mode="Markdown")



async def main():

    app = Application.builder().token(TOKEN).rate_limiter(AIORateLimiter()).build()



    app.add_handler(CommandHandler("start", start))

    app.add_handler(CommandHandler("menu", menu))

    app.add_handler(CommandHandler("rutina", rutina_manual))

    app.add_handler(CommandHandler("perfil", perfil))

    app.add_handler(CallbackQueryHandler(button_handler))



    hora = datetime.strptime("12:00", "%H:%M").time()  # 12:00 UTC ≈ 6:00 a.m. México

    app.job_queue.run_daily(enviar_rutinas, time=hora)



    print("✅ Bot corriendo...")

    await app.run_polling()
