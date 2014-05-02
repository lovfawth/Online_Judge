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
<table>
';

#my @result;
#push @result, 1000;
#store \@result, "library.txt";
#my $ret=retrieve("library.txt");
#print Dumper $ret;

open(INPUT, "library.txt");
my $total=0;
while (my $line=<INPUT>){
	if ($total%5==0){
		print '<tr>
		';
	}
	my @info=split(/_/,$line);
	print '<td><a href="prob.cgi?pid='.$info[0].'">'.$info[0].'</a></td>
	';
	$total++;
	if ($total%5==0){
		print '</tr>
		';
	}
}

print '</table>
</body>
</html>';
