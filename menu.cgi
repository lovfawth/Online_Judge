#!C:\Perl64\bin\perl.exe

use strict;
use CGI;
use Data::Dumper;

my $cgi=CGI->new;
print $cgi->header(-type=>"text/html");

print '<html><head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
 <meta http-equiv="content-language" content="en" />
 <meta name="keywords" content="..." />
 <meta name="robots" content="all,follow" />
 <meta name="description" content="..." />
 <link href="css/basic.css" rel="stylesheet" type="text/css" />
</head>
<body>
	<a href="home.html" target="content">Home</a>
	<br>
	<a href="library/library.cgi" target="content">Problems</a>
	<br>
	<a href="log.cgi" target="content">Judge Log</a>
	<br>
	<a href="statistics.cgi" target="content">Statistics</a>
	<br>
	<a href="admintools.cgi" target="content">Admin Tools</a>
	<br>
	<a href="help.html" target="content">Help</a>
	<br>
</body>
</html>';
