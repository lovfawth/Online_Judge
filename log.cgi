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
<meta http-equiv="refresh" content="15">
<link href="css/basic.css" rel="stylesheet" type="text/css" />

<title></title>
</head>
<body>
Current position: /<a href="../home.html">home</a>/<a href="log.cgi">Judge Log</a><br>
<br>
<input type=button value="Refresh" onclick="location.reload()">
<br>
';

print '<table width="100%" border="1">
	<tr>
		<th>Submit Time</th>
		<th>Language</th>
		<th>Problem ID</th>
		<th>Source Code</th>
		<th>Flag</th>
	</tr>
	';

my @log;

while (<INPUT>){
	push @log,$_;
}

foreach (reverse @log){
	my $line=$_;
	my @charas=split(/_/,$line);
	print '<tr>
		<td align="center">'.$charas[0].'</td>
		<td align="center">'.$charas[1].'</td>
		<td align="center">'.$charas[2].'</td>
		<td align="center"><a href="viewcode.cgi?sid='.$charas[3].'" target="_blank">Click to view</a></td>
		<td align="center">'.$charas[4].'</td>
	</tr>';
}

print '</body></html>';
