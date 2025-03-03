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
                    "CREATE (u)-[r:ES_AMIGO_DE {fecha_amistad: $fecha_amistad, mensaje: $mensaje, estado: $estado}]->(amigo)",
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