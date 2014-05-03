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
<link href="../css/basic.css" rel="stylesheet" type="text/css" />

<title></title>
</head>
<body>
Current position: /<a href="../home.html">home</a>/<a href="library.cgi">Problems</a><br>
<br>
';

print '<form name="form1" action="prob.cgi" method="post">Enter Problem ID: <input type="text" name="pid"/><input type="submit" value="Go!"></form>
<br>
';


print '<table width="80%" border="1">
	<tr>
		<th>Problem ID</th>
		<th>Problem Title</th>
	</tr>
';



open(INPUT, "library.txt");
my $total=0;
while (my $line=<INPUT>){
	my @info=split(/_/,$line);
	print '<tr>
	<td align="center" width="30%">'.$info[0].'</td><td align="center"><a href="prob.cgi?pid='.$info[0].'">'.$info[1].'</a></td>
	</tr>
	';
}

print '</table>
</body>
</html>';
