#!C:\Perl64\bin\perl.exe

#use strict;
use CGI;
use Data::Dumper;
use Storable;
use JSON;

my $cgi=CGI->new;
print $cgi->header(-type=>"text/html");

my $pid=$cgi->param("pid");
my $code=$cgi->param("code");
my $auth=$cgi->param("auth");
my $paswrd="auth";


print '
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhml" xml:lang="en" lang="en">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">

<title></title>
</head>
<body>
Current position: /<a href="home.html">home</a>/<a href="admintools.cgi">Admin tools</a>/result<br>
<br>
';

unless ($auth eq $paswrd){
	print "Autnentication failed!";
	print '</body></html>';
	exit(0);
}
my $dir='library\probs\ '.$pid.' \ ';
$dir=~s/\s//g;
my $res=`md $dir`;

my $ret=retrieve('library\library.txt');
push @$ret, $pid;
store $ret, "library/library.txt";

open(OUTPUT,'>library/probs/'.$pid.'/'.$pid.'.txt');


print OUTPUT $code;
close(OUTPUT);


print 'Adding problem succeeded.<br>
Please copy test data and report into problem folder.
</body></html>';

