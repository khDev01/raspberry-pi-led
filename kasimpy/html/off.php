
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="utf-8"/>
	<title>Home Page</title>
	<link rel="stylesheet" href="flex.css">
	<link rel="stylesheet" href="forms.css">
</head>
<body>
	<div class="nav">
		<a href="index.html">Home</a>
		<a href="led.php">LED</a>
		<a href="led.php">OFF</a>
	</div>
	<?php
exec('gpio mode 0 in');

?>
</body>	

</html>
