$(function() {

	var pie_option={
		chart: {
		    plotBackgroundColor: null,
		    plotBorderWidth: null,
		    plotShadow: false,
			backgroundColor: 'rgba(0,0,0,0)'
		},
		title: {
		    text: 'Browser market shares at a specific website, 2010'
		},
		tooltip: {
		    pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
		},
		plotOptions: {
		    pie: {
			allowPointSelect: true,
			cursor: 'pointer',
			dataLabels: {
			    enabled: true,
			    color: '#000000',
			    connectorColor: '#000000',
			    format: '<b>{point.name}</b>: {point.percentage:.1f} %'
			}
		    }
		},
		series: [{
		    type: 'pie',
		    name: 'Browser share',
		    data: [
			['Firefox',   45.0],
			['IE',       26.8],
			{
			    name: 'Chrome',
			    y: 12.8,
			    sliced: true,
			    selected: true
			},
			['Safari',    8.5],
			['Opera',     6.2],
			['Others',   0.7]
		    ]
		}]
	};
		
	$.getJSON('distribution.cgi',function(data){
		pie_option.series[0].data=data;
		pie_option.title.text='Judge Result distribution';
		$('#pie_chart').highcharts(pie_option);
	});

});