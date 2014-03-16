#!C:\Perl64\bin\perl.exe

#use strict;
use CGI;
use Data::Dumper;
use Storable;
use JSON;

my $cgi=CGI->new;
print $cgi->header(-type=>"text/html");
my $pid=$cgi->param("pid");
#my $pid="1001";


print '
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhml" xml:lang="en" lang="en">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">

<title></title>
</head>
<body>
';


print '<b>Problem '.$pid.':</b><br><br>';

open(INPUT,'probs/'.$pid.'/'.$pid.'.txt');

while (<INPUT>){
	print $_."<br>";
}


print '
<button type="button"><a href="submit.cgi?pid='.$pid.'">Submit</a></button>
</body></html>';


close(INPUT);
