odoo.define('ignite_backend_theme.SidebarMenu', [], function (require) {
    "use strict";
    // Sidebar toggle effect
    // $(document).on("click", "#openSidebar", function(event){
    //     $("#openSidebar").hide();
    //     $("#closeSidebar").show();
    // });
    // $(document).on("click", "#closeSidebar", function(event){
    //     $("#closeSidebar").hide();
    //     $("#openSidebar").show();
    // });
    
    $(document).on("click", "#openSidebar", function(event){
        // $("#openSidebar").hide();
        // $("#closeSidebar").show();
        $('#openSidebar').fadeOut(100, function() {
            $('#closeSidebar').fadeIn(100);
        });
        $("#sidebar_panel").css({'display':'block'});
        // add class show_full_sidebar to #sidebar_panel
        $("#sidebar_panel").addClass("show_full_sidebar");

        $(".sidebar_logo img").animate({ 'max-width': '100px' }, 300);
        $("#sidebar_panel").animate({ 'width': '300px' }, 300);
        
        $(".o_action_manager").addClass("o_action_manager_opened");
        $(".o_action_manager").removeClass("o_action_manager_closed");

        $(".top_heading").addClass("top_heading_opened");
        $(".top_heading").removeClass("top_heading_closed");

        // Add class in navbar
        var navbar = $(".o_main_navbar");
        var navbar_id = navbar.data("id");
        $("nav").addClass(navbar_id);
        navbar.addClass("small_nav");
        // Add class in action-manager
        var action_manager = $(".o_action_manager");
        var action_manager_id = action_manager.data("id");
        $("div").addClass(action_manager_id);
        action_manager.addClass("sidebar_margin");
        // Add class in top_heading
        var top_head = $(".top_heading");
        var top_head_id = top_head.data("id");
        $("div").addClass(top_head_id);
        top_head.addClass("sidebar_margin");
    });
    $(document).on("click", "#closeSidebar", function(event){
        // $("#closeSidebar").hide();
        // $("#openSidebar").show();
        $('#closeSidebar').fadeOut(100, function() {
            $('#openSidebar').fadeIn(100);
        });

        $("#sidebar_panel").css({'display':'block'});
        $("#sidebar_panel").removeClass("show_full_sidebar");

        $(".sidebar_logo img").animate({ 'max-width': '60px' }, 300);
        $("#sidebar_panel").animate({ 'width': '200px' }, 300);

        $(".o_action_manager").addClass("o_action_manager_closed");
        $(".o_action_manager").removeClass("o_action_manager_opened");
        $(".top_heading").addClass("top_heading_closed");
        $(".top_heading").removeClass("top_heading_opened");


        // Remove class in navbar
        var navbar = $(".o_main_navbar");
        var navbar_id = navbar.data("id");
        $("nav").removeClass(navbar_id);
        navbar.removeClass("small_nav");
        // Remove class in action-manager
        var action_manager = $(".o_action_manager");
        var action_manager_id = action_manager.data("id");
        $("div").removeClass(action_manager_id);
        action_manager.removeClass("sidebar_margin");
        // Remove class in top_heading
        var top_head = $(".top_heading");
        var top_head_id = top_head.data("id");
        $("div").removeClass(top_head_id);
        top_head.removeClass("sidebar_margin");
    });
    $(document).on("click", ".sidebar .sidebar_menu_item", function(event){
        var menu = $(".sidebar .sidebar_menu_item");
        var $this = $(this);
        var id = $this.data("id");
        $("header").removeClass().addClass(id);
        menu.removeClass("active");
        $this.addClass("active");

        // Sidebar close on menu-item click
        $('#closeSidebar').fadeOut(100, function() {
            $('#openSidebar').fadeIn(100);
        });
        
        $("#sidebar_panel").css({'display':'block'});
        $("#sidebar_panel").removeClass("show_full_sidebar");

        $(".sidebar_logo img").animate({ 'max-width': '60px' }, 300);
        $("#sidebar_panel").animate({ 'width': '200px' }, 300);

        $(".o_action_manager").addClass("o_action_manager_closed");
        $(".o_action_manager").removeClass("o_action_manager_opened");
        $(".top_heading").addClass("top_heading_closed");
        $(".top_heading").removeClass("top_heading_opened");


        // remove class in navbar
        var navbar = $(".o_main_navbar");
        var navbar_id = navbar.data("id");
        $("nav").removeClass(navbar_id);
        navbar.removeClass("small_nav");
        // Remove class in action-manager
        var action_manager = $(".o_action_manager");
        var action_manager_id = action_manager.data("id");
        $("div").removeClass(action_manager_id);
        action_manager.removeClass("sidebar_margin");
        // Remove class in top_heading
        var top_head = $(".top_heading");
        var top_head_id = top_head.data("id");
        $("div").removeClass(top_head_id);
        top_head.removeClass("sidebar_margin");
    });
});
