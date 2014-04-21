#!C:\Perl64\bin\perl.exe

#use strict;
use CGI;
use Data::Dumper;
use Storable;
use JSON;

my $cgi=CGI->new;
print $cgi->header(-type=>"text/html");

open(INPUT,'log/log.txt');

print '
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhml" xml:lang="en" lang="en">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">

<title></title>
</head>
<body>
Current position: /<a href="../home.html">home</a>/<a href="log.cgi">Judge Log</a><br>
<br>
';

print '<table>
	<tr>
		<th>Submit Time</th>
		<th>Language</th>
		<th>Source Code</th>
		<th>Problem</th>
		<th>Flag</th>
	</tr>
	';

while (<INPUT>){
	my $line=$_;
	my @charas=split(/_/,$line);
	print '<tr>
		<td>'.$charas[0].'</td>
		<td>'.$charas[1].'</td>
		<td>Click to view</td>
		<td>'.$charas[2].'</td>
		<td>'.$charas[3].'</td>
	</tr>';
}
