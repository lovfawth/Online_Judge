#!C:\Perl64\bin\perl.exe

use strict;
use CGI;
use Data::Dumper;

my $cgi=CGI->new;
print $cgi->header(-type=>"text/html");


#my $sname=$cgi->param("sname");
#$sname="tools";
print '
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhml" xml:lang="en" lang="en">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<title>Online Judge</title>
</head>
<frameset rows="80,*" framespacing="0" border="0" frameborder="0">
  <frame name="header" src="header.cgi" scrolling="none">
  <frameset cols="12%,*">
	<frame name="menu" src= "menu.cgi" scrolling ="auto">
	<frame name="content" src="" scrolling="auto">
  </frameset>
 
</frameset>

</html>
';
