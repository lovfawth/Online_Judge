#!C:\Perl64\bin\perl.exe

use strict;
use CGI;
use Data::Dumper;

my $cgi=CGI->new;
print $cgi->header(-type=>"text/html");

print '
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhml" xml:lang="en" lang="en">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<link href="css/basic.css" rel="stylesheet" type="text/css" />
</head>
<table width="100%">
	<tbody border="0">
		<tr border="0">
			<td border="0">
				<img border="0" src="pic/header.png" height="78">
			</td>
			<td border="0" align="right">
				<img border="0" src="pic/logo3.gif" height="78">
			</td>
		</tr>
	<tbody>
</table>
</html>';
