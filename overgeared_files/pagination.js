function gotoPage(a,b){a.includes("xxxxx")?(a="1"==b?a.replace("xxxxx",$("#p_num_b").val()):a.replace("xxxxx",$("#p_num_a").val()),window.location.replace(a)):"1"==b?window.location.replace(a+"?pg="+$("#p_num_b").val()):window.location.replace(a+"?pg="+$("#p_num_a").val())}$(document).ready(function(){$("#my_popup_b").popup({type:"tooltip",vertical:"bottom",transition:"0.3s all 0.1s",tooltipanchor:$(".my_popup_b_open")}),$("#my_popup_a").popup({type:"tooltip",vertical:"bottom",transition:"0.3s all 0.1s",tooltipanchor:$(".my_popup_a_open")})});