
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
	
	
	<form action="" method="post">
    <input type="submit" name="start" value="start" />
    <input type="submit" name="stop" value="stop" />
   </form>

	<?php
	/*
	exec('sudo python3 /home/pi/Desktop/Kasim/Test/led.py > /dev/null 2>/dev/null &');
	*/

  if(isset($_POST['start'])){
		exec('sudo python3 /home/pi/Documents/web/ledon.py > /dev/null 2>/dev/null &');
  }
  if(isset($_POST['stop'])){
		//exec('sudo touch /home/pi/Documents/web/ledoff.py');
		exec('sudo pkill -f /home/pi/Documents/web/ledon.py');
  }
	?>
</body>	

</html>
