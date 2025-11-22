<?php
$host = "localhost";
$user = "root";
$pass = "12345678"; # CAMBIAR CONTRASEÑA 
$dbname = "videojuegos"; # CAMBIAR NOMBRE DE BASE DE DATOS
try {
    $con = new PDO("mysql:host=$host;dbname=$dbname", $user, $pass);
    $con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $ex) {
    echo ($ex);
    die($ex->getMessage());
}
$sql1 = "select * from juegos"; # CAMBIAR NOMBRE DE LA TABLA DE ORIGEN
$stmt = $con->prepare($sql1);
$stmt->execute();
$registros = array();
while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
    $registros[] = $row;
}
print_r(json_encode($registros));
?>