#!C:\Perl64\bin\perl.exe

use strict;
use CGI;
use Data::Dumper;
use Storable;
use JSON;

my $cgi=CGI->new;
print $cgi->header(-type=>"text/html");
my $pid=$cgi->param("pid");



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
Current position: /<a href="../home.html">home</a>/<a href="library.cgi">Problems</a>/<a href="prob.cgi?pid='.$pid.'">'.$pid.'</a>/<a href="submit.cgi?pid='.$pid.'">submit</a><br>
<br>
';

print '<form name="form1" action="judge.cgi" method="post">
<table>
	<tbody>
	<tr>
		<td width="200">Problem ID:</td>
		<td><input type="text" name="pid" value="'.$pid.'"/></td>
	</tr>
	<tr>
		<td width="200">Language:<td>
		<select name="lang">
			<option value="cpp" selected="selected">C++</option>
			<option value="pas">Free Pascal</option>
		</select>
	</tr>
	<tr>
		<td width="200">Source Code:</td>
		<td><textarea cols="70" rows="30" name="code" id="code"/></textarea></td>
	</tr>
	<tr>
		<td align="center"><input type="submit" value="submit"></td>
	</tr>
	</tbody>
</table>

</form>

</body></html>
';
