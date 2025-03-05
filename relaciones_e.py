from randomProp import *


def agregar_propiedades_a_relacion_SIGUE(DriverSession, usuario):

    #seguidos pcrookall1g
    #aledwithg
    #iX2`Q{aa!|iDu

    with DriverSession as session:
        if usuario:
            usuario_seguido = input("Ingrese el nombre del que sigue y qioere cambiar la relacion: ")
            propiedades =  input("Ingrese las nombre de la propiedad y el valor separados por coma: (ej: motivo:amistad,prioridad:1,estado:activo)").split(",")
            propiedades = {prop.split(":")[0]: prop.split(":")[1] for prop in propiedades}

            
            try:
                set_clause = ", ".join([f"r.{prop} = ${prop}" for prop in propiedades])

                params = {
                    "seguidor": usuario,
                    "seguido": usuario_seguido,
                    **propiedades  
                }

                query = f"""
                    MATCH (u1:Usuario)-[r:SIGUE]->(u2:Usuario)
                    WHERE u1.username = $seguidor AND u2.username = $seguido
                    SET {set_clause}
                """

                
                session.run(query, params)
                print(f"Propiedades agregadas a la relación SIGUE entre {usuario} y {usuario_seguido}")

            except Exception as e:
                print(f"Error al agregar propiedades a la relación SIGUE: {e}")
        
        else: 
            print("No se ha iniciado sesión para ver los seguidores")


def agregar_propiedades_a_multiples_relaciones_SIGUE(DriverSession, usuario):

    with DriverSession as session:
        if usuario:
            usuarios_seguidos_input = input("Ingrese los nombres de los usuarios seguidos separados por coma: ")
            usuarios_seguidos = usuarios_seguidos_input.split(",")

            propiedades_input = input("Ingrese las propiedades a agregar (ej: motivo:amistad,prioridad:1,estado:activo): ")
            propiedades_pares = propiedades_input.split(",")
            propiedades = {prop.split(":")[0]: prop.split(":")[1] for prop in propiedades_pares}

            try:
                set_clause = ", ".join([f"r.{prop} = ${prop}" for prop in propiedades])

                for usuario_seguido in usuarios_seguidos:
                    usuario_seguido = usuario_seguido.strip()  # Eliminar espacios en blanco alrededor del username

                    params = {
                        "seguidor": usuario,
                        "seguido": usuario_seguido,
                        **propiedades
                    }

                    query = f"""
                        MATCH (u1:Usuario)-[r:SIGUE]->(u2:Usuario)
                        WHERE u1.username = $seguidor AND u2.username = $seguido
                        SET {set_clause}
                    """

                    session.run(query, params)
                    print(f"Propiedades agregadas a la relación SIGUE entre {usuario} y {usuario_seguido}")

            except Exception as e:
                print(f"Error al agregar propiedades a las relaciones SIGUE: {e}")

        else:
            print("No se ha iniciado sesión para agregar propiedades a las relaciones SIGUE")


def actualizar_propiedades_a_relacion_SIGUE(DriverSession, usuario):


    with DriverSession as session:
        if usuario:
            usuario_seguido = input("Ingrese el username del usuario seguido: ")
            propiedades_input = input("Ingrese las propiedades a actualizar (ej: motivo:amistad,prioridad:1,estado:activo): ")
            propiedades_pares = propiedades_input.split(",")
            propiedades = {prop.split(":")[0]: prop.split(":")[1] for prop in propiedades_pares}

            try:
                set_clause = ", ".join([f"r.{prop} = ${prop}" for prop in propiedades])

                params = {
                    "seguidor": usuario,
                    "seguido": usuario_seguido,
                    **propiedades
                }

                query = f"""
                    MATCH (u1:Usuario)-[r:SIGUE]->(u2:Usuario)
                    WHERE u1.username = $seguidor AND u2.username = $seguido
                    SET {set_clause}
                """

                session.run(query, params)
                print(f"Propiedades actualizadas en la relación SIGUE entre {usuario} y {usuario_seguido}")

            except Exception as e:
                print(f"Error al actualizar propiedades en la relación SIGUE: {e}")

        else:
            print("No se ha iniciado sesión para actualizar propiedades en las relaciones SIGUE")



def actualizar_propiedades_a_multiples_relaciones_SIGUE(DriverSession, usuario):

    with DriverSession as session:
        if usuario:
            usuarios_seguidos_input = input("Ingrese los usernames de los usuarios seguidos separados por coma: ")
            usuarios_seguidos = usuarios_seguidos_input.split(",")

            propiedades_input = input("Ingrese las propiedades a actualizar (ej: motivo:amistad,prioridad:1,estado:activo): ")
            propiedades_pares = propiedades_input.split(",")
            propiedades = {prop.split(":")[0]: prop.split(":")[1] for prop in propiedades_pares}

            try:
                set_clause = ", ".join([f"r.{prop} = ${prop}" for prop in propiedades])

                for usuario_seguido in usuarios_seguidos:
                    usuario_seguido = usuario_seguido.strip()  # Eliminar espacios en blanco alrededor del username

                    params = {
                        "seguidor": usuario,
                        "seguido": usuario_seguido,
                        **propiedades
                    }

                    query = f"""
                        MATCH (u1:Usuario)-[r:SIGUE]->(u2:Usuario)
                        WHERE u1.username = $seguidor AND u2.username = $seguido
                        SET {set_clause}
                    """

                    session.run(query, params)
                    print(f"Propiedades actualizadas en la relación SIGUE entre {usuario} y {usuario_seguido}")

            except Exception as e:
                print(f"Error al actualizar propiedades en las relaciones SIGUE: {e}")

        else:
            print("No se ha iniciado sesión para actualizar propiedades en las relaciones SIGUE")



def eliminar_propiedades_a_relacion_SIGUE(DriverSession, usuario):

    with DriverSession as session:
        if usuario:
            usuario_seguido = input("Ingrese el username del usuario seguido: ")
            propiedades_input = input("Ingrese las propiedades a eliminar separadas por coma (ej: motivo,prioridad,estado): ")
            propiedades = [prop.strip() for prop in propiedades_input.split(",")]

            try:
                remove_clause = ", ".join([f"r.{prop}" for prop in propiedades])

                params = {
                    "seguidor": usuario,
                    "seguido": usuario_seguido
                }

                query = f"""
                    MATCH (u1:Usuario)-[r:SIGUE]->(u2:Usuario)
                    WHERE u1.username = $seguidor AND u2.username = $seguido
                    REMOVE {remove_clause}
                """

                session.run(query, params)
                print(f"Propiedades eliminadas en la relación SIGUE entre {usuario} y {usuario_seguido}")

            except Exception as e:
                print(f"Error al eliminar propiedades en la relación SIGUE: {e}")

        else:
            print("No se ha iniciado sesión para eliminar propiedades en las relaciones SIGUE")


from randomProp import *

def eliminar_propiedades_a_multiples_relaciones_SIGUE(DriverSession, usuario):

    with DriverSession as session:
        if usuario:
            usuarios_seguidos_input = input("Ingrese los usernames de los usuarios seguidos separados por coma: ")
            usuarios_seguidos = usuarios_seguidos_input.split(",")

            propiedades_input = input("Ingrese las propiedades a eliminar separadas por coma (ej: motivo,prioridad,estado): ")
            propiedades = [prop.strip() for prop in propiedades_input.split(",")]

            try:
                remove_clause = ", ".join([f"r.{prop}" for prop in propiedades])

                for usuario_seguido in usuarios_seguidos:
                    usuario_seguido = usuario_seguido.strip()  # Eliminar espacios en blanco alrededor del username

                    params = {
                        "seguidor": usuario,
                        "seguido": usuario_seguido
                    }

                    query = f"""
                        MATCH (u1:Usuario)-[r:SIGUE]->(u2:Usuario)
                        WHERE u1.username = $seguidor AND u2.username = $seguido
                        REMOVE {remove_clause}
                    """

                    session.run(query, params)
                    print(f"Propiedades eliminadas en la relación SIGUE entre {usuario} y {usuario_seguido}")

            except Exception as e:
                print(f"Error al eliminar propiedades en las relaciones SIGUE: {e}")

        else:
            print("No se ha iniciado sesión para eliminar propiedades en las relaciones SIGUE")