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

<title></title>
</head>
<body>
<table>
';

#my @result;
#push @result, 1000;
#store \@result, "library.txt";
#my $ret=retrieve("library.txt");
#print Dumper $ret;

my $ret=retrieve("library.txt");
my $total=0;
foreach (sort @$ret){
	if ($total%5==0){
		print '<tr>
		';
	}
	print '<td><a href="prob.cgi?pid='.$_.'">'.$_.'</a></td>
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
