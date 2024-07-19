from config import * #TOKEN Y CHAT ID
import telebot #API DE TELEBOT
import time #TIEMPO DE ESPERA
from telebot.types import ReplyKeyboardMarkup #BOTONES
from telebot.types import ForceReply #CITAR MENSAJES
from telebot.types import ReplyKeyboardRemove #REMOVER BOTONES
from telebot.types import InlineKeyboardMarkup #BOTONES INLINE
from telebot.types import InlineKeyboardButton #DEFINIR BOTONES INLINE
from telebot.types import Update

#INSTANCIAR EL BOT
bot = telebot.TeleBot(telegram_token)
usuarios = {}


########################################### COMANDOS ############################################

# BIENVENIDA (COMANDO)
@bot.message_handler(commands=["start", "inicio", "reiniciar"])
def cmd_start(message):
    markup = ReplyKeyboardRemove() 
    bot.send_chat_action(message.chat.id, "typing")
    time.sleep(2) 
    bot.send_message(message.chat.id, '<i>🙋🏻‍♀️ Holaa ¡Bienvenido a <b>@Unimar_Bot</b></i>' '<i>! </i>' '\n' 'Mi nombre es ' '<b>Unimari</b>' ', la Asistente Virtual de la ' '<b>Universidad de Margarita</b>', parse_mode="html")
    bot.send_chat_action(message.chat.id, "typing")
    time.sleep(2) 
    markup = InlineKeyboardMarkup(row_width = 2)
    m1 = InlineKeyboardButton("Precios 💸", callback_data="consultar_precio")
    m2 = InlineKeyboardButton("Pensum y UC 🤔", callback_data="visualizar_pensum")
    m3 = InlineKeyboardButton("Contactos ☎", callback_data="contactar_decanatos")
    m4 = InlineKeyboardButton("Normativas 📝", callback_data="mostrar_normativas")
    m5 = InlineKeyboardButton("Correo institucional ✉️", callback_data="mostrar_ci")
    m6 = InlineKeyboardButton("Servicios 🏫", callback_data="ver_servicios")
    m7 = InlineKeyboardButton("Requisitos 📖", callback_data="requisitos_inscripcion")
    m8 = InlineKeyboardButton("Reportar 📬", callback_data="realizar_reporte")
    m9 = InlineKeyboardButton("Planillas 🗂", callback_data="ver_planillas")
    m10 = InlineKeyboardButton("Más información ➡️", callback_data="otras_cosas")
    markup.add(m1, m2, m3, m4, m5, m6, m7, m8, m9, m10)
    bot.send_message(message.chat.id, '<i>¿Cómo podría ayudarte?</i>' '\n' 'Puedes decirme qué tipo de ' '<b>información</b>' ' necesitas', reply_markup=markup, parse_mode="html")


# MENU (COMANDO)
@bot.message_handler(commands=["menu", "ayuda"])
def cmd_menu(message):
    markup = ReplyKeyboardRemove() 
    bot.send_chat_action(message.chat.id, "typing")
    time.sleep(2)
    markup = InlineKeyboardMarkup(row_width = 2)
    m1 = InlineKeyboardButton("Precios 💸", callback_data="consultar_precio")
    m2 = InlineKeyboardButton("Pensum y UC 🤔", callback_data="visualizar_pensum")
    m3 = InlineKeyboardButton("Contactos ☎", callback_data="contactar_decanatos")
    m4 = InlineKeyboardButton("Normativas 📝", callback_data="mostrar_normativas")
    m5 = InlineKeyboardButton("Correo institucional ✉️", callback_data="mostrar_ci")
    m6 = InlineKeyboardButton("Servicios 🏫", callback_data="ver_servicios")
    m7 = InlineKeyboardButton("Requisitos 📖", callback_data="requisitos_inscripcion")
    m8 = InlineKeyboardButton("Reportar 📬", callback_data="realizar_reporte")
    m9 = InlineKeyboardButton("Planillas 🗂", callback_data="ver_planillas")
    m10 = InlineKeyboardButton("Más información ➡️", callback_data="otras_cosas")
    markup.add(m1, m2, m3, m4, m5, m6, m7, m8, m9, m10)
    bot.send_message(message.chat.id, '<i>¿Cómo podría ayudarte?</i>' '\n' 'Puedes decirme qué tipo de ' '<b>información</b>' ' necesitas', reply_markup=markup, parse_mode="html")


# MENU DECANATOS (COMANDO) 
@bot.message_handler(commands=["decanatos"])
def cmd_decanatos(message):
    markup = InlineKeyboardMarkup(row_width = 1)
    bb1 = InlineKeyboardButton("📚 Estudios Generales 📚", callback_data="decanato_generales")
    bb2 = InlineKeyboardButton("🎨 Humanidades, Arte y Educación 🎨", callback_data="decanato_humanidades")
    bb3 = InlineKeyboardButton("📈 Ciencias Económicas 📈", callback_data="decanato_contaduría")
    bb4 = InlineKeyboardButton("⚖️ Ciencias Jurídicas y Políticas ‍⚖️", callback_data="decanato_derecho")
    bb5 = InlineKeyboardButton("👨‍💻 Ingeniería y Afines ‍👨‍💻", callback_data="decanato_ingeniería")
    bb6 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
    markup.add(bb1, bb2, bb3, bb4, bb5, bb6)
    bot.send_message(message.chat.id, '¿Qué ' '<b>Decanato </b>' 'desea contactar?', reply_markup=markup, parse_mode="html")


# MENU PRECIOS (COMANDO)
@bot.message_handler(commands=["precio","precios"])
def cmd_precios(message):
    markup = ReplyKeyboardRemove()
    bot.send_chat_action(message.chat.id, "typing")
    time.sleep(2) 
    markup = InlineKeyboardMarkup(row_width = 2)
    p1 = InlineKeyboardButton("Trimestre 📅", callback_data="precio_trimestre")
    p2 = InlineKeyboardButton("UC 🪙", callback_data="precio_unidades")
    p3 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
    markup.add(p1, p2, p3)
    bot.send_message(message.chat.id, '<i>¿Qué <b>precio</b> necesitas consultar de la <b>Universidad de Margarita</b>?</i>', reply_markup=markup, parse_mode="html")
    


# MENU PENSUM Y UNIDADES
@bot.message_handler(commands=["pensum", "unidades"])
def cmd_pensum(message):
    markup = ReplyKeyboardRemove()
    bot.send_chat_action(message.chat.id, "typing")
    time.sleep(2) 
    markup = InlineKeyboardMarkup(row_width = 2)
    b1 = InlineKeyboardButton("👨‍💻 Ingeniería de Sistemas 👨‍💻", callback_data="mostrar_pensum_ing")
    b2 = InlineKeyboardButton("🎨 Diseño Gráfico 🎨", callback_data="mostrar_pensum_dis")
    b3 = InlineKeyboardButton("🇬🇧 Idiomas Modernos 🇬🇧", callback_data="mostrar_pensum_idi")
    b4 = InlineKeyboardButton("📈 Contaduría 📈", callback_data="mostrar_pensum_cont")
    b5 = InlineKeyboardButton("💰 Administración 💰", callback_data="mostrar_pensum_adm")
    b6 = InlineKeyboardButton("⚖️ Derecho ⚖️", callback_data="mostrar_pensum_der")
    b7 = InlineKeyboardButton("🧠 Psicología 🧠", callback_data="mostrar_pensum_psi") 
    b8 = InlineKeyboardButton("🗞️ Comunicación Social 🗞️", callback_data="mostrar_pensum_com") 
    markup.add(b1, b2, b3, b4, b5, b6, b7, b8)
    bot.send_message(message.chat.id, '<i>¿Qué <b>Pensum de Estudios</b> y <b>Unidades de crédito</b> deseas visualizar?</i>', reply_markup=markup, parse_mode="html")


# MENU NORMATIVAS
@bot.message_handler(commands=["normativas, reglamento"])
def cmd_normativas(message):
    markup = ReplyKeyboardRemove()
    bot.send_chat_action(message.chat.id, "typing")
    time.sleep(2) 
    markup = InlineKeyboardMarkup(row_width = 1)
    n1 = InlineKeyboardButton("Trabajos de Investigación Cualitativa 📄", callback_data="normas_cuali")
    n2 = InlineKeyboardButton("Trabajos de Investigación Cuantitativa 📄", callback_data="normas_cuanti")
    n3 = InlineKeyboardButton("Evaluación y permanencia estudiantil 📄", callback_data="normas_perm")
    n4 = InlineKeyboardButton("Trabajo de Investigación de Pregrado 📄", callback_data="normas_traba")
    n5 = InlineKeyboardButton("Normas Metodológicas de Tesis y Trabajo de Grado 📄", callback_data="normas_tesis")
    n6 = InlineKeyboardButton("Normas Operativas del Proceso de Inscripción Administrativo 📄", callback_data="normas_admin")
    n7 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
    markup.add(n1,n2,n3,n4,n5,n6,n7)
    bot.send_message(message.chat.id, '<i>¿Qué <b>normativa</b> deseas visualizar de la <b>Universidad de Margarita</b>?</i>', reply_markup=markup, parse_mode="html")


# MENU PLANILLAS (COMANDO)
@bot.message_handler(commands=["planillas"])
def cmd_planillas(message):
    markup = ReplyKeyboardRemove()
    bot.send_chat_action(message.chat.id, "typing")
    time.sleep(2) 
    markup = InlineKeyboardMarkup(row_width = 1)
    p1 = InlineKeyboardButton("Planilla - Solicitud de Inscripción 📝", callback_data="planilla_inscrip")
    p2 = InlineKeyboardButton("Planilla - Inscripción de introductorio 📝", callback_data="planilla_intro")
    p3 = InlineKeyboardButton("Planilla - Solicitud Beca 📝", callback_data="planilla_beca")
    p4 = InlineKeyboardButton("Planilla - Solicitud de título (Grado y Postgrado) 📝", callback_data="planilla_grad")
    p5 = InlineKeyboardButton("Planilla - Actividades de extensión 📝", callback_data="planilla_acti")
    p6 = InlineKeyboardButton("Planilla - Solicitud de Extracréditos 📝", callback_data="planilla_extra")
    p7 = InlineKeyboardButton("Formato - Imposición de Medalla 📝", callback_data="planilla_pensum_meda")
    p8 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
    markup.add(p1, p2, p3, p4, p5, p6, p7, p8)
    bot.send_message(message.chat.id, '<i>¿Qué <b>planilla</b> necesitas que te envíe?</i>', reply_markup=markup, parse_mode="html")






# REPORTE (COMANDO)
@bot.message_handler(commands=["reporte"])

def pregunta_reporte(message):
    markup = ReplyKeyboardRemove()
    bot.send_chat_action(message.chat.id, "typing")
    time.sleep(2) 
    markup = InlineKeyboardMarkup(row_width = 2)
    rr1 = InlineKeyboardButton("Sí ✔️", callback_data="reportar_reporte")
    rr2 = InlineKeyboardButton("No ❌", callback_data="menu")
    markup.add(rr1, rr2)
    bot.send_message(message.chat.id, '<i>¿Quieres realizar un <b>reporte</b> a <b>Control de Estudios</b>?</i>', reply_markup=markup, parse_mode="html")

def cmd_reporte(message):
    markup = ReplyKeyboardRemove() 
    markup = ForceReply()
    bot.send_chat_action(message.chat.id, "typing")
    time.sleep(2) 
    bot.send_message(message.chat.id, 'Para enviar un <b>reporte</b> a <b>Control de Estudios</b>, debe ingresar primero una <b>descripción del inconveniente</b>', parse_mode="html")
    msg = bot.send_message(message.chat.id, "💬 Descripción:", reply_markup= markup)
    bot.register_next_step_handler(msg, reenviar_datos)


def reenviar_datos(message):
    if message.text == None:
        markup = ForceReply()
        enviado = bot.send_message(message.chat.id, '<i><b>Lo lamento, no entiendo tu mensaje</b></i>', parse_mode="html")
        msg = bot.send_message(message.chat.id, "💬 Descripción:", reply_markup= markup)
        bot.register_next_step_handler(msg, reenviar_datos)
    elif len(message.text) <= 500:
        bot.forward_message(id_canal, message_id=message.message_id, from_chat_id=message.chat.id)
        enviado = bot.send_message(message.chat.id, '<i><b>1...</b></i>', parse_mode="html")
        time.sleep(1)
        bot.edit_message_text('<i><b>2...</b></i>', message.chat.id, enviado.message_id, parse_mode="html")
        time.sleep(1)
        bot.edit_message_text('<i><b>3...</b></i>', message.chat.id, enviado.message_id, parse_mode="html")
        time.sleep(1)
        bot.edit_message_text('<i><b>✔️ ¡Tu solicitud fue enviada!</b></i>', message.chat.id, enviado.message_id, parse_mode="html")
        bot.send_message(message.chat.id, '<i>👨‍💼 Personal se pondrá en contacto contigo' '\n' '⚠️ Ten en cuenta que el horario de atención es:' '\n' '<b>📅 Lunes a Viernes</b>' '\n' '<b>🕐 8am a 12pm' '\n' '🕐 1pm a 5pm</b></i>', parse_mode="html")
    else:
        markup = ForceReply()
        enviado = bot.send_message(message.chat.id, '<i><b>Debes escribir un mensaje menor a 500 caracteres</b></i>', parse_mode="html")
        msg = bot.send_message(message.chat.id, "💬 Descripción:", reply_markup= markup)
        bot.register_next_step_handler(msg, reenviar_datos)





########################################### IF, ELIF Y ELSE ############################################

@bot.callback_query_handler(func=lambda X: True)
def respuesta_botones_contacto(call):
    cidd = call.from_user.id
    midd = call.message.id

# CONTACTO DECANATOS (IF/ELIF)
    if call.data == "decanato_generales":
        bot.send_chat_action(cidd, "upload_photo")
        foto = open("./img/decanatos/estudiosgenerales.jpg", "rb")
        bot.send_photo(cidd, foto) 
        bot.send_message(cidd, 'Esta es la <b>información</b> que necesitas para contactar al <b>Decanato de Estudios Generales</b>:' '\n' '\n' '<b>✉️ Correo: </b>' '\n'  'decanato.estudiosgenerales@unimar.edu.ve' '\n' '<b>📞 Teléfono: </b>' '\n' '02952871111' '\n' '<b>🕐 Horario de atención: </b>' '\n'  '<i>8am a 12pm / 1pm a 5pm</i>', parse_mode="html")
    elif call.data == "decanato_humanidades":
        bot.send_chat_action(cidd, "upload_photo")
        foto = open("./img/decanatos/humanidades.jpg", "rb")
        bot.send_photo(cidd, foto)
        bot.send_message(cidd, 'Esta es la <b>información</b> que necesitas para contactar al <b>Decanato de Humanidades, Arte y Educación</b>:' '\n' '\n' '<b>✉️ Correo: </b>' '\n'  'decanato.humarte@unimar.edu.ve' '\n' '<b>📞 Teléfono: </b>' '\n' '02952870466' '\n' '<b>🕐 Horario de atención: </b>' '\n'  '<i>8am a 12pm / 1pm a 5pm</i>', parse_mode="html")
    elif call.data == "decanato_contaduría":
        bot.send_chat_action(cidd, "upload_photo")
        foto = open("./img/decanatos/contaduría.jpg", "rb")
        bot.send_photo(cidd, foto)
        bot.send_message(cidd, 'Esta es la <b>información</b> que necesitas para contactar al <b>Decanato de Ciencias Económicas y Sociales</b>:' '\n' '\n' '<b>✉️ Correo: </b>' '\n' 'decanato.ceys@unimar.edu.ve' '\n' '<b>📞 Teléfono: </b>' '\n' '0295028701111' '\n' '<b>🕐 Horario de atención: </b>' '\n'  '<i>8am a 12pm / 1pm a 5pm</i>', parse_mode="html")
    elif call.data == "decanato_derecho":
        bot.send_chat_action(cidd, "upload_photo")
        foto = open("./img/decanatos/derecho.png", "rb")
        bot.send_photo(cidd, foto)
        bot.send_message(cidd, 'Esta es la <b>información</b> que necesitas para contactar al <b>Decanato de Ciencias Jurídicas y Políticas</b>:' '\n' '\n' '<b>✉️ Correo: </b>' '\n'  'decanato.derecho@unimar.edu.ve' '\n' '<b>📞 Teléfono: </b>' '\n' '02952870271' '\n'  f'<code>+58 0295-2871648</code>' '\n' '<b>⏲ Horario de atención: </b>' '\n'  '<i>8am a 12pm / 1pm a 5pm</i>', parse_mode="html")
    elif call.data == "decanato_ingeniería":
        bot.send_chat_action(cidd, "upload_photo")
        foto = open("./img/decanatos/ingeniería.jpg", "rb")
        bot.send_photo(cidd, foto)
        bot.send_message(cidd, 'Esta es la <b>información</b> que necesitas para contactar al <b>Decanato de Ingeniería y Afines</b>:' '\n' '\n' '<b>✉️ Correo: </b>' '\n'  'decanato.ingenieria@unimar.edu.ve' '\n' '<b>📞 Teléfono: </b>' '\n' '02952871111' '\n' '<b>⏲ Horario de atención: </b>' '\n'  '<i>8am a 12pm / 1pm a 5pm</i>', parse_mode="html")


# DECANATOS MENU (ELIF)
    elif call.data == "contactar_decanatos":
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(cidd, "typing")
        time.sleep(2)
        markup = InlineKeyboardMarkup(row_width = 1)
        bb1 = InlineKeyboardButton("📚 Estudios Generales 📚", callback_data="decanato_generales")
        bb2 = InlineKeyboardButton("🎨 Humanidades, Arte y Educación 🎨", callback_data="decanato_humanidades")
        bb3 = InlineKeyboardButton("📈 Ciencias Económicas 📈", callback_data="decanato_contaduría")
        bb4 = InlineKeyboardButton("⚖️ Ciencias Jurídicas y Políticas ‍⚖️", callback_data="decanato_derecho")
        bb5 = InlineKeyboardButton("👨‍💻 Ingeniería y Afines ‍👨‍💻", callback_data="decanato_ingeniería")
        bb6 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(bb1, bb2, bb3, bb4, bb5, bb6)
        bot.send_message(cidd, '¿Qué ' '<b>Decanato </b>' 'desea contactar?', reply_markup=markup, parse_mode="html")


# MENU PENSUM (ELIF)
    elif call.data == "visualizar_pensum":
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        b1 = InlineKeyboardButton("👨‍💻 Ingeniería de Sistemas 👨‍💻", callback_data="mostrar_pensum_ing")
        b2 = InlineKeyboardButton("🎨 Diseño Gráfico 🎨", callback_data="mostrar_pensum_dis")
        b3 = InlineKeyboardButton("🇬🇧 Idiomas Modernos 🇬🇧", callback_data="mostrar_pensum_idi")
        b4 = InlineKeyboardButton("📈 Contaduría 📈", callback_data="mostrar_pensum_cont")
        b5 = InlineKeyboardButton("💰 Administración 💰", callback_data="mostrar_pensum_adm")
        b6 = InlineKeyboardButton("⚖️ Derecho ⚖️", callback_data="mostrar_pensum_der")
        b7 = InlineKeyboardButton("🧠 Psicología 🧠", callback_data="mostrar_pensum_psi") 
        b8 = InlineKeyboardButton("🗞️ Comunicación Social 🗞️", callback_data="mostrar_pensum_com") 
        b9 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)
        bot.send_message(cidd, '<i>¿Qué <b>Pensum de Estudios</b> y <b>Unidades de crédito</b> deseas visualizar?</i>', reply_markup=markup, parse_mode="html")


# DOCUMENTOS PENSUM (ELIF)
    elif call.data == "mostrar_pensum_ing":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/pensum/Pensum de estudios - Ingeniería de Sistemas.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié el ' '<i>Pensum de estudios </i>''correspondiente a la carrera: \n' '<b>Ingeniería de Sistemas 👨‍💻</b>', parse_mode="html")
    elif call.data == "mostrar_pensum_dis":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/pensum/Pensum de estudios - Diseño Gráfico.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié el ' '<i>Pensum de estudios </i>''correspondiente a la carrera: \n' '<b>Diseño Gráfico 🎨</b>', parse_mode="html")
    elif call.data == "mostrar_pensum_idi":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/pensum/Pensum de estudios - Idiomas Modernos.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié el ' '<i>Pensum de estudios </i>''correspondiente a la carrera: \n' '<b>Idiomas Modernos 🇬🇧</b>', parse_mode="html")
    elif call.data == "mostrar_pensum_cont":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/pensum/Pensum de estudios - Contaduría.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié el ' '<i>Pensum de estudios </i>''correspondiente a la carrera: \n' '<b>Contaduría 📈</b>', parse_mode="html")
    elif call.data == "mostrar_pensum_adm":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/pensum/Pensum de estudios - Administración.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié el ' '<i>Pensum de estudios </i>''correspondiente a la carrera: \n' '<b>Administración 💰</b>', parse_mode="html")
    elif call.data == "mostrar_pensum_der":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/pensum/Pensum de estudios - Derecho.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié el ' '<i>Pensum de estudios </i>''correspondiente a la carrera: \n' '<b>Derecho ⚖️</b>', parse_mode="html")
    elif call.data == "mostrar_pensum_psi":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/pensum/Pensum de estudios - Psicología.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié el ' '<i>Pensum de estudios </i>''correspondiente a la carrera: \n' '<b>Psicología 🧠</b>', parse_mode="html")
    elif call.data == "mostrar_pensum_com":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/pensum/Pensum de estudios - Comunicación Social.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié el ' '<i>Pensum de estudios </i>' 'correspondiente a la carrera: \n' '<b>Comunicación Social 🗞️</b>', parse_mode="html")


# MENU PRECIO (IF)
    elif call.data == "consultar_precio":
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        p1 = InlineKeyboardButton("Trimestre 📅", callback_data="precio_trimestre")
        p2 = InlineKeyboardButton("UC 🪙", callback_data="precio_unidades")
        p3 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(p1, p2, p3)
        bot.send_message(cidd, '<i>¿Qué <b>precio</b> necesitas consultar de la <b>Universidad de Margarita</b>?</i>', reply_markup=markup, parse_mode="html")


# PRECIOS (ELIF)
    elif call.data == "precio_trimestre":
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        texto = 'El ' '<b>precio </b>' 'del ' '<b>Trimestre </b>' 'equivale a: ' '<b>350$</b>' '\n'  'El valor del dólar, según el ' '<i>BCV</i>' ', para el día de hoy ' '<i>(06-12-2022) </i>' 'es: ' '<b>11.69 Bs</b>'
        bot.send_message(cidd, texto, parse_mode="html")
    elif call.data == 'precio_unidades':
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        texto = 'El ' '<b>precio </b>' 'de las ' '<b>Unidades </b>' 'equivale a: ' '<b>50$</b>' '\n'  'El valor del dólar, según el ' '<i>BCV</i>' ', para el día de hoy ' '<i>(06-12-2022) </i>' 'es: ' '<b>11.69 Bs</b>'
        bot.send_message(cidd, texto, parse_mode="html")


# MENU NORMATIVAS (ELIF)
    elif call.data == "mostrar_normativas":
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 1)
        n1 = InlineKeyboardButton("Trabajos de Investigación Cualitativa 📄", callback_data="normas_cuali")
        n2 = InlineKeyboardButton("Trabajos de Investigación Cuantitativa 📄", callback_data="normas_cuanti")
        n3 = InlineKeyboardButton("Evaluación y permanencia estudiantil 📄", callback_data="normas_perm")
        n4 = InlineKeyboardButton("Trabajo de Investigación de Pregrado 📄", callback_data="normas_traba")
        n5 = InlineKeyboardButton("Normas Metodológicas de Tesis y Trabajo de Grado 📄", callback_data="normas_tesis")
        n6 = InlineKeyboardButton("Normas Operativas del Proceso de Inscripción Administrativo 📄", callback_data="normas_admin")
        n7 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(n1,n2,n3,n4,n5,n6, n7)
        bot.send_message(cidd, '<i>¿Qué <b>normativa</b> deseas visualizar de la <b>Universidad de Margarita</b>?</i>', reply_markup=markup, parse_mode="html")


# MOSTRAR NORMATIVAS (ELIF)
    elif call.data == "normas_cuali":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/normativas/Manual - Trabajos de Investigación Cualitativa.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié el ' '<i>Manual </i>''correspondiente a: \n' '<b>Trabajos de Investigación Cualitativa 📄</b>', parse_mode="html")
    elif call.data == "normas_cuanti":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/normativas/Manual - Trabajos de Investigación Cuantitativa.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié el ' '<i>Manual </i>''correspondiente a: \n' '<b>Trabajos de Investigación Cuantitativa 📄</b>', parse_mode="html")
    elif call.data == "normas_perm":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/normativas/Normas - Evaluación y permanencia estudiantil.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié el ' '<i>Manual </i>''correspondiente a: \n' '<b>Evaluación y permanencia estudiantil 📄</b>', parse_mode="html")
    elif call.data == "normas_traba":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/normativas/Normas - Trabajo de Investigación de Pregrado.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié el ' '<i>Manual </i>''correspondiente a: \n' '<b>Trabajo de Investigación de Pregrado 📄</b>', parse_mode="html")
    elif call.data == "normas_tesis":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/normativas/Normas Metodológicas - Tesis y Trabajo de Grado.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié el ' '<i>Manual </i>''correspondiente a: \n' '<b>Tesis y Trabajo de Grado 📄</b>', parse_mode="html")
    elif call.data == "normas_admin":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/normativas/Normas Operativas - Proceso de Inscripción Administrativo.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié el ' '<i>Manual </i>' 'correspondiente al: \n' '<b>Proceso de Inscripción Administrativo 📄</b>', parse_mode="html")


# CORREO INSTITUCIONAL (ELIF)
    elif call.data == "mostrar_ci":
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        x = bot.send_message(cidd, 'Todos los <b>estudiantes y docentes de la Universidad</b> tienen un <b>correo institucional</b> asignado', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(6)
        bot.edit_message_text('A través del <b>correo institucional</b> recibirás notificaciones de la <b>universidad, comunicaciones internas e información de las plataformas educativas y del Aula Virtual.</b>', cidd, x.message_id, parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(8)
        bot.send_chat_action(cidd, "typing")
        bot.edit_message_text('El <b>correo institucional</b> se obtiene de la siguiente forma:', cidd, x.message_id, parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        bot.edit_message_text('<i>1. En caso de ser estudiante del <b>curso Introductorio, pregrado o postgrado</b>, previamente debes haber realizado la <b>inscripción administrativa y académica</b>. Si realizarás un <b>curso, diplomado o taller</b> de las distintas <b>ofertas promocionadas</b> por el <b>Vicerrectorado de Extensión</b>, debes haber pagado la <b>matrícula</b>.\n \n 2. Ingresa a la <b>plataforma web</b> de UNIMAR y haz clic en el ícono de <b>Pagos OnLine</b>. \n \n 3. Ubica el <b>módulo de registro de datos</b> y oprime el botón <b>“Registra o actualiza tus datos personales”</b>. \n \n 4. Ingresa tu <b>número de Cédula</b> y pulsa <b>Buscar</b>. Aparecerán los datos asociados a tu usuario registrados en el sistema: <b>Nombre, Apellido, Fecha de Nacimiento, Sexo</b>. En caso de presentar error en los datos cargados, por favor envía un correo a: </i>control.estudios@unimar.edu.ve <i>solicitando la corrección, según sea el caso. \n \n 5. Ingresa la información para la categoría <b>Estado Civil, Correo Electrónico Personal y Número de Teléfono</b>. Luego, escribe el <b>código de validación</b> que aparece en la <b>imagen</b> y pulsa la opción <b>Validar</b> y después <b>Guardar</b>. \n \n 6. En breves minutos recibirás en tu <b>correo personal</b> los datos de acceso al <b>correo institucional</b>. \n \n 7. Inicia sesión con el <b>correo institucional</b> desde <b>Gmail</b> usando los datos suministrados anteriormente. <b>Te recomiendo cambiar la contraseña por una personal.</b> \n</i>', cidd, x.message_id, parse_mode="html")


# MENU PLANILLAS (ELIF)
    elif call.data == "ver_planillas":
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 1)
        p1 = InlineKeyboardButton("Planilla - Solicitud de Inscripción 📝", callback_data="planilla_inscrip")
        p2 = InlineKeyboardButton("Planilla - Inscripción de introductorio 📝", callback_data="planilla_intro")
        p3 = InlineKeyboardButton("Planilla - Solicitud Beca 📝", callback_data="planilla_beca")
        p4 = InlineKeyboardButton("Planilla - Solicitud de título (Grado y Postgrado) 📝", callback_data="planilla_grad")
        p5 = InlineKeyboardButton("Planilla - Actividades de extensión 📝", callback_data="planilla_acti")
        p6 = InlineKeyboardButton("Planilla - Solicitud de Extracréditos 📝", callback_data="planilla_extra")
        p7 = InlineKeyboardButton("Formato - Imposición de Medalla 📝", callback_data="planilla_pensum_meda")
        p8 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(p1, p2, p3, p4, p5, p6, p7, p8)
        bot.send_message(cidd, '<i>¿Qué <b>planilla</b> necesitas que te envíe?</i>', reply_markup=markup, parse_mode="html")


# MOSTRAR PLANILLAS (ELIF)
    elif call.data == "planilla_inscrip":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/planillas/Planilla - Solicitud de Inscripción.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié la ' '<i>Planilla </i>''correspondiente a la: \n' '<b>Solicitud de Inscripción 📝</b>', parse_mode="html")
    elif call.data == "planilla_intro":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/planillas/Planilla - Inscripción de introductorio.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié la ' '<i>Planilla </i>''correspondiente a la: \n' '<b>Inscripción del introductorio 📝</b>', parse_mode="html")
    elif call.data == "planilla_beca":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/planillas/Planilla - Solicitud Beca.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié la ' '<i>Planilla </i>''correspondiente a la: \n' '<b>Solicitud Beca 📝</b>', parse_mode="html")
    elif call.data == "planilla_grad":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/planillas/Planilla - Solicitud de título (Grado y Postgrado).pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié la ' '<i>Planilla </i>''correspondiente a la: \n' '<b>Solicitud de título (Grado y Postgrado) 📝</b>', parse_mode="html")
    elif call.data == "planilla_acti":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/planillas/Planilla - Actividades de extensión.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié la ' '<i>Planilla </i>''correspondiente a las: \n' '<b>Actividades de extensión 📝</b>', parse_mode="html")
    elif call.data == "planilla_extra":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/planillas/Planilla - Solicitud de Extracréditos.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié la ' '<i>Planilla </i>''correspondiente a la : \n' '<b>Solicitud de Extracréditos 📝</b>', parse_mode="html")
    elif call.data == "planilla_pensum_meda":
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/planillas/Formato - Imposición de Medalla.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié la ' '<i>Planilla </i>' 'correspondiente a la: \n' '<b>Imposición de Medalla 📝</b>', parse_mode="html")


# MENU MÁS INFORMACIÓN (ELIF)
    elif call.data == "otras_cosas":
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        o1 = InlineKeyboardButton("Ubicación 📍", url="https://goo.gl/maps/i8i8uz9jKYbgepyLA")
        o2 = InlineKeyboardButton("Sitio Web 🌐", url="https://www.portalunimar.unimar.edu.ve/")
        o3 = InlineKeyboardButton("Unimar Científica 🔎", url="https://unimarcientifica.edu.ve/")
        o4 = InlineKeyboardButton("Facebook 👤", url="https://www.facebook.com/univ.demargarita")
        o5 = InlineKeyboardButton("Instagram 📷", url="https://www.instagram.com/universidademargarita/")
        o6 = InlineKeyboardButton("YouTube ▶️", url="https://www.youtube.com/channel/UCnRVkJ1OW2oLN_TpvXAnUyw")
        o7 = InlineKeyboardButton("Twitter 🐦", url="https://twitter.com/somosunimar")
        o8 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(o1,o2,o3,o4,o5,o6,o7,o8)
        bot.send_message(cidd, '<i>Estos son algunos <b>enlaces</b> relacionados a la \n</i>' '<b>Universidad de Margarita</b>', reply_markup=markup, parse_mode="html")


# MENU (ELIF)
    elif call.data == "menu":
        markup = ReplyKeyboardRemove() 
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        m1 = InlineKeyboardButton("Precios 💸", callback_data="consultar_precio")
        m2 = InlineKeyboardButton("Pensum y UC 🤔", callback_data="visualizar_pensum")
        m3 = InlineKeyboardButton("Contactos ☎", callback_data="contactar_decanatos")
        m4 = InlineKeyboardButton("Normativas 📝", callback_data="mostrar_normativas")
        m5 = InlineKeyboardButton("Correo institucional ✉️", callback_data="mostrar_ci")
        m6 = InlineKeyboardButton("Servicios 🏫", callback_data="ver_servicios")
        m7 = InlineKeyboardButton("Requisitos 📖", callback_data="requisitos_inscripcion")
        m8 = InlineKeyboardButton("Reportar 📬", callback_data="realizar_reporte")
        m9 = InlineKeyboardButton("Planillas 🗂", callback_data="ver_planillas")
        m10 = InlineKeyboardButton("Más información  ➡️", callback_data="otras_cosas")
        markup.add(m1, m2, m3, m4, m5, m6, m7, m8, m9, m10)
        bot.send_message(cidd, '<i>¿Cómo podría ayudarte?</i>' '\n' 'Puedes decirme qué tipo de ' '<b>información</b>' ' necesitas', reply_markup=markup, parse_mode="html")

# MENU REQUISITOS (ELIF)
    elif call.data == "requisitos_inscripcion":
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        r1 = InlineKeyboardButton("Curso Introductorio", callback_data="requisitos_introductorio")
        r2 = InlineKeyboardButton("Pregrado", callback_data="requisitos_pregrado")
        r3 = InlineKeyboardButton("Equivalencias", callback_data="requisitos_equivalencias")
        r4 = InlineKeyboardButton("Postgrado", callback_data="requisitos_postgrado")
        r5 = InlineKeyboardButton("⬅️ Regresar", callback_data="menu")
        markup.add(r1,r2,r3,r4, r5)
        bot.send_message(cidd, '<i>¿Qué <b>requisitos</b> necesitas encontrar?</i>', reply_markup=markup, parse_mode="html")


# RESPUESTAS REQUISITOS (ELIF)
    elif call.data == "requisitos_introductorio":
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        x = bot.send_message(cidd, '<i>Para el nuevo ingreso del <b>Curso introductorio</b> en la <b>Universidad de Margarita</b>, se necesita la siguiente documentación: </i>', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        x = bot.send_message(cidd, '<i>📌 Ser <b>bachiller</b> o estar <b>cursando el 5to año de bachillerato.</b> \n \n' '📌 Fotocopia ampliada de la <b>Cédula de Identidad.</b> \n \n' '📌 <b>Planilla de Inscripción</b></i>', parse_mode="html")
        time.sleep(3)
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/planillas/Planilla - Inscripción de introductorio.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié la ' '<i>Planilla </i>''correspondiente a la: \n' '<b>Inscripción del introductorio 📝</b>', parse_mode="html")
    elif call.data == 'requisitos_equivalencias':
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        x = bot.send_message(cidd, '<i>Para el ingreso de <b>Técnicos Superiores</b> y <b>Licenciados</b> que aspiren ingresar a la <b>Universidad de Margarita</b>, mediante el Régimen Especial de <b>Equivalencias de Estudios</b>, deberán formalizar la respectiva tramitación de equivalencias, consignando la siguiente documentación: </i>', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(8)
        x = bot.send_message(cidd, '<i>📌 Una <b>copia legible</b> de la <b>Cédula de Identidad ampliada.</b> \n \n 📌 Una <b>copia</b> de la <b>Partida de Nacimiento.</b> \n \n 📌 Una <b>foto</b> de frente <b>tamaño carnet.</b> \n \n 📌 Título de bachiller <b>(original y fondo negro o copia a color autenticada al reverso por la unidad educativa de procedencia, ambas opciones deben tener timbres fiscales).</b> \n \n 📌 <b>Original</b> y una <b>copia</b> de las <b>notas certificadas</b> emitidas por la <b>universidad de procedencia</b> (Formato actual). \n \n 📌 Un <b>fondo negro</b> del Título de <b>Técnico Superior, Licenciado o equivalente.</b> \n \n 📌 <b>Notas Certificadas</b> del 7mo, 8vo y 9no grado de <b>Educación Básica</b> y del 1ro y 2do año de <b>Educación Diversificada</b> (Original y copia) \n \n 📌 <b>Original y fotocopia</b> del <b>pénsum</b>, emitido por la <b>universidad de procedencia.</b> \n \n 📌 <b>Contenido Programático</b> emitido por la <b>universidad de procedencia</b>, debidamente <b>encuadernado e identificado</b> con pestañas con el <b>nombre</b> de cada <b>asignatura.</b> \n \n 📌 <b>Planilla</b> del CNU Prueba de <b>Aptitud Académica</b> o <b>Registro Estudiantil</b> (RUSNIES). \n \n 📌 <b>Pagar el arancel</b> por el trámite de equivalencias. \n \n 📌 En caso de ser Técnico Superior deberá <b>aprobar</b> previamente el <b>curso introductorio.</b></i>', parse_mode="html")
    elif call.data == 'requisitos_postgrado':
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        x = bot.send_message(cidd, '<i>Para el ingreso de <b>Postgrado</b> en la <b>Universidad de Margarita</b>, se necesita la siguiente documentación: </i>', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(8)
        x = bot.send_message(cidd, '<i>📌 <b>Fondo Negro</b> del Título de <b>Pregrado</b> con vista al <b>original.</b> \n \n 📌 <b>Fotocopias</b> de las <b>notas certificadas</b> con vista al <b>original.</b> \n \n 📌 <b>Resumen Curricular.</b> \n \n 📌 <b>Fotocopia</b> de la <b>Cédula de Identidad.</b> \n \n 📌 2 <b>Fotos tamaño carnet.</b> \n \n 📌 Llenar la Planilla de Inscripción. \n \n 📌 <b>Cancelación</b> de la correspondiente <b>matrícula de inscripción.</b></i>', parse_mode="html")
        time.sleep(3)
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/planillas/Planilla - Inscripción de introductorio.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié la ' '<i>Planilla </i>''correspondiente a la: \n' '<b>Inscripción del introductorio 📝</b>', parse_mode="html")


# MENU REQUISITOS DE PREGRADO (ELIF)
    elif call.data == 'requisitos_pregrado':
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        rp1 = InlineKeyboardButton("Bachiller", callback_data="requisitos_bachiller")
        rp2 = InlineKeyboardButton("Licenciado", callback_data="requisitos_licenciado")
        rp3 = InlineKeyboardButton("Técnico Superior", callback_data="requisitos_superior")
        rp4 = InlineKeyboardButton("⬅️ Regresar", callback_data="menu")
        markup.add(rp1, rp2, rp3, rp4)
        bot.send_message(cidd, '<i>¿Qué requisitos de <b>Postgrado</b> necesitas?</i>', reply_markup=markup, parse_mode="html")

# REQUISITOS DE PREGRADO (ELIF)
    elif call.data == 'requisitos_bachiller':
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        x = bot.send_message(cidd, '<i>Para el nuevo ingreso de <b>Bachilleres</b> en la <b>Universidad de Margarita</b>, se necesita los siguientes requisitos: </i>', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        x = bot.send_message(cidd, '<i>📌 Aprobar el <b>Curso Introductorio</b> \n \n 📌 <b>Fotocopia</b> ampliada de la <b>Cédula de Identidad</b> \n \n 📌 <b>Copia</b> de la <b>Partida de Nacimiento.</b> \n \n 📌 <b>Copia</b> de la <b>Partida de Nacimiento.</b> \n \n 📌 <b>Notas Certificadas</b> del 7mo, 8vo y 9no grado de <b>Educación Básica</b> y del 1ro y 2do año de <b>Educación Diversificada (Original y copia).</b> \n \n 📌 <b>Título de bachiller</b> (original y fondo negro o copia a color autenticada al reverso por la unidad educativa de procedencia, ambas opciones deben tener timbres fiscales). \n \n 📌 Planilla del <b>CNU, Prueba de Aptitud Académica o Registro Estudiantil, RUSNIES.</b> \n \n 📌 <b>Planilla de Inscripción.</b> \n \n 📌 Planilla de Inscripción de <b>Actividades Deportivas.</b> \n \n 📌 1 <b>Foto</b> tipo carnet.</i> \n \n', parse_mode="html")
        time.sleep(3)
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/planillas/Planilla - Solicitud de Inscripción.pdf", "rb")
        archivo2 = open("./docs/planillas/Planilla - Actividades de extensión.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_document(cidd, archivo2)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié las ' '<i>Planillas </i>''correspondiente a: \n' '<b>Solicitud de Inscripción y Actividades de Extensión 📝</b>', parse_mode="html")
        
    elif call.data == "requisitos_licenciado":
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        x = bot.send_message(cidd, '<i>Para el nuevo ingreso del <b>Licenciados</b> en la <b>Universidad de Margarita</b>, se necesita los siguientes requisitos: </i>', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        x = bot.send_message(cidd, '📌 <b>Fotocopia ampliada</b> de la <b>Cédula de Identidad</b> \n \n 📌 <b>Copia</b> de la <b>Partida de Nacimiento.</b> \n \n 📌 <b>Notas Certificadas</b> del 7mo, 8vo y 9no grado de <b>Educación Básica</b> y del 1ro y 2do año de <b>Educación Diversificada</b> (Original y copia). \n \n 📌 <b>Título de bachiller</b> (original y fondo negro o copia a color autenticada al reverso por la unidad educativa de procedencia, ambas opciones deben tener timbres fiscales). \n \n 📌 Planilla del <b>CNU, Prueba de Aptitud Académica o Registro Estudiantil, RUSNIES.</b> \n \n 📌 Planilla de Inscripción. \n \n 📌 Planilla de Inscripción de Actividades Deportivas \n \n 📌 1 Foto tipo carnet. \n \n', parse_mode="html")
        time.sleep(3)
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/planillas/Planilla - Solicitud de Inscripción.pdf", "rb")
        archivo2 = open("./docs/planillas/Planilla - Actividades de extensión.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_document(cidd, archivo2)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié las ' '<i>Planillas </i>''correspondiente a: \n' '<b>Solicitud de Inscripción y Actividades de Extensión 📝</b>', parse_mode="html")

    elif call.data == "requisitos_superior":
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        x = bot.send_message(cidd, '<i>Para el nuevo ingreso del <b>Técnico Superior</b> en la <b>Universidad de Margarita</b>, se necesita los siguientes requisitos: </i>', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        x = bot.send_message(cidd, '📌 Aprobar el <b>Curso Introductorio.</b> \n \n 📌 <b>Fotocopia</b> ampliada de la <b>Cédula de Identidad.</b> \n \n 📌 <b>Copia</b> de la <b>Partida de Nacimiento.</b> \n \n 📌 <b>Notas Certificadas</b> del 7mo, 8vo y 9no grado de <b>Educación Básica</b> y del 1ro y 2do año de <b>Educación Diversificada (Original y copia).</b> \n \n 📌 <b>Título de bachiller</b> (original y fondo negro o copia a color autenticada al reverso por la unidad educativa de procedencia, ambas opciones deben tener timbres fiscales). \n \n 📌 Planilla del <b>CNU, Prueba de Aptitud Académica o Registro Estudiantil, RUSNIES.</b> \n \n 📌 <b>Planilla de Inscripción</b> \n \n 📌 Planilla Inscripción de <b>Actividades Deportivas</b> \n \n 📌 1 Foto tipo carnet. \n \n', parse_mode="html")
        time.sleep(3)
        bot.send_chat_action(cidd, "upload_document")
        archivo = open("./docs/planillas/Planilla - Solicitud de Inscripción.pdf", "rb")
        archivo2 = open("./docs/planillas/Planilla - Actividades de extensión.pdf", "rb")
        bot.send_document(cidd, archivo)
        bot.send_document(cidd, archivo2)
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Te envié las ' '<i>Planillas </i>''correspondiente a: \n' '<b>Solicitud de Inscripción y Actividades de Extensión 📝</b>', parse_mode="html")

# MENU SERVICIOS (ELIF)
    elif call.data == "ver_servicios":
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        s1 = InlineKeyboardButton("🙋‍♂️ Presencial", callback_data="modalidad_presencial")
        s2 = InlineKeyboardButton("👩‍💻 Online", callback_data="modalidad_online")
        s3 = InlineKeyboardButton("⬅️ Regresar", callback_data="menu")
        markup.add(s1,s2, s3)
        bot.send_message(cidd, '<i>¿Qué <b>modalidad</b> estudias?</i>', reply_markup=markup, parse_mode="html")


# MODALIDAD PRESENCIAL (ELIF)
    elif call.data == "modalidad_presencial":
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        ss1 = InlineKeyboardButton("Cambio de Carrera", callback_data="cambio_presencial")
        ss2 = InlineKeyboardButton("Reingreso", callback_data="reingreso_presencial")
        ss3 = InlineKeyboardButton("Equivalencias", callback_data="equivalencias_presencial")
        ss4 = InlineKeyboardButton("Retiro Trimestre", callback_data="retirot_presencial")
        ss5 = InlineKeyboardButton("Retiro Materia", callback_data="retirom_presencial")
        ss6 = InlineKeyboardButton("Solicitud Extracréditos", callback_data="solicitud_presencial")
        ss7 = InlineKeyboardButton("⬅️ Regresar", callback_data="menu")
        markup.add(ss1,ss2, ss3, ss4, ss5, ss6, ss7)
        bot.send_message(cidd, '<i>¿Qué <b>Servicio Académico</b> necesitas?</i>', reply_markup=markup, parse_mode="html")


# PASOS PRESENCIAL (ELIF)
    elif call.data == "cambio_presencial":
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        xd = bot.send_message(cidd, 'Para realizar un <b>Cambio de Carrera</b> de manera <b>Presencial</b> debes realizar los siguientes pasos: \n', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(8)
        bot.edit_message_text('<i>1. <b>Pagar</b> en <b>Dirección General de Administración</b> el servicio de <b>cambio de carrera</b>, indicando su <b>nueva elección</b>, este proceso debe realizarse <b>antes de pagar la matricula del trimestre</b>. <b>(Aplica solo para carrera UNIMAR).</b> \n \n 2. Consignar en el <b>Departamento de Control de Estudios</b> la <b>factura</b> para efectuar el <b>cambio de carrera</b> y procesar las equivalencias internas.</i>', cidd, xd.message_id, parse_mode="html")
        
    elif call.data == "reingreso_presencial":
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        xd = bot.send_message(cidd, 'Este proceso se debe realizar el estudiante que <b>tenga 2 o más periodos académicos sin cursar.</b> \n \n Para realizar un <b>Reingreso</b> de manera <b>Presencial</b> debes: \n', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(8)
        bot.edit_message_text('<i><b>Pagar</b> en la <b>Dirección General de Administración</b> el servicio de <b>reingreso</b>, dentro del <b>periodo</b> de la inscripción del trimestre</i>', cidd, xd.message_id, parse_mode="html")

    elif call.data == "equivalencias_presencial":
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        xd = bot.send_message(cidd, 'Para realizar <b>Equivalencias</b> de manera <b>Presencial</b> debes realizar los siguientes pasos: \n', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(8)
        bot.edit_message_text('<i>1. Verificar el <b>cronograma de recepción de documentación</b> 1 mes antes del siguiente trimestre. \n \n 2. <b>Recepción de documentos</b> exigido por la Universidad para el expediente del <b>trámite por equivalencia.</b> \n \n 3. Lapso para realizar y emitir el <b>estudio previo de materias</b> que puedan aprobar. \n \n 4. Luego de la emisión, el estudiante que acepte la cantidad de materias deberá continuar con el <b>proceso de equivalencia</b>, pagando el arancel correspondiente según su carrera \n <b>(Administración, Contaduría Pública, Derecho e Ingeniería de Sistemas por la Universidad Centroccidental “LISANDRO ALVARADO”)</b> \n <b>(Artes, Mención Diseño Gráfico e Idiomas Modernos por La Universidad del Zulia)</b> \n y hacer entrega del <b>expediente académico y la factura del pago del servicio.</b> \n \n 5. Se registra en el <b>Sistema de Control de Estudios</b> las materias del resultado del estudio previo, permitiéndose al estudiante <b>iniciar su trimestre.</b> \n \n 6. Se envían los expedientes a la <b>Universidad correspondiente</b> y espera el resultado emitido por la misma (El lapso dependerá de la Universidad a la que corresponda el estudio). \n \n 7. Una vez recibidas las <b>resoluciones de aprobación</b> de asignaturas por equivalencia, se procede a realizar la <b>carga de notas.</b> \n \n 8. Se informa al estudiante que debe realizar el <b>retiro</b> de sus <b>documentos originales</b> junto a la resolución emitida por la universidad que aprobó la equivalencia.</i>', cidd, xd.message_id, parse_mode="html")

    elif call.data == "retirot_presencial":
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        xd = bot.send_message(cidd, '<i>Los estudiantes inscritos formalmente en la Universidad de Margarita podrán <b>retirarse</b> del periodo académico que cursan, durante las primeras <b>3 semanas</b> de iniciado el trimestre.</i>', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(8)
        bot.edit_message_text('<i>Para formalizar su retiro, deberán dirigir y entregar una comunicación escrita manifestando tal decisión al Departamento de Control de Estudios y Dirección General de Administración indicando en ella sus datos personales. \n \n <b>📞 Número de telefónico \n 💳 Número de cuenta \n 🏦 Nombre del banco \n 👤 Nombre del titular de la cuenta</b> \n \n donde se realizará el reintegro, de haber realizado el pago en efectivo, el reintegro se realizará de la misma manera por las <b>taquillas de recepción.</b> (tres copias de la comunicación) realizará de la misma manera por las <b>taquillas de recepción.</b></i>', cidd, xd.message_id, parse_mode="html")

    elif call.data == "retirom_presencial":
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        xd = bot.send_message(cidd, '<i>El retiro de una <b>asignatura inscrita</b> en el trimestre deberá realizarse dentro de las <b>3 semanas una vez iniciada las clases.</b></i>', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(8)
        bot.edit_message_text('<i>1. Acudir al <b>Departamento de Control de Estudios</b> con su <b>registro de inscripción</b> y solicitar el <b>retiro de la asignatura correspondiente.</b> \n \n 2. Revisar en el portal de <b>alumnos online</b> de la <b>página web</b> las materias que se mantienen en su inscripción.</i>', cidd, xd.message_id, parse_mode="html")

    elif call.data == "solicitud_presencial":
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        xd = bot.send_message(cidd, '<i>El retiro de una <b>asignatura inscrita</b> en el trimestre deberá realizarse dentro de las <b>3 semanas una vez iniciada las clases.</b></i>', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(8)
        bot.edit_message_text('<i>1. Acudir al <b>Departamento de Control de Estudios</b> con su <b>registro de inscripción</b> y solicitar el <b>retiro de la asignatura correspondiente.</b> \n \n 2. Revisar en el portal de <b>alumnos online</b> de la <b>página web</b> las materias que se mantienen en su inscripción.</i>', cidd, xd.message_id, parse_mode="html")

# MODALIDAD PRESENCIAL (ELIF)
    elif call.data == "modalidad_online":
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        so1 = InlineKeyboardButton("Cambio de Carrera", callback_data="cambio_online")
        so2 = InlineKeyboardButton("Reingreso", callback_data="reingreso_online")
        so3 = InlineKeyboardButton("Retiro Trimestre", callback_data="retirot_online")
        so4 = InlineKeyboardButton("Retiro Materia", callback_data="retirom_online")
        so5 = InlineKeyboardButton("Solicitud Extracréditos", callback_data="solicitud_online")
        so6 = InlineKeyboardButton("⬅️ Regresar", callback_data="menu")
        markup.add(so1,so2, so3, so4, so5, so6)
        bot.send_message(cidd, '<i>¿Qué <b>Servicio Académico</b> necesitas?</i>', reply_markup=markup, parse_mode="html")

# PASOS ONLINE (ELIF)
    elif call.data == "cambio_online":
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        xd = bot.send_message(cidd, '<i>Para realizar un <b>Cambio de Carrera</b> de manera <b>Online</b> debes realizar los siguientes pasos: </i> \n', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(8)
        bot.edit_message_text('<i>1. Verificar en el Sistema de <b>Pagos Online</b> de la Universidad de Margarita <b>“Tarifa de Servicio”</b> el costo del <b>cambio de carrera.</b> \n \n 2. Realizar la <b>transferencia correspondiente y registrar el pago en el Sistema de Pagos Online.</b> \n \n 3. La <b>Dirección General de Administración</b> emitirá la factura y enviará al <b>Departamento de Control de Estudios</b>, quienes efectuarán el cambio y procesarán sus equivalencias internas.</i>', cidd, xd.message_id, parse_mode="html")
        
    elif call.data == "reingreso_online":
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        xd = bot.send_message(cidd, '<i>Este proceso se debe realizar el estudiante que <b>tenga 2 o más periodos académicos sin cursar.</b> \n \n Para realizar un <b>Reingreso</b> de manera <b>Presencial</b> debes:</i> \n', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(8)
        bot.edit_message_text('<i>1. Verificar en el Sistema de <b>Pagos Online</b> de la Universidad de Margarita <b>“Tarifa de Servicio”</b> el costo del <b>Reingreso</b> al <b>Sistema de Control de Estudios.</b> \n \n 2. Realizar la <b>transferencia correspondiente y registrar el pago en el Sistema de Pagos Online.</b> \n \n 3. La <b>Dirección General de Administración</b> emitirá la <b>factura</b> permitiendo posteriormente al estudiante <b>pagar e inscribir su trimestre.</b></i>', cidd, xd.message_id, parse_mode="html")


    elif call.data == "retirot_online":
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        xd = bot.send_message(cidd, '<i>Los estudiantes inscritos formalmente en la Universidad de Margarita podrán <b>retirarse</b> del periodo académico que cursan, durante las primeras <b>3 semanas</b> de iniciado el trimestre.</i>', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(8)
        bot.edit_message_text('<i>Para formalizar su retiro, deberán dirigir y entregar una comunicación escrita manifestando tal decisión al Departamento de Control de Estudios y Dirección General de Administración indicando en ella sus datos personales. \n \n <b>📞 Número de telefónico \n 💳 Número de cuenta \n 🏦 Nombre del banco \n 👤 Nombre del titular de la cuenta</b> \n \n Donde se realizará el reintegro, de haber realizado el pago en efectivo, el reintegro se realizará de la misma manera por las <b>taquillas de recepción.</b> (tres copias de la comunicación) realizará de la misma manera por las <b>taquillas de recepción.</b> \n \n 2. Los estudiantes <b>deberán enviar</b> la comunicación al <b>Departamento de Control de Estudios</b> para el retiro de las materias y al <b>Departamento de Cobranza</b> para el trámite administrativo. \n \n <b>✉️ control.estudios@unimar.edu.ve \n \n ✉️ cobranza@unimar.edu.ve</b></i>', cidd, xd.message_id, parse_mode="html")

    elif call.data == "retirom_online":
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        xd = bot.send_message(cidd, '<i>El retiro de una <b>asignatura inscrita</b> en el trimestre deberá realizarse dentro de las <b>3 semanas una vez iniciada las clases.</b></i>', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(8)
        bot.edit_message_text('<i>1. Enviar al <b>correo</b> al Departamento de <b>Control de Estudios</b> \n \n ✉️ control.estudios@unimar.edu.ve \n \n La solicitud de la materia que desea retirar, indicando su: \n \n <b>📌 Nombre y Apellido \n 📌 Cédula de Identidad \n 📌 Carrera y Asignatura.</b> \n \n 2. Revisar en el portal de <b>alumnos online</b> de la <b>página web</b> las materias que se mantienen en su inscripción.</i>', cidd, xd.message_id, parse_mode="html")

    elif call.data == "solicitud_online":
        bot.send_chat_action(cidd, "typing")
        time.sleep(3)
        xd = bot.send_message(cidd, '<i>Este proceso pueden realizar los estudiantes que se encuentren en el <b>9no trimestre con un promedio igual o mayor a 14 puntos.</b></i>', parse_mode="html")
        bot.send_chat_action(cidd, "typing")
        time.sleep(8)
        bot.edit_message_text('<i>1. Verificar el cronograma de recepción de la planilla <b>Solicitud de Extra Crédito</b> \n \n 2. Realizar la solicitud y enviar la planilla al correo electrónico del <b>Departamento de Control de Estudios</b> en el periodo establecido. \n \n control.estudios@unimar.edu.ve \n \n 3. El <b>Departamento de Control de Estudios</b> realiza la <b>evaluación de las solicitudes</b>, procede a realizar el <b>acta de unidades de créditos aprobadas</b> y la publicación de la misma.</i>', cidd, xd.message_id, parse_mode="html")


# MENU REPORTE
    elif call.data == "realizar_reporte":
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        rr1 = InlineKeyboardButton("Sí ✔️", callback_data="reportar_reporte")
        rr2 = InlineKeyboardButton("No ❌", callback_data="menu")
        markup.add(rr1, rr2)
        bot.send_message(cidd, '<i>¿Quieres realizar un <b>reporte</b> a <b>Control de Estudios</b>?</i>', reply_markup=markup, parse_mode="html")

# REPORTE
    elif call.data == "reportar_reporte":
        markup = ReplyKeyboardRemove() 
        markup = ForceReply()
        bot.send_chat_action(cidd, "typing")
        time.sleep(2) 
        bot.send_message(cidd, 'Para enviar un <b>reporte</b> a <b>Control de Estudios</b>, debe ingresar primero una <b>descripción del inconveniente</b>', parse_mode="html")
        msg = bot.send_message(cidd, "💬 Descripción:", reply_markup= markup)
        bot.register_next_step_handler(msg, reenviar_datos)


########################################### RESPONDER MENSAJES ############################################


@bot.message_handler(content_types=["text"])
def mensajes_texto(message):


# RESPUESTA PRECIO
    if "precio" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        p1 = InlineKeyboardButton("Trimestre 📅", callback_data="precio_trimestre")
        p2 = InlineKeyboardButton("UC 🪙", callback_data="precio_unidades")
        p3 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(p1, p2, p3)
        bot.send_message(message.chat.id, '<i>¿Qué <b>precio</b> necesitas consultar de la <b>Universidad de Margarita</b>?</i>', reply_markup=markup, parse_mode="html")


# RESPUESTA MENU
    elif "menu" in message.text:
        markup = ReplyKeyboardRemove() 
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        m1 = InlineKeyboardButton("Precios 💸", callback_data="consultar_precio")
        m2 = InlineKeyboardButton("Pensum y UC 🤔", callback_data="visualizar_pensum")
        m3 = InlineKeyboardButton("Contactos ☎", callback_data="contactar_decanatos")
        m4 = InlineKeyboardButton("Normativas 📝", callback_data="mostrar_normativas")
        m5 = InlineKeyboardButton("Correo institucional ✉️", callback_data="mostrar_ci")
        m6 = InlineKeyboardButton("Servicios 🏫", callback_data="ver_servicios")
        m7 = InlineKeyboardButton("Requisitos 📖", callback_data="requisitos_inscripcion")
        m8 = InlineKeyboardButton("Reportar 📬", callback_data="realizar_reporte")
        m9 = InlineKeyboardButton("Planillas 🗂", callback_data="ver_planillas")
        m10 = InlineKeyboardButton("Más información ➡️", callback_data="otras_cosas")
        markup.add(m1, m2, m3, m4, m5, m6, m7, m8, m9, m10)
        bot.send_message(message.chat.id, '<i>¿Cómo podría ayudarte?</i>' '\n' 'Puedes decirme qué tipo de ' '<b>información</b>' ' necesitas', reply_markup=markup, parse_mode="html")
    elif "ayuda" in message.text:
        markup = ReplyKeyboardRemove() 
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        m1 = InlineKeyboardButton("Precios 💸", callback_data="consultar_precio")
        m2 = InlineKeyboardButton("Pensum y UC 🤔", callback_data="visualizar_pensum")
        m3 = InlineKeyboardButton("Contactos ☎", callback_data="contactar_decanatos")
        m4 = InlineKeyboardButton("Normativas 📝", callback_data="mostrar_normativas")
        m5 = InlineKeyboardButton("Correo institucional ✉️", callback_data="mostrar_ci")
        m6 = InlineKeyboardButton("Servicios 🏫", callback_data="ver_servicios")
        m7 = InlineKeyboardButton("Requisitos 📖", callback_data="requisitos_inscripcion")
        m8 = InlineKeyboardButton("Reportar 📬", callback_data="realizar_reporte")
        m9 = InlineKeyboardButton("Planillas 🗂", callback_data="ver_planillas")
        m10 = InlineKeyboardButton("Más información ➡️", callback_data="otras_cosas")
        markup.add(m1, m2, m3, m4, m5, m6, m7, m8, m9, m10)
        bot.send_message(message.chat.id, '<i>¿Cómo podría ayudarte?</i>' '\n' 'Puedes decirme qué tipo de ' '<b>información</b>' ' necesitas', reply_markup=markup, parse_mode="html")
    elif "menú" in message.text:
        markup = ReplyKeyboardRemove() 
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        m1 = InlineKeyboardButton("Precios 💸", callback_data="consultar_precio")
        m2 = InlineKeyboardButton("Pensum y UC 🤔", callback_data="visualizar_pensum")
        m3 = InlineKeyboardButton("Contactos ☎", callback_data="contactar_decanatos")
        m4 = InlineKeyboardButton("Normativas 📝", callback_data="mostrar_normativas")
        m5 = InlineKeyboardButton("Correo institucional ✉️", callback_data="mostrar_ci")
        m6 = InlineKeyboardButton("Servicios 🏫", callback_data="ver_servicios")
        m7 = InlineKeyboardButton("Requisitos 📖", callback_data="requisitos_inscripcion")
        m8 = InlineKeyboardButton("Reportar 📬", callback_data="realizar_reporte")
        m9 = InlineKeyboardButton("Planillas 🗂", callback_data="ver_planillas")
        m10 = InlineKeyboardButton("Más información ➡️", callback_data="otras_cosas")
        markup.add(m1, m2, m3, m4, m5, m6, m7, m8, m9, m10)
        bot.send_message(message.chat.id, '<i>¿Cómo podría ayudarte?</i>' '\n' 'Puedes decirme qué tipo de ' '<b>información</b>' ' necesitas', reply_markup=markup, parse_mode="html")


# RESPUESTA PENSUM
    elif "pensum" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        b1 = InlineKeyboardButton("👨‍💻 Ingeniería de Sistemas 👨‍💻", callback_data="mostrar_pensum_ing")
        b2 = InlineKeyboardButton("🎨 Diseño Gráfico 🎨", callback_data="mostrar_pensum_dis")
        b3 = InlineKeyboardButton("🇬🇧 Idiomas Modernos 🇬🇧", callback_data="mostrar_pensum_idi")
        b4 = InlineKeyboardButton("📈 Contaduría 📈", callback_data="mostrar_pensum_cont")
        b5 = InlineKeyboardButton("💰 Administración 💰", callback_data="mostrar_pensum_adm")
        b6 = InlineKeyboardButton("⚖️ Derecho ⚖️", callback_data="mostrar_pensum_der")
        b7 = InlineKeyboardButton("🧠 Psicología 🧠", callback_data="mostrar_pensum_psi") 
        b8 = InlineKeyboardButton("🗞️ Comunicación Social 🗞️", callback_data="mostrar_pensum_com") 
        markup.add(b1, b2, b3, b4, b5, b6, b7, b8)
        bot.send_message(message.chat.id, '<i>¿Qué <b>Pensum de Estudios</b> y <b>Unidades de crédito</b> deseas visualizar?</i>', reply_markup=markup, parse_mode="html")


# RESPUESTA NORMATIVAS
    elif "normativas" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 1)
        n1 = InlineKeyboardButton("Trabajos de Investigación Cualitativa 📄", callback_data="normas_cuali")
        n2 = InlineKeyboardButton("Trabajos de Investigación Cuantitativa 📄", callback_data="normas_cuanti")
        n3 = InlineKeyboardButton("Evaluación y permanencia estudiantil 📄", callback_data="normas_perm")
        n4 = InlineKeyboardButton("Trabajo de Investigación de Pregrado 📄", callback_data="normas_traba")
        n5 = InlineKeyboardButton("Normas Metodológicas de Tesis y Trabajo de Grado 📄", callback_data="normas_tesis")
        n6 = InlineKeyboardButton("Normas Operativas del Proceso de Inscripción Administrativo 📄", callback_data="normas_admin")
        n7 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(n1,n2,n3,n4,n5,n6,n7)
        bot.send_message(message.chat.id, '<i>¿Qué <b>normativa</b> deseas visualizar de la <b>Universidad de Margarita</b>?</i>', reply_markup=markup, parse_mode="html")
    elif "normas" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 1)
        n1 = InlineKeyboardButton("Trabajos de Investigación Cualitativa 📄", callback_data="normas_cuali")
        n2 = InlineKeyboardButton("Trabajos de Investigación Cuantitativa 📄", callback_data="normas_cuanti")
        n3 = InlineKeyboardButton("Evaluación y permanencia estudiantil 📄", callback_data="normas_perm")
        n4 = InlineKeyboardButton("Trabajo de Investigación de Pregrado 📄", callback_data="normas_traba")
        n5 = InlineKeyboardButton("Normas Metodológicas de Tesis y Trabajo de Grado 📄", callback_data="normas_tesis")
        n6 = InlineKeyboardButton("Normas Operativas del Proceso de Inscripción Administrativo 📄", callback_data="normas_admin")
        n7 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(n1,n2,n3,n4,n5,n6,n7)
        bot.send_message(message.chat.id, '<i>¿Qué <b>normativa</b> deseas visualizar de la <b>Universidad de Margarita</b>?</i>', reply_markup=markup, parse_mode="html")
    elif "reglamentos" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 1)
        n1 = InlineKeyboardButton("Trabajos de Investigación Cualitativa 📄", callback_data="normas_cuali")
        n2 = InlineKeyboardButton("Trabajos de Investigación Cuantitativa 📄", callback_data="normas_cuanti")
        n3 = InlineKeyboardButton("Evaluación y permanencia estudiantil 📄", callback_data="normas_perm")
        n4 = InlineKeyboardButton("Trabajo de Investigación de Pregrado 📄", callback_data="normas_traba")
        n5 = InlineKeyboardButton("Normas Metodológicas de Tesis y Trabajo de Grado 📄", callback_data="normas_tesis")
        n6 = InlineKeyboardButton("Normas Operativas del Proceso de Inscripción Administrativo 📄", callback_data="normas_admin")
        n7 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(n1,n2,n3,n4,n5,n6,n7)
        bot.send_message(message.chat.id, '<i>¿Qué <b>normativa</b> deseas visualizar de la <b>Universidad de Margarita</b>?</i>', reply_markup=markup, parse_mode="html")
    elif "normativa" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 1)
        n1 = InlineKeyboardButton("Trabajos de Investigación Cualitativa 📄", callback_data="normas_cuali")
        n2 = InlineKeyboardButton("Trabajos de Investigación Cuantitativa 📄", callback_data="normas_cuanti")
        n3 = InlineKeyboardButton("Evaluación y permanencia estudiantil 📄", callback_data="normas_perm")
        n4 = InlineKeyboardButton("Trabajo de Investigación de Pregrado 📄", callback_data="normas_traba")
        n5 = InlineKeyboardButton("Normas Metodológicas de Tesis y Trabajo de Grado 📄", callback_data="normas_tesis")
        n6 = InlineKeyboardButton("Normas Operativas del Proceso de Inscripción Administrativo 📄", callback_data="normas_admin")
        n7 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(n1,n2,n3,n4,n5,n6,n7)
        bot.send_message(message.chat.id, '<i>¿Qué <b>normativa</b> deseas visualizar de la <b>Universidad de Margarita</b>?</i>', reply_markup=markup, parse_mode="html")
    elif "reglas" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 1)
        n1 = InlineKeyboardButton("Trabajos de Investigación Cualitativa 📄", callback_data="normas_cuali")
        n2 = InlineKeyboardButton("Trabajos de Investigación Cuantitativa 📄", callback_data="normas_cuanti")
        n3 = InlineKeyboardButton("Evaluación y permanencia estudiantil 📄", callback_data="normas_perm")
        n4 = InlineKeyboardButton("Trabajo de Investigación de Pregrado 📄", callback_data="normas_traba")
        n5 = InlineKeyboardButton("Normas Metodológicas de Tesis y Trabajo de Grado 📄", callback_data="normas_tesis")
        n6 = InlineKeyboardButton("Normas Operativas del Proceso de Inscripción Administrativo 📄", callback_data="normas_admin")
        n7 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(n1,n2,n3,n4,n5,n6,n7)
        bot.send_message(message.chat.id, '<i>¿Qué <b>normativa</b> deseas visualizar de la <b>Universidad de Margarita</b>?</i>', reply_markup=markup, parse_mode="html")


# RESPUESTA PLANILLAS
    elif "planillas" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 1)
        p1 = InlineKeyboardButton("Planilla - Solicitud de Inscripción 📝", callback_data="planilla_inscrip")
        p2 = InlineKeyboardButton("Planilla - Inscripción de introductorio 📝", callback_data="planilla_intro")
        p3 = InlineKeyboardButton("Planilla - Solicitud Beca 📝", callback_data="planilla_beca")
        p4 = InlineKeyboardButton("Planilla - Solicitud de título (Grado y Postgrado) 📝", callback_data="planilla_grad")
        p5 = InlineKeyboardButton("Planilla - Actividades de extensión 📝", callback_data="planilla_acti")
        p6 = InlineKeyboardButton("Planilla - Solicitud de Extracréditos 📝", callback_data="planilla_extra")
        p7 = InlineKeyboardButton("Formato - Imposición de Medalla 📝", callback_data="planilla_pensum_meda")
        p8 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(p1, p2, p3, p4, p5, p6, p7, p8)
        bot.send_message(message.chat.id, '<i>¿Qué <b>planilla</b> necesitas que te envíe?</i>', reply_markup=markup, parse_mode="html")
    elif "solicitud" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 1)
        p1 = InlineKeyboardButton("Planilla - Solicitud de Inscripción 📝", callback_data="planilla_inscrip")
        p2 = InlineKeyboardButton("Planilla - Inscripción de introductorio 📝", callback_data="planilla_intro")
        p3 = InlineKeyboardButton("Planilla - Solicitud Beca 📝", callback_data="planilla_beca")
        p4 = InlineKeyboardButton("Planilla - Solicitud de título (Grado y Postgrado) 📝", callback_data="planilla_grad")
        p5 = InlineKeyboardButton("Planilla - Actividades de extensión 📝", callback_data="planilla_acti")
        p6 = InlineKeyboardButton("Planilla - Solicitud de Extracréditos 📝", callback_data="planilla_extra")
        p7 = InlineKeyboardButton("Formato - Imposición de Medalla 📝", callback_data="planilla_pensum_meda")
        p8 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(p1, p2, p3, p4, p5, p6, p7, p8)
        bot.send_message(message.chat.id, '<i>¿Qué <b>planilla</b> necesitas que te envíe?</i>', reply_markup=markup, parse_mode="html")
    elif "planilla" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 1)
        p1 = InlineKeyboardButton("Planilla - Solicitud de Inscripción 📝", callback_data="planilla_inscrip")
        p2 = InlineKeyboardButton("Planilla - Inscripción de introductorio 📝", callback_data="planilla_intro")
        p3 = InlineKeyboardButton("Planilla - Solicitud Beca 📝", callback_data="planilla_beca")
        p4 = InlineKeyboardButton("Planilla - Solicitud de título (Grado y Postgrado) 📝", callback_data="planilla_grad")
        p5 = InlineKeyboardButton("Planilla - Actividades de extensión 📝", callback_data="planilla_acti")
        p6 = InlineKeyboardButton("Planilla - Solicitud de Extracréditos 📝", callback_data="planilla_extra")
        p7 = InlineKeyboardButton("Formato - Imposición de Medalla 📝", callback_data="planilla_pensum_meda")
        p8 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(p1, p2, p3, p4, p5, p6, p7, p8)
        bot.send_message(message.chat.id, '<i>¿Qué <b>planilla</b> necesitas que te envíe?</i>', reply_markup=markup, parse_mode="html")


# MENU DECANATOS
    elif "contacto" in message.text:
        markup = InlineKeyboardMarkup(row_width = 1)
        bb1 = InlineKeyboardButton("📚 Estudios Generales 📚", callback_data="decanato_generales")
        bb2 = InlineKeyboardButton("🎨 Humanidades, Arte y Educación 🎨", callback_data="decanato_humanidades")
        bb3 = InlineKeyboardButton("📈 Ciencias Económicas 📈", callback_data="decanato_contaduría")
        bb4 = InlineKeyboardButton("⚖️ Ciencias Jurídicas y Políticas ‍⚖️", callback_data="decanato_derecho")
        bb5 = InlineKeyboardButton("👨‍💻 Ingeniería y Afines ‍👨‍💻", callback_data="decanato_ingeniería")
        bb6 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(bb1, bb2, bb3, bb4, bb5, bb6)
        bot.send_message(message.chat.id, '¿Qué ' '<b>Decanato </b>' 'desea contactar?', reply_markup=markup, parse_mode="html")
    elif "contactos" in message.text:
        markup = InlineKeyboardMarkup(row_width = 1)
        bb1 = InlineKeyboardButton("📚 Estudios Generales 📚", callback_data="decanato_generales")
        bb2 = InlineKeyboardButton("🎨 Humanidades, Arte y Educación 🎨", callback_data="decanato_humanidades")
        bb3 = InlineKeyboardButton("📈 Ciencias Económicas 📈", callback_data="decanato_contaduría")
        bb4 = InlineKeyboardButton("⚖️ Ciencias Jurídicas y Políticas ‍⚖️", callback_data="decanato_derecho")
        bb5 = InlineKeyboardButton("👨‍💻 Ingeniería y Afines ‍👨‍💻", callback_data="decanato_ingeniería")
        bb6 = InlineKeyboardButton("⬅️ Regresar",callback_data="menu")
        markup.add(bb1, bb2, bb3, bb4, bb5, bb6)
        bot.send_message(message.chat.id, '¿Qué ' '<b>Decanato </b>' 'desea contactar?', reply_markup=markup, parse_mode="html")


# CORREO INSTITUCIONAL
    elif "correo institucional" in message.text:
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(3)
        x = bot.send_message(message.chat.id, 'Todos los <b>estudiantes y docentes de la Universidad</b> tienen un <b>correo institucional</b> asignado', parse_mode="html")
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(6)
        bot.edit_message_text('A través del <b>correo institucional</b> recibirás notificaciones de la <b>universidad, comunicaciones internas e información de las plataformas educativas y del Aula Virtual.</b>', message.chat.id, x.message_id, parse_mode="html")
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(8)
        bot.send_chat_action(message.chat.id, "typing")
        bot.edit_message_text('El <b>correo institucional</b> se obtiene de la siguiente forma:', message.chat.id, x.message_id, parse_mode="html")
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(3)
        bot.edit_message_text('<i>1. En caso de ser estudiante del <b>curso Introductorio, pregrado o postgrado</b>, previamente debes haber realizado la <b>inscripción administrativa y académica</b>. Si realizarás un <b>curso, diplomado o taller</b> de las distintas <b>ofertas promocionadas</b> por el <b>Vicerrectorado de Extensión</b>, debes haber pagado la <b>matrícula</b>.\n \n 2. Ingresa a la <b>plataforma web</b> de UNIMAR y haz clic en el ícono de <b>Pagos OnLine</b>. \n \n 3. Ubica el <b>módulo de registro de datos</b> y oprime el botón <b>“Registra o actualiza tus datos personales”</b>. \n \n 4. Ingresa tu <b>número de Cédula</b> y pulsa <b>Buscar</b>. Aparecerán los datos asociados a tu usuario registrados en el sistema: <b>Nombre, Apellido, Fecha de Nacimiento, Sexo</b>. En caso de presentar error en los datos cargados, por favor envía un correo a: </i>control.estudios@unimar.edu.ve <i>solicitando la corrección, según sea el caso. \n \n 5. Ingresa la información para la categoría <b>Estado Civil, Correo Electrónico Personal y Número de Teléfono</b>. Luego, escribe el <b>código de validación</b> que aparece en la <b>imagen</b> y pulsa la opción <b>Validar</b> y después <b>Guardar</b>. \n \n 6. En breves minutos recibirás en tu <b>correo personal</b> los datos de acceso al <b>correo institucional</b>. \n \n 7. Inicia sesión con el <b>correo institucional</b> desde <b>Gmail</b> usando los datos suministrados anteriormente. <b>Te recomiendo cambiar la contraseña por una personal.</b> \n</i>', message.chat.id, x.message_id, parse_mode="html")


# REPORTAR RESPUESTA

    elif "reportar" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        rr1 = InlineKeyboardButton("Sí ✔️", callback_data="reportar_reporte")
        rr2 = InlineKeyboardButton("No ❌", callback_data="menu")
        markup.add(rr1, rr2)
        bot.send_message(message.chat.id, '<i>¿Quieres realizar un <b>reporte</b> a <b>Control de Estudios</b>?</i>', reply_markup=markup, parse_mode="html")
    elif "reporte" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        rr1 = InlineKeyboardButton("Sí ✔️", callback_data="reportar_reporte")
        rr2 = InlineKeyboardButton("No ❌", callback_data="menu")
        markup.add(rr1, rr2)
        bot.send_message(message.chat.id, '<i>¿Quieres realizar un <b>reporte</b> a <b>Control de Estudios</b>?</i>', reply_markup=markup, parse_mode="html")
    elif "control de estudios" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        rr1 = InlineKeyboardButton("Sí ✔️", callback_data="reportar_reporte")
        rr2 = InlineKeyboardButton("No ❌", callback_data="menu")
        markup.add(rr1, rr2)
        bot.send_message(message.chat.id, '<i>¿Quieres realizar un <b>reporte</b> a <b>Control de Estudios</b>?</i>', reply_markup=markup, parse_mode="html")

# MENU SERVICIOS
    elif "servicios" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        s1 = InlineKeyboardButton("🙋‍♂️ Presencial", callback_data="modalidad_presencial")
        s2 = InlineKeyboardButton("👩‍💻 Online", callback_data="modalidad_online")
        s3 = InlineKeyboardButton("⬅️ Regresar", callback_data="menu")
        markup.add(s1,s2, s3)
        bot.send_message(message.chat.id, '<i>¿Qué <b>modalidad</b> estudias?</i>', reply_markup=markup, parse_mode="html")
    elif "reingreso" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        s1 = InlineKeyboardButton("🙋‍♂️ Presencial", callback_data="modalidad_presencial")
        s2 = InlineKeyboardButton("👩‍💻 Online", callback_data="modalidad_online")
        s3 = InlineKeyboardButton("⬅️ Regresar", callback_data="menu")
        markup.add(s1,s2, s3)
        bot.send_message(message.chat.id, '<i>¿Qué <b>modalidad</b> estudias?</i>', reply_markup=markup, parse_mode="html")
    elif "equivalencia" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        s1 = InlineKeyboardButton("🙋‍♂️ Presencial", callback_data="modalidad_presencial")
        s2 = InlineKeyboardButton("👩‍💻 Online", callback_data="modalidad_online")
        s3 = InlineKeyboardButton("⬅️ Regresar", callback_data="menu")
        markup.add(s1,s2, s3)
        bot.send_message(message.chat.id, '<i>¿Qué <b>modalidad</b> estudias?</i>', reply_markup=markup, parse_mode="html")
    elif "cambio de carrera" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        s1 = InlineKeyboardButton("🙋‍♂️ Presencial", callback_data="modalidad_presencial")
        s2 = InlineKeyboardButton("👩‍💻 Online", callback_data="modalidad_online")
        s3 = InlineKeyboardButton("⬅️ Regresar", callback_data="menu")
        markup.add(s1,s2, s3)
        bot.send_message(message.chat.id, '<i>¿Qué <b>modalidad</b> estudias?</i>', reply_markup=markup, parse_mode="html")
    elif "cambiar carrera" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        s1 = InlineKeyboardButton("🙋‍♂️ Presencial", callback_data="modalidad_presencial")
        s2 = InlineKeyboardButton("👩‍💻 Online", callback_data="modalidad_online")
        s3 = InlineKeyboardButton("⬅️ Regresar", callback_data="menu")
        markup.add(s1,s2, s3)
        bot.send_message(message.chat.id, '<i>¿Qué <b>modalidad</b> estudias?</i>', reply_markup=markup, parse_mode="html")

# MENU REQUISITOS 
    elif "requisitos" in message.text:
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        markup = InlineKeyboardMarkup(row_width = 2)
        r1 = InlineKeyboardButton("Curso Introductorio", callback_data="requisitos_introductorio")
        r2 = InlineKeyboardButton("Pregrado", callback_data="requisitos_pregrado")
        r3 = InlineKeyboardButton("Equivalencias", callback_data="requisitos_equivalencias")
        r4 = InlineKeyboardButton("Postgrado", callback_data="requisitos_postgrado")
        r5 = InlineKeyboardButton("⬅️ Regresar", callback_data="menu")
        markup.add(r1,r2,r3,r4, r5)
        bot.send_message(message.chat.id, '<i>¿Qué <b>requisitos</b> necesitas encontrar?</i>', reply_markup=markup, parse_mode="html")


# SALUDO
    elif "hola" in message.text:
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(2) 
        bot.send_message(message.chat.id, '<i>👋 ¡Holaa!</i>',parse_mode="html")



# RESPUESTAS QUE NO PROGRAMÉ

    elif len(message.text) >= 500:
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(5)
        bot.send_message(message.chat.id, 'Por favor, envía un mensaje menor a 500 caracteres', parse_mode="html")
    
    else:
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(5)
        bot.send_message(message.chat.id, '<i>🙇🏻‍♀️ <b>¡Lo siento!</b> No puedo entender lo que dices \n \n Parece ser que aún <b>no me han programado una respuesta para ese mensaje</b> 🥺 \n \n Espero poder entender lo que dices en un futuro, <b>pronto...</b> \n Por favor, si necesitas algo no dudes en utilizar el <b>/menu</b></i>', parse_mode="html")


########################################### DOCUMENTOS ############################################


#documentos, audio, ETC

@bot.message_handler(content_types=["photo"])
def bot_mensajes_photo(message):
        bot.reply_to(message, "Por favor, introduzca un comando")

@bot.message_handler(content_types=["document"])
def bot_mensajes_document(message):
    bot.reply_to(message, "Por favor, introduzca un comando")

@bot.message_handler(content_types=["audio"])
def bot_mensajes_audio(message):
    bot.reply_to(message, "Por favor, introduzca un comando")

@bot.message_handler(content_types=["sticker"])
def bot_mensajes_sticker(message):
    bot.reply_to(message, "Por favor, introduzca un comando")

@bot.message_handler(content_types=["video_note"])
def bot_mensajes_videonote(message):
    bot.reply_to(message, "Por favor, introduzca un comando")

@bot.message_handler(content_types=["voice"])
def bot_mensajes_voice(message):
    bot.reply_to(message, "Por favor, introduzca un comando")

@bot.message_handler(content_types=["location"])
def bot_mensajes_location(message):
    bot.reply_to(message, "Por favor, introduzca un comando")

@bot.message_handler(content_types=["contact"])
def bot_mensajes_contact(message):
    bot.reply_to(message, "Por favor, introduzca un comando")

@bot.message_handler(content_types=["video"])
def bot_mensajes_video(message):
    bot.reply_to(message, "Por favor, introduzca un comando")

#MAIN
if __name__ == '__main__':
    print("Iniciando el Bot...")
    bot.delete_webhook
    time.sleep(1)
    bot.infinity_polling()