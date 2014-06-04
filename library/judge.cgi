#!C:\Perl64\bin\perl.exe

#use strict;
use CGI;
use Data::Dumper;
use Storable;
use JSON;
use Win32::Job;

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
<link href="../css/basic.css" rel="stylesheet" type="text/css" />

<title></title>
</head>
<body>
Current position: /<a href="../home.html">home</a>/<a href="library.cgi">Problems</a>/<a href="prob.cgi?pid='.$pid.'">'.$pid.'</a>/<a href="submit.cgi?pid='.$pid.'">submit</a>/judge result<br>
<br>
<br>
Judge result:
<br>
';

my($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time());
my $format_time=sprintf("%d-%02d-%02d %02d:%02d:%02d",$year+1900,$mon+1,$mday,$hour,$min,$sec);
my $t=time();


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

if ($code =~ /system\(.*\);/ && $lang eq "cpp" || $code =~ /exec\(.*\);/ && $lang eq "pas"){
	open(LOG,">>../log/log.txt");
	print LOG $format_time."_";
	if ($lang eq "cpp"){
		print LOG "C++_";
	}else{
		print LOG "Pascal_";
	}
	print LOG "$pid\_$t$lang\_";
	print LOG "Cheat\n";
	close(LOG);
	print 'Cheat!
</body></html>';
	exit(0);
}

my $ret=`$compile`;
unless ($ret eq "" && $lang eq "cpp" || !($ret=~/Compilation aborted/) && $lang eq "pas"){
	open(LOG,">>../log/log.txt");
	print LOG $format_time."_";
	if ($lang eq "cpp"){
		print LOG "C++_";
	}else{
		print LOG "Pascal_";
	}
	print LOG "$pid\_$t$lang\_";
	print LOG "Compile Error\n";
	close(LOG);
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
my $timedout=0;
for (my $i1=1;$i1<=$num;$i1++){
	my $copyin='copy '."probs\\$pid\\".$pid."_".$i1.".in $pid.in";
	`$copyin`;
	my $exe="$pid.exe";
	#$exe=~s/\s//g;
	#my $return=`$exe`;
	my $job=Win32::Job->new();
	my $finished;
	#$job->spawn(undef,"$exe",(),);
	$job->spawn(undef,"$exe",(),);
	$finished=$job->run(1);
	unless ($finished){
		$timedout=1;
		`del $pid.out`;
		`del $pid.in`;
		last;
	}else{
		my $fccmd="fc $pid.out probs/$pid/".$pid."_$i1.out";
		my $fc=`$fccmd`;
		`del $pid.out`;
		`del $pid.in`;
		unless ($fc =~ /FC: no differences encountered/){
			$wa=1;
			last;
		}
	}
}

#my $delexe="$pid.exe";
#$delexe=~s/\s//g;
`del $pid.exe`;



`move $source $t$lang.txt`;
`move $t$lang.txt ../code/`;
open(LOG,">>../log/log.txt");
print LOG $format_time."_";
if ($lang eq "cpp"){
	print LOG "C++_";
}else{
	print LOG "Pascal_";
}


print LOG "$pid\_$t$lang\_";


if ($wa){
	print 'Wrong Answer!';
	print LOG "Wrong Answer\n";
}elsif ($timedout) {
	print 'Time Limit Excceeded!';
	print LOG "Time Limit Excceeded\n";
}else {
	print 'Accepted!';
	print LOG "Accepted\n";
}

close(LOG);

print '<br><a href="report.cgi?pid='.$pid.'">View report</a>';

print '</body></html>';

