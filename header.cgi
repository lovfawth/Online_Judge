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
</head>
<b>Welcome to Online Judge!</b>
</html>';
