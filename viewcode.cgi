#!C:\Perl64\bin\perl.exe

#use strict;
use CGI;
use Data::Dumper;
use Storable;
use JSON;

my $cgi=CGI->new;
print $cgi->header(-type=>"text/html");
my $sid=$cgi->param("sid");



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
Current position: /<a href="../home.html">home</a>/<a href="log.cgi">Judge Log</a><br>
<br>
<pre>
';

open(INPUT, "code/$sid.txt");

while (!eof(INPUT)){
	$char=getc(INPUT);
	print $char;
}


print '</pre>
</body>
</html>
';
