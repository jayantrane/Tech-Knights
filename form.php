<?php
//index.php

$error = '';
$name = '';
$email = '';
$number = '';
$no_of_hacks = '';
$no_of_hacks_won = '';
$github_link = '';
$uploadOk = 1;
//$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

function clean_text($string)
{
 $string = trim($string);
 $string = stripslashes($string);
 $string = htmlspecialchars($string);
 return $string;
}

if(isset($_POST["submit"]))
{
 if(empty($_POST["name"]))
 {
  $error .= '<p><label class="text-danger">Please Enter your Name</label></p>';
 }
 else
 {
  $name = clean_text($_POST["name"]);
  if(!preg_match("/^[a-zA-Z ]*$/",$name))
  {
   $error .= '<p><label class="text-danger">Only letters and white space allowed</label></p>';
  }
 }
 if(empty($_POST["email"]))
 {
  $error .= '<p><label class="text-danger">Please Enter your Email</label></p>';
 }
 else
 {
  $email = clean_text($_POST["email"]);
  if(!filter_var($email, FILTER_VALIDATE_EMAIL))
  {
   $error .= '<p><label class="text-danger">Invalid email format</label></p>';
  }
 }
 
$number = $_POST["number"];
$no_of_hacks = $_POST["no_of_hacks"];
$no_of_hacks_won = $_POST["no_of_hacks_won"];
$github_link = $_POST["github_link"];



 if($error == '')
 {
  $file_open = fopen("kjsce.csv", "a");
  $no_rows = count(file("kjsce.csv"));
  if($no_rows > 1)
  {
   $no_rows = ($no_rows - 1) + 1;
  }
  $form_data = array(
   'Name'  => $name,
   'Email Address'  => $email,
   'Mobile Number' => $number,
   'No of Hackathons' => $no_of_hacks,
   'No of Hackathons Won' =>$no_of_hacks_won,
   'Github Link' =>$github_link
  );
  fputcsv($file_open, $form_data);
  $error = '<label class="text-success">Thank you for contacting us</label>';
  $name = '';
  $email = '';
  $number = '';
$no_of_hacks = '';
$no_of_hacks_won = '';
$github_link = '';
 }

}
?>
<!DOCTYPE html>
<html>
 <head>
  <title>How to Store Form data in CSV File using PHP</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
 </head>
 <body>
  <br />
  <div class="container">
   <h2 align="center">How to Store Form data in CSV File using PHP</h2>
   <br />
   <div class="col-md-6" style="margin:0 auto; float:none;">
    <form method="post">
     <h3 align="center">Contact Form</h3>
     <br />
     <?php echo $error; ?>
     <div class="form-group">
      <label>Enter Name</label>
      <input type="text" name="name" placeholder="Enter Name" class="form-control" value="<?php echo $name; ?>" />
     </div>
     <div class="form-group">
      <label>Enter Email</label>
      <input type="text" name="email" class="form-control" placeholder="Enter Email" value="<?php echo $email; ?>" />
     </div>
      <div class="form-group">
      <label>Enter Contact Number</label>
      <input type="number" name="number" class="form-control" placeholder="Enter Contact Number" value="<?php echo $number; ?>" />
     </div>
     <div class="form-group">
      <label>Enter Number of Hackathons Attended</label>
      <input type="number" name="no_of_hacks" class="form-control" placeholder="Enter Number" value="<?php echo $no_of_hacks; ?>" />
     </div>
     <div class="form-group">
      <label>Enter Number of Hackathons Won</label>
      <input type="number" name="no_of_hacks_won" class="form-control" placeholder="Enter Number" value="<?php echo $no_of_hacks_won; ?>" />
     </div>
     <div class="form-group">
      <label>Enter The Github Link</label>
      <input type="url" name="github_link" class="form-control" placeholder="Enter Link" value="<?php echo $github_link; ?>" />
     </div>
     <div class="form-group">
      <label>Upload file</label>
      <input type="file" name="pdf_file" id="pdf_file" accept="application/pdf" />
     </div>
     
     <div class="form-group" align="center">
      <input type="submit" name="submit" class="btn btn-info" value="Submit" />
     </div>
    </form>
   </div>
  </div>
 </body>
</html>