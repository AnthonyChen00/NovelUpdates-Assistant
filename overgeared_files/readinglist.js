var saveedit;function saverl_settings(){var e="";e="checked"==$("#chkenablerl").attr("checked")?"1":"0","checked"==$("#chkhl1").attr("checked")?e+=",1":e+=",0","checked"==$("#chknewhl").attr("checked")?e+=",1":e+=",0",e=(e=(e=e+","+$("#hlreadcolor").spectrum("get").toHexString())+","+$("#hlnewcolor").spectrum("get").toHexString())+","+$("#hlalcolor").spectrum("get").toHexString(),"checked"==$("#chkalhl").attr("checked")?e+=",1":e+=",0","checked"==$("#chkhidehl").attr("checked")?e+=",1":e+=",0","checked"==$("#chkpublicread").attr("checked")?e+=",1":e+=",0","checked"==$("#chkquickadd").attr("checked")?e+=",1":e+=",0","checked"==$("#chkdisablenotes").attr("checked")?e+=",1":e+=",0",$("#elements_readinglist").val(e);var t=$("#hdlist").chosen().val();$("#elements_favs").val(t)}function enablehl(){"checked"==$("#chkenablerl").attr("checked")?($("#chkhl1").prop("disabled",!1),$("#chknewhl").prop("disabled",!1),$("#chkalhl").prop("disabled",!1),$("#chkhidehl").prop("disabled",!1),$("#chkpublicread").prop("disabled",!1),$("#chkquickadd").prop("disabled",!1)):($("#chkhl1").prop("disabled",!0),$("#chknewhl").prop("disabled",!0),$("#chkalhl").prop("disabled",!0),$("#chkhidehl").prop("disabled",!0),$("#chkpublicread").prop("disabled",!0),$("#chkquickadd").prop("disabled",!0)),$("#chkdisablenotes").prop("disabled",!1)}function unchhl(){"checked"==$("#chkalhl").attr("checked")&&$("#chkhidehl").attr("checked",!1)}function unchhide(){"checked"==$("#chkhidehl").attr("checked")&&$("#chkalhl").attr("checked",!1)}function bookmarkme(e,t,a,c){if($(a).parents("tr.newcolorme."+t).removeAttr("style"),"checked"==$(a).attr("checked")?(1==c&&$("tr.colorme."+t).removeAttr("style"),$("tr.colorme."+t).removeClass("colorme "+t),$(".checkme"+t).attr("checked",!1),$(a).attr("checked",!0),1==c&&($(a).parents("tr").addClass("colorme "+t),$(".colorme").attr("style","background-color: "+$("#hlcolor").attr("value")+" !important")),$("label[for='chklist"+e+"']").attr("title","Remove from Reading List")):($("tr.colorme."+t).removeAttr("style"),$("tr.colorme."+t).removeClass("colorme "+t),$(a).attr("checked",!1),$("label[for='chklist"+e+"']").attr("title","Add to Reading List")),varChecked="","checked"==$(a).attr("checked")?varChecked="yes":varChecked="no",$(a).prop("disabled",!0),1==!0){var i;(i=window.XMLHttpRequest?new XMLHttpRequest:new ActiveXObject("Microsoft.XMLHTTP")).onreadystatechange=function(){4==i.readyState&&200==i.status&&$(a).prop("disabled",!1)};var l="https://www.novelupdates.com/readinglist_update.php?rid="+e+"&sid="+t+"&checked="+varChecked;i.open("GET",l,!0),i.send()}}function enablepopover(){$("span#bmicon").webuiPopover({type:"async",async:{before:function(e,t){$(".webui-popover-content").html("")},success:function(e,t){$(".webui-popover-title").html("Latest Chapters")}},width:"180px",cache:!1,content:function(e){for(var t in e)"<li>"+e[t]+"</li>";return"</ul>",e}})}function latestchp(e,t,a,c,i){if($(".show-pop."+t).attr("data-url","https://www.novelupdates.com/readinglist_getchp.php?rid="+$("#series"+t).val()+"&sid="+t+"&date="+i),"yes"==c&&($(a).prop("disabled",!0),$(a).addClass("grayed"),$("#mystatus"+e).text($("#mylatest"+e).text()),$("#mystatus"+e).attr("href",$("#mylatest"+e).attr("href"))),"no"==c&&($("#mystatus"+$("#series"+t).val()).text($("#mycurrent"+e).text()),$("#mystatus"+$("#series"+t).val()).attr("href",$("#mycurrent"+e).attr("href"))),1==!0){var l;(l=window.XMLHttpRequest?new XMLHttpRequest:new ActiveXObject("Microsoft.XMLHTTP")).onreadystatechange=function(){4==l.readyState&&200==l.status&&"yes"==c&&($(a).prop("disabled",!1),0<$(".nu_editnotes").length?$(".bm_hide_me"+e).hide():$(".bmhide."+e).hide(),$(".rlnotes_morechp."+e).hide(),$("span#bmicon").webuiPopover("hide"))};var d="https://www.novelupdates.com/readinglist_update.php?rid="+e+"&sid="+t+"&checked=yes";l.open("GET",d,!0),l.send()}}function hiderlset(e){"yes"==$(e).attr("datahide")?($(".rlnewsettings").hide(),$(e).attr("datahide","no"),$(e).text("Global Settings")):($(".rlnewsettings").show(),$(e).attr("datahide","yes"),$(e).text("Hide Settings"),$(".rllocalsettings").hide(),$("#rl_local").attr("datahide","no"),$("#rl_local").text("List Settings"))}function hidelocal(e){"yes"==$(e).attr("datahide")?($(".rllocalsettings").hide(),$(e).attr("datahide","no"),$(e).text("List Settings")):($(".rllocalsettings").show(),$(e).attr("datahide","yes"),$(e).text("Hide Settings"),$(".rlnewsettings").hide(),$("#rl_global").attr("datahide","no"),$("#rl_global").text("Global Settings"))}function delchkrl(){var e=new Array;$("input:checkbox[name=check]:checked").each(function(){e.push($(this).val())}),0<e.length?$("#elements_st_checked_read").val("0:0,"+e.join()):$("#elements_st_checked_read").val("0:0"+e.join()),chkvaluesnew("delete")}function chkvaluesnew(e){var t=new Array;$("input:checkbox[name=check]:checked").each(function(){var e=$(this).val().split(":");t.push(e[1])});var a=new Array;$("input:checkbox[name=check]:not(:checked)").each(function(){var e=$(this).val().split(":");a.push(e[1])}),0<t.length&&($("#elementscheck").val(e),$("#elements_st_checked").val(t.join()),$("#elements_st_unchecked").val(a.join()))}function edit_mbrl(e,t,a){var c=t.replace("editrl","");"no"==$(e).attr("ised")?(savedinfo=$("#"+t).html(),$("#"+t).replaceWith('<input style="width: 75px !important; height: 24px !important; padding: 0px !important; margin-top: 2px;" id="'+t+'" class="rlt_input" type="text" name="list_name" size="24" maxlength="255" value="'+savedinfo+'"> <span id="rl_upme" class="rl_upme'+t+'" onclick="ch_valrl_code(\''+t+"','"+c+"','"+a+'\',\'mb\')"><img src="https://www.novelupdates.com/rl_update2.png" alt="update" class="rl_update" title="Update" style="margin-bottom: -5px;"></span>'),$(e).attr("ised","yes"),$("#etimg"+c).replaceWith('<img style="top:4px;" id="etimg'+c+'" src="https://www.novelupdates.com/wp-content/themes/ndupdates-child/js/icons/close.png" alt="cancel">')):(savedinfo=$("#"+t).val(),$("#"+t).replaceWith('<span id="'+t+'">'+savedinfo+"</span>"),$(".rl_upme"+t).replaceWith(""),$(e).attr("ised","no"),$("#etimg"+c).replaceWith('<img id="etimg'+c+'" src="https://www.novelupdates.com/wp-content/themes/ndupdates-child/js/icons/editico.png" alt="edit">'))}function edit_rl(e,t,a){var c=t.replace("editrl","");"no"==$(e).attr("ised")?(savedinfo=$("#"+t).html(),$("#"+t).replaceWith('<input style="width: 75px !important; height: 28px !important; padding: 0px !important; margin-top: 2px;" id="'+t+'" class="rlt_input" type="text" name="list_name" size="24" maxlength="255" value="'+savedinfo+'"> <span id="rl_upme" class="rl_upme'+t+'" onclick="ch_valrl_code(\''+t+"','"+c+"','"+a+'\')"><img src="https://www.novelupdates.com/rl_update2.png" alt="update" class="rl_update" title="Update"></span>'),$(e).attr("ised","yes"),$(e).attr("title","Cancel"),$("#etimg"+c).replaceWith('<img style="top:4px;" id="etimg'+c+'" src="https://www.novelupdates.com/wp-content/themes/ndupdates-child/js/icons/close.png" alt="cancel">')):(savedinfo=$("#"+t).val(),$("#"+t).replaceWith('<div id="'+t+'">'+savedinfo+"</div>"),$(".rl_upme"+t).replaceWith(""),$(e).attr("ised","no"),$(e).attr("title","Edit"),$("#etimg"+c).replaceWith('<img id="etimg'+c+'" src="https://www.novelupdates.com/wp-content/themes/ndupdates-child/js/icons/editico.png" alt="edit">'))}function ch_valrl_code(e,t,a,c){var i=$("#"+e).val();if(1==!0){var l;(l=window.XMLHttpRequest?new XMLHttpRequest:new ActiveXObject("Microsoft.XMLHTTP")).onreadystatechange=function(){4==l.readyState&&200==l.status&&($("#editrl"+t).replaceWith('<span id="editrl'+t+'">'+i+"</span>"),$(".rl_upmeeditrl"+t).replaceWith(""),$("#edtmn"+t).attr("ised","no"),$("#etimg"+t).replaceWith('<img id="etimg'+t+'" src="https://www.novelupdates.com/wp-content/themes/ndupdates-child/js/icons/editico.png" alt="edit">'))};var d="https://www.novelupdates.com/readinglist_manualupdate.php?tdata="+i+"&sid="+t+"&lid="+a;l.open("GET",d,!0),l.send()}}