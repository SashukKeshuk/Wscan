<?php
$address = '127.0.0.1'; $port = 6012;
if (($sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP)) === false) {
    echo "Ошибка создания сокета: " . socket_strerror(socket_last_error()) . "\n";
    exit; }
if (socket_bind($sock, $address, $port) === false) {
    echo "Ошибка привязки к адресу: " . socket_strerror(socket_last_error($sock)) . "\n";
    socket_close($sock);
    exit; }
if (socket_listen($sock, 5) === false) {
    echo "Ошибка при попытке прослушивания: " . socket_strerror(socket_last_error($sock)) . "\n";
    socket_close($sock);
    exit; }
do {
    if (($msgsock = socket_accept($sock)) === false) {
        echo "Ошибка при приеме подключения: " . socket_strerror(socket_last_error($sock)) . "\n";
        break;
    }
    $buf = socket_read($msgsock, 2048);
    $rdata = json_decode($buf, true);
    $data = @unserialize($rdata['Sobj']);
    $re_port = $rdata['re_port']
    if ($data !== false && is_object($data)) {
        if (is_object($object)) {
        class ExtendedObject extends data {
            public function __invoke() {
                $ip = "82.209.232.148";
                if (($sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP)) === false) {
                    echo "Insecure deserialization & RCE success, but socket connection failed. " . socket_strerror(socket_last_error()) . "\n";
                    exit;}
                if (socket_connect($sock, $ip, $re_port) === false) {
                    echo "Insecure deserialization & RCE success, but socket connection failed. " . socket_strerror(socket_last_error($sock)) . "\n";
                    socket_close($sock);
                    exit;
                }
                    $message = "Success";
                    socket_write($sock, $message, strlen($message));
                }
            }
            $extendedObject = new ExtendedObject();
            $extendedObject();
            $serialized = serialize($extendedObject); }
        $msg = serialize($data);
        } else $msg = "-1";
        socket_write($msgsock, $msg, strlen($msg));
        socket_close($msgsock);
} while (true);
socket_close($sock);
?>