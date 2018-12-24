function show_search_bar(strItem)
{
	
	var strClassName = $(strItem).children('i').attr('class');
	
	
	if ( strClassName == 'fa fa-search menu' )
	{
		$('.fa.fa-search.menu').attr('class', 'fa fa-times menu');
		$(strItem).addClass('selected');
		$(strItem).attr('title', 'Hide Search');
		$('.nu_menu_search').show();
		
		$("[id='searchme-rl newmenu']").focus();
	}
	else
	{
		$('.fa.fa-times.menu').attr('class', 'fa fa-search menu');
		$(strItem).removeClass('selected');
		$(strItem).attr('title', 'Search');
		$('.nu_menu_search').hide();
	}
}

function search_btn_click()
{
	$( "#search_nu_novel" ).submit();
}

function toggleUserMenu()
{
	var displayMenu = $('.lo_main').css('display');
	

	if ( displayMenu == 'block' )
	{
		$('.lo_main').hide();
		$('.arrow-up_toc_username').hide();
	}
	else
	{
		$('.lo_main').show();
		$('.arrow-up_toc_username').show();
	}
	
	
}

function toggleMobileMenu()
{
	var displayHeight = $('.w-nav-list').css('height');

	if ( displayHeight == '0px' )
	{
		$('.w-nav-list').css('display','block');
		$('.w-nav-list').css('opacity','1');
		$('.w-nav-list').css('height','auto');
		$('.w-nav-list').css('padding-top','0px');
		$('.w-nav-list').css('padding-bottom','0px');
	}
	else
	{
		$('.w-nav-list').css('display','none');
		$('.w-nav-list').css('height','0px');
		$('.w-nav-list').css('opacity','0');
	}
}