<?php

function run_code($code, $stdin){
    /* Run code */

    // write code to a temp file
    $tmp_path = '/tmp/temp-script-' . time() . rand() . '.pashm';
    $tmp_path_stdin = $tmp_path . '.stdin';
    $tmp_path_out = $tmp_path . '.out';
    $f = fopen($tmp_path, 'w');
    fwrite($f, $code);
    fclose($f);

    // write recived stdin to tempfile
    $f = fopen($tmp_path_stdin, 'w');
    fwrite($f, $stdin);
    fclose($f);

    // run code with `runner` user and put output to temp file
    $cmd = 'runuser -l runner -c "cat ' . $tmp_path_stdin . ' | pashmak ' . $tmp_path . ' 2> ' . $tmp_path_out . '"';
    system($cmd);

    // return output
    $f = fopen($tmp_path_out, 'r');
    $output = fread($f, filesize($tmp_path_out)+1);
    fclose($f);

    // remove temp files
    unlink($tmp_path);
    unlink($tmp_path_stdin);
    unlink($tmp_path_out);

    return $output;
}

// check form submited
$code = '';
$stdin = '';
if($_SERVER['REQUEST_METHOD'] === 'POST'){
    $code = $_POST['code'];
    $stdin = $_POST['stdin'];
}

// if any code submited, run this and show output
ob_start();
$output = null;
if($code !== ''){
    $output = run_code($code, $stdin);
    echo $output;
}
$output = ob_get_clean();

// show view
include 'view.php';
