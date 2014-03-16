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
my $lang=$cgi->param("lang");



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




my $cppcompdir='C:\Dev-Cpp\bin\g++.exe ';
my $pascompdir='C:\FPC\2.6.2\bin\i386-win32\fpc.exe ';


my $source='source.'.$lang;
open(OUTPUT,">$source");
print OUTPUT $code;
close(OUTPUT);

#`move /y $source probs/$pid`;
my $compile;
if ($lang eq "cpp"){
	$compile=$cppcompdir."$source";
	}else{
		$compile=$pascompdir."$source";
	}
my $ret=`$compile`;
unless ($ret eq "" && $lang eq "cpp" || !($ret=~/Compilation aborted/) && $lang eq "pas"){
	print 'Compile Error!
</body></html>';
	exit(0);
}
if ($lang eq "pas"){
	`del source.o`;
}
if ($lang eq "cpp"){
	`move /y a.exe $pid.exe`;
}else{
	`move /y source.exe $pid.exe`
}
my $i="dir probs\\".$pid."\\ /b";
my @ret=`$i`;
my $num=@ret;
$num/=2;
$num--;
my $wa=0;
for (my $i1=1;$i1<=$num;$i1++){
	my $copyin='copy '."probs\\$pid\\".$pid."_".$i1.".in $pid.in";
	`$copyin`;
	my $exe="$pid.exe";
	#$exe=~s/\s//g;
	my $return=`$exe`;
	my $fccmd="fc $pid.out probs/$pid/".$pid."_$i1.out";
	my $fc=`$fccmd`;
	`del $pid.out`;
	`del $pid.in`;
	unless ($fc =~ /FC: no differences encountered/){
		$wa=1;
		last;
	}
}

#my $delexe="$pid.exe";
#$delexe=~s/\s//g;
`del $pid.exe`;
`del $source`;

if ($wa){
	print 'Wrong Answer!';
}else{
	print 'Accepted!';
}

print '<br><a href="report.cgi?pid='.$pid.'">View report</a>';

print '</body></html>';

