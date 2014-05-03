#!C:\Perl64\bin\perl.exe

use strict;
use CGI;
use Data::Dumper;
use Storable;
use JSON;

my $cgi=CGI->new;
print $cgi->header(-type=>"text/html");



print '
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhml" xml:lang="en" lang="en">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<link href="css/basic.css" rel="stylesheet" type="text/css" />

<title></title>
</head>
<body>
Current position: /<a href="home.html">home</a>/<a href="admintools.cgi">Admin tools</a><br>
<br>
';

open(INPUT, "library/library.txt");
my $pid;
while (my $line=<INPUT>){
	my @charas=split(/_/, $line);
	$pid=@charas[0];
}

$pid++;

close(INPUT);

print '<form name="form1" action="addprob.cgi" method="post">
<table>
	<tbody>
	<tr>
		<td width="200">Problem ID:</td>
		<td><input type="text" name="pid" value="'.$pid.'" readonly="readonly"/></td>
	</tr>
	<tr>
		<td width="200">Problem Title:</td>
		<td><input type="text" name="ptitle"/></td>
	</tr>
	<tr>
		<td width="200">Problem Discription:</td>
		<td><textarea cols="70" rows="30" name="code" id="code"/></textarea></td>
	</tr>
	<tr>
		<td width="200">Authentication Code:</td>
		<td><input type="text" name="auth"/></td>
	</tr>
	<tr>
		<td align="center"><input type="submit" value="submit"></td>
	</tr>
	</tbody>
</table>

</form>

</body></html>
';
