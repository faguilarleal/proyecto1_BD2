from randomProp import *

def usuario_sigue_usuario(session):

    usuarios = session.run("MATCH (u:Usuario) RETURN u.username as username")
    for usuario in usuarios: 
        usuarios_a_seguir = escoger_usuarios_random(session)

        for seguido in usuarios_a_seguir:
            fecha = fecha_random()
            estado = estado_random()
            etiqueta = etiqueta_random()
            try: 
                session.run(
                    "MATCH (u:Usuario {username: $username}), (seguido:Usuario {username: $seguido}) "
                    "CREATE (u)-[r:SIGUE {fechaSeguimiento: $fecha, etiqueta: $etiqueta, estado: $estado}]->(seguido)",
                    username = usuario['username'],
                    fecha=fecha,
                    etiqueta=etiqueta,
                    estado=estado,
                    seguido=seguido, 
                        
                    
                    )
                print(f"{usuario['username']} sigue a {seguido}")
            except Exception as e:
                print(e)
                print(f"Error en {usuario['username']} sigue a {seguido}")

def usuario_solicita_amistad_usuario(session):
    usuarios = session.run("MATCH (u:Usuario) RETURN u.username as username")
    for usuario in usuarios: 
        usuarios_a_solicitar = escoger_usuarios_random(session)

        for solicitado in usuarios_a_solicitar:
            fecha = fecha_random()
            estado = estado_random()
            mensaje= mensaje_random()
            try: 
                session.run(
                    "MATCH (u:Usuario {username: $username}), (solicitado:Usuario {username: $solicitado}) "
                    "CREATE (u)-[r:SOLICITA_AMISTAD {fechaSolicitud: $fecha, mensaje: $mensaje, estado: $estado}]->(solicitado)",
                    username = usuario['username'],
                    fecha=fecha,
                    mensaje=mensaje,
                    estado=estado,
                    solicitado=solicitado, 
                        
                    
                    )
                print(f"{usuario['username']} le mando solicitud de amistad a {solicitado}")
            except Exception as e:
                print(e)
                print(f"Error en {usuario['username']} le mando solicitud  a {solicitado}")

def usuario_es_amigo_de_usuario(session):

    usuarios = session.run("MATCH (u:Usuario) RETURN u.username as username")
    for usuario in usuarios: 
        amigos = escoger_usuarios_random(session)

        for amigo in amigos:
            fecha_amistad = fecha_random()
            nivel_confianza = confianza_random()
            tipo_de_relacion = tipo_de_relacion_random()
            try: 
                session.run(
                    "MATCH (u:Usuario {username: $username}), (amigo:Usuario {username: $amigo}) "
                    "CREATE (u)-[r:ES_AMIGO_DE {fecha_amistad: $fecha_amistad, nivel_confianza: $nivel_confianza, tipo_relacion: $tipo_de_relacion}]->(amigo)",
                    username = usuario['username'],
                    fecha_amistad=fecha_amistad,
                    nivel_confianza = nivel_confianza,
                    tipo_de_relacion = tipo_de_relacion,
                    amigo=amigo, 
                        
                    
                    )
                print(f"{usuario['username']} es amigo de {amigo}")
            except Exception as e:
                print(e)
                print(f"Error en {usuario['username']} es amigo de {amigo}")
            

def usuario_bloquea_usuario(session):

    usuarios = session.run("MATCH (u:Usuario) RETURN u.username as username")
    for usuario in usuarios: 
        bloqueados = escoger_usuarios_random(session)

        for bloqueado in bloqueados:
            fecha_bloqueo = fecha_random()
            motivo = motivo_bloqueo_reporte_random()
            estado_bloqueo = estado_bloqueo_random()

            try: 
                session.run(
                    "MATCH (u:Usuario {username: $username}), (bloqueado:Usuario {username: $bloqueado}) "
                    "CREATE (u)-[r:BLOQUEA {fecha_bloqueo: $fecha_bloqueo, motivo: $motivo, estado_bloqueo: $estado_bloqueo}]->(bloqueado)",
                    username = usuario['username'],
                    fecha_bloqueo=fecha_bloqueo,
                    motivo = motivo,
                    estado_bloqueo = estado_bloqueo,
                    bloqueado=bloqueado, 
                        
                    
                    )
                print(f"{usuario['username']} ha bloqueado a {bloqueado}")
            except Exception as e:
                print(e)
                print(f"Error en {usuario['username']} ha bloqueado a {bloqueado}")


def usuario_reporta_usuario(session):

    usuarios = session.run("MATCH (u:Usuario) RETURN u.username as username")
    for usuario in usuarios: 
        reportados = escoger_usuarios_random(session)

        for reportado in reportados:
            fecha_reporte = fecha_random()
            motivo = motivo_bloqueo_reporte_random()
            comentarios_reporte = comentarios_reporte_random()

            try: 
                session.run(
                    "MATCH (u:Usuario {username: $username}), (reportado:Usuario {username: $reportado}) "
                    "CREATE (u)-[r:REPORTA {fecha_reporte: $fecha_reporte, motivo: $motivo, comentarios_reporte: $comentarios_reporte}]->(reportado)",
                    username = usuario['username'],
                    fecha_reporte=fecha_reporte,
                    motivo = motivo,
                    comentarios_reporte = comentarios_reporte,
                    reportado=reportado, 
                        
                    
                    )
                print(f"{usuario['username']} ha reportado a {reportado}")
            except Exception as e:
                print(e)
                print(f"Error en {usuario['username']} ha reportado a {reportado}")


def usuario_menciona_usuario(session):

    usuarios = session.run("MATCH (u:Usuario) RETURN u.username as username")
    for usuario in usuarios: 
        mencionados = escoger_usuarios_random(session)

        for mencionado in mencionados:
            fecha_mencion = fecha_random()
            contexto =  contexto_contenido_random()
            visibilidad = visibilidad_random()

            try: 
                session.run(
                    "MATCH (u:Usuario {username: $username}), (mencionado:Usuario {username: $mencionado}) "
                    "CREATE (u)-[r:MENCIONA {fecha_mencion: $fecha_mencion, contexto: $contexto, visibilidad: $visibilidad}]->(mencionado)",
                    username = usuario['username'],
                    fecha_mencion=fecha_mencion,
                    contexto = contexto,
                    visibilidad = visibilidad,
                    mencionado=mencionado, 
                        
                    
                    )
                print(f"{usuario['username']} ha mencionado a {mencionado}")
            except Exception as e:
                print(e)
                print(f"Error en {usuario['username']} ha mencionado a {mencionado}")

def usuario_reporta_publicacion(session):

    usuarios = session.run("MATCH (u:Usuario) RETURN u.username as username")
    for usuario in usuarios: 
        publicaciones_a_reportar = escoger_publicacion_random(session)

        for publicacion in publicaciones_a_reportar:
            fecha_reporte = fecha_random()
            motivo = motivo_bloqueo_reporte_random()
            comentarios_reporte = comentarios_reporte_random()
            
            try: 
                session.run(
                    "MATCH (u:Usuario {username: $username}), (publicacion:Publicacion {id_publicacion: $id_publicacion}) "
                    "CREATE (u)-[r:REPORTA {fecha_reporte: $fecha_reporte, motivo: $motivo, comentarios_reporte: $comentarios_reporte}]->(publicacion)",
                    username = usuario['username'],
                    fecha_reporte=fecha_reporte,
                    motivo=motivo,
                    comentarios_reporte=comentarios_reporte,
                    id_publicacion=publicacion, 
                        
                    
                    )
                print(f"{usuario['username']} ha reportado la publicacion con el id de:  {publicacion}")
            except Exception as e:
                print(e)
                print(f"Error en {usuario['username']} ha reportado {publicacion}")



def usuario_reporta_comentario(session):

    usuarios = session.run("MATCH (u:Usuario) RETURN u.username as username")
    for usuario in usuarios: 
        comentarios_a_reportar = escoger_comentarios_random(session)

        for comentario in comentarios_a_reportar:
            fecha_reporte = fecha_random()
            motivo = motivo_bloqueo_reporte_random()
            comentarios_reporte = comentarios_reporte_random()
            
            try: 
                session.run(
                    "MATCH (u:Usuario {username: $username}), (comentario: Comentario {id_comentario: $id_comentario}) "
                    "CREATE (u)-[r:REPORTA {fecha_reporte: $fecha_reporte, motivo: $motivo, comentarios_reporte: $comentarios_reporte}]->(comentario)",
                    username = usuario['username'],
                    fecha_reporte=fecha_reporte,
                    motivo=motivo,
                    comentarios_reporte=comentarios_reporte,
                    id_comentario=comentario, 
                    )
                print(f"{usuario['username']} ha reportado el comenatio con el id de:  {comentario}")
            except Exception as e:
                print(e)
                print(f"Error en {usuario['username']} ha reportado {comentario}")



def usuario_publica_publicacion(session):
    publicaciones = session.run("MATCH (p:Publicacion) RETURN p.id_publicacion as id_publicacion")
    publicaciones = [record["id_publicacion"] for record in publicaciones]

    for publicacion_id in publicaciones:
        usuario = escoger_un_usuario_random(session)

        fecha_publicacion = fecha_random()
        contenido = contenido_random()  
        visibilidad = visibilidad_random()

        try:
            session.run(
                """
                MATCH (u:Usuario {username: $username}), (p:Publicacion {id_publicacion: $id_publicacion})
                MERGE (u)-[:PUBLICA {
                    fecha_publicacion: $fecha_publicacion,
                    contenido: $contenido,
                    visibilidad: $visibilidad
                }]->(p)
                """,
                username=usuario,
                id_publicacion=publicacion_id,
                fecha_publicacion=fecha_publicacion,
                contenido=contenido,
                visibilidad=visibilidad
            )
            print(f"{usuario} ha publicado la publicación con el ID: {publicacion_id}")
        except Exception as e:
            print(e)
            print(f"Error al asignar publicación {publicacion_id} a {usuario['username']}")

def usuario_publica_historia(session):
    historias = session.run("MATCH (h:Historia) RETURN h.id_historia as id_historia")
    historias = [record["id_historia"] for record in historias]

    for id_historia in historias:
        usuario = escoger_un_usuario_random(session)
        fecha_historia = fecha_random()
        contenido = contenido_random()
        visibilidad = visibilidad_random()

        try:
            session.run(
                """
                MATCH (u:Usuario {username: $username}), (h:Historia {id_historia: $id_historia})
                SET h.username = $username
                MERGE (u)-[:PUBLICA {
                    fecha_historia: $fecha_historia,
                    contenido: $contenido,
                    visibilidad: $visibilidad
                }]->(h)
                """,
                username=usuario,
                id_historia=id_historia,
                fecha_historia=fecha_historia,
                contenido=contenido,
                visibilidad=visibilidad
            )
            print(f"{usuario} ha publicado la historia con el ID: {id_historia}")
        except Exception as e:
            print(e)
            print(f"Error al publicar historia {id_historia} por parte de {usuario['username']}")

def usuario_comparte_publicacion(session):
    publicaciones = session.run("MATCH (p:Publicacion) RETURN p.id_publicacion as id_publicacion")
    publicaciones = [record["id_publicacion"] for record in publicaciones]

    for publicacion_id in publicaciones:
        usuario = escoger_un_usuario_random(session)

        fecha_publicacion = fecha_random()
        contenido = contenido_random()  
        visibilidad = visibilidad_random()

        try:
            session.run(
                """
                MATCH (u:Usuario {username: $username}), (p:Publicacion {id_publicacion: $id_publicacion})
                MERGE (u)-[:COMPARTE {
                    fecha_compartida: $fecha_publicacion,
                    comentario: $contenido,
                    visibilidad: $visibilidad
                }]->(p)
                """,
                username=usuario,
                id_publicacion=publicacion_id,
                fecha_publicacion=fecha_publicacion,
                contenido=contenido,
                visibilidad=visibilidad
            )
            print(f"{usuario} ha compartido la publicación con el ID: {publicacion_id}")
        except Exception as e:
            print(e)
            print(f"Error al asignar publicación {publicacion_id} a {usuario}")


def usuario_envia_mensaje(session):
    mensajes = session.run("MATCH (p:Mensaje) RETURN p.id_mensaje as id_mensaje")
    mensajes = [record["id_mensaje"] for record in mensajes]

    for mensaje in mensajes:
        usuario = escoger_un_usuario_random(session)
        fecha_publicacion = fecha_random()
        tipo = tipo_random() 
        estado = estado_mensaje_random()

        try:
            session.run(
                """
                MATCH (u:Usuario {username: $username}), (p:Mensaje {id_mensaje: $id_mensaje})
                MERGE (u)-[:ENVIA {
                    fecha_mensaje: $fecha_mensaje,
                    tipo: $tipo,
                    estado: $estado
                }]->(p)
                """,
                username=usuario,
                id_mensaje=mensaje,
                fecha_mensaje=fecha_publicacion,
                tipo=tipo,
                estado=estado
            )
            print(f"{usuario} ha enviado mensaje ID: {mensaje}")
        except Exception as e:
            print(e)
            print(f"Error al asignar publicación {mensaje} a {usuario}")


def usuario_comenta_comentario(session):
    comentarios = session.run("MATCH (p:Comentario) RETURN p.id_comentario as id_comentario")
    comentarios = [record["id_comentario"] for record in comentarios]

    for comentario in comentarios:
        usuario = escoger_un_usuario_random(session)
        fecha_comentario = fecha_random()
        tipo = tipo_random()
        editado = random.choice([True, False])

        try:
            session.run(
                """
                MATCH (u:Usuario {username: $username}), (p:Comentario {id_comentario: $id_comentario})
                MERGE (u)-[:COMENTA {
                    fecha_comentario: $fecha_comentario,
                    tipo: $tipo,
                    editado: $editado
                }]->(p)
                """,
                username=usuario,
                id_comentario=comentario,
                fecha_comentario=fecha_comentario,
                tipo=tipo,
                editado=editado
            )
            print(f"{usuario} ha comentado en el mensaje ID: {comentario}")
        except Exception as e:
            print(e)
            print(f"Error al asignar comentario en el mensaje ID: {comentario} por {usuario}")


def comentario_pertenece_publicacion(session):
    comentarios = session.run("MATCH (c:Comentario) RETURN c.id_comentario as id_comentario")
    comentarios = [record["id_comentario"] for record in comentarios]

    for comentario in comentarios:
        publicaciones = escoger_una_publicacion_random(session)
        
        fecha_pertenencia = fecha_random()
        tipo = tipo_random()
        editado = random.choice([True, False])
        try:
            session.run(
                "MATCH (c:Comentario {id_comentario: $id_comentario}), (publicacion:Publicacion {id_publicacion: $id_publicacion}) "
                """MERGE (c)-[:PERTENECE_A {
                    Fecha_pertenencia: $fecha_pertenencia,
                    tipo: $tipo,
                    editado: $editado
                }]->(publicacion)""",
                id_comentario=comentario,
                fecha_pertenencia=fecha_pertenencia,
                tipo=tipo,
                editado=editado,
                id_publicacion=publicaciones
            )
            print(f"El comentario con el id de: {comentario} pertenece a la publicacion con el id de: {publicaciones}")
        except Exception as e:
            print(e)
            print(f"Error en el comentario con el id de: {comentario['id_comentario']} pertenece a la publicacion {publicacion}")





def usuario_pertenece_grupo(session):
    grupos = session.run("MATCH (c:Grupo) RETURN c.id_grupo as id_grupo")
    grupos = [record["id_grupo"] for record in grupos]

    for grupo in grupos:
        usuarios = escoger_usuarios_random(session)
        for usuario in usuarios:
            fecha_miembro = fecha_random()
            rol = tipo_rol()
            creador = random.choice([True, False])
            
            try:
                session.run(
                    "MATCH (c:Grupo {id_grupo: $id_grupo}), (u:Usuario {username: $usuario}) "
                    """MERGE (u)-[:PERTENECE_A {
                        Fecha_pertenencia: $fecha_pertenencia,
                        rol: $rol,
                        creador: $creador
                    }]->(c)""",
                    id_grupo=grupo,
                    fecha_pertenencia=fecha_miembro,
                    rol=rol,
                    creador=creador,
                    usuario=usuario
                )
                print(f"el usuario {usuario} pertenece al grupo {grupo}")
            except Exception as e:
                print(e)
                print(f"Error en {usuario} {grupo}")



def usuario_pertenece_evento(session):
    eventos = session.run("MATCH (c:Evento) RETURN c.id_evento as id_evento")
    eventos = [record["id_evento"] for record in eventos]

    for evento in eventos:
        usuarios = escoger_usuarios_random(session)
        for usuario in usuarios:
            fecha_miembro = fecha_random()
            rol = tipo_rol()
            creador = random.choice([True, False])
            
            try:
                session.run(
                    "MATCH (c:Evento {id_evento: $id_evento}), (u:Usuario {username: $usuario}) "
                    """MERGE (u)-[:PERTENECE_A {
                        Fecha_pertenencia: $fecha_pertenencia,
                        rol: $rol,
                        creador: $creador
                    }]->(c)""",
                    id_evento=evento,
                    fecha_pertenencia=fecha_miembro,
                    rol=rol,
                    creador=creador,
                    usuario=usuario
                )
                print(f"el usuario {usuario} pertenece al evento {evento}")
            except Exception as e:
                print(e)
                print(f"Error en {usuario} {evento}")


