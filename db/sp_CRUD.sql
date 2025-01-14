use eventos;

DELIMITER //
CREATE PROCEDURE ObtenerUsuarios(
    IN tipo int)
BEGIN
	select eu.ci, eu.nombre, eu.apellido
	from eventos_usuario eu
	inner join eventos_tipousuario et 
	on et.id_tipo_usuario = eu.tipo_usuario_id 
	where eu.tipo_usuario_id  = tipo;
END //
DELIMITER ;