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
<link href="../css/basic.css" rel="stylesheet" type="text/css" />
<script src="js/jquery-1.8.3.js" type="text/javascript"></script>
<script src="js/highcharts.js" type="text/javascript"></script>
<script src="js/addinfo.js" type="text/javascript"></script>

<title></title>
</head>
<body>
<input type="hidden" id="pid" value="'.$pid.'"/>
Current position: /<a href="../home.html">home</a>/<a href="library.cgi">Problems</a>/<a href="prob.cgi?pid='.$pid.'">'.$pid.'</a><br>
<br>
';
open(LIB,"library.txt");
my $flag=1;
while (my $line=<LIB>){
	my @info=split(/_/,$line);
	if ($info[0] eq $pid){
		$flag=0;
		last;
	}
}
close(LIB);
if ($flag){
	print 'There is not a #'.$pid.' problem. Please go <a href="javascript:history.go(-1)">back</a>
	</body></html>';
	exit(0);
}

print '<b>Problem '.$pid.':</b><br><br>';

open(INPUT,'probs/'.$pid.'/'.$pid.'.txt');

while (<INPUT>){
	print $_."<br>";
}

close(INPUT);

print '
<br>
<input type="button" value="submit" onclick="location.href='."\'submit.cgi?pid=$pid\'".';">
<br>
<br>
Additional information:
<div id="pie_chart" class="pie"></div>
</body></html>';


