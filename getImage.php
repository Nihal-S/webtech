<?php
	header("Content-type:image/jpg");
	if ($_POST["id"] == 0){
		$fname = "3.jpg";
	}
	else if ($_POST["id"] == 1){
		$fname = "1.jpeg";
	}
	else if ($_POST["id"] == 2){
		$fname = "2.jpg";
	}
	else if ($_POST["id"] == 3){
		$fname = "3.jpg";
	}
	else{
		$fname = "4.png";
	}
    $file = fopen($fname,"rb");
    $size = filesize($fname);
    $media = fread($file,$size);
	fclose($file);
    echo $media;
?>
