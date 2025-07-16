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
  
    zona = pytz.timezone("America/Mexico_City")
    dia_actual = datetime.now(zona).strftime('%A').lower()
    dias_semana = {
        'monday': 'lunes',
        'tuesday': 'martes',
        'wednesday': 'miércoles',
        'thursday': 'jueves',
        'friday': 'viernes',
        'saturday': 'sábado',
        'sunday': 'domingo'
    }
    dia = dias_semana[dia_actual]

    rutina_dia = rutinas[tipo][nivel][dia]

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
        "🏁 Paso a paso, día a día. ¡Vamos!",
        "🔥 Hoy también cuenta.",
        "💪 Hazlo por ti.",
        "🛑 No pares ahora.",
        "📈 1% mejor cada día.",
        "🚀 Sigue empujando.",
        "🧠 La constancia gana.",
        "😤 El cambio duele, pero vale.",
        "🧘 Cuerpo en movimiento, mente en calma.",
        "⏳ Disciplina > Motivación.",
        "❌ Sin excusas, solo acción.",
        "✊ Tú puedes con esto.",
        "📆 Hoy sí, mañana también.",
        "🌧️ Hazlo aunque no tengas ganas.",
        "🥵 Lo difícil vale la pena.",
        "👣 Cada paso cuenta.",
        "⚡ Entrena duro, vive fácil.",
        "🪞 Tú eres tu competencia.",
        "🔁 No es magia, es hábito.",
        "🧱 Ponte fuerte, no excusas.",
        "🎯 Haz que cuente.",
        "💥 Duele, pero sirve.",
        "🐢 Sigue, aunque cueste.",
        "🌬️ Respira y continúa.",
        "🙏 Hoy entrenas, mañana agradeces.",
        "🚧 Rompe tus límites.",
        "🏋️ Más fuerte cada día.",
        "🔨 Hazlo con todo.",
        "📉 Menos excusas, más resultados.",
        "🧬 Sé tu mejor versión.",
        "👀 Tu esfuerzo se nota.",
        "🏃 Corre, levanta, repite.",
        "📅 Cada día cuenta.",
        "✅ Hazlo valer.",
        "💦 Suda con orgullo.",
        "🚫 Nada te detiene.",
        "🔊 Tu cuerpo te lo pide.",
        "👟 Haz ruido con tus pasos.",
        "💓 Movimiento es vida.",
        "😮‍💨 Ríndete solo al cansancio.",
        "☀️ Empieza, lo demás fluye.",
        "🎧 Enfócate, entrena, crece.",
        "🕹️ No te detengas.",
        "🏆 Lo estás logrando.",
        "💣 Haz que duela, luego que valga.",
        "⏱️ Un día menos, una meta más cerca.",
        "🧰 Hazlo fuerte, hazlo bien.",
        "👑 Tú puedes, tú mandas.",
        "🥇 El sudor es tu medalla.",
        "🧭 Deja huella, no excusa.",
        "🔁 Hoy te toca mejorar.",
    ]

    agua = round(random.uniform(2.0, 3.5), 1)
    frase = random.choice(frases)

    return f"""{frase}

🏋️‍♂️ *Esto te toca hoy ({dia.title()})* 🏃‍♀️

{rutina_dia}

🍽️ Desayuno: {desayuno}
🍛 Comida: {comida}
🌙 Cena: {cena}
💧 Agua: {agua} litros

¡Hazlo por ti, {usuario['nombre']}! 💥 ¿Estás list@?"""



    rutinas = {

        "gym": {
        "principiante": {
            "lunes": """*Lunes - Pecho*

1️⃣ Press de pecho con mancuernas — 3x12  
2️⃣ Aperturas con mancuernas — 3x15  
3️⃣ Flexiones modificadas — 3x10  
⏱️ Descanso: 45 segundos entre series""",

            "martes": """*Martes - Espalda*
1️⃣ Remo con banda elástica — 3x15  
2️⃣ Peso muerto con mancuerna ligera — 3x12  
3️⃣ Superman en el suelo — 3x20 seg  
⏱️ Descanso: 45 segundos entre ejercicios""",

            "miércoles": """*Miércoles - Piernas*
1️⃣ Sentadillas — 4x12  
2️⃣ Desplantes hacia atrás — 3x10 por pierna  
3️⃣ Puente de glúteo — 3x15  
⏱️ Descanso: 60 segundos entre series""",

            "jueves": """*Jueves - Core / Abdomen*
1️⃣ Crunch clásico — 3x20  
2️⃣ Plancha — 3x30 segundos  
3️⃣ Elevaciones de piernas — 3x15  
⏱️ Descanso: 30 segundos entre ejercicios""",

            "viernes": """*Viernes - Brazos*
1️⃣ Curl de bíceps con botellas — 3x12  
2️⃣ Fondos en silla (tríceps) — 3x10  
3️⃣ Curl martillo — 3x10  
⏱️ Descanso: 45 segundos entre series""",

            "sábado": """*Sábado - Hombros*
1️⃣ Elevaciones frontales — 3x12  
2️⃣ Elevaciones laterales — 3x12  
3️⃣ Press militar con mancuernas — 3x10  
⏱️ Descanso: 45 segundos entre series""",

            "domingo": """*Domingo - Full Body*
1️⃣ Circuito: 30 seg cada ejercicio (3 vueltas):  
- Sentadilla  
- Jumping jacks  
- Plancha  
- Lagartijas en rodillas  
⏱️ Descanso: 1 min entre circuitos"""
        },
        "intermedio": {
            "lunes": """💥 *Pecho + Tríceps*

1. Press banca plano – 4x10  
2. Aperturas con mancuernas – 4x12  
3. Fondos en banco – 3x12  
4. Press cerrado – 3x10  
⏱️ *Descanso:* 60-90 seg""",

            "martes": """🦵 *Piernas*

1. Sentadilla con barra – 4x10  
2. Prensa de piernas – 4x12  
3. Zancadas caminando – 3x12 por pierna  
4. Elevación de talones – 4x20  
⏱️ *Descanso:* 60 seg""",

            "miércoles": """🏃‍♂️ *Cardio + Core*

1. Bicicleta o caminadora – 10 min  
2. Crunch abdominal – 4x20  
3. Plancha con elevación de pierna – 4x30 seg  
4. Elevación de piernas – 4x15  
⏱️ *Descanso:* 30-45 seg""",

            "jueves": """💪 *Espalda + Bíceps*

1. Jalón al pecho – 4x10  
2. Remo con barra – 4x12  
3. Curl con mancuernas – 3x12  
4. Curl martillo – 3x10  
⏱️ *Descanso:* 60-90 seg""",

            "viernes": """🔥 *Full Body Funcional*

1. Thrusters (sentadilla + press) – 4x10  
2. Swing con kettlebell o mancuerna – 3x15  
3. Jump squats – 3x12  
4. Escaladores – 3x30 seg  
⏱️ *Descanso:* 45-60 seg""",

            "sábado": """🧘 *Estiramientos + Core*

1. Estiramiento dinámico de cuerpo completo – 10 min  
2. Plancha lateral – 3x30 seg por lado  
3. Crunch bicicleta – 3x20  
4. Estiramientos pasivos finales – 5 min""",

            "domingo": """🚶‍♂️ *Descanso activo*

Recomendado:  
– Caminata ligera 30-45 min  
– Estiramientos suaves  
– Paseo relajado o movilidad"""
        },
        "avanzado": {
            "lunes": """🔥 *Pecho + Tríceps (Hipertrofia)*

1. Press banca con barra – 5x8  
2. Press inclinado con mancuernas – 4x10  
3. Aperturas en polea – 4x12  
4. Fondos lastrados – 3x8  
5. Rompecráneos – 3x10  
⏱️ *Descanso:* 60-90 seg""",

            "martes": """🦵 *Piernas (Fuerza + Volumen)*

1. Sentadilla profunda – 5x5  
2. Peso muerto rumano – 4x8  
3. Prensa inclinada – 4x10  
4. Curl femoral acostado – 3x12  
5. Elevaciones de talones en máquina – 4x20  
⏱️ *Descanso:* 60-90 seg""",

            "miércoles": """💨 *HIIT + Core*

1. Sprint 30 seg / trote 90 seg – 8 rondas  
2. Crunch en polea alta – 4x20  
3. Plancha con desplazamiento – 4x45 seg  
4. Russian twists con peso – 4x20  
⏱️ *Descanso:* 30-45 seg""",

            "jueves": """💪 *Espalda + Bíceps (Volumen)*

1. Dominadas lastradas – 4x8  
2. Remo con barra – 5x10  
3. Jalón en polea cerrada – 4x12  
4. Curl con barra Z – 4x10  
5. Curl concentrado – 3x12  
⏱️ *Descanso:* 60-90 seg""",

            "viernes": """🧱 *Full Body – Potencia*

1. Power Clean o Clean & Press – 5x5  
2. Burpees con salto alto – 4x12  
3. Swing con kettlebell – 4x15  
4. Thrusters – 4x10  
⏱️ *Descanso:* 60-90 seg""",

            "sábado": """🧘 *Movilidad + Estiramientos + Core*

1. Estiramientos dinámicos – 10 min  
2. Bird-dog – 3x20  
3. Elevaciones de piernas – 3x20  
4. Foam rolling en espalda, glúteos y piernas – 10 min  
⏱️ *Descanso libre*""",

            "domingo": """🚶‍♂️ *Descanso Activo*

– Caminata ligera o bici 45 min  
– Estiramientos suaves  
– Hidratación y buena alimentación  
⏱️ *Tu cuerpo también entrena descansando*"""
        }
    },
    "running": {
        "principiante": {
            "lunes": """🏃‍♂️ *Easy Run + Técnica*

- Duración total: 30 minutos  
- 5 min caminata rápida (calentamiento)  
- 20 min trote suave (ritmo cómodo, puedes hablar sin agitarte)  
- 5 min de ejercicios técnicos:  
  - Skipping alto (3x20 seg)  
  - Talones a glúteo (3x20 seg)  
⏱️ Descanso entre ejercicios: 30 seg""",

            "martes": """🔥 *Fartlek Básico*

- Duración total: 25 minutos  
- 5 min caminata rápida (calentamiento)  
- Fartlek: 1 min rápido / 2 min trote x 5 rondas  
- 5 min caminata para enfriar  
💡 Corre rápido ≠ sprint, busca ritmo fuerte sostenible  
⏱️ Descanso activo: trote suave""",

            "miércoles": """🧘‍♂️ *Recuperación Activa + Core*

- Caminata ligera 30 min o bicicleta suave  
- Core (3 rondas):  
  1. Plancha 30 seg  
  2. Crunch abdominal 20 rep  
  3. Elevación de piernas 15 rep  
⏱️ Descanso entre ejercicios: 30 seg""",

            "jueves": """🏁 *Intervalos Cortos*

- Duración total: 30 minutos  
- 5 min calentamiento (caminata + trote suave)  
- Intervalos: 30 seg rápido / 90 seg trote x 6 repeticiones  
- 5 min trote muy suave + estiramientos  
💡 Enfócate en mantener buena técnica""",

            "viernes": """💨 *Tempo Run Suave*

- Duración total: 25-30 minutos  
- 5 min trote suave  
- 15 min ritmo medio (80% de tu capacidad)  
- 5-10 min trote para enfriar  
🎯 Ritmo medio: ya no puedes hablar cómodamente""",

            "sábado": """🏃‍♀️ *Long Run*

- Duración: 40 minutos  
- 10 min caminata + trote muy suave  
- 25 min trote constante (ritmo muy relajado)  
- 5 min caminata para finalizar  
💡 Este día es para aumentar resistencia""",

            "domingo": """🧘 *Descanso Activo + Estiramientos*

- Caminata suave 20-30 minutos  
- Estiramientos estáticos (piernas, espalda baja, glúteos)  
- Respiración profunda y relajación  
😌 Cuerpo y mente también necesitan recuperación"""
        },
        "intermedio": {
            "lunes": """🏃‍♂️ *Easy Run + Técnica*

- Duración total: 40 minutos  
- 10 min trote suave (calentamiento)  
- 25 min trote continuo (ritmo fácil de mantener)  
- 5 min técnica:  
  - Skipping (3x30 seg)  
  - Talones a glúteo (3x30 seg)  
⏱️ Descanso entre ejercicios: 30 seg""",

            "martes": """🔥 *Intervalos Progresivos*

- Duración total: 40 minutos  
- 10 min trote suave (calentamiento)  
- 6x (1 min rápido / 1 min medio / 1 min trote)  
- 5 min caminata para enfriar  
🎯 Ritmo rápido: 85-90%  
🎯 Ritmo medio: 75-80%""",

            "miércoles": """🧘‍♂️ *Recuperación Activa + Core*

- Caminata o bici suave: 30 min  
- Core funcional (3 rondas):  
  1. Plancha frontal 45 seg  
  2. Crunch bicicleta 20 rep  
  3. Elevaciones de piernas 15 rep  
⏱️ Descanso entre rondas: 45 seg""",

            "jueves": """🏁 *Tempo Run*

- Duración total: 40 minutos  
- 10 min trote suave  
- 20 min ritmo umbral (duro pero sostenible, sin poder hablar)  
- 10 min trote lento  
🎯 Ideal para mejorar tolerancia al esfuerzo sostenido""",

            "viernes": """⛰️ *Fartlek por Tiempo*

- Duración total: 35 minutos  
- 10 min calentamiento  
- 5x (2 min rápido / 2 min lento)  
- 5 min enfriamiento  
💡 Usa un parque o zona sin semáforos para fluir mejor""",

            "sábado": """🏃‍♀️ *Long Run Progresivo*

- Duración: 50 minutos  
- 10 min trote muy suave  
- 30 min trote continuo  
- Últimos 10 min: sube el ritmo gradualmente cada 2-3 min  
🎯 Mejora fondo y tolerancia a fatiga""",

            "domingo": """🧘 *Descanso o Caminata Suave*

- Caminata ligera 30 min  
- Estiramientos estáticos (5-10 min)  
- Movilidad de tobillos, cadera y espalda  
😌 Día de recuperación activa"""
        },
        "avanzado": {
            "lunes": """💨 *Series en pista (velocidad)*

- Calentamiento: 10 min trote suave  
- Técnica de carrera: skipping y talones 2x30 seg  
- 6x400m (ritmo muy fuerte)  
  ⏱️ Descanso entre repeticiones: 90 seg caminando  
- 10 min trote muy suave para enfriar  
🎯 Ritmo: 90-95% esfuerzo máximo""",

            "martes": """🧘‍♂️ *Descanso Activo + Core*

- Caminata ligera o bici suave: 30-40 min  
- Core avanzado:  
  1. Plancha frontal: 1 min  
  2. Crunch oblicuo cruzado: 3x15  
  3. Escaladores: 3x40 seg  
⏱️ Descanso entre ejercicios: 30-45 seg""",

            "miércoles": """🏁 *Tempo Run Extendido*

- 10 min trote suave  
- 30 min ritmo tempo (zona de umbral: exigente pero controlado)  
- 5 min trote suave para enfriar  
🎯 Ritmo: 85-90% de esfuerzo""",

            "jueves": """🔥 *Fartlek por bloques*

- Calentamiento: 10 min trote  
- Bloques:  
  - 4x (2 min rápido / 1 min trote)  
  - 3x (3 min fuerte / 1 min trote)  
  - 2x (1 min explosivo / 1 min trote)  
- 5 min caminata suave  
🎯 Ritmo rápido: competitivo, explosivo""",

            "viernes": """💪 *Cuestas (Fuerza específica)*

- 10 min trote suave  
- Técnica: skipping + talones 2x30 seg  
- 8 repeticiones de cuestas de 30-45 seg (pendiente del 5-8%)  
  ⏱️ Descanso bajando caminando  
- 5-10 min trote muy suave  
🎯 Mejora potencia, zancada y técnica""",

            "sábado": """🦵 *Long Run con ritmo objetivo*

- 70 minutos  
  - 20 min ritmo suave  
  - 40 min ritmo medio (zona aeróbica alta)  
  - 10 min final fuerte, cerca de ritmo de carrera  
🎯 Ideal para pruebas de 10k o medio maratón""",

            "domingo": """😌 *Recuperación Total o Movilidad*

- Caminata 20-30 min (opcional)  
- Rutina de movilidad:  
  - Estiramientos activos (piernas, cadera, espalda)  
  - Respiración y relajación  
🧘 Día para recuperar cuerpo y mente"""
        }
    },
    "mixto": {
        "principiante": {
            "lunes": """🏃‍♂️ *Cardio Suave + Core Básico*

1. Caminata rápida o trote suave – 15 min  
2. Crunch abdominal – 3x15  
3. Elevación de piernas – 3x10  
4. Plancha – 3x20 seg  
⏱️ Descanso: 45-60 seg entre ejercicios  
🎯 Enfócate en respirar bien y controlar el movimiento""",

            "martes": """🏋️‍♀️ *Cuerpo Superior Básico*

1. Flexiones en rodillas – 3x10  
2. Remo con banda elástica o mancuerna – 3x12  
3. Curl de bíceps con botella o mancuernas – 3x12  
4. Press de hombros sentado – 3x10  
⏱️ Descanso: 60 seg  
🎯 Técnica sobre peso. Usa lo que tengas en casa si no vas a gym""",

            "miércoles": """🧘 *Estiramiento y Movilidad*

1. Estiramiento de cuello y hombros – 3 min  
2. Estiramiento de espalda baja y caderas – 3 min  
3. Estiramiento de piernas (isquiotibiales, cuádriceps) – 3 min  
4. Respiración profunda + movilidad articular – 5 min  
🎯 Ideal para soltar el cuerpo y prevenir lesiones""",

            "jueves": """🦵 *Piernas y Glúteos*

1. Sentadillas asistidas (con silla) – 3x12  
2. Elevaciones de talón de pie – 3x20  
3. Puente de glúteo – 3x15  
4. Zancadas cortas (opcional con apoyo) – 3x10 por pierna  
⏱️ Descanso: 60 seg  
🎯 Fortalece la base sin impacto""",

            "viernes": """🔥 *Circuito Funcional*

Circuito x 3 rondas (20 seg trabajo / 40 seg descanso):  
1. Jumping jacks (o marcha en sitio)  
2. Sentadillas  
3. Plancha de antebrazo  
4. Abdominales bicicleta  
🎯 Haz a tu ritmo, enfocado en moverte sin agotarte""",

            "sábado": """🏃 *Fartlek Suave (Juego de Ritmos)*

1. Calentamiento caminando – 5 min  
2. Fartlek básico (repetir 4 veces):  
   - 1 min trote rápido  
   - 2 min caminata  
3. Enfriamiento caminando – 5 min  
🎯 Ayuda a mejorar tu capacidad cardiovascular sin forzar demasiado""",

            "domingo": """😌 *Descanso Activo y Recuperación*

1. Caminata ligera o bici – 30 min  
2. Estiramientos suaves – 10 min  
3. Respiración profunda y relajación  
🎯 Día para reponer energías"""
        }
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
    "🔥 Hoy también cuenta.",
    "💪 Hazlo por ti.",
    "🛑 No pares ahora.",
    "📈 1% mejor cada día.",
    "🚀 Sigue empujando.",
    "🧠 La constancia gana.",
    "😤 El cambio duele, pero vale.",
    "🧘 Cuerpo en movimiento, mente en calma.",
    "⏳ Disciplina > Motivación.",
    "❌ Sin excusas, solo acción.",
    "✊ Tú puedes con esto.",
    "📆 Hoy sí, mañana también.",
    "🌧️ Hazlo aunque no tengas ganas.",
    "🥵 Lo difícil vale la pena.",
    "👣 Cada paso cuenta.",
    "⚡ Entrena duro, vive fácil.",
    "🪞 Tú eres tu competencia.",
    "🔁 No es magia, es hábito.",
    "🧱 Ponte fuerte, no excusas.",
    "🎯 Haz que cuente.",
    "💥 Duele, pero sirve.",
    "🐢 Sigue, aunque cueste.",
    "🌬️ Respira y continúa.",
    "🙏 Hoy entrenas, mañana agradeces.",
    "🚧 Rompe tus límites.",
    "🏋️ Más fuerte cada día.",
    "🔨 Hazlo con todo.",
    "📉 Menos excusas, más resultados.",
    "🧬 Sé tu mejor versión.",
    "👀 Tu esfuerzo se nota.",
    "🏃 Corre, levanta, repite.",
    "📅 Cada día cuenta.",
    "✅ Hazlo valer.",
    "💦 Suda con orgullo.",
    "🚫 Nada te detiene.",
    "🔊 Tu cuerpo te lo pide.",
    "👟 Haz ruido con tus pasos.",
    "💓 Movimiento es vida.",
    "😮‍💨 Ríndete solo al cansancio.",
    "☀️ Empieza, lo demás fluye.",
    "🎧 Enfócate, entrena, crece.",
    "🕹️ No te detengas.",
    "🏆 Lo estás logrando.",
    "💣 Haz que duela, luego que valga.",
    "⏱️ Un día menos, una meta más cerca.",
    "🧰 Hazlo fuerte, hazlo bien.",
    "👑 Tú puedes, tú mandas.",
    "🥇 El sudor es tu medalla.",
    "🧭 Deja huella, no excusa.",
    "🔁 Hoy te toca mejorar.",

    ]

    agua = round(random.uniform(2.0, 3.5), 1)

    rutina_dia = random.choice(rutinas[tipo][nivel])

    frase = random.choice(frases)

    return f"""{frase}

🏋️‍♂️ *Esto te toca hoy* 🏃‍♀️

{rutina_dia}

🍽️ Desayuno: {desayuno}

🍛 Comida: {comida}

🌙 Cena: {cena}

💧 Agua: {agua} litros

¡Hazlo por ti, {usuario['nombre']}! 💥 ¿Estas list@? """

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

nest_asyncio.apply()

asyncio.get_event_loop().run_until_complete(main())
